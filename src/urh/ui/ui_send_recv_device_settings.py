# -*- coding: utf-8 -*-

#
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_FormDeviceSettings(object):
    def setupUi(self, FormDeviceSettings):
        FormDeviceSettings.setObjectName("FormDeviceSettings")
        FormDeviceSettings.resize(860, 668)
        self.verticalLayout = QtWidgets.QVBoxLayout(FormDeviceSettings)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.groupBoxDeviceSettings = QtWidgets.QGroupBox(FormDeviceSettings)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.groupBoxDeviceSettings.setFont(font)
        self.groupBoxDeviceSettings.setStyleSheet("QGroupBox\n"
"{\n"
"border: none;\n"
"}\n"
"\n"
"QGroupBox::title {\n"
"    subcontrol-origin: margin;\n"
"}\n"
"QGroupBox::indicator:unchecked {\n"
" image: url(:/icons/icons/collapse.svg)\n"
"}\n"
"QGroupBox::indicator:checked {\n"
" image: url(:/icons/icons/uncollapse.svg)\n"
"}")
        self.groupBoxDeviceSettings.setFlat(True)
        self.groupBoxDeviceSettings.setCheckable(True)
        self.groupBoxDeviceSettings.setObjectName("groupBoxDeviceSettings")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.groupBoxDeviceSettings)
        self.gridLayout_6.setContentsMargins(-1, 15, -1, -1)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.frame_2 = QtWidgets.QFrame(self.groupBoxDeviceSettings)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.frame_2.setFont(font)
        self.frame_2.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setLineWidth(0)
        self.frame_2.setObjectName("frame_2")
        self.gridLayout = QtWidgets.QGridLayout(self.frame_2)
        self.gridLayout.setObjectName("gridLayout")
        self.label_3 = QtWidgets.QLabel(self.frame_2)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 0, 0, 1, 1)
        self.cbDevice = QtWidgets.QComboBox(self.frame_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cbDevice.sizePolicy().hasHeightForWidth())
        self.cbDevice.setSizePolicy(sizePolicy)
        self.cbDevice.setObjectName("cbDevice")
        self.cbDevice.addItem("")
        self.cbDevice.addItem("")
        self.gridLayout.addWidget(self.cbDevice, 0, 1, 1, 1)
        self.labelChannel = QtWidgets.QLabel(self.frame_2)
        self.labelChannel.setObjectName("labelChannel")
        self.gridLayout.addWidget(self.labelChannel, 2, 0, 1, 1)
        self.comboBoxChannel = QtWidgets.QComboBox(self.frame_2)
        self.comboBoxChannel.setObjectName("comboBoxChannel")
        self.gridLayout.addWidget(self.comboBoxChannel, 2, 1, 1, 1)
        self.labelAntenna = QtWidgets.QLabel(self.frame_2)
        self.labelAntenna.setObjectName("labelAntenna")
        self.gridLayout.addWidget(self.labelAntenna, 3, 0, 1, 1)
        self.comboBoxAntenna = QtWidgets.QComboBox(self.frame_2)
        self.comboBoxAntenna.setObjectName("comboBoxAntenna")
        self.gridLayout.addWidget(self.comboBoxAntenna, 3, 1, 1, 1)
        self.labelIP = QtWidgets.QLabel(self.frame_2)
        self.labelIP.setObjectName("labelIP")
        self.gridLayout.addWidget(self.labelIP, 4, 0, 1, 1)
        self.lineEditIP = QtWidgets.QLineEdit(self.frame_2)
        self.lineEditIP.setObjectName("lineEditIP")
        self.gridLayout.addWidget(self.lineEditIP, 4, 1, 1, 1)
        self.labelPort = QtWidgets.QLabel(self.frame_2)
        self.labelPort.setObjectName("labelPort")
        self.gridLayout.addWidget(self.labelPort, 5, 0, 1, 1)
        self.spinBoxPort = QtWidgets.QSpinBox(self.frame_2)
        self.spinBoxPort.setMinimum(1)
        self.spinBoxPort.setMaximum(65535)
        self.spinBoxPort.setProperty("value", 1234)
        self.spinBoxPort.setObjectName("spinBoxPort")
        self.gridLayout.addWidget(self.spinBoxPort, 5, 1, 1, 1)
        self.labelFreq = QtWidgets.QLabel(self.frame_2)
        self.labelFreq.setObjectName("labelFreq")
        self.gridLayout.addWidget(self.labelFreq, 6, 0, 1, 1)
        self.spinBoxFreq = KillerDoubleSpinBox(self.frame_2)
        self.spinBoxFreq.setDecimals(3)
        self.spinBoxFreq.setMinimum(0.001)
        self.spinBoxFreq.setMaximum(1000000000000.0)
        self.spinBoxFreq.setObjectName("spinBoxFreq")
        self.gridLayout.addWidget(self.spinBoxFreq, 6, 1, 1, 1)
        self.labelSampleRate = QtWidgets.QLabel(self.frame_2)
        self.labelSampleRate.setObjectName("labelSampleRate")
        self.gridLayout.addWidget(self.labelSampleRate, 7, 0, 1, 1)
        self.spinBoxSampleRate = KillerDoubleSpinBox(self.frame_2)
        self.spinBoxSampleRate.setDecimals(3)
        self.spinBoxSampleRate.setMinimum(0.001)
        self.spinBoxSampleRate.setMaximum(1000000000000.0)
        self.spinBoxSampleRate.setObjectName("spinBoxSampleRate")
        self.gridLayout.addWidget(self.spinBoxSampleRate, 7, 1, 1, 1)
        self.labelBandwidth = QtWidgets.QLabel(self.frame_2)
        self.labelBandwidth.setObjectName("labelBandwidth")
        self.gridLayout.addWidget(self.labelBandwidth, 8, 0, 1, 1)
        self.btnLockBWSR = QtWidgets.QToolButton(self.frame_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnLockBWSR.sizePolicy().hasHeightForWidth())
        self.btnLockBWSR.setSizePolicy(sizePolicy)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/icons/lock.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnLockBWSR.setIcon(icon)
        self.btnLockBWSR.setIconSize(QtCore.QSize(16, 16))
        self.btnLockBWSR.setCheckable(True)
        self.btnLockBWSR.setChecked(True)
        self.btnLockBWSR.setObjectName("btnLockBWSR")
        self.gridLayout.addWidget(self.btnLockBWSR, 7, 2, 2, 1)
        self.labelGain = QtWidgets.QLabel(self.frame_2)
        self.labelGain.setObjectName("labelGain")
        self.gridLayout.addWidget(self.labelGain, 9, 0, 1, 1)
        self.spinBoxBandwidth = KillerDoubleSpinBox(self.frame_2)
        self.spinBoxBandwidth.setDecimals(3)
        self.spinBoxBandwidth.setMinimum(0.001)
        self.spinBoxBandwidth.setMaximum(1000000000000.0)
        self.spinBoxBandwidth.setObjectName("spinBoxBandwidth")
        self.gridLayout.addWidget(self.spinBoxBandwidth, 8, 1, 1, 1)
        self.gridLayout_5 = QtWidgets.QGridLayout()
        self.gridLayout_5.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.sliderGain = QtWidgets.QSlider(self.frame_2)
        self.sliderGain.setMaximum(100)
        self.sliderGain.setSingleStep(1)
        self.sliderGain.setOrientation(QtCore.Qt.Horizontal)
        self.sliderGain.setObjectName("sliderGain")
        self.gridLayout_5.addWidget(self.sliderGain, 0, 0, 1, 1)
        self.spinBoxGain = QtWidgets.QSpinBox(self.frame_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.spinBoxGain.sizePolicy().hasHeightForWidth())
        self.spinBoxGain.setSizePolicy(sizePolicy)
        self.spinBoxGain.setMinimum(0)
        self.spinBoxGain.setMaximum(99)
        self.spinBoxGain.setProperty("value", 40)
        self.spinBoxGain.setObjectName("spinBoxGain")
        self.gridLayout_5.addWidget(self.spinBoxGain, 0, 1, 1, 1)
        self.gridLayout.addLayout(self.gridLayout_5, 9, 1, 1, 1)
        self.labelIFGain = QtWidgets.QLabel(self.frame_2)
        self.labelIFGain.setObjectName("labelIFGain")
        self.gridLayout.addWidget(self.labelIFGain, 10, 0, 1, 1)
        self.gridLayout_7 = QtWidgets.QGridLayout()
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.sliderIFGain = QtWidgets.QSlider(self.frame_2)
        self.sliderIFGain.setOrientation(QtCore.Qt.Horizontal)
        self.sliderIFGain.setObjectName("sliderIFGain")
        self.gridLayout_7.addWidget(self.sliderIFGain, 0, 0, 1, 1)
        self.spinBoxIFGain = QtWidgets.QSpinBox(self.frame_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.spinBoxIFGain.sizePolicy().hasHeightForWidth())
        self.spinBoxIFGain.setSizePolicy(sizePolicy)
        self.spinBoxIFGain.setObjectName("spinBoxIFGain")
        self.gridLayout_7.addWidget(self.spinBoxIFGain, 0, 1, 1, 1)
        self.gridLayout.addLayout(self.gridLayout_7, 10, 1, 1, 1)
        self.labelBasebandGain = QtWidgets.QLabel(self.frame_2)
        self.labelBasebandGain.setObjectName("labelBasebandGain")
        self.gridLayout.addWidget(self.labelBasebandGain, 11, 0, 1, 1)
        self.gridLayout_8 = QtWidgets.QGridLayout()
        self.gridLayout_8.setObjectName("gridLayout_8")
        self.sliderBasebandGain = QtWidgets.QSlider(self.frame_2)
        self.sliderBasebandGain.setSliderPosition(0)
        self.sliderBasebandGain.setOrientation(QtCore.Qt.Horizontal)
        self.sliderBasebandGain.setInvertedAppearance(False)
        self.sliderBasebandGain.setInvertedControls(False)
        self.sliderBasebandGain.setTickPosition(QtWidgets.QSlider.NoTicks)
        self.sliderBasebandGain.setTickInterval(0)
        self.sliderBasebandGain.setObjectName("sliderBasebandGain")
        self.gridLayout_8.addWidget(self.sliderBasebandGain, 0, 0, 1, 1)
        self.spinBoxBasebandGain = QtWidgets.QSpinBox(self.frame_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.spinBoxBasebandGain.sizePolicy().hasHeightForWidth())
        self.spinBoxBasebandGain.setSizePolicy(sizePolicy)
        self.spinBoxBasebandGain.setObjectName("spinBoxBasebandGain")
        self.gridLayout_8.addWidget(self.spinBoxBasebandGain, 0, 1, 1, 1)
        self.gridLayout.addLayout(self.gridLayout_8, 11, 1, 1, 1)
        self.labelFreqCorrection = QtWidgets.QLabel(self.frame_2)
        self.labelFreqCorrection.setObjectName("labelFreqCorrection")
        self.gridLayout.addWidget(self.labelFreqCorrection, 12, 0, 1, 1)
        self.spinBoxFreqCorrection = QtWidgets.QSpinBox(self.frame_2)
        self.spinBoxFreqCorrection.setMinimum(-1000)
        self.spinBoxFreqCorrection.setMaximum(1000)
        self.spinBoxFreqCorrection.setProperty("value", 1)
        self.spinBoxFreqCorrection.setObjectName("spinBoxFreqCorrection")
        self.gridLayout.addWidget(self.spinBoxFreqCorrection, 12, 1, 1, 1)
        self.labelDirectSampling = QtWidgets.QLabel(self.frame_2)
        self.labelDirectSampling.setObjectName("labelDirectSampling")
        self.gridLayout.addWidget(self.labelDirectSampling, 13, 0, 1, 1)
        self.comboBoxDirectSampling = QtWidgets.QComboBox(self.frame_2)
        self.comboBoxDirectSampling.setObjectName("comboBoxDirectSampling")
        self.gridLayout.addWidget(self.comboBoxDirectSampling, 13, 1, 1, 1)
        self.labelNRepeat = QtWidgets.QLabel(self.frame_2)
        self.labelNRepeat.setObjectName("labelNRepeat")
        self.gridLayout.addWidget(self.labelNRepeat, 14, 0, 1, 1)
        self.spinBoxNRepeat = QtWidgets.QSpinBox(self.frame_2)
        self.spinBoxNRepeat.setMaximum(999999999)
        self.spinBoxNRepeat.setObjectName("spinBoxNRepeat")
        self.gridLayout.addWidget(self.spinBoxNRepeat, 14, 1, 1, 1)
        self.labelDeviceIdentifier = QtWidgets.QLabel(self.frame_2)
        self.labelDeviceIdentifier.setObjectName("labelDeviceIdentifier")
        self.gridLayout.addWidget(self.labelDeviceIdentifier, 1, 0, 1, 1)
        self.comboBoxDeviceIdentifier = QtWidgets.QComboBox(self.frame_2)
        self.comboBoxDeviceIdentifier.setEditable(False)
        self.comboBoxDeviceIdentifier.setInsertPolicy(QtWidgets.QComboBox.NoInsert)
        self.comboBoxDeviceIdentifier.setObjectName("comboBoxDeviceIdentifier")
        self.gridLayout.addWidget(self.comboBoxDeviceIdentifier, 1, 1, 1, 1)
        self.btnRefreshDeviceIdentifier = QtWidgets.QToolButton(self.frame_2)
        icon = QtGui.QIcon.fromTheme("view-refresh")
        self.btnRefreshDeviceIdentifier.setIcon(icon)
        self.btnRefreshDeviceIdentifier.setObjectName("btnRefreshDeviceIdentifier")
        self.gridLayout.addWidget(self.btnRefreshDeviceIdentifier, 1, 2, 1, 1)
        self.gridLayout_6.addWidget(self.frame_2, 0, 0, 1, 1)
        self.verticalLayout.addWidget(self.groupBoxDeviceSettings)

        self.retranslateUi(FormDeviceSettings)
        self.groupBoxDeviceSettings.toggled['bool'].connect(self.frame_2.setVisible)
        FormDeviceSettings.setTabOrder(self.groupBoxDeviceSettings, self.cbDevice)
        FormDeviceSettings.setTabOrder(self.cbDevice, self.comboBoxChannel)
        FormDeviceSettings.setTabOrder(self.comboBoxChannel, self.comboBoxAntenna)
        FormDeviceSettings.setTabOrder(self.comboBoxAntenna, self.lineEditIP)
        FormDeviceSettings.setTabOrder(self.lineEditIP, self.spinBoxPort)
        FormDeviceSettings.setTabOrder(self.spinBoxPort, self.spinBoxFreq)
        FormDeviceSettings.setTabOrder(self.spinBoxFreq, self.spinBoxSampleRate)
        FormDeviceSettings.setTabOrder(self.spinBoxSampleRate, self.spinBoxBandwidth)
        FormDeviceSettings.setTabOrder(self.spinBoxBandwidth, self.btnLockBWSR)
        FormDeviceSettings.setTabOrder(self.btnLockBWSR, self.sliderGain)
        FormDeviceSettings.setTabOrder(self.sliderGain, self.spinBoxGain)
        FormDeviceSettings.setTabOrder(self.spinBoxGain, self.sliderIFGain)
        FormDeviceSettings.setTabOrder(self.sliderIFGain, self.spinBoxIFGain)
        FormDeviceSettings.setTabOrder(self.spinBoxIFGain, self.sliderBasebandGain)
        FormDeviceSettings.setTabOrder(self.sliderBasebandGain, self.spinBoxBasebandGain)
        FormDeviceSettings.setTabOrder(self.spinBoxBasebandGain, self.spinBoxFreqCorrection)
        FormDeviceSettings.setTabOrder(self.spinBoxFreqCorrection, self.comboBoxDirectSampling)
        FormDeviceSettings.setTabOrder(self.comboBoxDirectSampling, self.spinBoxNRepeat)

    def retranslateUi(self, FormDeviceSettings):
        _translate = QtCore.QCoreApplication.translate
        FormDeviceSettings.setWindowTitle(_translate("FormDeviceSettings", "Form"))
        self.groupBoxDeviceSettings.setTitle(_translate("FormDeviceSettings", "Device settings"))
        self.label_3.setText(_translate("FormDeviceSettings", "Device:"))
        self.cbDevice.setItemText(0, _translate("FormDeviceSettings", "USRP"))
        self.cbDevice.setItemText(1, _translate("FormDeviceSettings", "HackRF"))
        self.labelChannel.setText(_translate("FormDeviceSettings", "Channel:"))
        self.labelAntenna.setText(_translate("FormDeviceSettings", "Antenna:"))
        self.labelIP.setText(_translate("FormDeviceSettings", "IP address:"))
        self.lineEditIP.setText(_translate("FormDeviceSettings", "127.0.0.1"))
        self.labelPort.setText(_translate("FormDeviceSettings", "Port number:"))
        self.labelFreq.setText(_translate("FormDeviceSettings", "Frequency (Hz):"))
        self.labelSampleRate.setText(_translate("FormDeviceSettings", "Sample rate (Sps):"))
        self.labelBandwidth.setText(_translate("FormDeviceSettings", "Bandwidth (Hz):"))
        self.btnLockBWSR.setText(_translate("FormDeviceSettings", "..."))
        self.labelGain.setToolTip(_translate("FormDeviceSettings", "<html><head/><body><p>The gain (more exactly RF gain) is the gain applied to the RF signal. This amplifies the high frequent signal arriving at the antenna of your Software Defined Radio.</p></body></html>"))
        self.labelGain.setText(_translate("FormDeviceSettings", "Gain:"))
        self.sliderGain.setToolTip(_translate("FormDeviceSettings", "<html><head/><body><p>The gain (more exactly RF gain) is the gain applied to the RF signal. This amplifies the high frequent signal arriving at the antenna of your Software Defined Radio.</p></body></html>"))
        self.spinBoxGain.setToolTip(_translate("FormDeviceSettings", "<html><head/><body><p>The gain (more exactly RF gain) is the gain applied to the RF signal. This amplifies the high frequent signal arriving at the antenna of your Software Defined Radio.</p></body></html>"))
        self.labelIFGain.setToolTip(_translate("FormDeviceSettings", "<html><head/><body><p>The IF Gain is applied to the Intermediate Frequency signal in your Software Defined Radio. An IF signal has a lower frequency than the high frequent RF signal, so signal processing can be applied more efficiently.</p></body></html>"))
        self.labelIFGain.setText(_translate("FormDeviceSettings", "IF Gain:"))
        self.sliderIFGain.setToolTip(_translate("FormDeviceSettings", "<html><head/><body><p>The IF Gain is applied to the Intermediate Frequency signal in your Software Defined Radio. An IF signal has a lower frequency than the high frequent RF signal, so signal processing can be applied more efficiently.</p></body></html>"))
        self.spinBoxIFGain.setToolTip(_translate("FormDeviceSettings", "<html><head/><body><p>The IF Gain is applied to the Intermediate Frequency signal in your Software Defined Radio. An IF signal has a lower frequency than the high frequent RF signal, so signal processing can be applied more efficiently.</p></body></html>"))
        self.labelBasebandGain.setToolTip(_translate("FormDeviceSettings", "<html><head/><body><p>The baseband gain is applied to the baseband signal in your software defined radio. The baseband signal is at low frequency and gathered from the RF signal by <span style=\" font-weight:600;\">complex downsampling</span>.</p></body></html>"))
        self.labelBasebandGain.setText(_translate("FormDeviceSettings", "Baseband gain:"))
        self.sliderBasebandGain.setToolTip(_translate("FormDeviceSettings", "<html><head/><body><p>The baseband gain is applied to the baseband signal in your software defined radio. The baseband signal is at low frequency and gathered from the RF signal by <span style=\" font-weight:600;\">complex downsampling</span>.</p></body></html>"))
        self.spinBoxBasebandGain.setToolTip(_translate("FormDeviceSettings", "<html><head/><body><p>The baseband gain is applied to the baseband signal in your software defined radio. The baseband signal is at low frequency and gathered from the RF signal by <span style=\" font-weight:600;\">complex downsampling</span>.</p></body></html>"))
        self.labelFreqCorrection.setToolTip(_translate("FormDeviceSettings", "<html><head/><body><p>Set the frequency correction in <span style=\" font-weight:600;\">ppm</span>. If you do not know what to enter here, just leave it to one.</p></body></html>"))
        self.labelFreqCorrection.setText(_translate("FormDeviceSettings", "Frequency correction:"))
        self.spinBoxFreqCorrection.setToolTip(_translate("FormDeviceSettings", "<html><head/><body><p>Set the frequency correction in <span style=\" font-weight:600;\">ppm</span>. If you do not know what to enter here, just leave it to one.</p></body></html>"))
        self.labelDirectSampling.setToolTip(_translate("FormDeviceSettings", "<html><head/><body><p>Set the direct sampling mode. If you do not know what to choose here, just set it to disabled. The<span style=\" font-weight:600;\"> native backend</span> is recommended, when using this setting.</p></body></html>"))
        self.labelDirectSampling.setText(_translate("FormDeviceSettings", "Direct sampling:"))
        self.comboBoxDirectSampling.setToolTip(_translate("FormDeviceSettings", "<html><head/><body><p>Set the direct sampling mode. If you do not know what to choose here, just set it to disabled. The<span style=\" font-weight:600;\"> native backend</span> is recommended, when using this setting.</p></body></html>"))
        self.labelNRepeat.setText(_translate("FormDeviceSettings", "Repeat:"))
        self.spinBoxNRepeat.setSpecialValueText(_translate("FormDeviceSettings", "Infinite"))
        self.labelDeviceIdentifier.setText(_translate("FormDeviceSettings", "Device Identifier:"))
        self.btnRefreshDeviceIdentifier.setText(_translate("FormDeviceSettings", "..."))

from urh.ui.KillerDoubleSpinBox import KillerDoubleSpinBox
from . import urh_rc
