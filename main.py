import PySimpleGUI as sg
import codecs as cdc
import os.path
import json


def addtofile(credential, file):
    with open(file, 'a+') as fp:
        json.dump(credential, fp)
        fp.write('\n')


def readlines(file):
    with open(file, "r") as fp:
        data = [json.loads(cdc.decode(each_line, 'rot13')) for each_line in fp]
        return data


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
            global login_array
            login_array = readlines(loginfile)
            window.close()
        elif event == 'Cancel' or event == sg.WIN_CLOSED:
            break

    window.close()


def main():
    layout = [[sg.Text('Welcome to DigiCore Password Manager V1.0')],
              [sg.Table(values=login_array, headings=headings)],
              [sg.Button('Add'), sg.Button('Remove')]]
    window = sg.Window('Password Manager', layout)
    while True:
        event, values = window.read()
        if event == "Exit" or event == sg.WIN_CLOSED:
            break
        if event == 'Add':
            openAdd()

    window.close()


loginfile = 'dcore_logins.json'
headings = ['Username', 'Password', 'Site/Service']
sg.theme('DarkAmber')
login_array = readlines(loginfile)

if __name__ == "__main__":
    main()
