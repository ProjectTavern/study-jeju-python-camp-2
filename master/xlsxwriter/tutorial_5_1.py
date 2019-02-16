import xlsxwriter

workbook = xlsxwriter.Workbook('tutorial_5_1.xlsx')
worksheet = workbook.add_worksheet()

worksheet.insert_image('B2', r'c:\imgs\python.png')

workbook.close()



