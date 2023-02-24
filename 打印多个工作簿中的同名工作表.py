from pathlib import Path
import xlwings as xw
folder_path = Path('汇总压实度报告')
file_list = folder_path.glob('*.*')
app = xw.App(visible=False, add_book=False)
for i in file_list:
    workbook = app.books.open(i)
    worksheet = workbook.sheets['11111']
    worksheet.api.PrintOut(Copies=3, ActivePrinter='DESKTOP-HP01', Collate=True)
    workbook.close()
app.quit()