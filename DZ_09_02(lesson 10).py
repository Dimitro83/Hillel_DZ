inputdata = ['Страна', 'шалаш', 'Летел', 'вертолёт', 'УЧУ', 'мэм', 'язык']


def polindrom(a):
    return a.upper() == a[::-1].upper()


outputdata = list(filter(polindrom, inputdata))
print(f'inputdata: {inputdata},\noutputdata: {outputdata}')
