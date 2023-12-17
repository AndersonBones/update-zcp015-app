from Export import Export_ZCP015
from Base import Base_ZCP015
import PySimpleGUI as sg
from pathlib import Path
import os
import multiprocessing




sg.theme('Dark Grey 14')

class Gui():
    def __init__(self) -> None:
        self.layout = [[sg.Text('Atualização de Base de dados ZCP015', font=('Arial Bold', 15))],
                [sg.Text('Selecione a base com os novos dados', text_color='#7CB9E8')],
                [sg.Input(text_color='#7CB9E8', size=60, key='-IN-'), sg.FileBrowse(button_text='Procurar', s=15, file_types=(("Excel files","*.xlsx"),))],
                [sg.Exit(button_text='Sair', button_color="red", s=6), sg.OK(button_text='Processar', s=10, button_color='green')]]

        self.window = sg.Window('UPDATE ZCP015', self.layout, size=(600, 150))

    
    def run_process(self, path):
        Export_ZCP015(path).update()
        #   Base_ZCP015(path).start_update()

    def main(self):
        while True:
            event, values = self.window.read()
        
            if event in (sg.WINDOW_CLOSED, 'Sair'):
                break
            
            if os.path.exists(values['-IN-']) == False and event == 'Processar':
                sg.popup_error('Selecione um arquivo válido!', title='Error')
            

            if os.path.exists(values['-IN-']) == True and event == "Processar":
                
                self.run_process(values['-IN-'])
                sg.popup_ok(f'Concluido :)\n{"-"*50}', title='Salvo com sucesso')

        self.window.close()


if __name__ == '__main__':
    Gui().main()