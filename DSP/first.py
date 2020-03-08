import numpy as np
import wave
import struct
import matplotlib.pyplot as plt

#this is a G#
fr = 36.71
#sampling rate
num_samples = 48000
# The sampling rate of the analog to digital convert
sampling_rate = 48000.0
#"loudness"
amplitude = 16000/2
file = "test_chord.wav"
full = [0*z for z in range(num_samples)]
#monster lenght sine declaration
sine_wave = [
#np.sin(2 * np.pi * fr * x/sampling_rate) for x in range(num_samples)]
np.sin(2 * np.pi * 82.41 * x/sampling_rate) for x in range(num_samples)]

octave = [
np.sin(2 * np.pi * 82.41*2 * y/sampling_rate) for y in range(num_samples)]

b = [
np.sin(2 * np.pi * 123.47 * y/sampling_rate) for y in range(num_samples)]
#"""
for i in range(len(sine_wave)):
    full[i] = sine_wave[i] + b[i] + octave[i]
#"""
#number of frames (or samples)
nframes = num_samples
comptype = "NONE"
compname = "not compressed"
nchannels = 1 #mono
sampwidth = 2 #bytes

wav_file=wave.open(file, 'w')
wav_file.setparams(
(nchannels, sampwidth, int(sampling_rate), nframes, comptype, compname))

#for s in sine_wave:
for s in full:
   wav_file.writeframes(struct.pack('h', int(s*amplitude)))

plt.subplot(4,1,1)
plt.title("Original sine wave")
# Need to add empty space, else everything looks scrunched up!
plt.subplots_adjust(hspace=.5)
plt.plot(sine_wave[:1000])
plt.subplot(4,1,2)
plt.title("Octave 1")
plt.plot(octave[:1000])
plt.subplot(4,1,3)
plt.title("Octave 2")
plt.plot(b[:1000])
plt.subplot(4,1,4)
plt.title("Original + Octaves")
plt.plot(full[:3000])
plt.show()
