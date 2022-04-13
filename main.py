# DigiCore Password Manager
# Created by Rangga Ardianto 12/03/2022
# Last updated 14/04/2022

# Import modules
import PySimpleGUI as sg
import codecs as cdc
import json
import os


def add_to_file(credential, file):
    with open(file, 'a+') as fp:  # Open file for appending
        json.dump(credential, fp)  # Append to json
        fp.write('\n')  # Make a new line


# Interpret JSON file
def read_lines(file):
    if os.path.exists(file):  # Check if file exists
        with open(file, "r") as fp:
            # Load each line for array and decode cipher
            data = [json.loads(cdc.decode(each_line, 'rot13')) for each_line in fp]
            return data
    else:
        fp = open(file, 'w')  # Create new file


# Window for data entry
def open_add():
    credential = []  # A record if you will
    # Layout of GUI
    layout = [[sg.Text('Credentials')],
              [sg.Text('Enter Username'), sg.InputText()],
              [sg.Text('Enter Password'), sg.InputText()],
              [sg.Text('Enter Site/Service'), sg.InputText()],
              [sg.Button('Ok'), sg.Button('Cancel')]]  # 'Ok' and 'Cancel' buttons
    window = sg.Window('Add a login', layout, modal=True)  # Sets name of window and it's layout
    while True:
        event, values = window.read()  # Always read window inputs
        if event == 'Ok':  # If 'Ok' button is pressed
            # Append and encode each index of record
            credential.append(cdc.encode(values[0], 'rot_13'))
            credential.append(cdc.encode(values[1], 'rot_13'))
            credential.append(cdc.encode(values[2], 'rot_13'))
            add_to_file(credential, login_file)  # Appends to file
            window.close()
            account_table.update(read_lines(login_file))  # Refreshes table
        elif event == 'Cancel' or event == sg.WIN_CLOSED:
            break

    window.close()


def main():
    layout = [[sg.Text('Welcome to DigiCore Password Manager V1.0')],
              [sg.Table(values=login_array,
                        headings=headings,
                        key='_table_',
                        justification='left',
                        enable_events=True)],  # Enable outputs from table
              [sg.Button('Add'), sg.Button('Remove'), sg.Button('Exit')]]
    window = sg.Window('Password Manager', layout)
    global account_table
    account_table = window['_table_']  # The table object
    while True:
        event, values = window.read()
        if event == "Exit" or event == sg.WIN_CLOSED:
            break
        if event == 'Add':
            open_add()
        if event == '_table_':
            if values['_table_']:  # Checks if table has any values before setting index
                selected_row_index = values['_table_'][0]
            else:
                pass  # Do nothing

        if event == 'Remove':
            remove_row(login_file, selected_row_index)
            account_table.update(read_lines(login_file))

    window.close()


def remove_row(file, row):
    with open(login_file, "r+") as f:
        lines = f.readlines()  # Interpret lines
        del lines[row]  # Delete the line in the selected row
        f.seek(0)
        f.truncate()
        f.writelines(lines)  # Rewrite lines to apply changes


login_file = 'dcore_logins.json'
headings = ['Username', 'Password', 'Site/Service']
sg.theme('DarkAmber')  # GUI Theme
login_array = read_lines(login_file)

# Calls main to begin program
if __name__ == "__main__":
    main()
