# This Python file uses the following encoding: utf-8
import platform
import subprocess
import sys
import threading
import time

import GPUtil
import psutil
from PySide6.QtCore import QObject, Signal, Slot, QThread, QTimer
from PySide6.QtWidgets import QApplication, QWidget, QGroupBox
from PySide6.QtWidgets import QHBoxLayout, QVBoxLayout, QLineEdit, QLabel

# Important:
# You need to run the following command to generate the ui_form.py file
#     pyside6-uic form.ui -o ui_form.py, or
#     pyside2-uic form.ui -o ui_form.py
from ui_form import Ui_Widget


class Worker(QObject):
    finished = Signal()
    update_ui_proc = Signal(psutil.Process)

    def __init__(self, ui, parent=None):
        super().__init__(parent)
        self.running = True
        self.ui = ui

    @Slot()
    def processar(self):
        # self.clear_list.emit()
        try:
            processos = psutil.process_iter()

            for proc in processos:
                try:
                    if proc.pid == 0:
                        continue
                    self.update_ui_proc.emit(proc)
                except (psutil.AccessDenied, psutil.NoSuchProcess) as err:
                    print(f"Erro ao acessar informações do processo: {err}")
                    continue
                except Exception as e:
                    print(e)
                    continue
        except Exception as e:
            print(e)

        self.finished.emit()


class Updater(QObject):
    finished = Signal()
    remove_item = Signal(QGroupBox)
    running = True
    pai = None

    def __init__(self, parent=None):
        super().__init__(parent)

    @Slot()
    def run(self, pid: int, group: QGroupBox, fields: dict):

        while self.running:
            process = psutil.process_iter()

            proc = [proc for proc in process if proc.pid == pid][0]
            try:
                if proc.pid == pid:
                    fields['name'].setText(proc.name())
                    fields['cpu_percent'].setText(f'{proc.cpu_percent():.2f}%')
                    fields['memory_percent'].setText(f'{proc.memory_percent():.2f} MB')
                    fields['status'].setText(proc.status())
                    fields['exe'].setText(proc.exe())
            except Exception as e:
                self.pai.processos.remove(proc.pid)
                self.remove_item.emit(group, proc.pid)
                break

            time.sleep(1)
        self.finished.emit()

    @staticmethod
    def stop_threads():
        Updater.running = False


class Widget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Widget()
        self.ui.setupUi(self)
        self.running = True
        self.ui.atualizarprocess.clicked.connect(self.atualizar_processos)
        self.timer = QTimer()
        self.timer.timeout.connect(self.init_process)
        self.timer.start(10000)
        self.processos: list[int] = []
        Updater.pai = self

    def init_process(self):
        self.worker = Worker(self.ui)
        self.workerThread = QThread()
        self.worker.moveToThread(self.workerThread)
        self.worker.finished.connect(self.workerThread.quit)
        self.worker.update_ui_proc.connect(self.atualizar_interface)
        self.workerThread.started.connect(self.worker.processar)  # Inicia o processamento quando a thread é iniciada
        self.workerThread.start()

    def preencher_so(self):
        self.ui.soname.setText(platform.system())
        self.ui.soarq.setText(platform.architecture()[0])
        self.ui.soversion.setText(platform.version())
        self.ui.soprocessor.setText(platform.processor().split(" ")[0])
        total_ram = psutil.virtual_memory().total / (1024 ** 3)
        self.ui.soram.setText(f"{total_ram:.2f} GB")

    def preencher_processor(self):
        so = platform.platform().lower()
        if "linux" in so:
            result = subprocess.run(['cat', '/proc/cpuinfo'], capture_output=True, text=True)
            output = [line.split(':')[-1].strip() for line in result.stdout.split('\n') if 'model name' in line]
            output = output[0]
            self.preencher_campos_processor(output.split(" "))
        elif "windows" in so:
            result = subprocess.run(['wmic', 'cpu', 'get', 'name'], capture_output=True, text=True)
            output = result.stdout.strip().split('\n')[-1].split(" ")
            self.preencher_campos_processor(output)

    def preencher_campos_processor(self, output: list):
        self.ui.processorfamily.setText(output[1])
        self.ui.processor.setText(output[2])
        self.ui.processorarq.setText(platform.processor().split(" ")[0])
        self.ui.processorfreq.setText(output[-1])
        self.ui.processorcores.setText(str(psutil.cpu_count(False)))
        self.ui.processorthreads.setText(str(psutil.cpu_count(True)))
        threading.Thread(target=self.update_cpu_usage, args=()).start()

    def update_gpu_usage(self, gpu_name, campo: QLineEdit):
        while self.running:
            time.sleep(1)
            gpus = GPUtil.getGPUs()
            uso_gpu = [gpu.load * 100 for gpu in gpus if gpu.name == gpu_name]
            if uso_gpu:
                campo.setText(f'{uso_gpu[0]:.2f}%')
            if not self.isVisible():
                self.running = False  # Altera o sinalizador quando a janela não está mais visível
                break

    def update_gpu_temp(self, gpu_name, campo: QLineEdit):
        while self.running:
            time.sleep(1)
            gpus = GPUtil.getGPUs()
            temp = [gpu.temperature for gpu in gpus if gpu.name == gpu_name]
            if temp:
                campo.setText(f'{temp[0]:.2f}°C')
            if not self.isVisible():
                self.running = False  # Altera o sinalizador quando a janela não está mais visível
                break

    def update_gpu_memory(self, gpu_name, campo_memoFree: QLineEdit, campo_memoUsed: QLineEdit):
        while self.running:
            time.sleep(1)
            gpus = GPUtil.getGPUs()
            memoFree = [gpu.memoryFree for gpu in gpus if gpu.name == gpu_name]
            memoUsed = [gpu.memoryUsed for gpu in gpus if gpu.name == gpu_name]
            if memoFree and memoUsed:
                campo_memoFree.setText(f'{memoFree[0]:.2f}MB')
                campo_memoUsed.setText(f'{memoUsed[0]:.2f}MB')
            if not self.isVisible():
                self.running = False  # Altera o sinalizador quando a janela não está mais visível
                break

    def update_cpu_usage(self):
        while self.running:
            time.sleep(1)
            uso_cpu = psutil.cpu_percent()
            self.ui.processorutil.setText(f'{uso_cpu}%')
            if not self.isVisible():
                self.running = False
                break

    def update_ui(self):
        self.ui.GPUs.update()  # Atualize o layout para refletir as alterações
        # self.repaint()  # Redesenha a janela para mostrar as atualizações

    def update_ui_process(self):
        self.ui.scrollProcessos.update()
        # self.repaint()

    def preencher_gpus(self):
        # Colocando as GPUs
        gpus = GPUtil.getGPUs()

        for gpu in gpus:
            # Adicione o widget ao layout vertical dentro do widget pai
            group_box = QGroupBox(f'GPU {gpus.index(gpu) + 1}')

            hbox_layout = QHBoxLayout()
            group_box.setLayout(hbox_layout)

            # Primeiro campo
            field1_layout = QVBoxLayout()
            label1 = QLabel('Nome')
            line_edit1 = QLineEdit()
            line_edit1.setText(gpu.name)
            line_edit1.setReadOnly(True)
            field1_layout.addWidget(label1)
            field1_layout.addWidget(line_edit1)

            # Segundo campo
            field2_layout = QVBoxLayout()
            label2 = QLabel('Memória total')
            line_edit2 = QLineEdit()
            line_edit2.setText(f"{gpu.memoryTotal}")
            line_edit2.setReadOnly(True)
            field2_layout.addWidget(label2)
            field2_layout.addWidget(line_edit2)

            # Quinto campo
            field5_layout = QVBoxLayout()
            label5 = QLabel('Memória livre')
            line_edit5 = QLineEdit()
            line_edit5.setReadOnly(True)
            field5_layout.addWidget(label5)
            field5_layout.addWidget(line_edit5)

            # Sexto campo
            field6_layout = QVBoxLayout()
            label6 = QLabel('Memória sendo usada')
            line_edit6 = QLineEdit()
            line_edit6.setReadOnly(True)
            field6_layout.addWidget(label6)
            field6_layout.addWidget(line_edit6)
            threading.Thread(target=self.update_gpu_memory, args=(gpu.name, line_edit5, line_edit6)).start()

            # Terceiro campo
            field3_layout = QVBoxLayout()
            label3 = QLabel('Uso')
            line_edit3 = QLineEdit()
            line_edit3.setReadOnly(True)
            threading.Thread(target=self.update_gpu_usage, args=(gpu.name, line_edit3)).start()
            field3_layout.addWidget(label3)
            field3_layout.addWidget(line_edit3)

            # Quarto campo
            field4_layout = QVBoxLayout()
            label3 = QLabel('Temperatura')
            line_edit3 = QLineEdit()
            line_edit3.setReadOnly(True)
            threading.Thread(target=self.update_gpu_temp, args=(gpu.name, line_edit3)).start()
            field4_layout.addWidget(label3)
            field4_layout.addWidget(line_edit3)

            # Adicionando os campos ao layout horizontal
            hbox_layout.addLayout(field1_layout)
            hbox_layout.addLayout(field2_layout)
            hbox_layout.addLayout(field5_layout)
            hbox_layout.addLayout(field6_layout)
            hbox_layout.addLayout(field3_layout)
            hbox_layout.addLayout(field4_layout)

            self.ui.scrollGPUs.addWidget(group_box)

            self.update_ui()  # Chame o método para atualizar a interface

    def atualizar_processos(self):
        threading.Thread(target=self.limpar_scroll_area, args=()).start()  # Limpa os widgets antigos

        processos = psutil.process_iter()

        for proc in processos:
            try:
                if proc.pid == 0:
                    continue

                widget_processo, fields = self.criar_widget_processo(proc)
                self.ui.scrollProcessos.addWidget(widget_processo)

            except (psutil.AccessDenied, psutil.NoSuchProcess) as err:
                print(f"Erro ao acessar informações do processo: {err}")
                continue
            except Exception as e:
                print(e)
                continue

        self.update_ui_process()

    def limpar_scroll_area(self):
        # Obtém o layout da QScrollArea
        scroll_layout = self.ui.scrollProcessos.layout()
        self.processos.clear()

        # Remove todos os widgets filhos
        while scroll_layout.count():
            item = scroll_layout.takeAt(0)
            widget = item.widget()
            if widget:
                widget.setParent(None)  # Remove o widget do layout
                widget.deleteLater()  # Deleta o widget da memória
            else:
                # Se o item não for um widget, deleta o item diretamente
                del item

    def criar_widget_processo(self, proc):
        group_box = QGroupBox(f'Processo: {proc.name()}')

        hbox_layout = QHBoxLayout()
        group_box.setLayout(hbox_layout)

        # Primeiro campo
        field1_layout = QVBoxLayout()
        label1 = QLabel('Nome')
        line_edit1 = QLineEdit()
        line_edit1.setText(proc.name())
        line_edit1.setReadOnly(True)
        field1_layout.addWidget(label1)
        field1_layout.addWidget(line_edit1)

        # Segundo campo
        field2_layout = QVBoxLayout()
        label2 = QLabel('CPU %')
        line_edit2 = QLineEdit()
        line_edit2.setText(f"{proc.cpu_percent()}")
        line_edit2.setReadOnly(True)
        field2_layout.addWidget(label2)
        field2_layout.addWidget(line_edit2)

        # Terceiro campo
        field3_layout = QVBoxLayout()
        label3 = QLabel('Memória %')
        line_edit3 = QLineEdit()
        line_edit3.setReadOnly(True)
        line_edit3.setText(f"{proc.memory_percent()}")
        field3_layout.addWidget(label3)
        field3_layout.addWidget(line_edit3)

        # Quarto campo
        field4_layout = QVBoxLayout()
        label4 = QLabel('Status')
        line_edit4 = QLineEdit()
        line_edit4.setReadOnly(True)
        line_edit4.setText(f"{proc.status()}")
        field4_layout.addWidget(label4)
        field4_layout.addWidget(line_edit4)

        # Quinto campo
        field5_layout = QVBoxLayout()
        label5 = QLabel('Caminho')
        line_edit5 = QLineEdit()
        line_edit5.setReadOnly(True)
        line_edit5.setText(f"{proc.exe()}")
        field5_layout.addWidget(label5)
        field5_layout.addWidget(line_edit5)

        # Adicionando os campos ao layout horizontal
        hbox_layout.addLayout(field1_layout)
        hbox_layout.addLayout(field2_layout)
        hbox_layout.addLayout(field3_layout)
        hbox_layout.addLayout(field4_layout)
        hbox_layout.addLayout(field5_layout)

        return group_box, {'name': line_edit1, 'cpu_percent': line_edit2,
                           'memory_percent': line_edit3,
                           'status': line_edit4, 'exe': line_edit5}

    def remover_elemento(self, widget, pid):
        layout = self.ui.scrollProcessos.layout()
        if pid in self.processos:
            self.processos.remove(pid)

        if layout is not None:
            layout.removeWidget(widget)
            widget.setParent(None)
            widget.deleteLater()

    def atualizar_interface(self, widget_processo):
        try:
            if widget_processo.pid not in self.processos:
                self.processos.append(widget_processo.pid)
                element, fields = self.criar_widget_processo(widget_processo)
                self.ui.scrollProcessos.addWidget(element)

                # Criar instâncias separadas de Updater e QThread para cada processo
                updater = Updater()
                thread = QThread()
                self.thread().children().append(thread)

                updater.moveToThread(thread)
                updater.finished.connect(lambda: self.cleanup_thread(thread, updater))  # Conectar uma vez só
                updater.remove_item.connect(lambda x: self.remover_elemento(x, widget_processo.pid))

                # Connect the signal to start the updater
                thread.started.connect(lambda: updater.run(widget_processo.pid, element, fields))

                # Iniciar a thread
                # thread.start()
        except Exception as e:
            print(f"Erro ao atualizar a interface: {e}")

    def cleanup_thread(self, thread, updater):
        try:
            if thread.isRunning():
                thread.quit()
                thread.wait()
            updater.deleteLater()
            thread.deleteLater()
        except Exception as e:
            print(f"Erro ao limpar thread e updater: {e}")

    def closeEvent(self, event):
        # Sinalize para encerrar threads aqui
        # Emita um sinal para que as threads parem
        Updater.stop_threads()
        self.running = False
        event.accept()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = Widget()
    widget.show()
    widget.preencher_so()
    widget.preencher_processor()
    widget.preencher_gpus()
    sys.exit(app.exec())
