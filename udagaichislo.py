from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton
from PyQt6.QtCore import Qt
import random
import sys

class GuessNumberGame(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.secret_number = random.randint(1, 100)
        self.attempts_left = 5

        self.setWindowTitle("Угадай число")
        self.setGeometry(100, 100, 400, 200)

        self.label = QLabel("Введите число от 1 до 100:", self)
        self.entry = QLineEdit(self)
        self.submit_button = QPushButton("Проверить", self)
        self.result_label = QLabel("", self)

        self.submit_button.clicked.connect(self.check_guess)

        layout = QVBoxLayout(self)
        layout.addWidget(self.label)
        layout.addWidget(self.entry)
        layout.addWidget(self.submit_button)
        layout.addWidget(self.result_label)

    def check_guess(self):
        try:
            guess = int(self.entry.text())
        except ValueError:
            self.result_label.setText("Пожалуйста, введите целое число.")
            return

        if 1 <= guess <= 100:
            self.attempts_left -= 1
            if guess == self.secret_number:
                self.result_label.setText("Поздравляем! Вы угадали число.")
                self.submit_button.setDisabled(True)
            else:
                if guess < self.secret_number:
                    hint = "Больше."
                else:
                    hint = "Меньше."

                if self.attempts_left > 0:
                    self.result_label.setText(f"Неверно. {hint} Осталось попыток: {self.attempts_left}")
                else:
                    self.result_label.setText(f"Игра окончена. Вы не угадали. Загаданное число было {self.secret_number}.")
                    self.submit_button.setDisabled(True)
        else:
            self.result_label.setText("Пожалуйста, введите число от 1 до 100.")

def main():
    app = QApplication(sys.argv)
    game = GuessNumberGame()
    game.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()
