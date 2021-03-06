import psutil
import datetime
import os

fileName = "myLoggedData.csv" # Create this file (empty) before running the app. 

# adding the header.
if os.stat(fileName).st_size==0:
    file1=open(fileName,'a')
    file1.write("date,cpu_frequency,cpu_percentage,cpu1,memory_percent\n")
    file1.close()

print("Starting to log.")
while True:
    currentState=[]
    currentState.append(str(datetime.datetime.now()))
    currentState.append(psutil.cpu_freq().current / 100) # scaling down, to fit in rest of the values.
    cpu_percent=psutil.cpu_percent(interval=15, percpu=True) # since interval=15 is used, there is no need to sleep.
    sum=0
    for i in cpu_percent:
        sum+=i
    currentState.append(sum/len(cpu_percent))
    currentState.append(cpu_percent[0]) # just to compare a little bit.
    currentState.append(psutil.virtual_memory().percent)
    x=",".join(map(str,currentState)) + "\n"
    print("currentState = ")
    print(currentState)
    file1=open(fileName,'a')
    file1.write(x)
    file1.close()


