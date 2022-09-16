import PySimpleGUI  as sg
from PySimpleGUI.PySimpleGUI import InputText
from fileXML import openXml
from fileTXT import openTXT
from info import startInfo
from fileJSON import openJSON
from fileZIP import openZIP


def main():
    layout = [
    [sg.Text('Разработка безопасного программного обеспечения. Практика 1'), sg.Cancel('Выход')],
    [sg.Button('Информация', key = 'info_button'), sg.Button('TXT файл', key = 'txtFile_button'), sg.Button('XML файл', key = 'xmlFile_button'),sg.Button('JSON файл', key = 'jsonFile_button'), sg.Button('ZIP архив', key = 'zipFile_button')],
    [sg.Output(size=(76, 15), key='file_output')]
    ]
    window = sg.Window('Pr1', layout)
    while True:                               
        event, values = window.read()
        if event in (None, 'Exit', 'Выход'):
            break

        if event == 'txtFile_button':
            window['file_output'].update('')
            openTXT()

        if event == 'xmlFile_button':
            window['file_output'].update('')
            openXml()

        if event == 'info_button':
            window['file_output'].update('')
            window['file_output'].update(startInfo())

        if event == 'jsonFile_button':
            window['file_output'].update('')
            openJSON()

        if event == 'zipFile_button':
            window['file_output'].update('')
            openZIP()



if __name__ == "__main__":
    main()