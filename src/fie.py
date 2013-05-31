import numpy

class FIE(dict):
    """Represents N*(N-1)/2 interaction energies
    """

    def __init__(self, filename=""):
        """Parses an FMO log file for interaction energies
           everything is stored in a dictionary indexed from
           1 to N*(N-1)/2

           values for ifg and jfg are also stored

           parameters
             filename:    the filename to load
        """
        if len(filename) == 0: return
        
        f = open(filename,'r')
        parsing = False
        ijfg = 0

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
                self[ijfg] = {}
                alldata = line.split()
                self[ijfg]['I'] = int(alldata[0])
                self[ijfg]['J'] = int(alldata[1])
                self[ijfg]['C'] = "C1" in alldata[2]
                fself = map(float, alldata[3:])
                self[ijfg]['FIE'] = fself[-1]
        f.close()
        self.length = ijfg

    def toSquareMap(self):
        """Converts the N*(N-1)/2 values to a square map of
           size N*N - negative values are stored in one half:
        """
        l1 = int(numpy.sqrt(2*self.length))+1
        d = numpy.zeros((l1,l1))
        for ijfg in range(1, self.length+1):
            i = self[ijfg]['I']
            j = self[ijfg]['J']
            val = self[ijfg]['FIE']
            if val < 0:
                d[i-1][j-1] = self[ijfg]['FIE']
            else:
                d[j-1][i-1] = self[ijfg]['FIE']
        return d

    def __sub__(self, other):
        if self.length != other.length:
            raise ValueError("FIEs must be of equal length. Got %3i and %3i" % (self.length, other.length))
        datas = FIE()
        for ijfg in range(1, self.length+1):
            if self[ijfg]['I'] != other[ijfg]['I']: raise ValueError("FIEs do not match.")
            if self[ijfg]['J'] != other[ijfg]['J']: raise ValueError("FIEs do not match.")
            datas[ijfg] = {}
            datas[ijfg]['I'] = self[ijfg]['I']
            datas[ijfg]['J'] = self[ijfg]['J']
            datas[ijfg]['FIE'] = self[ijfg]['FIE'] - other[ijfg]['FIE']
        datas.length = ijfg
        return datas
