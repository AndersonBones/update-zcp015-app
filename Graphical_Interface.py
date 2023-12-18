from Export import Export_ZCP015
from Base import Base_ZCP015
import PySimpleGUI as sg
from pathlib import Path
import os
import multiprocessing
import threading
from time import sleep




sg.theme('Dark Grey 14')

class Gui():
    def __init__(self) -> None:
        self.popup_status = False
        self.layout = [[sg.Text('Atualização de Base de dados ZCP015', font=('Arial Bold', 15))],
                [sg.Text('Selecione a base com os novos dados', text_color='#7CB9E8')],
                [sg.Input(text_color='#7CB9E8', size=70, key='-IN-'), sg.FileBrowse(button_text='Procurar', s=15, file_types=(("Excel files","*.xlsx"),))],
                [sg.Exit(button_text='Sair', button_color="red", s=6), sg.OK(button_text='Processar', s=10, button_color='green')]]

        self.window = sg.Window('UPDATE ZCP015', self.layout, size=(620, 150))

    
    def run_export_process(self, path): 
        Export_ZCP015(path).update()
        
        Base_ZCP015(path).start_update()
        self.popup_status = True
       
    def main(self):
       
        while True:
            self.event, self.values = self.window.read(timeout=200)
        
            if self.event in (sg.WINDOW_CLOSED, 'Sair'):
                break
            
            if os.path.exists(self.values['-IN-']) == False and self.event == 'Processar':
                sg.popup_error('Selecione um arquivo válido!', title='Error')
            

            if os.path.exists(self.values['-IN-']) == True and self.event == "Processar":
                if not self.popup_status:
                    thr = threading.Thread(target=self.run_export_process, args=(self.values['-IN-'],), daemon=True)
                    thr.start()
                    
                
            if self.popup_status:
                sg.popup_ok(f'Concluido :)\n{"-"*50}', title='Salvo com sucesso')
                self.popup_status = False
        self.window.close()


def run_gui():
    Gui().main()

if __name__ == '__main__':
    run_gui()
