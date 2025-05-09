import sys
from PyQt5.QtWidgets import QApplication, QLabel
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt, QTimer
import random
import os

class DuckWindow(QLabel):
    def __init__(self):
        super().__init__()
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.setWindowFlag(Qt.WindowStaysOnTopHint)
        self.setWindowFlag(Qt.Tool)
        self.setAttribute(Qt.WA_TranslucentBackground) #Transparent
        self.showFullScreen()

        base_path = os.path.dirname(os.path.abspath(sys.argv[0]))
        duck_image_path = os.path.join(base_path, 'duck.png')

        self.duck_pixmap = QPixmap(duck_image_path).scaled(80, 80) #80x80
        self.ducks = []

        screen_width = self.width()
        screen_height = self.height()

        for i in range(10):
            label = QLabel(self)
            label.setPixmap(self.duck_pixmap)
            label.move(random.randint(0, screen_width), random.randint(0, screen_height))
            label.show()
            self.ducks.append(label)

        self.timer = QTimer()
        self.timer.timeout.connect(self.move_ducks)
        self.timer.start(30)

    def move_ducks(self):
        for duck in self.ducks:
            x = duck.x() + 3
            if x > self.width():
                x = -80
            duck.move(x, duck.y())


    def close_window(self):
        self.close()

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Escape:
            QApplication.quit()

    def mousePressEvent(self, event):
        QApplication.quit()


def main():
    args = sys.argv
    #["duckFly.scr", "/s"]
    if len(args) > 1:
        arg = args[1].lower()
        if arg.startswith("/s"):
            app = QApplication(sys.argv)
            screenSaverWindow = DuckWindow()
            sys.exit(app.exec_())
        elif arg.startswith("/c"):
            print("Keine Einstellungen verfügbar.")
        elif arg.startswith("/p"):
            # Ignore
            pass
    else:
        # Fallback
        app = QApplication(sys.argv)
        screenSaverWindow = DuckWindow()
        sys.exit(app.exec_())

if __name__ == "__main__":
    main()