#!/usr/bin/python3
from numpy import array,arange,abs as np_abs
from numpy.fft import rfft, rfftfreq
from scipy.io import wavfile
import matplotlib.pyplot as plt
d = {'A':697,'B':770,'C':852,'D':941,'C1':1209,'C2':1336,'C3':1477} 
for z in range(10):
 samplerate,data=wavfile.read('/home/vlad/KP/dtmf_wav/dtmf%i.wav' % z)
 FD=44100
 N=len(data)
 time=data/float(FD)
 spectrum=rfft(data)
 amplitude=np_abs(spectrum)/N #амплитуда
 freq=rfftfreq(N,1./FD) #частота
 m=0
 ma=max(amplitude)-200
 file=open('spec.txt','w')
 print('FILE',z)
 for i in (amplitude):
  m+=1
  if i>ma:
   print('AMP=%0.3f'% i,'\t','FREQ=%.3f' % freq[m])
