# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'toolbox.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QInputDialog, QLineEdit, QFileDialog
from PIL import Image, ImageTk
import keras
from keras.models import load_model
import cv2
from tkinter import filedialog
import easygui
import glob
import imutils
import copy
import numpy as np
class Ui_Plant_disease_Tool_Box(object):
    def setupUi(self, Plant_disease_Tool_Box):
        Plant_disease_Tool_Box.setObjectName("Plant_disease_Tool_Box")
        Plant_disease_Tool_Box.resize(1156, 722)
        Plant_disease_Tool_Box.setStyleSheet("border-bottom-color: qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.5, stop:0 rgba(175, 179, 185, 255), stop:1 rgba(255, 255, 255, 255));")
        self.label = QtWidgets.QLabel(Plant_disease_Tool_Box)
        self.label.setGeometry(QtCore.QRect(410, 20, 451, 51))
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Plant_disease_Tool_Box)
        self.label_2.setGeometry(QtCore.QRect(290, 140, 371, 291))
        font = QtGui.QFont()
        font.setFamily("Courier 10 Pitch")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Plant_disease_Tool_Box)
        self.label_3.setGeometry(QtCore.QRect(730, 140, 371, 291))
        font = QtGui.QFont()
        font.setFamily("Courier 10 Pitch")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.groupBox = QtWidgets.QGroupBox(Plant_disease_Tool_Box)
        self.groupBox.setGeometry(QtCore.QRect(30, 40, 211, 341))
        font = QtGui.QFont()
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.groupBox.setFont(font)
        self.groupBox.setObjectName("groupBox")
        self.label_5 = QtWidgets.QLabel(self.groupBox)
        self.label_5.setGeometry(QtCore.QRect(10, 180, 171, 17))
        self.label_5.setText("")
        self.label_5.setObjectName("label_5")
        self.checkBox = QtWidgets.QCheckBox(self.groupBox)
        self.checkBox.setGeometry(QtCore.QRect(0, 250, 211, 22))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.checkBox.setFont(font)
        self.checkBox.setObjectName("checkBox")
        self.checkBox_2 = QtWidgets.QCheckBox(self.groupBox)
        self.checkBox_2.setGeometry(QtCore.QRect(10, 50, 171, 22))
        self.checkBox_2.setObjectName("checkBox_2")
        self.checkBox_3 = QtWidgets.QCheckBox(self.groupBox)
        self.checkBox_3.setGeometry(QtCore.QRect(10, 90, 141, 22))
        self.checkBox_3.setObjectName("checkBox_3")
        self.checkBox_4 = QtWidgets.QCheckBox(self.groupBox)
        self.checkBox_4.setGeometry(QtCore.QRect(10, 130, 141, 22))
        self.checkBox_4.setObjectName("checkBox_4")
        self.checkBox_5 = QtWidgets.QCheckBox(self.groupBox)
        self.checkBox_5.setGeometry(QtCore.QRect(10, 170, 191, 22))
        self.checkBox_5.setObjectName("checkBox_5")
        self.pushButton_3 = QtWidgets.QPushButton(Plant_disease_Tool_Box)
        self.pushButton_3.setEnabled(True)
        self.pushButton_3.setGeometry(QtCore.QRect(300, 620, 111, 27))
        self.pushButton_3.setAutoDefault(True)
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton = QtWidgets.QPushButton(Plant_disease_Tool_Box)
        self.pushButton.setGeometry(QtCore.QRect(700, 620, 99, 27))
        self.pushButton.setAutoDefault(True)
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(Plant_disease_Tool_Box)
        self.pushButton_2.setGeometry(QtCore.QRect(500, 620, 111, 27))
        self.pushButton_2.setAutoDefault(True)
        self.pushButton_2.setObjectName("pushButton_2")

        self.retranslateUi(Plant_disease_Tool_Box)
        QtCore.QMetaObject.connectSlotsByName(Plant_disease_Tool_Box)

    def retranslateUi(self, Plant_disease_Tool_Box):
        _translate = QtCore.QCoreApplication.translate
        Plant_disease_Tool_Box.setWindowTitle(_translate("Plant_disease_Tool_Box", "Dialog"))
        self.label.setText(_translate("Plant_disease_Tool_Box", "Plant Disease Classification Tool Box"))
        self.label_2.setText(_translate("Plant_disease_Tool_Box", "              Input"))
        self.label_3.setText(_translate("Plant_disease_Tool_Box", "              Output"))
        self.groupBox.setTitle(_translate("Plant_disease_Tool_Box", "    Trained Models"))
        self.checkBox.setText(_translate("Plant_disease_Tool_Box", "Real Time classification"))
        self.checkBox_2.setText(_translate("Plant_disease_Tool_Box", " Load_VGG16"))
        self.checkBox_3.setText(_translate("Plant_disease_Tool_Box", "Load_Resnet18"))
        self.checkBox_4.setText(_translate("Plant_disease_Tool_Box", "Load_Resnet34"))
        self.checkBox_5.setText(_translate("Plant_disease_Tool_Box", "Load_Custom_model"))
        self.pushButton_3.setText(_translate("Plant_disease_Tool_Box", "Load_Image"))
        self.pushButton.setText(_translate("Plant_disease_Tool_Box", "Stop"))
        self.pushButton_2.setText(_translate("Plant_disease_Tool_Box", "Process"))
        self.pushButton_3.clicked.connect(self.load_image)
        self.pushButton.clicked.connect(self.stop)
        self.pushButton_2.clicked.connect(self.process)



    def load_image(self):
            global image
            global a
            global qImg
            path = easygui.fileopenbox()
            image = cv2.cvtColor(cv2.imread(path), cv2.COLOR_BGR2RGB)
            image = cv2.resize(image, (371, 291))
            height, width, channel = image.shape
            bytesPerLine = 3 * width
            qImg = QImage(image.data, width, height, bytesPerLine, QImage.Format_RGB888)
            pixmap = QPixmap(qImg)
            self.label_2.setPixmap(pixmap)
            self.label_3.clear()
            a = image

    def realtime(self):
        global cap
        path = easygui.fileopenbox()
        # path = QFileDialog.getOpenFileName(self, 'Load', '/home')
        model = load_model(path)
        # model = load_model('../saved_models/resnet18.h5')
        # list the classes
        classes = ['Black_Measles', 'Blackrot', 'Isariopsis', "MDB_disease", "No_disease", "Spyder", "mildiou"]

        cap = cv2.VideoCapture(0)

        while True:
            _, frame = cap.read()

            # Convert the captured frame into RGB

            output = frame.copy()
            # output = imutils.resize(output, width=400)

            # our model was trained on RGB ordered images but OpenCV represents
            # images in BGR order, so swap the channels, and then resize to
            # 224x224 (the input dimensions for VGG16)
            image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            image = cv2.resize(image, (256, 256))

            image = np.reshape(image, [1, 256, 256, 3])
            image = image.astype("float32") / 255

            preds = model.predict(image)

            # label
            i = np.argmax(preds)
            label = classes[i]

            # draw the prediction on the output image
            text = "{}: {:.2f}%  ".format(label, preds.item(i) * 100)
            text2 = "Press Q to Stop"
            cv2.putText(output, text, (5, 20), cv2.FONT_HERSHEY_SIMPLEX, 1.0, (0, 0, 255), 2)
            cv2.putText(output, text2, (5, 60), cv2.FONT_HERSHEY_SIMPLEX, 1.0, (0, 0, 255), 2)
            # show the output image
            cv2.imshow("Output", output)
            nn = cv2.resize(output, (371, 291))
            frame2 = cv2.cvtColor(nn, cv2.COLOR_BGR2RGB)
            h, w, ch = frame2.shape
            bytesPerLine = ch * w
            convertToQtFormat = QtGui.QImage(frame2.data, w, h, bytesPerLine, QtGui.QImage.Format_RGB888)
            pixmap = QPixmap(convertToQtFormat)
            self.label_3.setPixmap(pixmap)

            key = cv2.waitKey(1)
            if key == ord('q'):
                break

        cap.release()
        cv2.destroyAllWindows()
        self.label_3.clear()

    def Vgg(self):
        path = easygui.fileopenbox()
        # path = QFileDialog.getOpenFileName(self, 'Load', '/home')
        model = load_model(path)
        output = a.copy()
        output = cv2.cvtColor(a, cv2.COLOR_BGR2RGB)
        output = imutils.resize(output, width=400)
        image = cv2.resize(a, (256, 256))

        image = np.reshape(image, [1, 256, 256, 3])
        image = image.astype("float32") / 255

        # predict
        pred = model.predict(image)

        # list the classes
        classes = ['Black_Measles', 'Blackrot', 'Isariopsis', "MDB_disease", "No_disease", "Spyder", "mildiou"]

        # label
        i = np.argmax(pred)
        label = classes[i]

        # draw the prediction on the output image
        text = "{}: {:.2f}%".format(label, pred.item(i) * 100)
        cv2.putText(output, text, (3, 40), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 0, 255), 2)
        # cv2.imshow("Output", output)
        img2 = cv2.cvtColor(output, cv2.COLOR_BGR2RGB)
        height, width, channel = img2.shape
        bytesPerLine = 3 * width
        qImg = QImage(img2.data, width, height, bytesPerLine, QImage.Format_RGB888)
        pixmap = QPixmap(qImg)
        self.label_3.setPixmap(pixmap)


    def resnet18(self):
        path = easygui.fileopenbox()
        # path = QFileDialog.getOpenFileName(self, 'Load', '/home')
        model = load_model(path)
        output = a.copy()
        output = cv2.cvtColor(a, cv2.COLOR_BGR2RGB)
        output = imutils.resize(output, width=400)
        image = cv2.resize(a, (256, 256))

        image = np.reshape(image, [1, 256, 256, 3])
        image = image.astype("float32") / 255

        # predict
        pred = model.predict(image)

        # list the classes
        classes = ['Black_Measles', 'Blackrot', 'Isariopsis', "MDB_disease", "No_disease", "Spyder", "mildiou"]

        # label
        i = np.argmax(pred)
        label = classes[i]

        # draw the prediction on the output image
        text = "{}: {:.2f}%".format(label, pred.item(i) * 100)
        cv2.putText(output, text, (3, 40), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 0, 255), 2)
        # cv2.imshow("Output", output)
        img2 = cv2.cvtColor(output, cv2.COLOR_BGR2RGB)
        height, width, channel = img2.shape
        bytesPerLine = 3 * width
        qImg = QImage(img2.data, width, height, bytesPerLine, QImage.Format_RGB888)
        pixmap = QPixmap(qImg)
        self.label_3.setPixmap(pixmap)

    def resnet34(self):
        path = easygui.fileopenbox()
        # path = QFileDialog.getOpenFileName(self, 'Load', '/home')
        model = load_model(path)
        output = a.copy()
        output = cv2.cvtColor(a, cv2.COLOR_BGR2RGB)
        output = imutils.resize(output, width=400)
        image = cv2.resize(a, (256, 256))

        image = np.reshape(image, [1, 256, 256, 3])
        image = image.astype("float32") / 255

        # predict
        pred = model.predict(image)

        # list the classes
        classes = ['Black_Measles', 'Blackrot', 'Isariopsis', "MDB_disease", "No_disease", "Spyder", "mildiou"]

        # label
        i = np.argmax(pred)
        label = classes[i]

        # draw the prediction on the output image
        text = "{}: {:.2f}%".format(label, pred.item(i) * 100)
        cv2.putText(output, text, (3, 40), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 0, 255), 2)
        # cv2.imshow("Output", output)
        img2 = cv2.cvtColor(output, cv2.COLOR_BGR2RGB)
        height, width, channel = img2.shape
        bytesPerLine = 3 * width
        qImg = QImage(img2.data, width, height, bytesPerLine, QImage.Format_RGB888)
        pixmap = QPixmap(qImg)
        self.label_3.setPixmap(pixmap)

    def custom_model(self):
        path = easygui.fileopenbox()
        # path = QFileDialog.getOpenFileName(self, 'Load', '/home')
        model = load_model(path)
        output = a.copy()
        output = cv2.cvtColor(a, cv2.COLOR_BGR2RGB)
        output = imutils.resize(output, width=400)
        image = cv2.resize(a, (256, 256))

        image = np.reshape(image, [1, 256, 256, 3])
        image = image.astype("float32") / 255

        # predict
        pred = model.predict(image)

        # list the classes
        classes = ['Black_Measles', 'Blackrot', 'Isariopsis', "MDB_disease", "No_disease", "Spyder", "mildiou"]

        # label
        i = np.argmax(pred)
        label = classes[i]

        # draw the prediction on the output image
        text = "{}: {:.2f}%".format(label, pred.item(i) * 100)
        cv2.putText(output, text, (3, 40), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 0, 255), 2)
        # cv2.imshow("Output", output)
        img2 = cv2.cvtColor(output, cv2.COLOR_BGR2RGB)
        height, width, channel = img2.shape
        bytesPerLine = 3 * width
        qImg = QImage(img2.data, width, height, bytesPerLine, QImage.Format_RGB888)
        pixmap = QPixmap(qImg)
        self.label_3.setPixmap(pixmap)


    def stop(self):
        if cv2.waitKey(1):
            #cap = cv2.VideoCapture(0)
            cap.release()
            cv2.destroyAllWindows()
            self.label_3.clear()

    def process(self,i):
      if self.checkBox.isChecked() == True:
            self.realtime()
      elif self.checkBox_2.isChecked() == True:
            self.Vgg()
      elif self.checkBox_3.isChecked() == True:
               self.resnet18()
      elif self.checkBox_4.isChecked() == True:
                self.resnet34()
      elif self.checkBox_5.isChecked() == True:
                self.custom_model()
      else:
          pass

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Plant_disease_Tool_Box = QtWidgets.QDialog()
    ui = Ui_Plant_disease_Tool_Box()
    ui.setupUi(Plant_disease_Tool_Box)
    Plant_disease_Tool_Box.show()
    sys.exit(app.exec_())
