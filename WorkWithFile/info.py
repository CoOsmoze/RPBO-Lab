from asyncio.windows_events import NULL
import wmi

# 1
def startInfo():
    c = wmi.WMI ()
    result = ''
    for d in c.Win32_LogicalDisk():
        print(type(d.FreeSpace))
        freeplace = NULL
        place = NULL
        if (d.FreeSpace is None):
            freeplace = d.FreeSpace
            place = d.Size
        else:
            freeplace = round(int(d.FreeSpace) / 1024 / 1024 / 1024)
            place = round(int(d.Size) / 1024 / 1024 / 1024)
        #print(f"Название: {d.Caption}, Свободное пространство: {d.FreeSpace}, Объем диска: {d.Size}, Тип: {d.DriveType}, Метка: {d.VolumeName}")
        result += "Название: " + str(d.Caption) + ", Свободное пространство: " + str(freeplace) + ", Объем диска: " + str(place) + ",  Тип: " + str(d.DriveType) +", Метка: " + str(d.VolumeName) +"\n"
    return result