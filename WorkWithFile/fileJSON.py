import os
import json
import datetime
import PySimpleGUI  as sg

#3

class JSONFile:
    pathFile = ""
    students = {}
    students['student'] = []

    def loading(self):
        self.students['student'] = []
        if (os.path.isfile(self.pathFile)):
            with open(self.pathFile) as json_file:
                data = json.load(json_file)
                for p in data['student']:
                    self.students['student'].append({
                    'name': p['name'],
                    'age': p['age']
                })

    def writeToFile(self):
        with open(self.pathFile, 'w') as f:
            json.dump(self.students, f)
            sg.popup_ok('Данные записаны.')

    def readFromFile(self):
        try:
            with open(self.pathFile) as json_file:
                data = json.load(json_file)
                result =""
                for p in data['student']:
                    result += 'Name :' + p['name'] + '\nAge: ' + p['age']  + '\n'
                    self.students['student'].append({
                    'name': p['name'],
                    'age': p['age']
                })
                print (result)
        except BaseException:
            sg.popup_error("Файл не читаем")

    def addData(self, name, age):
        self.students['student'].append({
                    'name': name,
                    'age': age
                })

    def removeFile(self):
        os.remove(self.pathFile)
        sg.popup_ok("Файл удален")


fileJSON = JSONFile()

def openJSON():
    layout = [
    [sg.Text('Работа с JSON')],
    [sg.Text('Путь к файлу'), sg.InputText(key = "file_path"), sg.FileBrowse()], 
    [sg.Button('Удалить файл', key = 'delete_button'), sg.Button('Записать в файл', key = 'add_button'), sg.Button('Прочитать файл', key = 'read_button')],
    [sg.Output(size=(72, 15), key='file_output')]
    ]
    window = sg.Window('JSON', layout, modal=True)
    while True:                               
        event, values = window.read()
        if event in (None, 'Exit', 'Выход'):
            break

        if event == 'delete_button':
            window['file_output'].update('')
            fileJSON.pathFile = values['file_path']
            try:
                fileJSON.removeFile()
                window['file_path']('')
            except BaseException:
                sg.popup_error("Такого файла нет")

        
        if event == 'read_button':
            window['file_output'].update('')
            fileJSON.pathFile = values['file_path']
            fileJSON.loading()
            values['file_output'] = fileJSON.readFromFile()

        if event == 'add_button':
            window['file_output'].update('')
            if not values['file_path'].strip():
                sg.popup_error("Нет пути файла")
            else:
                fileJSON.pathFile = values['file_path']
                fileJSON.loading()
                openJSONAdd()



def openJSONAdd():
    layout = [
    [sg.Text('Добавление')],
    [sg.Text('Имя'), sg.InputText( key = "name")],
    [sg.Text('Возраст'), sg.InputText( key = "age")],
    [ sg.Button('Добавить', key = 'add_button')]
    ]
    
    window = sg.Window('XML', layout, modal=True)
    while True:                               
        event, values = window.read()
        if event in (None, 'Exit', 'Выход'):
            break

        
        if event == 'add_button':
            name = values['name']
            age = values['age']
            if  not name.strip() or not age.strip():
                sg.popup_error("Поля не заполнены")
            else:
                window['name']('')
                window['age']('')
                fileJSON.addData(name, age)
                fileJSON.writeToFile()
                window.close()
            
