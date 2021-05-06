import math
import sys
# Ranges in the fio logfile are in bytes
KB=1024
MB=KB*1024
GB=MB*1024
#Total LBARANGE
LBARANGE=(10*GB)-1
#For purposes of the chart take SQRT of LBARANGE
LBAXY=math.sqrt(LBARANGE)
XRANGE=math.floor(LBAXY)
YRANGE=math.ceil(LBAXY)

filename=sys.argv[1]
print("LBA Range is ",LBARANGE)
with open(filename) as f:
    for line in f:
        #Only process lines in the form of
        #device operation size length
        ff=line.find("read")
        if ff < 0:
            continue
        data=line.split()
        LBA=int(data[2])
        LBAX=(LBA%XRANGE)
        LBAY=round((LBA/YRANGE))
        print(LBA,LBAX,LBAY)
