from PyQt6.QtWidgets import QWidget, QLabel, QVBoxLayout

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Gestor de Clientes")
        self.setGeometry(100, 100, 800, 600)

        layout = QVBoxLayout()
        label = QLabel("Bem-vindo ao Gestor de Clientes!")

        layout.addWidget(label)
        self.setLayout(layout)
