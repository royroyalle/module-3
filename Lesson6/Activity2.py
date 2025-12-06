import random
import time
def randomDate(sd, ed):
    print("Printing random date between", sd, "and", ed)
    rg = random.random()
    date_Format = '%m/%d/%Y'
    st = time.mktime(time.strptime(sd, date_Format))
    et = time.mktime(time.strptime(ed, date_Format))
    rt = st + rg * (et-st)
    rd = time.strftime(date_Format, time.localtime(rt))
    return rd
print("Random Date =", randomDate("1/08/2018", "12/03/2020"))