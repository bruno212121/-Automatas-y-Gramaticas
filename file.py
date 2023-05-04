import re 

class OpenFile:

    @staticmethod
    def read_file():
        file = open("Usuarios_WiFi.txt", "r")
        lines = file.readlines()
        file.close()
        #print("archivooooooo", lines)
        return lines

    @staticmethod
    def show_line(line):
        line = list(re.split(r'\n', line))
        #print("Lineas::",line)
        return line

read_file = OpenFile.read_file()
show = OpenFile.show_line(read_file[0])
