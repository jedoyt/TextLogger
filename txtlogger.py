import datetime

now = str(datetime.datetime.now())
print("Enter date and time of actual event/activity completion.")
actualCompletionDate = input("(yyyy-mm-dd hh:mm:ss): ")

if actualCompletionDate == 'now':
    actualCompletionDate = now

now_split = now.split() # ['yyyy-mm-dd','hh:mm:ss.xxxxxx']
now_date_split = now_split[0].split('-') # ['yyyy','mm','dd']
now_time_split = now_split[1].split(':') # ['hh','mm','ss.xxxxxx']
now_ts = now_date_split + now_time_split # ['yyyy','mm','dd','hh','mm','ss.xxxxxx']
timestamp = ''.join(now_ts[:-1]) # "file_yyyymmddhhmm"
filename = "log_" + timestamp + ".txt"

logFile = open(filename, 'w')

logContent = str(input("Type your log entry: "))

logFile.write(str(actualCompletionDate) + '\n' + logContent)

logFile.close()
