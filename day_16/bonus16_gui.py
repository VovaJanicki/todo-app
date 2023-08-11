import PySimpleGUI as sg
import make_archive from zip_crator
label1 = sg.Text("Select files to compress: ")
input1 = sg.Input()
choose_button1 = sg.FilesBrowse("Choose", key="file")

label2 = sg.Text("Select destination folder: ")
input2 = sg.Input()
choose_button2 = sg.FilesBrowse("Choose", key="folder")
compress_button = sg.Button("Compress file")
window = sg.Window("File Compressor",
                   layout=[[label1, choose_button1, input1],
                           [label2, choose_button2,input2],
                           [compress_button]])
                    make_archive(filepaths)

while True:
    event, values = window.read()
    print(event, values)
    filepath = values["files"].split(';')
    folder = values("folder")

window.close()
