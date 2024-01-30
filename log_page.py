import sys
import os
from PyQt5.QtWidgets import (QApplication, QWidget, QPushButton, QTextEdit, QComboBox, QFileDialog,
                            QHBoxLayout, QVBoxLayout)

from main import MyApp

class LogPage(QWidget):
    def __init__(self):
        super().__init__()
        self.window_width, self.window_height = 400, 200
        self.setWindowTitle("Log_Page")
        self.setMinimumSize(self.window_width, self.window_height)


        layout = QVBoxLayout()
        self.setLayout(layout)


        btn = QPushButton('Escolher diretório')
        btn.setStyleSheet('''
        QPushButton {
            background-color: rgb(142, 202, 230);
            border-style: outset;
            border-width: 2px;
            border-radius: 10px;
            border-color: beige;
            font: bold 14px;
            min-width: 10em;
            padding: 6px;
        }
                          
        QPushButton#evilButton:pressed {
            background-color: rgb(224, 0, 0);
            border-style: inset;
        }
    ''')
        btn.clicked.connect(self.launchDialog)
        layout.addWidget(btn)

        self.textbox = QTextEdit()
       
        self.textbox.width = 50
        layout.addWidget(self.textbox)
        btn = QPushButton('Confirmar')
        btn.setStyleSheet('''
        QPushButton {
            background-color: rgb(142, 202, 230);
            border-style: outset;
            border-width: 2px;
            border-radius: 10px;
            border-color: beige;
            font: bold 14px;
            min-width: 10em;
            padding: 6px;
        }
                          
        QPushButton#evilButton:pressed {
            background-color: rgb(224, 0, 0);
            border-style: inset;
        }
    ''')
        btn.width = 100
        btn.clicked.connect(self.launchDialog)
        layout.addWidget(btn)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setStyleSheet('''
        QWidget {
            font-size: 20px;
        }
    ''')
    
    myApp = MyApp()

    myApp.show()

    try:
        sys.exit(app.exec())
    except SystemExit:
        print('Closing Window...')