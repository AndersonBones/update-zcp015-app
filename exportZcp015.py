import pandas as pd
from time import sleep
import openpyxl as xl
from datetime import datetime

class Export_ZCP015():
    
    def __init__(self) -> None:

        self.path = r'C:\Users\anderson.bones\Desktop\update-zcp015-app\Export Sap\EXPORT.XLSX'
        self.file_name = self.path.split("\\")[-1]
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

    def save_file(self):
        try:
            print("Salvando Base tratada... ")
            self.output_file_name = datetime.today().replace().strftime('%d-%m-%Y (%H-%M-%S)')
            self.df.to_excel(f"./files/temp/output.xlsx", sheet_name=self.Sheet, index=False, header=True)
            print('Concluido.')
        except Exception as e:
            print("Erro ao salvar base tratada...")
            print(e)

    def update(self):
        self.remove_null_romaneio()
        self.set_data_pesagem()
        self.sort_data_pesagem()
        self.remove_duplicates()
        self.save_file()



