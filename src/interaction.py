import sys
import numpy

def parse_file(filename):
    f = open(filename,'r')
    parsing = False
    ijfg = 0
    
    datas = {}
    
    for line in f:
        if "I    J DL  Z    R" in line and not parsing:
            parsing = True
            cnt = 3
    
        if parsing:
            cnt -= 1
    
        if parsing and cnt <= 0:
            line = line.replace("\n", "")
            if len(line) == 0:
                parsing = False
                break
            ijfg += 1
            datas[ijfg] = {}
            alldata = line.split()
            datas[ijfg]['I'] = int(alldata[0])
            datas[ijfg]['J'] = int(alldata[1])
            datas[ijfg]['C'] = "C1" in alldata[2]
            fdatas = map(float, alldata[3:])
            datas[ijfg]['IFIE'] = fdatas[-1]
    
    f.close()
    return ijfg,datas

def extract_datas(d,i,n):
    """returns vector of data
       and two table rows with data
    """
    # datas holds the final data to be parsed
    # here we must extract it
    datas = {}
    idx = 0
    ijfg = 0

    rowi = []
    rowj = []
    for ifg in range(2,n+1):
        for jfg in range(1,ifg):
            ijfg += 1
            if ifg != i: continue
            rowi.append("%i" % (ifg))
            rowj.append("%i" % (jfg))
            idx+=1
            datas[idx] = d[ijfg]
    realdata = numpy.zeros(idx)
    for i in range(idx):
        realdata[i] = datas[i+1]
    return [rowi,rowj],realdata

def subtract_datas(d1,d2,length):
    datas = {}
    for ijfg in range(1, length+1):
        datas[ijfg] = {}
        key = 'IFIE'; datas[ijfg][key] = d2[ijfg][key] - d1[ijfg][key]

    return datas

def datas_tovector(dd,key,length):
    data = numpy.zeros(length)
    for ijfg in range(1, length+1):
        data[ijfg-1] = dd[ijfg][key]
    return data
    #return numpy.abs(data)

def diff(f1, f2):

  l1,d1 = parse_file(f1)
  l2,d2 = parse_file(f2)

  if l1 != l2:
      print "error"
      sys.exit()

  dd = subtract_datas(d1,d2,l1)
  return datas_tovector(dd,'IFIE',l1)

uco = diff(sys.argv[1], sys.argv[2])
con = numpy.zeros(len(uco))
if len(sys.argv) > 3:
  con = diff(sys.argv[3], sys.argv[4])
d = uco-con

text,data = extract_datas(d,301,302)

import pylab

fig = pylab.figure(figsize=(10,2))
ax = fig.add_subplot(111)
fig.subplots_adjust(bottom = 0.2)
fig.subplots_adjust(left = 0.05)
fig.subplots_adjust(right = 0.95)

table = ax.table(cellText=text,loc='bottom')
table_props = table.properties()
table_cells = table_props['child_artists']
for cell in table_cells: 
    cell.set_fontsize(2)
    cell.set_height(0.05)
    cell.set_edgecolor('w')
    
ind = numpy.arange(1, len(data)+1)
ax.bar(ind,data,facecolor='#000000', edgecolor=None, linewidth=0, width=1.0)
ax.set_xlim(min(ind),max(ind)+1)
ax.set_xticks([])
pylab.savefig('out.eps',dpi=300)

sys.exit()

ifrom = 1 #len(d)-302
ito = len(d)
print "2-body E(uco)     =%8.4f" % sum(uco[ifrom-1:ito])
print "2-body E(con)     =%8.4f" % sum(con[ifrom-1:ito])
print "2-body E(uco-con) =%8.4f" % sum(d[ifrom-1:ito])
ind = numpy.arange(ifrom,ito+1) #l1+1)
pylab.bar(ind, d[ifrom-1:ito], facecolor='#000000', edgecolor=None, linewidth=0)
pylab.title("Pair-wise interaction energy differences for the entire enzyme")
pylab.xlabel("fragment pair index")
pylab.xlim(ifrom,ito)
pylab.ylabel('$\Delta \Delta E$ [kcal/mol]')

pylab.savefig('dd.eps', dpi=300)
