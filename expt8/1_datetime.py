import datetime

if __name__ == '__main__':
   now = datetime.datetime.now()
   time_now = now.strftime('%H:%M:%S')
   print('The time now = ', time_now)
   print(now)

