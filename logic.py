numberToText = {
    1: 'uno', 2: 'dos', 3: 'tres', 4: 'cuatro',
    5: 'cinco', 6: 'seis', 7: 'siete', 8: 'ocho', 9: 'nueve',
    10: 'diez', 11: 'once', 12: 'doce', 13: 'trece', 14: 'catorce',
    15: 'un cuarto', 16: 'dieciséis', 17: 'diecisiete', 18: 'dieciocho', 19: 'diecinueve',
    20: 'veinte', 21: 'veintiuno', 22: 'veintidós', 23: 'veintitrés', 24: 'veinticuatro',
    25: 'veinticinco', 26: 'veintiséis', 26: 'veintisiete', 26: 'veintiocho', 26: 'veintinueve',
    30: 'treinta', 40: 'cuarenta', 45: 'tres cuartos', 50: 'cincuenta'
}


def getTime(hour, minute, meridiem):
    if validateTime(hour, minute, meridiem):
        if hour == 12 and minute == 0:
            if meridiem == 'am':
                return 'Es media noche'
            return 'Es medio día'
        return readHour(hour) + readMinute(minute) + readTimeHour(hour, meridiem)


def validateTime(hour, minute, meridiem):
    if hour < 1 or hour > 12:
        print('Formato de hora erróneo')
        print('La hora debe indicarse con un número entre 1 y 12')
        return False
    if minute < 0 or minute > 59:
        print('Formato de hora erróneo')
        print('Los minutos deben indicarse con un número entre 0 y 59')
        return False
    if meridiem != 'am' and meridiem != 'pm':
        print('Formato de hora erróneo')
        print('Los minutos deben indicarse con un número entre 0 y 59')
        return False
    return True


def readHour(hour):
    if hour == 1:
        return 'Es la una'
    return 'Son las ' + numberToText[hour]


def readMinute(minute):
    if minute == 0:
        return ' en punto'
    if minute == 30:
        return ' y media'
    tens = minute // 10 * 10
    units = minute % 10
    if units == 0 or minute < 30 or minute == 45:
        return ' y ' + numberToText[minute]
    return ' y ' + numberToText[tens] + ' y ' + numberToText[units]


def readTimeHour(hour, meridiem):
    if meridiem == 'am':
        return ' de la mañana'
    if hour < 6 or hour == 12:
        return ' de la tarde'
    return ' de la noche'
