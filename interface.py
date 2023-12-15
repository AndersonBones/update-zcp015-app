from exportZcp015 import Export_ZCP015
from BaseZcp015 import Base_ZCP015
import PySimpleGUI as sg

sg.theme('Dark Grey 13')

layout = [[sg.Text('Atualização de Base de dados ZCP015', font=('Arial Bold', 15))],
        [sg.Text('Selecione a base com os novos dados', text_color='#7CB9E8')],
          [sg.Input(disabled=True, text_color='black', size=65, key='-IN-'), sg.FileBrowse(button_text='Procurar base', file_types=(("Excel files","*.xlsx"),))],
          [sg.OK(button_text='Processar'), sg.Cancel(button_text='Cancelar')],
          [sg.Text('Status',font=('Arial Bold', 15))]]

window = sg.Window('UPDATE ZCP015', layout, size=(600, 300))


while True:
    event, values = window.read()
    print(event, values)

    if event in (sg.WINDOW_CLOSED, 'Exit'):
        break
    if values['-IN-'] == "" and event == 'Processar':
        sg.popup_error('Selecione o arquivo')

    elif values['-IN-'] != "" and event == "Processar":

        Export_ZCP015(values['-IN-']).update()
        


window.close()

