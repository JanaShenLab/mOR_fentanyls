import pandas as pd

#read the output file ("DZ") obtained from PLUMED
#CV1 is z-position (used as cutoff for exit)
data = pd.read_csv('DZ',delimiter='\s+',comment='#',
        header=None,names=['time','CV1','CV2','bias','rct','acc']) 

#z = 15 angstrom from COM of binding pocket as exit cutoff
data = data[:data[data['CV1']>15].index[0]+1]

x = data['time'].tolist()
y = data['acc'].tolist()
print('real exit time (sec): ', x[-1]*y[-1]/10**11)

