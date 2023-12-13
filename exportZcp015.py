import pandas as pd
from time import sleep
import openpyxl as xl

class Export_ZCP015():
    def __init__(self) -> None:
        try:
            print('reading file...')
            self.path = r'C:\Users\Anderson\Desktop\Update ZCP015\EXPORT.XLSX'
            self.wb = xl.load_workbook(self.path) 
            self.Sheet=self.wb.sheetnames[0]
            self.df = pd.read_excel(self.path, sheet_name=self.Sheet)
        
        except Exception as e:
            print('Error read file operation...')
            

    def remove_null_romaneio(self):
        try:
            print('removing null romaneio...')

            self.df.dropna(subset=['Romaneio'], how='all', inplace=True)
        except Exception as e:
            print('Error in remove_null_romaneio...')

    def sort_data_pesagem(self):
        try:
            print('sorting table by "Dt. Pesagem Inicial"...')
            self.df.sort_values(by='Dt. Pesagem Inicial', inplace=True)
        except Exception as e:
            print("Error in sort_data_pesagem...")

    def set_data_pesagem(self):
        try:
            print('set set_data_pesagem...')
            if len(self.df['Dt. Pesagem Inicial']) == len(self.df['Data de criação']):
                for index in range(0,len(self.df['Dt. Pesagem Inicial'])):
                    if self.df.iat[index, 4] is pd.NaT:
                        self.df.iat[index, 4] = self.df.iat[index, 32]
        except Exception as e:
            print('Error in set_data_pesagem...')


    def remove_duplicates(self):
        try:
            print('removing duplicates rows...')
            self.newDF = self.df.drop_duplicates(keep='first')
        except Exception as e:
            print("Error in remove_duplicates...")

    def save_file(self):
        try:
            print("saving output file... ")
            self.df.to_excel("./files/temp/output.xlsx", sheet_name=self.Sheet, index=False, header=True)
        except Exception as e:
            print("Error in save_file...")

    def update(self):
        self.remove_null_romaneio()
        self.set_data_pesagem()
        self.sort_data_pesagem()
        self.remove_duplicates()
        self.save_file()



Export_ZCP015().update()