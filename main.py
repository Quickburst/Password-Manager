# DigiCore Password Manager
# Created by Rangga Ardianto 12/03/2022
# Last updated 13/04/2022


import PySimpleGUI as sg
import codecs as cdc
import json
import os


def add_to_file(credential, file):
    with open(file, 'a+') as fp:
        json.dump(credential, fp)
        fp.write('\n')


def read_lines(file):
    if os.path.exists(file):
        with open(file, "r") as fp:
            data = [json.loads(cdc.decode(each_line, 'rot13')) for each_line in fp]
            return data
    else:
        fp = open(file, 'w')


def open_add():
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
            add_to_file(credential, login_file)
            window.close()
            account_table.update(read_lines(login_file))
        elif event == 'Cancel' or event == sg.WIN_CLOSED:
            break

    window.close()


def main():
    layout = [[sg.Text('Welcome to DigiCore Password Manager V1.0')],
              [sg.Table(values=login_array, headings=headings, key='_table_', justification='left',
                        enable_events=True)],
              [sg.Button('Add'), sg.Button('Remove')]]
    window = sg.Window('Password Manager', layout)
    global account_table
    account_table = window['_table_']
    while True:
        event, values = window.read()
        if event == "Exit" or event == sg.WIN_CLOSED:
            break
        if event == 'Add':
            open_add()

    window.close()


login_file = 'dcore_logins.json'
headings = ['Username', 'Password', 'Site/Service']
sg.theme('DarkAmber')
login_array = read_lines(login_file)

if __name__ == "__main__":
    main()
