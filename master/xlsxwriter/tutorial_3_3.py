import xlsxwriter
import json

workbook = xlsxwriter.Workbook('tutorial_3_3.xlsx')
worksheet = workbook.add_worksheet()

f = open("json.js", 'r')
jsonString = f.read()
dictData = json.loads(jsonString)

bold = workbook.add_format({'bold': True})

row = 0
col = 0
print (len(dictData))
while row < len(dictData):
    worksheet.write(row, col, dictData[row]['name'])
    worksheet.write(row, col + 1, dictData[row]['age'])
    adult = '=IF(B' + str(row + 1) + '>19,"Adult", "Minors")'
    worksheet.write_formula(row, col + 2, adult)
    row += 1
f.close()
workbook.close()



