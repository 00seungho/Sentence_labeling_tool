import json

from PySide6.QtWidgets import QApplication, QMainWindow, QMessageBox,QListWidgetItem,QGridLayout,QWidget,QLabel,QFileDialog
from PySide6.QtGui import QImage, QPixmap,QFontDatabase,QFont,QColor,QTextCharFormat,QTextCursor,QAction,QKeySequence,QShortcut
from main_ui import Ui_MainWindow
import sys
import pandas as pd
import os
import time
class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setFixedSize(800, 600)
        self.setupUi(self)
        self.fileopen.triggered.connect(self.load_tsv)
        self.org_value.setReadOnly(True)
        self.nowindex = 0
        self.lenvalue = 0
        self.tsvfile = None
        self.filename = ""
        self.next.clicked.connect(self.nextBtn)
        self.prev.clicked.connect(self.prevBtn)
        self.nextshortcut = QShortcut(QKeySequence("Ctrl+F"), self)
        self.nextshortcut.activated.connect(self.nextBtn)
        self.prevshortcut = QShortcut(QKeySequence("Ctrl+D"), self)
        self.prevshortcut.activated.connect(self.prevBtn)
        self.copyshortcut = QShortcut(QKeySequence("Ctrl+S"), self)
        self.copyshortcut.activated.connect(self.copyshortcutAct)
        self.resetshortcut = QShortcut(QKeySequence("Ctrl+Q"), self)
        self.resetshortcut.activated.connect(self.allDistory)
        self.nowsentence_value.returnPressed.connect(self.enterindex)
        self.help.triggered.connect(self.helpmsg)
    def helpmsg(self):
        QMessageBox.information(self,"단축키","원문 복사 CTRL + S \n라벨 문장 삭제 CTRL + Q \n다음 문장 CTRL + F\n이전 문장 CTRL + D")

    def allDistory(self):
        self.label_value.setText("")
    def enterindex(self):
        try:
            text = int(self.nowsentence_value.text())
        except ValueError as e:
            #문자열 들어올때 행동
            return
        if self.tsvfile is None:
            QMessageBox.warning(self, '경고', '파일을 먼저 선택해 주세요')
            return
        if text > self.lenvalue:
            QMessageBox.warning(self, '경고', f'{self.lenvalue}까지의 값을 입력해 주세요')
            return
        if text <= -1:
            QMessageBox.warning(self, '경고', f'0이상의 값을 입력해 주세요')
            return
        self.nowindex = text
        self.tsvfile.iloc[self.nowindex, 1] = self.label_value.toPlainText()
        self.save_tsv()
        self.writeMetaData()
        self.org_value.setText(self.tsvfile.iloc[self.nowindex, 0])
        if self.tsvfile.iloc[self.nowindex, 1] == "":
            self.label_value.setText("")
        else:
            self.label_value.setText(self.tsvfile.iloc[self.nowindex, 1])
        # self.nowsentence_value.setText(str(self.nowindex + 1))


    def copyshortcutAct(self):
        tempcopy = self.org_value.toPlainText()
        self.label_value.setText(tempcopy)

    def writeMetaData(self):
        with open(self.filename+"_meta_data.json", 'w',encoding="utf-8",) as jsonfile:
            newItem = {"nowindx":self.nowindex}
            json.dump(newItem,jsonfile)

    def load_tsv(self):
        filePath, _ = QFileDialog.getOpenFileName(self, '파일열기', '', 'tsv Files (*.tsv);;All Files (*)')
        if filePath:
            try:
                self.filename = os.path.splitext(filePath)[0]
                self.tsvfile = pd.read_csv(filePath,sep="\t")
                if "Kr" in self.tsvfile.columns:
                    self.tsvfile = self.tsvfile.fillna("")
                else:
                    self.tsvfile["Kr"] = ""
                if os.path.exists(self.filename+"_meta_data.json"):
                    with open(self.filename+"_meta_data.json", "r",encoding="utf-8") as jsfe:
                        metadata = json.load(jsfe)
                        self.nowindex = metadata["nowindx"]
                else:
                    self.writeMetaData()
                    self.nowindex = 0

                self.lenvalue = len(self.tsvfile)-1

                self.nowsentence_value.setText(str(self.nowindex))
                self.allsentence_value.setText(str(self.lenvalue))
                self.org_value.setText(self.tsvfile.iloc[self.nowindex,0])
                if self.tsvfile.iloc[self.nowindex,1] is None:
                    self.label_value.setText("")
                else:
                    self.label_value.setText(self.tsvfile.iloc[self.nowindex,1])
            except Exception as e:
                print(f"Error reading file: {e}")

    def save_tsv(self):
        self.tsvfile.to_csv(f'{self.filename}.tsv', sep='\t', index=False)

    def nextBtn(self):
        time.sleep(0.01)
        if self.filename == "":
            QMessageBox.warning(self, '경고', '파일을 먼저 선택해 주세요')
        else:
            if self.nowindex >= self.lenvalue:
                QMessageBox.warning(self, '경고', '문장의 끝 입니다.')
            else:
                self.tsvfile.iloc[self.nowindex,1] = self.label_value.toPlainText()
                self.save_tsv()
                self.nowindex += 1
                self.writeMetaData()
                self.org_value.setText(self.tsvfile.iloc[self.nowindex, 0])
                if self.tsvfile.iloc[self.nowindex, 1] == "":
                    self.label_value.setText("")
                else:
                    self.label_value.setText(self.tsvfile.iloc[self.nowindex, 1])
                self.nowsentence_value.setText(str(self.nowindex))


    def prevBtn(self):
        time.sleep(0.01)
        if self.filename == "":
            QMessageBox.warning(self, '경고', '파일을 먼저 선택해 주세요')
        else:
            self.tsvfile.iloc[self.nowindex, 1] = self.label_value.toPlainText()
            self.save_tsv()
            if self.nowindex == 0:
                QMessageBox.warning(self, '경고', '첫번째 문장입니다.')
            else:
                self.nowindex -= 1
                self.writeMetaData()
                self.org_value.setText(self.tsvfile.iloc[self.nowindex, 0])
                if self.tsvfile.iloc[self.nowindex, 1] == "":
                    self.label_value.setText("")
                else:
                    self.label_value.setText(self.tsvfile.iloc[self.nowindex, 1])
                self.nowsentence_value.setText(str(self.nowindex))

if __name__ == "__main__":
    app = QApplication(sys.argv)
    # QFontDatabase.addApplicationFont('font/NanumGothic.ttf')
    # font = QFont('NanumGothic.ttf')
    # app.setFont(font)
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec())
