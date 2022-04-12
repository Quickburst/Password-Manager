import PySimpleGUI as sg
import codecs as cdc
import os.path


def addtofile(credential, file):
    with open(file, 'a+') as f:
        f.write(str(credential))


def readlines(file):
    with open(file) as f:
        contents = f.read()
        return contents


def openAdd():
    credential = []
    layout = [[sg.Text('Credentials')],
              [sg.Text('Enter Username'), sg.InputText()],
              [sg.Text('Enter Password'), sg.InputText()],
              [sg.Text('Enter Site/Service'), sg.InputText()],
              [sg.Button('Ok'), sg.Button('Cancel')]]
    window = sg.Window('Add a login', layout, modal=True)
    while True:
        event, values = window.read()
        if event == 'Ok':
            credential.append(cdc.encode(values[0], 'rot_13'))
            credential.append(cdc.encode(values[1], 'rot_13'))
            credential.append(cdc.encode(values[2], 'rot_13'))
            addtofile(credential, loginfile)
            window.close()
        elif event == 'Cancel' or event == sg.WIN_CLOSED:
            break

    window.close()


def main():
    loginlist = []
    layout = [[sg.Text('Some text on Row 1')],
              [sg.Table(values=loginlist, headings=headings)],
              [sg.Button('Add'), sg.Button('Remove')]]
    window = sg.Window('Password Manager', layout)
    while True:
        event, values = window.read()
        if os.path.isfile(loginfile):
            loginlist = readlines(loginfile)
        if event == "Exit" or event == sg.WIN_CLOSED:
            break
        if event == 'Add':
            openAdd()

    window.close()


loginfile = 'dcore_logins.txt'
headings = ['Username', 'Password', 'Site/Service']
sg.theme('DarkAmber')

if __name__ == "__main__":
    main()
