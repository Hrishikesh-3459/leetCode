def reformatDate(date):
    year = date[-4:]
    if date[1].isdigit():
        day = date[0] + date[1]
    else:
        day = '0' + date[0]
    month = date.split()[1]
    di = {"Jan": '01', "Feb": '02', "Mar": '03', "Apr": '04', "May": '05', "Jun": '06', "Jul": '07', "Aug": '08', "Sep": '09', "Oct": '10', "Nov": '11', "Dec": '12'}
    ans = '-'.join([year, di[month], day])
    return ans