import xlsxwriter

workbook = xlsxwriter.Workbook('tutorial_1_5.xlsx')
worksheet = workbook.add_worksheet()

bold = workbook.add_format({'bold': True})

student_math_score = (
    ['hojun', 95],
    ['eunjung', 75],
    ['subin', 98],
    ['eunbin', 67],
)

row = 0
col = 0

for student, score in (student_math_score):
    worksheet.write(row, col, student)
    worksheet.write(row, col + 1, score)
    Pass = '=IF(B' + str(row + 1) + '>70,"Pass", "Fail")'
    worksheet.write_formula(row, col + 2, Pass)
    row += 1

worksheet.write(row, 0, 'Sum', bold)
worksheet.write(row, 1, '=SUM(B1:B4)', bold)
#worksheet.write_formula(B5, '=B1 + B2 + B3 + B4')
worksheet.write(row + 1, 0, 'Average', bold)
worksheet.write(row + 1, 1, '=AVERAGE(B1:B4)', bold)
#worksheet.write_formula(B6, '= (B1 + B2 + B3 + B4) / 4')

worksheet.write_formula('A7', '=DATEVALUE("1-Jan-2013")')

workbook.close()



