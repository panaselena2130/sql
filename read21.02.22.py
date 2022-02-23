from time import sleep
import sqlite3
import datetime

con = sqlite3.connect('C:\\Users\Lena\Desktop\shop.sqlite')
cursor = con.cursor()
sltime=10

cursor.execute( '''CREATE TABLE IF NOT EXISTS just
                (
                
                station_id,
                last_date,
                alarm1,
                alarm2,
                PRIMARY KEY(alarm1)
                )
               ''')
while True:

  with open('C:\\Users\Lena\Desktop\status1.txt', 'r') as f:
      l_date = datetime.datetime.now().strftime('%Y-%m-%d %H:%M')
      a = f.readlines()[-1]
      last = a

      print(a, type(a),'a')
      a=a.split()
      a.insert(1,l_date)
      print(a,type(a))

      cursor.execute("INSERT or REPLACE INTO just VALUES (?,?,?,?)", (a))


      con.commit()
      sleep(sltime)
      #
      # con.commit()


    # last=a[-1]
    # print(last,'last')

# for letter in a:
#
#       if last != letter:
#
#         a.append(letter)
#         print(a)
#       #   continue
#       # else:
#       #    a.append(letter)
#       #    print(a,type(a))

# sleep(sltime)




    # y = a.pop()
    # a.insert(len(a), y)
    # flag = True
    # indexIndex = 0.5
    #
    # for letter in a:
    #     if letter == y:
    #         indexIndex = a.index(letter)
    #
    # for letter in a:
    #     if a.index(letter) == indexIndex:
    #         continue
    #     else:
    #         print(letter, end='')
    #
    # print(y, end= '')
    # sleep(sltime)













