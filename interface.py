from exportZcp015 import Export_ZCP015
from BaseZcp015 import Base_ZCP015



import tkinter as tk
from tkinter import ttk
from tkinter import filedialog as fd
from tkinter.messagebox import showinfo


class Gui_ZCP015():
    def __init__(self) -> None:
        self.gui = tk.Tk()
        self.gui.title('Update Data Base') #set title

        self.explanation = """Atualização de relatórios SAP"""
        # set window size
        self.gui.geometry('300x400')
        self.gui.resizable(False, False)

        self.selected_size = tk.StringVar()

        
    def set_explanation(self):
        self.w2 = tk.Label(self.gui, justify=tk.LEFT, 
              font=("Helvetica", 14),
              text=self.explanation).pack(ipady=10, ipadx=10, side='top', anchor='w')
    

    def selected_file(self):
        filetypes = (
            ("Excel files","*.xlsx"),("Excel file 97-2003","*.xls")
        )

        filename = fd.askopenfilename(title='Importar Arquivo',initialdir='/',filetypes=filetypes)

        if(not filename):
            showinfo(title='Selecionar arquivo',message='Nenhum arquivo selecionado!')
        else:
            print(filename)

    def handle_select_file(self):
        self.open_button = ttk.Button(self.gui, text='Importar Arquivo',command=self.selected_file)
        self.open_button.pack(expand=True)

    def show_selected_size(self):
        showinfo(
            title='Result',
            message=self.selected_size.get()
        )

    def select_transation(self):
        self.transation_options = (('Complemento ZCP015', 'ZCP015'), 
                                   ('Fretes ZLES018', 'ZLES018'), 
                                   ('Relatório ZMM036', 'ZMM036'))

        for option in self.transation_options:
            self.r = ttk.Radiobutton(
                self.gui,
                text=option[0],
                value=option[1],
                variable=self.selected_size
            )
            self.r.pack(fill='x', padx=5, pady=5)
        
        self.button = ttk.Button(
            self.gui,
            text="Selecionar Base",
            command=self.selected_file,
        )

    

        self.button.place(relx=0.5, rely=0.9, anchor='center')

    def start(self):
        self.set_explanation()
        self.select_transation()
        
        self.gui.mainloop()






Export_ZCP015().update()
Base_ZCP015().sort_data_pesagem()
