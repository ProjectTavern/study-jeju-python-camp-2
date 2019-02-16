import xlsxwriter

workbook = xlsxwriter.Workbook('tutorial_2.xlsx')
worksheet = workbook.add_worksheet()

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
    row += 1

worksheet.write(row, 0, 'Average')
worksheet.write(row, 1, '=AVERAGE(B1:B4)')

workbook.close()
