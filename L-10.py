import sqlite3
conn = sqlite3.connect('titanicDB.db')
curs = conn.cursor()

# 3) get number of passengers (rows in the table)
curs.execute('select count(*) from passenger')

print('\n---------------------------------------------------\n')
print('Number of passengers: ' + str(curs.fetchone()) + '\n')

# 4) get number of passengers with no age
curs.execute('SELECT count(*) from passenger where age = NULL')

print('Number of passengers with no age: ' + str(curs.fetchone()) + '\n')

# 5) get number of passengers under the age of 1
curs.execute('select count(*) from passenger where age < 1')

print('Number of passengers under the age of 1: ' + str(curs.fetchone()) + '\n')

# 6) gets the cheapest fare and how many people paid it.
curs.execute('select fare, count(fare) from passenger group by fare ' +
             'Having count(fare) > (select min(cnt) from (select count(fare) ' +
             'as cnt from passenger group by fare))')

print('The cheapest fare and how many people paid it: ' + str(curs.fetchone()) + '\n')

# 7) gets the most expensive fare and the number of people that paid it.

curs.execute('select fare, count(fare) from passenger group by fare ' +
             'Having count(fare) > (select min(cnt) from (select count(fare) ' +
             'as cnt from passenger group by fare))')

print('The most expensive fair and how many people paid it:' + str(curs.fetchall()[-1]) + '\n')
print('\n---------------------------------------------------')

