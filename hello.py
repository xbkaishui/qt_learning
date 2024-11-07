import sys
from PySide2.QtWidgets import QApplication, QMainWindow, QTextEdit, QPushButton, QVBoxLayout, QWidget, QMessageBox, QSizePolicy

app = QApplication(sys.argv)
window = QMainWindow()
window.setFixedSize(500, 400)  # 设置主窗口宽500，高400
window.setWindowTitle("Hello PySide2")

# 创建一个中心小部件和布局
central_widget = QWidget()
layout = QVBoxLayout(central_widget)

def show_text():
    # 获取富文本框中的文本
    text = text_input.toPlainText()
    # 创建消息框并显示文本
    msg_box = QMessageBox()
    msg_box.setWindowTitle("hello")
    msg_box.setText(text)
    msg_box.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)  # 设置大小策略为可扩展
    msg_box.exec_()

# 添加富文本框和按钮
text_input = QTextEdit()
text_input.setFixedSize(200, 50)  # 设置宽200，高50
text_input.setStyleSheet("background-color: yellow;")  # 设置背景为蓝色

button = QPushButton("点击我")
button.clicked.connect(show_text)  # 连接按钮点击事件到 show_text 函数

layout.addWidget(text_input)
layout.addWidget(button)

window.setCentralWidget(central_widget)
window.show()

sys.exit(app.exec_())


