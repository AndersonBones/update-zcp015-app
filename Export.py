import pandas as pd
from time import sleep
import openpyxl as xl
from datetime import datetime
from UliPlot.XLSX import auto_adjust_xlsx_column_width

import locale

locale.setlocale(locale.LC_ALL, 'pt_BR.utf8')

class Export_ZCP015():
    
    def __init__(self, path) -> None:
        self.path = path
        self.file_name = self.path.split("/")[-1]
        try:
            print(f'Lendo base: {self.file_name}')
            self.wb = xl.load_workbook(self.path) 
            self.Sheet=self.wb.sheetnames[0]
            self.df = pd.read_excel(self.path, sheet_name=self.Sheet)
        
        except Exception as e:
            print(f"Erro na leitura da base: {self.file_name[-1]}")
            

    def remove_null_romaneio(self):
        try:
            print('Removendo Romaneios nulos...')

            self.df.dropna(subset=['Romaneio'], how='all', inplace=True)
        except Exception as e:
            print('Erro ao remover romaneios nulos...')

    def dateTime_format(self):
        print('Ajustando formado de data...')
        self.df['Dt. Pesagem Inicial'] = self.df['Dt. Pesagem Inicial'].dt.strftime('%d/%m/%Y')
        self.df['Data Nota Fiscal'] = self.df['Data Nota Fiscal'].dt.strftime('%d/%m/%Y')
        self.df['Data de criação'] = self.df['Data de criação'].dt.strftime('%d/%m/%Y')
        print('Formato de data ajustado.')

    def sort_data_pesagem(self):
        try:
            print('Ordenando coluna "Dt. Pesagem Inicial"...')
            self.df.sort_values(by=['Dt. Pesagem Inicial', 'Hora Pesagem Inicial'], inplace=True)
            
        except Exception as e:
            print('Erro ao ordenar coluna "Dt. Pesagem Inicial"...')


    def set_data_pesagem(self):
        try:
            print('Tratando romaneios sem "Dt. Pesagem Inicial"...')
            if len(self.df['Dt. Pesagem Inicial']) == len(self.df['Data de criação']):
                for index in range(0,len(self.df['Dt. Pesagem Inicial'])):
                    if self.df.iat[index, 4] is pd.NaT:
                        self.df.iat[index, 4] = self.df.iat[index, 32]
        except Exception as e:
            print('Erro ao Tratar romaneios sem "Dt. Pesagem Inicial"...')


    def remove_duplicates(self):
        try:
            print('Removendo Linhas duplicadas...')
            self.newDF = self.df.drop_duplicates()
        except Exception as e:
            print("Erro ao remover linhas duplicadas...")

    def auto_adjust_column(self, df):
        for column in df:
            column_length = max(self.df[column].astype(str).map(len).max(), len(column))
            col_idx = df.columns.get_loc(column)
            self.writer.sheets[self.Sheet].set_column(col_idx, col_idx, column_length+2)

    def save_file(self):
        try:
            self.writer = pd.ExcelWriter(self.path, engine='xlsxwriter')
            print("Salvando Base tratada... ")
            self.output_file_name = datetime.today().replace().strftime('%d-%m-%Y (%H-%M-%S)')
            
            self.df.to_excel(self.writer, sheet_name=self.Sheet, index=False, header=True)

            self.auto_adjust_column(self.df)

            self.writer.close()
            print('Concluido.')
        except Exception as e:
            print("Erro ao salvar base tratada...")
            print(e)

    def update(self):
        self.remove_null_romaneio()
        self.set_data_pesagem()
        self.sort_data_pesagem()
        self.dateTime_format()
        self.remove_duplicates()
        self.save_file()



