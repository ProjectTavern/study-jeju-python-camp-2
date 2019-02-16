import xlsxwriter

workbook = xlsxwriter.Workbook('student_score.xlsx')
worksheet = workbook.add_worksheet()

bold = workbook.add_format({'bold': True})

columns = (
    ['국어', '영어', '수학', '과학', '평균', '합격여부']
)

student_math_score = (
    ['hojun', 95, 72, 36, 90],
    ['eunjung', 75, 42, 55, 62],
    ['subin', 98, 30, 61, 30],
    ['eunbin', 67, 70, 70, 81]
)

for index, column in enumerate(columns):
    worksheet.write(0, index + 1, column)

for rowIndex, scoreData in enumerate(student_math_score):
    row = rowIndex + 1
    for col, inform in enumerate(scoreData):
        worksheet.write(row, col, inform)
    average = '=AVERAGE(B' + str(row + 1) + ':E' + str(row + 1) + ')'
    Pass = '=IF(F' + str(row + 1) + '>70,"Pass", "Fail")'
    worksheet.write_formula(row, len(scoreData), average)
    worksheet.write_formula(row, len(scoreData) + 1, Pass)

workbook.close()
