import sys
import locale
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel
from PyQt5.QtCore import Qt, QTimer
import psutil
from time import strftime

def get_battery_status():
    battery = psutil.sensors_battery()
    if battery is not None:
        return battery.percent, battery.power_plugged
    else:
        return None, None

class TransparentWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("bdt")  # Set the title here
        self.setWindowFlags(Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint)
        self.setAttribute(Qt.WA_TranslucentBackground, True)
        self.setGeometry(100, 100, 300, 100)

        self.time_label = QLabel(self)
        self.time_label.setAlignment(Qt.AlignCenter)
        self.time_label.setStyleSheet("QLabel { color: #a9a8a8; font-size: 24px; }")
        self.time_label.setGeometry(0, 0, 300, 50)

        self.date_label = QLabel(self)  # Add label for date
        self.date_label.setAlignment(Qt.AlignCenter)
        self.date_label.setStyleSheet("QLabel { color: #a9a8a8; font-size: 18px; }")
        self.date_label.setGeometry(0, 40, 300, 25)  # Adjust the position and height

        self.battery_label = QLabel(self)
        self.battery_label.setAlignment(Qt.AlignCenter)
        self.battery_label.setStyleSheet("QLabel { color: #a9a8a8; font-size: 18px; }")
        self.battery_label.setGeometry(0, 65, 300, 25)  # Adjust the position and height

        self.update_time_and_battery()

    def update_time_and_battery(self):
        time_string = strftime("%H:%M")
        # Set the locale to English explicitly
        locale.setlocale(locale.LC_TIME, 'en_US.UTF-8')
        date_string = strftime("%a, %m.%d")  # Using English month names
        self.time_label.setText(time_string)
        self.date_label.setText(date_string)

        battery_percent, is_plugged = get_battery_status()
        if battery_percent is not None:
            if is_plugged:
                self.battery_label.setText(f"⚡ {int(battery_percent)}%")
            else:
                self.battery_label.setText(f"{int(battery_percent)}%")

        # Update time and battery status every 1000ms
        QTimer.singleShot(1000, self.update_time_and_battery)

    def mousePressEvent(self, event):
        self.old_pos = event.globalPos()

    def mouseMoveEvent(self, event):
        delta = event.globalPos() - self.old_pos
        self.move(self.x() + delta.x(), self.y() + delta.y())
        self.old_pos = event.globalPos()

if __name__ == "__main__":
    app = QApplication(sys.argv)

    win = TransparentWindow()
    win.show()

    sys.exit(app.exec_())
