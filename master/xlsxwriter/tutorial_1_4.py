import xlsxwriter

workbook = xlsxwriter.Workbook('tutorial_1_4_format.xlsx')
worksheet = workbook.add_worksheet()

worksheet.set_column('A:A', 30)

number = 42705.5
red = cell_format.set_font_color('red')
worksheet.write('B1', 'Format', red)

worksheet.write('A1', number) #1900년을 기준으로 365일 1년으로 계산

format1 = workbook.add_format({'num_format': 'yy/mm/dd'})
worksheet.write('A2', number, format1)

format2 = workbook.add_format({'num_format': 'yyyy-mm-dd'})
worksheet.write('A3', number, format2)

format3 = workbook.add_format({'num_format': 'yy/mm/dd hh:mm'})
worksheet.write('A4', number, format3)

format4 = workbook.add_format({'num_format': 'yyyy mmm dd'})
worksheet.write('A5', number, format4)

format5 = workbook.add_format({'num_format': 'yyyy mmm dd hh:mm AM/PM'})
worksheet.write('A6', number, format5)

workbook.close()

