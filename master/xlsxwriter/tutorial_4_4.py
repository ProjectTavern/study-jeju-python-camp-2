import xlsxwriter

workbook = xlsxwriter.Workbook('tutorial_4_5.xlsx')
worksheet = workbook.add_worksheet()

chart = workbook.add_chart({'type': 'pie'})
bold = workbook.add_format({'bold': True})

chart.set_x_axis({
    'name': 'student score',
    'name_font': {'size': 14, 'bold': True},
})

data = [
    [70, 64, 30],
    [45, 33, 90],
    [25, 44, 30],
]
worksheet.write(0, 1, 'math', bold)
worksheet.write(0, 2, 'sciece', bold)
worksheet.write(0, 3, 'computer', bold)
worksheet.write(1, 0, 'hojun', bold)
worksheet.write(2, 0, 'eunjung', bold)
worksheet.write(3, 0, 'subin', bold)
worksheet.write(4, 0, 'Average', bold)
worksheet.write_column('B2', data[0])
worksheet.write_column('C2', data[1])
worksheet.write_column('D2', data[2])
worksheet.write(4, 1, '=AVERAGE(B2:B4)', bold)
worksheet.write(4, 2, '=AVERAGE(C2:C4)', bold)
worksheet.write(4, 3, '=AVERAGE(D2:D4)', bold)

chart.add_series({'categories': '=Sheet1!$A$2:$A$4',\
                  'values': '=Sheet1!$B$2:$B$4',\
                  'name':'Sheet1!$B$1'})
chart.add_series({'values': '=Sheet1!$C$2:$C$4','name':'Sheet1!$C$1'})
chart.add_series({'values': '=Sheet1!$D$2:$D$4','name':'Sheet1!$D$1'})

worksheet.insert_chart('A7', chart)

workbook.close()



