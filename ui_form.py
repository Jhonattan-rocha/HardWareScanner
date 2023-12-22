# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form.ui'
##
## Created by: Qt User Interface Compiler version 6.6.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QGroupBox, QHBoxLayout, QLabel,
    QLineEdit, QPushButton, QScrollArea, QSizePolicy,
    QVBoxLayout, QWidget)

class Ui_Widget(object):
    def setupUi(self, Widget):
        if not Widget.objectName():
            Widget.setObjectName(u"Widget")
        Widget.resize(888, 640)
        Widget.setMinimumSize(QSize(888, 640))
        self.verticalLayout_2 = QVBoxLayout(Widget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.SOinfos = QVBoxLayout()
        self.SOinfos.setObjectName(u"SOinfos")
        self.groupBox = QGroupBox(Widget)
        self.groupBox.setObjectName(u"groupBox")
        self.horizontalLayout = QHBoxLayout(self.groupBox)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, -1, -1, -1)
        self.label = QLabel(self.groupBox)
        self.label.setObjectName(u"label")

        self.verticalLayout_3.addWidget(self.label)

        self.soname = QLineEdit(self.groupBox)
        self.soname.setObjectName(u"soname")
        self.soname.setReadOnly(True)

        self.verticalLayout_3.addWidget(self.soname)


        self.horizontalLayout.addLayout(self.verticalLayout_3)

        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(-1, -1, 0, -1)
        self.label_2 = QLabel(self.groupBox)
        self.label_2.setObjectName(u"label_2")

        self.verticalLayout_4.addWidget(self.label_2)

        self.soarq = QLineEdit(self.groupBox)
        self.soarq.setObjectName(u"soarq")
        self.soarq.setReadOnly(True)

        self.verticalLayout_4.addWidget(self.soarq)


        self.horizontalLayout.addLayout(self.verticalLayout_4)

        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(-1, -1, 0, -1)
        self.label_3 = QLabel(self.groupBox)
        self.label_3.setObjectName(u"label_3")

        self.verticalLayout_5.addWidget(self.label_3)

        self.soversion = QLineEdit(self.groupBox)
        self.soversion.setObjectName(u"soversion")
        self.soversion.setReadOnly(True)

        self.verticalLayout_5.addWidget(self.soversion)


        self.horizontalLayout.addLayout(self.verticalLayout_5)

        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(-1, -1, 0, -1)
        self.label_4 = QLabel(self.groupBox)
        self.label_4.setObjectName(u"label_4")

        self.verticalLayout_6.addWidget(self.label_4)

        self.soprocessor = QLineEdit(self.groupBox)
        self.soprocessor.setObjectName(u"soprocessor")
        self.soprocessor.setReadOnly(True)

        self.verticalLayout_6.addWidget(self.soprocessor)


        self.horizontalLayout.addLayout(self.verticalLayout_6)

        self.verticalLayout_7 = QVBoxLayout()
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(-1, -1, 0, -1)
        self.label_5 = QLabel(self.groupBox)
        self.label_5.setObjectName(u"label_5")

        self.verticalLayout_7.addWidget(self.label_5)

        self.soram = QLineEdit(self.groupBox)
        self.soram.setObjectName(u"soram")
        self.soram.setReadOnly(True)

        self.verticalLayout_7.addWidget(self.soram)


        self.horizontalLayout.addLayout(self.verticalLayout_7)


        self.SOinfos.addWidget(self.groupBox)


        self.verticalLayout_2.addLayout(self.SOinfos)

        self.groupBox_2 = QGroupBox(Widget)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.horizontalLayout_2 = QHBoxLayout(self.groupBox_2)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(-1, -1, 0, -1)
        self.label_6 = QLabel(self.groupBox_2)
        self.label_6.setObjectName(u"label_6")

        self.verticalLayout.addWidget(self.label_6)

        self.processorfamily = QLineEdit(self.groupBox_2)
        self.processorfamily.setObjectName(u"processorfamily")
        self.processorfamily.setReadOnly(True)

        self.verticalLayout.addWidget(self.processorfamily)


        self.horizontalLayout_2.addLayout(self.verticalLayout)

        self.verticalLayout_8 = QVBoxLayout()
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(-1, -1, 0, 0)
        self.label_7 = QLabel(self.groupBox_2)
        self.label_7.setObjectName(u"label_7")

        self.verticalLayout_8.addWidget(self.label_7)

        self.processor = QLineEdit(self.groupBox_2)
        self.processor.setObjectName(u"processor")
        self.processor.setReadOnly(True)

        self.verticalLayout_8.addWidget(self.processor)


        self.horizontalLayout_2.addLayout(self.verticalLayout_8)

        self.verticalLayout_10 = QVBoxLayout()
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_10.setContentsMargins(-1, -1, 0, -1)
        self.label_9 = QLabel(self.groupBox_2)
        self.label_9.setObjectName(u"label_9")

        self.verticalLayout_10.addWidget(self.label_9)

        self.processorarq = QLineEdit(self.groupBox_2)
        self.processorarq.setObjectName(u"processorarq")
        self.processorarq.setReadOnly(True)

        self.verticalLayout_10.addWidget(self.processorarq)


        self.horizontalLayout_2.addLayout(self.verticalLayout_10)

        self.verticalLayout_9 = QVBoxLayout()
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(-1, -1, 0, -1)
        self.label_8 = QLabel(self.groupBox_2)
        self.label_8.setObjectName(u"label_8")

        self.verticalLayout_9.addWidget(self.label_8)

        self.processorfreq = QLineEdit(self.groupBox_2)
        self.processorfreq.setObjectName(u"processorfreq")
        self.processorfreq.setReadOnly(True)

        self.verticalLayout_9.addWidget(self.processorfreq)


        self.horizontalLayout_2.addLayout(self.verticalLayout_9)

        self.verticalLayout_11 = QVBoxLayout()
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(-1, -1, 0, -1)
        self.label_10 = QLabel(self.groupBox_2)
        self.label_10.setObjectName(u"label_10")

        self.verticalLayout_11.addWidget(self.label_10)

        self.processorcores = QLineEdit(self.groupBox_2)
        self.processorcores.setObjectName(u"processorcores")
        self.processorcores.setReadOnly(True)

        self.verticalLayout_11.addWidget(self.processorcores)


        self.horizontalLayout_2.addLayout(self.verticalLayout_11)

        self.verticalLayout_12 = QVBoxLayout()
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.verticalLayout_12.setContentsMargins(-1, -1, 0, -1)
        self.label_11 = QLabel(self.groupBox_2)
        self.label_11.setObjectName(u"label_11")

        self.verticalLayout_12.addWidget(self.label_11)

        self.processorthreads = QLineEdit(self.groupBox_2)
        self.processorthreads.setObjectName(u"processorthreads")
        self.processorthreads.setReadOnly(True)

        self.verticalLayout_12.addWidget(self.processorthreads)


        self.horizontalLayout_2.addLayout(self.verticalLayout_12)

        self.verticalLayout_13 = QVBoxLayout()
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.verticalLayout_13.setContentsMargins(-1, -1, 0, -1)
        self.label_13 = QLabel(self.groupBox_2)
        self.label_13.setObjectName(u"label_13")

        self.verticalLayout_13.addWidget(self.label_13)

        self.processorutil = QLineEdit(self.groupBox_2)
        self.processorutil.setObjectName(u"processorutil")
        self.processorutil.setReadOnly(True)

        self.verticalLayout_13.addWidget(self.processorutil)


        self.horizontalLayout_2.addLayout(self.verticalLayout_13)


        self.verticalLayout_2.addWidget(self.groupBox_2)

        self.GPUs = QScrollArea(Widget)
        self.GPUs.setObjectName(u"GPUs")
        self.GPUs.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 868, 86))
        self.verticalLayout_15 = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.scrollGPUs = QVBoxLayout()
        self.scrollGPUs.setObjectName(u"scrollGPUs")

        self.verticalLayout_15.addLayout(self.scrollGPUs)

        self.GPUs.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout_2.addWidget(self.GPUs)

        self.groupBox_3 = QGroupBox(Widget)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.groupBox_3.setMinimumSize(QSize(0, 350))
        self.verticalLayout_14 = QVBoxLayout(self.groupBox_3)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.atualizarprocess = QPushButton(self.groupBox_3)
        self.atualizarprocess.setObjectName(u"atualizarprocess")

        self.verticalLayout_14.addWidget(self.atualizarprocess)

        self.scrollAreaProcessos = QScrollArea(self.groupBox_3)
        self.scrollAreaProcessos.setObjectName(u"scrollAreaProcessos")
        self.scrollAreaProcessos.setWidgetResizable(True)
        self.scrollAreaWidgetContents_2 = QWidget()
        self.scrollAreaWidgetContents_2.setObjectName(u"scrollAreaWidgetContents_2")
        self.scrollAreaWidgetContents_2.setGeometry(QRect(0, 0, 848, 282))
        self.verticalLayout_16 = QVBoxLayout(self.scrollAreaWidgetContents_2)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.scrollProcessos = QVBoxLayout()
        self.scrollProcessos.setObjectName(u"scrollProcessos")

        self.verticalLayout_16.addLayout(self.scrollProcessos)

        self.scrollAreaProcessos.setWidget(self.scrollAreaWidgetContents_2)

        self.verticalLayout_14.addWidget(self.scrollAreaProcessos)


        self.verticalLayout_2.addWidget(self.groupBox_3)


        self.retranslateUi(Widget)

        QMetaObject.connectSlotsByName(Widget)
    # setupUi

    def retranslateUi(self, Widget):
        Widget.setWindowTitle(QCoreApplication.translate("Widget", u"HardwareScanner", None))
        self.groupBox.setTitle(QCoreApplication.translate("Widget", u"Sistema Operacional", None))
        self.label.setText(QCoreApplication.translate("Widget", u"SO", None))
#if QT_CONFIG(accessibility)
        self.soname.setAccessibleName(QCoreApplication.translate("Widget", u"soname", None))
#endif // QT_CONFIG(accessibility)
        self.label_2.setText(QCoreApplication.translate("Widget", u"Arquitetura", None))
        self.label_3.setText(QCoreApplication.translate("Widget", u"Vers\u00e3o", None))
        self.label_4.setText(QCoreApplication.translate("Widget", u"Processador", None))
        self.label_5.setText(QCoreApplication.translate("Widget", u"RAM dispon\u00edvel", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("Widget", u"Processador", None))
        self.label_6.setText(QCoreApplication.translate("Widget", u"Familia", None))
        self.label_7.setText(QCoreApplication.translate("Widget", u"Modelo", None))
        self.label_9.setText(QCoreApplication.translate("Widget", u"Arquitetura", None))
        self.label_8.setText(QCoreApplication.translate("Widget", u"Frequencia Base", None))
        self.label_10.setText(QCoreApplication.translate("Widget", u"Cores", None))
        self.label_11.setText(QCoreApplication.translate("Widget", u"Threads", None))
        self.label_13.setText(QCoreApplication.translate("Widget", u"Uso", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("Widget", u"Processos", None))
        self.atualizarprocess.setText(QCoreApplication.translate("Widget", u"Atualizar", None))
    # retranslateUi

