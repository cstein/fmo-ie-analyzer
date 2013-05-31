from matplotlib.colors import LinearSegmentedColormap, hex2color

def color(r,g,b):
  if r > 255: raise ValueError("r between 0 and 255")
  if g > 255: raise ValueError("r between 0 and 255")
  if b > 255: raise ValueError("r between 0 and 255")
  rs = str(hex(r))[2:].upper()
  gs = str(hex(g))[2:].upper()
  bs = str(hex(b))[2:].upper()
  if len(rs) == 1: rs = "0"+rs
  if len(gs) == 1: gs = "0"+gs
  if len(bs) == 1: bs = "0"+bs
  return "#%s%s%s" % (rs,gs,bs)

def hexidx(i,n):
  return int(round(255.0*(i)/n))

def validx(f,t,i,k,n):
  return f+t*(i+k)/n

def make_colormap(name,absmax,zero_spread,n):
  if n < 2: raise ValueError("n > 1 requred.")
  # first we add some white padding
  #colors = [(0.5-zero_spread, "#FFFFFF"), (0.5, "#FFFFFF"), (0.5+zero_spread, "#FFFFFF")]
  colors = [(0.5, "#FFFFFF")]

  # make colornumbers
  cidx = [hexidx(i,n) for i in range(n)]
  ridx = [validx(0.0,0.5-zero_spread,i,0,n) for i in range(n)]
  ridx.reverse()
  bidx = [validx(0.5+zero_spread,0.5-zero_spread,i,1,n) for i in range(n)]

  # now we add colors
  reds = [color(255,c,c) for c in cidx]
  reds.reverse()
  blus = [color(c,c,255) for c in cidx]
  blus.reverse()
  # reds are negative so they are added here
  # from lightest to darkest
  cdict = dict(red=[], green=[], blue=[])
  for item in zip(ridx,reds):
    colors.insert(0,item)

  for item in zip(bidx,blus):
    colors.append(item)

  # transfer colorarray to cdict
  for val,cc in colors:
    r,g,b = hex2color(cc)
    cdict['red'].append((val,r,r))
    cdict['green'].append((val,g,g))
    cdict['blue'].append((val,b,b))
  return LinearSegmentedColormap(name, cdict)
