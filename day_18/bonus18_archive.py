import PySimpleGUI as sg
from zip_extractor import extract_archive

sg.theme("Black")

label1 = sg.Text("Select archive:")
input1 = sg.Input()
choose_button1 = sg.FilesBrowse("Choose file", key="archive")

label2 = sg.Text("Select destination DIR:")
input2 = sg.Input()
choose_button2 = sg.FolderBrowse("Choose file", key="folder")

extract_button = sg.Button("Extrac")
output_label = sg.Text(key="output", text_color="green")

col1 = sg.Column([[label1, input1, choose_button1]])
col2 = sg.Column([[label2, input2, choose_button2]])


window = sg.Window("Archive extractor",
                   layout=[[col1], [col2], [extract_button]])
# window.read()
while True:
    event, values = window.read()
    print(event, values)

    archivepath = values["archive"]
    dest_dir = values["folder"]
    extract_archive(archivepath, dest_dir)
    window["output"].update(value="Extraction completed")

window.close()
