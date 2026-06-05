def psl(text):
    alph = "АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯABCDEFGHIJKLMNOPQRSTUVWXYZ"
    result = ""
    out = []
    txt = text.upper()
    for char in txt:
            if char in alph:
                per = ""
                period1 = 'АБВГ,'
                period2 = 'ДЕЖЗ.'
                period3 = 'ИЙКЛ-'
                period4 = 'МНОП!'
                period5 = 'РСТУ?'
                period6 = 'ФХЦЧ:'
                period7 = 'ШЩЪЫ;'
                period8 = 'ЬЭЮЯ'
                period9 = "ABCD"
                period10 = "EFGH"
                period11 = "IJKL"
                period12 = "MNOP"
                period13 = "QRST"
                period14 = "UVWX"
                period15 = "YZ"
                if char in period1:
                    per = '1'
                if char in period2:
                    per = '2'
                if char in period3:
                    per = '3'
                if char in period4:
                    per = '4'
                if char in period5:
                    per = '5'
                if char in period6:
                    per = '6'
                if char in period7:
                    per = '7'
                if char in period8:
                    per = '8'
                if char in period9:
                    per = '9'
                if char in period10:
                    per = '10'
                if char in period11:
                    per = '11'
                if char in period12:
                    per = '12'
                if char in period13:
                    per = '13'
                if char in period14:
                    per = '14'
                if char in period15:
                    per = '15'
            if char == 'А' or char == 'Д' or char == 'И' or char == 'М' or char == 'Р' or char == 'Ф' or char == 'Ц' or char == 'Ь' or char == 'A' or char == 'E' or char == 'I' or char == 'M' or char == 'Q' or char == 'U' or char == 'Y':
                res = per + '11'
            if char == 'Б' or char == 'Е' or char == 'Й' or char == 'Н' or char == 'С' or char == 'Х' or char == 'Щ' or char == 'Э' or char == 'B' or char == 'F' or char == 'J' or char == 'N' or char == 'R' or char == 'V' or char == 'Z':
                res = per + '121'
            if char == 'В' or char == 'Ж' or char == 'К' or char == 'О' or char == 'Т' or char == 'Ц' or char == 'Ъ' or char == 'Ю' or char == 'C' or char == 'G' or char == 'K' or char == 'O' or char == 'S' or char == 'W':
                res = per + '1331'
            if char == 'Г' or char == 'З' or char == 'Л' or char == 'П' or char == 'У' or char == 'Ч' or char == 'Ы' or char == 'Я' or char == 'D' or char == 'H' or char == 'L' or char == 'P' or char == 'T' or char == 'X':
                res = per + '14641'
            if char == ',':
                res = '//'
            if char == '.':
                res = 'S'
            if char == '-':
                res = 't'
            if char == '!':
                res = 'o'
            if char == '?':
                res ='q'
            if char == ':':
                res = 'ss'
            if char == ';':
                res = 's//'
            result = res
            out.append(result)
            outn = '.'.join(out)
    return outn
input = input('Enter your massege: ')
ans = psl(input)
print(ans)