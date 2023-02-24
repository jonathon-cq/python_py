import xlwings as xw
app = xw.App(visible=False, add_book=False)
workbook = app.books.open('YSD2200--.xls')
worksheet = workbook.sheets['原始记录']
worksheet.api.PrintOut(Copies=1, ActivePrinter='DESKTOP-HP01', Collate=True)   #copies为设置打印次数
workbook.close()
app.quit()
