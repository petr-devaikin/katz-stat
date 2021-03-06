from datetime import datetime
from dateutil import relativedelta as rdelta

ages = {}

f = open('date-sum-bd-gender.csv')
for line in f:
    data = line.split(';')
    if data[2]:
        money = int(data[1])
        oper = datetime.strptime(data[0], '%m/%d/%Y')
        bd = datetime.strptime(data[2], '%m/%d/%Y') if '/' in data[2] else datetime.strptime(data[2], '%d.%m.%Y')
        age = rdelta.relativedelta(oper ,bd)
        if not age.years in ages:
            ages[age.years] = 0
        ages[age.years] += money

        if age.years == 17:
            print data[2]

nf = open('date-sum-bd-gender-result.js', 'w')
nf.write('var genderData = {')
for age in ages:
    nf.write('%d: %d,' % (age, ages[age]))
nf.write('}')