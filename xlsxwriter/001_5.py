import xlsxwriter

workbook = xlsxwriter.Workbook('tutorial_1_5.xlsx')
worksheet = workbook.add_worksheet()

bold = workbook.add_format({'bold': True})

student_math_score = (
    ['hojun', 95],
    ['eunjung', 75],
    ['subin', 98],
    ['eunbin', 67]
)

row = 0
col = 0