import sys
import requests
from PyQt5.QtCore import QSize
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QLineEdit, QVBoxLayout, QWidget

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setFixedSize(QSize(400, 300))

        self.setWindowTitle("My App")

        self.label = QLabel()
        self.answer = QLabel()

        self.input = QLineEdit()
        self.input.setPlaceholderText("Type city you're currently in...")
        self.input.textChanged.connect(self.weather)

        layout = QVBoxLayout()
        layout.addWidget(self.input)
        layout.addWidget(self.answer)
        layout.addWidget(self.label)

        container = QWidget()
        container.setLayout(layout)

        self.setCentralWidget(container)
    def weather(self):
        city =self.input.text()
        base_url = f"https://api.openweathermap.org/data/2.5/weather?appid=f68c228a96e5e4ece4a10a990838364c&q={city}&units=metric"
        owm_response = requests.get(base_url)
        if owm_response.status_code == 200:
            weather = owm_response.json()
            temp = weather['main']['temp']
            string = f"City: {city}\nTemperature: {temp}°C\nHumidity: {weather['main']['humidity']}%"
            self.label.setText(string)
            # answ = "A cold, isn't it?" if temp<=0  elif temp>0 and temp<10 ""  else ''#didn't work
            if temp <= 0:
                answ ="A cold, isn't it?"
            elif temp > 0 and temp < 10:
                answ ="Cool."
            else:
                answ ="Nice weather we're having."
            self.answer.setText(answ)

app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()


