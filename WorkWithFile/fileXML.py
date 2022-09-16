import os
import xml.etree.ElementTree as ET
import xml.dom.minidom
import PySimpleGUI  as sg

#4
class XMLFile:
    pathFile = ""
    def readFile(self):
        try:
            dom = xml.dom.minidom.parse(self.pathFile)
            pretty_xml_as_string = dom.toprettyxml()
            print(pretty_xml_as_string)
        except BaseException:
            sg.popup_error("Файл не читаем")
    
    def writeFile(self, authorText, titleText):
        if (os.path.isfile(self.pathFile)):

            parser = ET.XMLParser(encoding="utf-8")
            tree = ET.parse(self.pathFile, parser=parser)

            root = tree.getroot()
            book = ET.SubElement(root, 'book')

            author = ET.SubElement(book, 'author')
            title = ET.SubElement(book, 'title')
            author.text = authorText
            title.text = titleText
            tree.write(self.pathFile, encoding="utf-8")
            sg.popup_ok("Запись добавлена")
        else:
            sg.popup_ok("Файла с таким названием нет, он будет создан")
            data = ET.Element('library')
            book = ET.SubElement(data, 'book')
            author = ET.SubElement(book, 'author')
            title = ET.SubElement(book, 'title')
            author.text = authorText
            title.text = titleText
            mydata = ET.tostring(data, encoding="utf-8", method="xml")
            with open(self.pathFile, 'w', encoding='utf-8') as myfile:
                myfile.write(mydata.decode(encoding = "utf-8"))
            sg.popup_ok("Запись добавлена")
            sg.ok
    
    def deleteFile(self):
        os.remove(self.pathFile)
        sg.popup_ok("Файл удален")

fileXML = XMLFile()

def openXml():
    layout = [
    [sg.Text('Работа с XML')],
    [sg.Text('Путь к файлу'), sg.InputText(key = "file_path"), sg.FileBrowse()], 
    [sg.Button('Удалить файл', key = 'delete_button'), sg.Button('Добавить в файл', key = 'add_button'), sg.Button('Прочитать файл', key = 'read_button')],
    [sg.Output(size=(72, 15), key='file_output')]
    ]
    window = sg.Window('XML', layout, modal=True)
    while True:                               
        event, values = window.read()
        if event in (None, 'Exit', 'Выход'):
            break

        if event == 'delete_button':
            window['file_output'].update('')
            fileXML.pathFile = values['file_path']
            try:
                fileXML.deleteFile()
                window['file_path']('')
            except BaseException:
                sg.popup_error("Такого файла нет")

        
        if event == 'read_button':
            window['file_output'].update('')
            fileXML.pathFile = values['file_path']
            values['file_output'] = fileXML.readFile()

        if event == 'add_button':
            window['file_output'].update('')
            if not values['file_path'].strip():
                sg.popup_error("Нет пути файла")
            else:
                fileXML.pathFile = values['file_path']
                openXmlAdd()



def openXmlAdd():
    layout = [
    [sg.Text('Добавление')],
    [sg.Text('Автор'), sg.InputText( key = "author")],
    [sg.Text('Название книги'), sg.InputText( key = "title")],
    [ sg.Button('Добавить', key = 'add_button')]
    ]
    
    window = sg.Window('XML', layout, modal=True)
    while True:                               
        event, values = window.read()
        if event in (None, 'Exit', 'Выход'):
            break

        
        if event == 'add_button':
            author = values['author']
            title = values['title']
            if  not author.strip() or not title.strip():
                sg.popup_error("Поля не заполнены")
            else:
                window['author']('')
                window['title']('')
                fileXML.writeFile(author, title)
                window.close()
            
