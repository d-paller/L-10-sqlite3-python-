import sqlite3
conn = sqlite3.connect('passenger.db')
curs = conn.cursor()

# 3) get number of passengers (rows in the table)
curs.execute('select count(*) from passenger')

print(curs.fetchone())
print('Using rowCount: ' + curs.rowcount)

# 4) get number of passengers with no age
curs.execute('SELECT count(*) from passenger where age = NULL')

print(curs.fetchone())

# 5) get number of passengers under the age of 1
curs.execute('select count(*) from passenger where age < 1')

print(curs.fetchone())

# 6) gets the cheapest fare and how many people paid it.
curs.execute('select fare, count(fare) from passenger group by fare ' +
             'Having count(fare) > (select min(cnt) from (select count(fare) ' +
             'as cnt from passenger group by fare)))')

print(curs.fetchone())

# 7) gets the most expensive fare and the number of people that paid it.

curs.execute('select fare, count(fare) from passenger group by fare ' +
             'Having count(fare) > (select min(cnt) from (select count(fare) ' +
             'as cnt from passenger group by fare)))')

print(curs.fetchone())

