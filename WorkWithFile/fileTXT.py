from asyncio.windows_events import NULL
import os
import PySimpleGUI  as sg

#2
class TXTFile:
    pathFile = ""
    def writeFile(self, string):
        openFile = NULL
        if (os.path.isfile(self.pathFile)):
            openFile = open(self.pathFile, 'a')
        else:
            openFile = open(self.pathFile, 'w+')
        openFile.write(string)
        openFile.close()
        sg.popup_ok("Строка добавлена")
    
    def readFile(self):
        try:
            with open(self.pathFile, 'r') as f_obj:
                print (f_obj.read())
        except BaseException:
            sg.popup_error("Файл не читаем")
    
    def deleteFile(self):
        os.remove(self.pathFile)
        sg.popup_ok("Файл удален")


fileTXT = TXTFile()

def openTXT():
    layout = [
    [sg.Text('Работа с TXT')],
    [sg.Text('Путь к файлу'), sg.InputText(key = "file_path"), sg.FileBrowse()], 
    [sg.Button('Удалить файл', key = 'delete_button'), sg.Button('Добавить в файл', key = 'add_button'), sg.Button('Прочитать файл', key = 'read_button')],
    [sg.Output(size=(72, 15), key='file_output')]
    ]
    window = sg.Window('TXT', layout, modal=True)
    while True:                               
        event, values = window.read()
        if event in (None, 'Exit', 'Выход'):
            break

        if event == 'delete_button':
            window['file_output'].update('')
            fileTXT.pathFile = values['file_path']
            try:
                fileTXT.deleteFile()
                window['file_path']('')
            except BaseException:
                sg.popup_error("Такого файла нет")
        
        if event == 'read_button':
            window['file_output'].update('')
            fileTXT.pathFile = values['file_path']
            values['file_output'] = fileTXT.readFile()

        if event == 'add_button':
            if not values['file_path'].strip():
                sg.popup_error("Нет пути файла")
            else:
                fileTXT.pathFile = values['file_path']
                openTXTAdd()

def openTXTAdd():
    layout = [
    [sg.Text('Добавление строки')],
    [sg.InputText( key = "string")],
    [ sg.Button('Добавить', key = 'add_button')]
    ]
    
    window = sg.Window('TXT', layout, modal=True)
    while True:                               
        event, values = window.read()
        if event in (None, 'Exit', 'Выход'):
            break
        
        if event == 'add_button':
            string = values['string']
            if  not string.strip():
                sg.popup_error("Поле не заполнено")
            else:
                window['string']('')
                fileTXT.writeFile(string)
                window.close()