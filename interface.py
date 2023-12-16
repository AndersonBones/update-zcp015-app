from exportZcp015 import Export_ZCP015
from BaseZcp015 import Base_ZCP015
import PySimpleGUI as sg
from pathlib import Path
import os




sg.theme('Dark Grey 14')

layout = [[sg.Text('Atualização de Base de dados ZCP015', font=('Arial Bold', 15))],
          [sg.Text('Selecione a base com os novos dados', text_color='#7CB9E8')],
          [sg.Input(text_color='#7CB9E8', size=60, key='-IN-'), sg.FileBrowse(button_text='Procurar', s=15, file_types=(("Excel files","*.xlsx"),))],
          [sg.Exit(button_text='Sair', button_color="red", s=6), sg.OK(button_text='Processar', s=10)]]

window = sg.Window('UPDATE ZCP015', layout, size=(550, 160))


while True:
    event, values = window.read()
 
    if event in (sg.WINDOW_CLOSED, 'Sair'):
        break
    if os.path.exists((values['-IN-'])) == False and event == 'Processar':
        
        sg.popup_error('Selecione um arquivo válido!', title='Error')

    elif os.path.exists((values['-IN-'])) == True and event == "Processar":
        
        Export_ZCP015(values['-IN-']).update()
        Base_ZCP015(values['-IN-']).start_update()
        sg.popup_ok('Concluido :)', title='Salvo com sucesso')


window.close()

