import sys

for i in range(1,442):
    f = open('./'+str(i)+'.csv','r')
    temp = f.read()
    f.close()
    f = open('./'+str(i)+'.csv','w')
    f.write('TimestampLocal,UsageKW\n')
    f.write(temp)
    f.close()
