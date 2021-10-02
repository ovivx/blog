import requests_html
from PySide2.QtWidgets import *
import sys


class ZRBZ():

    def __init__(self, title, num):

        self.url = "https://www.xiaodigu.cn/gpwz/?主题={}&字数=200".format(
            title, num)
        self.sess = requests_html.HTMLSession()

    def get_txt(self):

        r = self.sess.get(self.url)
        r.html.render()
        txt = r.html.find("div#文章", first=True).text
        return txt


class mianwindow(QWidget):

    def __init__(self):

        super().__init__()

        self.initUI()

    def initUI(self):

        self.setWindowTitle("狗屁不通感悟生成")
        self.setFixedSize(400, 300)

        self.lable = QLabel("论文名称", self)
        self.lable.move(5, 15)
        self.title_edit = QLineEdit(self)
        self.title_edit.move(60, 10)

        self.num_select_label = QLabel("字数",self)
        self.num_select_label.move(260,15)

        self.num_select = QSpinBox(self)
        self.num_select.setValue(60)
        self.num_select.move(300,10)

        self.text_edit = QTextEdit(self)
        self.text_edit.move(5,40)
        self.text_edit.setFixedSize(390,200)

        self.btn = QPushButton("生成或追加",self)
        self.btn.move(150,260)
        self.btn.clicked.connect(self.get_title)

    def get_title(self):

        title = self.title_edit.text()
        num = self.num_select.text()
        zrbz = ZRBZ(title,num)

        txt = zrbz.get_txt()

        with open("./感悟.txt","a") as f:

            f.write(f"{title}感悟")
            f.write("\n")
            f.write(txt)
            f.write("\n")

        self.text_edit.setText(txt)

        QMessageBox.information(self,"提示","狗屁不通的感悟已生成")

        




if __name__ == "__main__":

    app = QApplication(sys.argv)
    window = mianwindow()
    window.show()
    sys.exit(app.exec_())
