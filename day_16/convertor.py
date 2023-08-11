import PySimpleGUI as sg
from converter import convert

feet_label1 = sg.Text("Enter feet: ")
feet_input1 = sg.Input(key="feet")

inches_label2 = sg.Text("Enter inches: ")
inches_input2 = sg.Input(key="inches")

convert_button = sg.Button("Convert")
output_label = sg.Text("", key="output")

window = sg.Window('Convertor',
                   layout=[[feet_label1, feet_input1],
                           [inches_label2, inches_input2],
                           [convert_button, output_label]])
while True:
    event, values = window.read()
    feet = float(values["feet"])
    inches = float(values["inches"])
    result = convert(feet, inches)
    window["output"].update(value=f"{result} m", text_color="white")
window.close()



