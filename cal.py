import psutil
disk_usage = 20
cpu_usage = 75
def system_health_check(disk_usage, cpu_usage):
  if((psutil.disk_usage('/')>=disk_usage) and 
  (psutil.cpu_percent<=cpu_usage)) :
    return True
  else :
    return False
while(True):
  print("1 - Disk Usage")
  print("2 - CPU Usage")
  print("3 - health Check")
  print("9 - Exit")
  mychoice=int(input("Please enter your choice : "))
  if (mychoice==1):
    print("Percentage of disk used : ", psutil.disk_usage('/'))
    continue
  if (mychoice==2):
    print("Percentage of CPU used : ", psutil.cpu_percent())
    continue
  if (mychoice==3)
    if system_health_check(20,75):
      print("System is healthy")
    else :
      print("Error")
  if (mychoice==9):
    print("good bye")
    break
