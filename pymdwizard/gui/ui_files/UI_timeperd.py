# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'timeperd.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(313, 173)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Form.sizePolicy().hasHeightForWidth())
        Form.setSizePolicy(sizePolicy)
        self.verticalLayout_11 = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout_11.setContentsMargins(3, 3, 3, 3)
        self.verticalLayout_11.setSpacing(6)
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        self.fgdc_timeperd = QtWidgets.QGroupBox(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.fgdc_timeperd.sizePolicy().hasHeightForWidth())
        self.fgdc_timeperd.setSizePolicy(sizePolicy)
        self.fgdc_timeperd.setMinimumSize(QtCore.QSize(0, 0))
        self.fgdc_timeperd.setObjectName("fgdc_timeperd")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.fgdc_timeperd)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label_2 = QtWidgets.QLabel(self.fgdc_timeperd)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        font.setBold(False)
        font.setItalic(True)
        font.setWeight(50)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("font: italic;")
        self.label_2.setWordWrap(True)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_4.addWidget(self.label_2)
        self.widget_2 = QtWidgets.QWidget(self.fgdc_timeperd)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_2.sizePolicy().hasHeightForWidth())
        self.widget_2.setSizePolicy(sizePolicy)
        self.widget_2.setObjectName("widget_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget_2)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.widget = QtWidgets.QWidget(self.widget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget.sizePolicy().hasHeightForWidth())
        self.widget.setSizePolicy(sizePolicy)
        self.widget.setObjectName("widget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout_2.setContentsMargins(3, 3, 3, 0)
        self.verticalLayout_2.setSpacing(3)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_3 = QtWidgets.QLabel(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        font.setItalic(True)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("font: italic;")
        self.label_3.setWordWrap(True)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_2.addWidget(self.label_3)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.radio_single = QtWidgets.QRadioButton(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.radio_single.sizePolicy().hasHeightForWidth())
        self.radio_single.setSizePolicy(sizePolicy)
        self.radio_single.setChecked(True)
        self.radio_single.setObjectName("radio_single")
        self.horizontalLayout_4.addWidget(self.radio_single)
        self.radio_range = QtWidgets.QRadioButton(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.radio_range.sizePolicy().hasHeightForWidth())
        self.radio_range.setSizePolicy(sizePolicy)
        self.radio_range.setObjectName("radio_range")
        self.horizontalLayout_4.addWidget(self.radio_range)
        self.radio_multiple = QtWidgets.QRadioButton(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.radio_multiple.sizePolicy().hasHeightForWidth())
        self.radio_multiple.setSizePolicy(sizePolicy)
        self.radio_multiple.setObjectName("radio_multiple")
        self.horizontalLayout_4.addWidget(self.radio_multiple)
        self.verticalLayout_2.addLayout(self.horizontalLayout_4)
        self.fgdc_timeinfo = QtWidgets.QStackedWidget(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.fgdc_timeinfo.sizePolicy().hasHeightForWidth())
        self.fgdc_timeinfo.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        self.fgdc_timeinfo.setFont(font)
        self.fgdc_timeinfo.setObjectName("fgdc_timeinfo")
        self.fgdc_sngdate = QtWidgets.QWidget()
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.fgdc_sngdate.sizePolicy().hasHeightForWidth())
        self.fgdc_sngdate.setSizePolicy(sizePolicy)
        self.fgdc_sngdate.setObjectName("fgdc_sngdate")
        self.verticalLayout_10 = QtWidgets.QVBoxLayout(self.fgdc_sngdate)
        self.verticalLayout_10.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.verticalLayout_10.setContentsMargins(9, 9, 0, 0)
        self.verticalLayout_10.setSpacing(6)
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        spacerItem = QtWidgets.QSpacerItem(0, 0, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout_10.addItem(spacerItem)
        self.fgdc_timeinfo.addWidget(self.fgdc_sngdate)
        self.fgdc_rngdates = QtWidgets.QWidget()
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.fgdc_rngdates.sizePolicy().hasHeightForWidth())
        self.fgdc_rngdates.setSizePolicy(sizePolicy)
        self.fgdc_rngdates.setObjectName("fgdc_rngdates")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.fgdc_rngdates)
        self.verticalLayout_7.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.verticalLayout_7.setContentsMargins(0, 9, 0, 0)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.layout_daterange = QtWidgets.QHBoxLayout()
        self.layout_daterange.setSpacing(0)
        self.layout_daterange.setObjectName("layout_daterange")
        self.verticalLayout_3.addLayout(self.layout_daterange)
        self.verticalLayout_7.addLayout(self.verticalLayout_3)
        spacerItem1 = QtWidgets.QSpacerItem(0, 0, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout_7.addItem(spacerItem1)
        self.fgdc_timeinfo.addWidget(self.fgdc_rngdates)
        self.fgdc_mdattim = QtWidgets.QWidget()
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.fgdc_mdattim.sizePolicy().hasHeightForWidth())
        self.fgdc_mdattim.setSizePolicy(sizePolicy)
        self.fgdc_mdattim.setObjectName("fgdc_mdattim")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout(self.fgdc_mdattim)
        self.verticalLayout_9.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.verticalLayout_9.setContentsMargins(4, 4, 4, 0)
        self.verticalLayout_9.setSpacing(3)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.layout_multipledates = QtWidgets.QVBoxLayout()
        self.layout_multipledates.setContentsMargins(-1, 0, -1, -1)
        self.layout_multipledates.setObjectName("layout_multipledates")
        self.horizontalLayout_6.addLayout(self.layout_multipledates)
        self.verticalLayout_9.addLayout(self.horizontalLayout_6)
        self.fgdc_timeinfo.addWidget(self.fgdc_mdattim)
        self.verticalLayout_2.addWidget(self.fgdc_timeinfo)
        self.horizontalLayout.addWidget(self.widget)
        self.verticalLayout_4.addWidget(self.widget_2)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_8 = QtWidgets.QLabel(self.fgdc_timeperd)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_8.sizePolicy().hasHeightForWidth())
        self.label_8.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label_8.setFont(font)
        self.label_8.setStyleSheet("font: bold;")
        self.label_8.setObjectName("label_8")
        self.verticalLayout.addWidget(self.label_8)
        self.fgdc_current = QtWidgets.QComboBox(self.fgdc_timeperd)
        self.fgdc_current.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.fgdc_current.setEditable(True)
        self.fgdc_current.setObjectName("fgdc_current")
        self.fgdc_current.addItem("")
        self.fgdc_current.setItemText(0, "")
        self.fgdc_current.addItem("")
        self.fgdc_current.addItem("")
        self.fgdc_current.addItem("")
        self.fgdc_current.addItem("")
        self.verticalLayout.addWidget(self.fgdc_current)
        self.verticalLayout_4.addLayout(self.verticalLayout)
        self.verticalLayout_11.addWidget(self.fgdc_timeperd)

        self.retranslateUi(Form)
        self.fgdc_timeinfo.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.fgdc_timeperd.setWhatsThis(_translate("Form", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">Time Period Information</span></p><p>&lt;FGDC shortname: <span style=\" font-style:italic;\">timeperd</span>&gt;</p><p><br/></p><p>Time period(s) for which the dataset corresponds to the currentness reference.</p><p><br/></p><p>Specify only one of:</p><p><span style=\" font-size:11pt;\">    single date if the dataset ... </span></p><p><span style=\" font-size:11pt;\">     a Date range if it ...</span></p><p><span style=\" font-size:11pt;\">    or multiple dates if ...</span></p><p><br/></p><p>Choose only one.</p></body></html>"))
        self.fgdc_timeperd.setTitle(_translate("Form", "Time Period Information"))
        self.label_2.setText(_translate("Form", "What is the time period represented in the dataset?"))
        self.label_3.setText(_translate("Form", "Select one of \'Single Date\', \'Date Range\', or \'Multiple Dates\'."))
        self.radio_single.setText(_translate("Form", "Single"))
        self.radio_range.setText(_translate("Form", "Range"))
        self.radio_multiple.setText(_translate("Form", "Multiple"))
        self.label_8.setWhatsThis(_translate("Form", "<html><head/><body><p>currentness what\'s this....</p><p>fakls;dfhjl;sakdjfl</p></body></html>"))
        self.label_8.setText(_translate("Form", "Currentness Reference"))
        self.fgdc_current.setItemText(1, _translate("Form", "ground condition"))
        self.fgdc_current.setItemText(2, _translate("Form", "observed"))
        self.fgdc_current.setItemText(3, _translate("Form", "publication date"))
        self.fgdc_current.setItemText(4, _translate("Form", "See Supplemental Info"))

