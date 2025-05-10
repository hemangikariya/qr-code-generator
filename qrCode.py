
import sys
import qrcode
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QFileDialog, QMessageBox
from PyQt5.QtGui import QPixmap
from PIL import Image

class QRCodeApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QR Code Generator - PyQt5")
        self.setGeometry(100, 100, 400, 400)

        # Widgets
        self.label = QLabel("Enter text or URL:")
        self.input_field = QLineEdit()
        self.generate_btn = QPushButton("Generate QR")
        self.qr_label = QLabel()
        self.save_btn = QPushButton("Save QR Code")
        self.save_btn.setEnabled(False)

        # Layout
        layout = QVBoxLayout()
        layout.addWidget(self.label)
        layout.addWidget(self.input_field)
        layout.addWidget(self.generate_btn)
        layout.addWidget(self.qr_label)
        layout.addWidget(self.save_btn)

        self.setLayout(layout)

        # Actions
        self.generate_btn.clicked.connect(self.generate_qr)
        self.save_btn.clicked.connect(self.save_qr)

    def generate_qr(self):
        data = self.input_field.text().strip()
        if not data:
            QMessageBox.warning(self, "Warning", "Please enter some text or URL.")
            return

        qr = qrcode.make(data)
        qr.save("temp_qr.png")

        pixmap = QPixmap("temp_qr.png")
        self.qr_label.setPixmap(pixmap.scaled(200, 200))
        self.save_btn.setEnabled(True)

    def save_qr(self):
        file_path, _ = QFileDialog.getSaveFileName(self, "Save QR Code", "", "PNG Files (*.png);;All Files (*)")
        if file_path:
            img = Image.open("temp_qr.png")
            img.save(file_path)
            QMessageBox.information(self, "Saved", f"QR Code saved to:\n{file_path}")

# Run App
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = QRCodeApp()
    window.show()
    sys.exit(app.exec_())


