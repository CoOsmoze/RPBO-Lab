import os
import PySimpleGUI  as sg
import zipfile
from tkinter import *
from tkinter.filedialog import askopenfilename

class ZIPFile:
    pathFile = ""
    def readArhive(self):
        try:
            with zipfile.ZipFile(self.pathFile, 'r') as zip:
                print('Содержимое архива:')
                zip.printdir()
        except BaseException:
            sg.popup_error("Архива нет")

    def arhive(self):
        with zipfile.ZipFile(self.pathFile, 'w') as zip:
            Tk().withdraw() 
            filename = askopenfilename()
            try:
                zip.write(filename, os.path.basename(filename))
                os.remove(filename)
            except BaseException:
                sg.popup_error("Не выбран файл для архивации")
                return
            print('Архивация. Данные об архиве:')
            print(os.stat(self.pathFile))
            print('Содержимое архива:')
            zip.printdir()

    def notArhive(self):
        if (zipfile.is_zipfile(self.pathFile)):
            zip = zipfile.ZipFile(self.pathFile, 'r')
            print('Разархивация. Данные о файле:')
            for file_info in zip.infolist(): 
                print(file_info.filename, file_info.date_time, file_info.file_size)
                zip.extract(file_info.filename.split('\\')[0])
            zip.close()
        else:
            sg.popup_error("Это не архив")

    def deleteZip(self):
            os.remove(self.pathFile)
            sg.popup_ok("Архив удален")

fileZIP = ZIPFile()

def openZIP():
    layout = [
    [sg.Text('Работа с ZIP')],
    [sg.Text('Архив:'), sg.InputText(key = "zip_path"), sg.Button('Удалить архив', key = 'delete_button')],
    [sg.Button('Прочитать архив', key = 'readArhive_button')],
    [sg.Button('Архивировать', key = 'arhive_button')],
    [sg.Button('Разархивировать', key = 'notarhive_button')],
    [sg.Output(size=(72, 15), key='file_output')]
    ]
    window = sg.Window('ZIP', layout, modal=True)
    while True:                               
        event, values = window.read()
        if event in (None, 'Exit', 'Выход'):
            break

        if event == 'delete_button':
            window['file_output'].update('')
            fileZIP.pathFile = values['zip_path']
            try:
                fileZIP.deleteZip()
                window['zip_path']('')
            except BaseException:
                sg.popup_error("Такого архива нет")

        if event == 'readArhive_button':
            window['file_output'].update('')
            if not values['zip_path'].strip():
                sg.popup_error("Нет пути к архиву")
            else:
                fileZIP.pathFile = values['zip_path']
                values['file_output'] = fileZIP.readArhive()
        
        if event == 'arhive_button':
            window['file_output'].update('')
            if not values['zip_path'].strip():
                sg.popup_error("Нет пути к архиву")
            else:
                fileZIP.pathFile = values['zip_path']
                values['file_output'] = fileZIP.arhive()

        if event == 'notarhive_button':
            window['file_output'].update('')
            if not values['zip_path'].strip():
                sg.popup_error("Нет пути к архиву")
            else:
                fileZIP.pathFile = values['zip_path']
                values['file_output'] = fileZIP.notArhive()


