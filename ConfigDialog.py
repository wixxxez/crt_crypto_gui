
from PyQt5.QtWidgets import QPushButton, QDialog, QVBoxLayout, QLabel, QLineEdit, QDialogButtonBox


class ConfigDialog(QDialog):
    
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Configuration")

        layout = QVBoxLayout()

        label1 = QLabel("Input 1:")
        self.input1 = QLineEdit()

        label2 = QLabel("Input 2:")
        self.input2 = QLineEdit()

        submit_button = QPushButton("Submit")
        submit_button.clicked.connect(self.submit)
        submit_button.setObjectName("SubmitButton")  # Set object name for the CSS styling

        layout.addWidget(label1)
        layout.addWidget(self.input1)
        layout.addWidget(label2)
        layout.addWidget(self.input2)
        layout.addWidget(submit_button)

        self.setLayout(layout)
    
    
    def submit(self):
        input1_value = self.input1.text()
        input2_value = self.input2.text()

        # Perform necessary actions with the input values
        print("Input 1:", input1_value)
        print("Input 2:", input2_value)

        self.accept()