# pip3 install xlsxwriter
import xlsxwriter

# 워크북 xlsx 파일 생성하기
workbook = xlsxwriter.Workbook('2_1.xlsx')

# 워크 시트 생성하기
worksheet = workbook.add_worksheet('First_sheet')

# 셀에 값 입력하기
worksheet.write('A1', 'Hello')
worksheet.write('B1', 'World')

# 좌표로도 입력할 수 있습니다.
worksheet.write(0, 2, "It's me")

# 수식 넣기
worksheet.write(1, 0, 2)
worksheet.write(1, 1, 4)
worksheet.write(2, 0, '=A2+B2')

workbook.close()