import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLineEdit, QHBoxLayout, QVBoxLayout, QPushButton
class Calculator(QWidget):
    def __init__(self):
        super(Calculator, self).__init__()
        self.vbox = QVBoxLayout(self)
        self.hbox_input = QHBoxLayout()
        self.hbox_null = QHBoxLayout()
        self.hbox_first = QHBoxLayout()
        self.hbox_result = QHBoxLayout()
        self.hbox_fourth = QHBoxLayout()

        self.vbox.addLayout(self.hbox_input)
        self.vbox.addLayout(self.hbox_null)
        self.vbox.addLayout(self.hbox_first)
        self.vbox.addLayout(self.hbox_result)
        self.vbox.addLayout(self.hbox_fourth)

        self.input = QLineEdit(self)
        self.hbox_input.addWidget(self.input)

        self.b_1 = QPushButton("1", self)
        self.hbox_null.addWidget(self.b_1)

        self.b_2 = QPushButton("2", self)
        self.hbox_null.addWidget(self.b_2)

        self.b_3 = QPushButton("3", self)
        self.hbox_null.addWidget(self.b_3)

        self.b_4 = QPushButton("4", self)
        self.hbox_first.addWidget(self.b_4)

        self.b_5 = QPushButton("5", self)
        self.hbox_first.addWidget(self.b_5)

        self.b_6 = QPushButton("6", self)
        self.hbox_first.addWidget(self.b_6)

        self.b_7 = QPushButton("7", self)
        self.hbox_result.addWidget(self.b_7)

        self.b_8 = QPushButton("8", self)
        self.hbox_result.addWidget(self.b_8)

        self.b_9 = QPushButton("9", self)
        self.hbox_result.addWidget(self.b_9)

        self.b_0 = QPushButton("0", self)
        self.hbox_fourth.addWidget(self.b_0)

        self.b_plus = QPushButton("+", self)
        self.hbox_result.addWidget(self.b_plus)

        self.b_difference = QPushButton("-", self)
        self.hbox_result.addWidget(self.b_difference)

        self.b_result = QPushButton("=", self)
        self.hbox_result.addWidget(self.b_result)

        self.b_multiplication = QPushButton("*", self)
        self.hbox_first.addWidget(self.b_multiplication)

        self.b_division = QPushButton("/", self)
        self.hbox_first.addWidget(self.b_division)

        self.b_clear = QPushButton("C", self)
        self.hbox_first.addWidget(self.b_clear)

        self.b_dot = QPushButton(".", self)
        self.hbox_first.addWidget(self.b_dot)

        self.b_plus.clicked.connect(lambda: self._operation("+"))
        self.b_result.clicked.connect(self._result)
        self.b_difference.clicked.connect(lambda: self._operation("-"))
        self.b_multiplication.clicked.connect(lambda: self._operation("*"))
        self.b_division.clicked.connect(lambda: self._operation("/"))
        self.b_dot.clicked.connect(lambda: self._operation("."))
        self.b_clear.clicked.connect(lambda: self._operation("C"))

        self.b_1.clicked.connect(lambda: self._button("1"))
        self.b_2.clicked.connect(lambda: self._button("2"))
        self.b_3.clicked.connect(lambda: self._button("3"))
        self.b_4.clicked.connect(lambda: self._button("4"))
        self.b_5.clicked.connect(lambda: self._button("5"))
        self.b_6.clicked.connect(lambda: self._button("6"))
        self.b_7.clicked.connect(lambda: self._button("7"))
        self.b_8.clicked.connect(lambda: self._button("8"))
        self.b_9.clicked.connect(lambda: self._button("9"))
        self.b_0.clicked.connect(lambda: self._button("0"))

    def _button(self, param):
        line = self.input.text()
        self.input.setText(line + param)

    def _operation(self, op):
        self.num_1 = int(self.input.text())
        self.op = op
        self.input.setText("")

    def _result(self):
        self.num_2 = int(self.input.text())
        if self.op == "+":
            self.input.setText(str(float(self.num_1) + float(self.num_2)))
        if self.op =="-":
            self.input.setText(str(float(self.num_1) - float(self.num_2)))
        if self.op =="/":
            print(self.num_2)
            if self.num_2==0:
                print(self.num_2)
                self.line = self.input.setText('error')
            else:
                print(1)
                self.line.setText(str(float(self.num_1) / float(self.num_2)))

        if self.op == "*":
            self.line.setText(str(float(self.num1) * float(self.num2)))


app = QApplication(sys.argv)

win = Calculator()
win.show()

sys.exit(app.exec_())