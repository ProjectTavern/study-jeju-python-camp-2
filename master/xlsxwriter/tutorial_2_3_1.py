import xlsxwriter

#워크북 xlsx 파일 생성하기
workbook = xlsxwriter.Workbook('2_2.xlsx')

#워크 시트 생성하기
worksheet = workbook.add_worksheet('First_sheet')

student_math_score = (
    ['hojun', 95],
    ['eunjung', 75],
    ['subin', 98],
    ['eunbin', 67]
)

row = 0
col = 0

for student, score in student_math_score:
    worksheet.write(row, col, student)
    worksheet.write(row, col + 1, score)

    row += 1

#형식
bold = workbook.add_format({'bold': True})

worksheet.write(row, 0, 'Average', bold)
worksheet.write(row, 1, '=AVERAGE(B1:B4)', bold)

workbook.close()
