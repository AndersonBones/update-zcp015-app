import pandas as pd
from time import sleep
import os
import openpyxl as xl
from datetime import datetime

class Base_ZCP015():
    def __init__(self) -> None:
        self.path_export = r'C:\Users\Anderson\Desktop\Update ZCP015\files\temp\output.xlsx'
        self.path_base = r'C:\Users\Anderson\Desktop\Update ZCP015\files\ZCP015.xlsx'

        # get first day of month
        self.input_dt = datetime.today()
        self.res = self.input_dt.replace(day=1).strftime('%d-%m-%Y')

        # get sheet names
        self.work_book_export = xl.load_workbook(self.path_export) 
        self.export_sheet=self.work_book_export.sheetnames[0]

        self.work_base = xl.load_workbook(self.path_base) 
        self.base_sheet=self.work_base.sheetnames[0]

        #read excel files
        self.df_base = pd.read_excel(self.path_base, sheet_name=self.base_sheet)
        print('Lendo Base...')

        self.df_export = pd.read_excel(self.path_export, sheet_name=self.export_sheet)
        print('Lendo Export...')

        self.dfs = []


    def sort_data_pesagem(self):
        #self.writer = pd.ExcelWriter(self.path_base, engine='xlsxwriter') # base file
        self.df_base.sort_values(by=['Dt. Pesagem Inicial', 'Hora Pesagem Inicial'], inplace=True)
        print('Organizando Data pesagem incial...')

    def remove_current_values(self):
        self.df_base.drop(self.df_base.loc[self.df_base['Dt. Pesagem Inicial'] > '2023-11-30 23:59:59'].index, inplace=True)
        self.df_base.to_excel('./files/temp/result.xlsx', sheet_name=self.base_sheet, index=False, header=True)
        
    def update_data_base(self):
        self.dfs.append(self.df_base)
        self.dfs.append(self.df_export)

        self.df_master = pd.concat(self.dfs, axis=False)
        print("Concatenando informações...")
        self.df_master.to_excel(self.writer, sheet_name=self.base_sheet, index=False, header=True)
        print('Salvando base de dados...')
        self.writer.close()
        print('Concluido.')
    
    def start_update(self):
        self.sort_data_pesagem()
        self.remove_current_values()
        
        

Base_ZCP015().start_update()