from PyQt5.QtWidgets import QApplication, QWidget
import GUI_ui


def fishButtonEvent():
    print("fish button clicked")  # PRINTER


def displayResButtonEvent(displayResText):
    print("display res changed to " + displayResText)  # PRINTER


def interactKeyButton():
    print("interact key button clicked")  # PRINTER


def createListeners():
    ui.fishButton.clicked.connect(fishButtonEvent)
    ui.displayResCombo.currentTextChanged.connect(displayResButtonEvent)
    ui.interactKeyButton.clicked.connect(interactKeyButton)


app = QApplication([])  # init app
window = QWidget()  # init window
ui = GUI_ui.Ui_window()  # assign auto-generated window object
ui.setupUi(window)  # create gui parts
createListeners()  # add event listeners
window.show()  # auto-hidden by default
app.exec()  # run event listener loop I think?
