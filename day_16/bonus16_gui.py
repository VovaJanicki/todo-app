import PySimpleGUI as sg

label1 = sg.Text("Select files to compress: ")
input1 = sg.Input()
choose_button1 = sg.FilesBrowse("Chose")

label2 = sg.Text("Select destination folder: ")
input2 = sg.Input()
choose_button2 = sg.FilesBrowse("Choose")
compress_button = sg.Button("Compress file")
window = sg.Window("File Compressor",
                   layout=[[label1, choose_button1, input1],
                           [label2, choose_button2,input2],
                           [compress_button]])
window.read()
window.close()
