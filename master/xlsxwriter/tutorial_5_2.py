import xlsxwriter

workbook = xlsxwriter.Workbook('tutorial_5_2.xlsx')
worksheet = workbook.add_worksheet()

worksheet.insert_image('B2', r'c:\imgs\python.png',\
                       {'x_offset': 20, 'y_offset': 10})

workbook.close()



