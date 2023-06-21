
from PyQt5.QtWidgets import QPushButton,QMessageBox, QDialog, QVBoxLayout, QLabel, QLineEdit, QDialogButtonBox
from ErrorHandler import WarningMessage

class ConfigDialog(QDialog):
    
    def __init__(self, callback_form):
        super().__init__()
        self.setWindowTitle("Configuration")
        self.resize(400,200)
        self.callback = callback_form
        layout = QVBoxLayout()

        label1 = QLabel("Enter your message:")
        label1.setStyleSheet("color: orange;")
        self.input1 = QLineEdit()
        self.input1.setPlaceholderText("Input your text here")
        self.input1.setStyleSheet("color:orange;")
        label2 = QLabel("Keys per Layer:")
        label2.setStyleSheet("color: orange;")
        self.input2 = QLineEdit()
        self.input2.setPlaceholderText("Input len of keys per layer")
        self.input2.setStyleSheet("color:orange;")
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
        if input1_value == "":
            WarningMessage("Invalid Input", "Message cannot be empty")
            return
        elif input2_value == "":
            WarningMessage("Invalid Input", "Keys per layer cannot be empty")
            return 
        elif not input1_value.replace(" ","").isalpha():
            WarningMessage( "Invalid Input", "Enter your message should contain only letters.")
            return
        elif not input2_value.isdigit():
            WarningMessage("Invalid Input","Keys per Layer should be an integer.")
            
            return
        
        self.accept(input1_value)
        
    def accept(self, input_value) -> None:
        self.callback(input_value)
        return super().accept()