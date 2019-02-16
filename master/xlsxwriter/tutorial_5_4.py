import xlsxwriter

workbook = xlsxwriter.Workbook('tutorial_5_4.xlsx')
worksheet = workbook.add_worksheet()

worksheet.insert_image('B2', r'c:\imgs\python.png',\
                       {'x_offset': 20, 'y_offset': 10,\
                        'x_scale': 0.5, 'y_scale': 0.5,\
                        'url': 'http://python.org'})

workbook.close()




