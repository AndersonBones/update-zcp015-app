from Export import Export_ZCP015
from Base import Base_ZCP015
import PySimpleGUI as sg
from pathlib import Path
import os
import multiprocessing
import threading
from time import sleep




sg.theme('DarkTeal10')

class Gui():
    def __init__(self) -> None:
        self.popup_status = False
        self.layout = [[sg.Text('Atualização de Base de dados ZCP015', font=('Arial Bold', 15))],
                [sg.Text('Selecione a base com os novos dados')],
                [sg.Input( size=70, key='-IN-'), sg.FileBrowse(button_text='Procurar', s=15, file_types=(("Excel files","*.xlsx"),))],
                [sg.Checkbox("Atualizar ZCP015", key='s1')],
                [sg.Exit(button_text='Sair', button_color="red", s=6, pad=(5, (15, 0))), sg.OK(button_text='Processar', s=10, pad=(5, (15, 0)))]]

        self.window = sg.Window('UPDATE ZCP015', self.layout, size=(620, 180))

    
    def run_export_process(self, path): 
        Export_ZCP015(path).update()
        
        #Base_ZCP015(path).start_update()
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
                sg.popup_ok(f'Tarefa Concluida com sucesso :)\n{"-"*50}', title='Salvo com sucesso')
                self.popup_status = False
        self.window.close()


def run_gui():
    Gui().main()

if __name__ == '__main__':
    run_gui()
