'''
This file contains modules for different effects and tools to modilfy or filter 
input stream of audio. This file is a part of DSP final project. 
'''
# 
# Created by 
# Drumil Mahajan, New York University, School of Engineering, 
# Class of 2017. 

import random
import cmath
import pyaudio
import struct
import wave
import math
import numpy as np
	
	
def clip_n(input_data, n):
	'''
	This function takes two arguments.
	stream is a floating point number
	n is an integer

	This funtions bound the value of input_data between max and min of n bit signed number
	'''
	
	self.input_data = input_data
	self.n = n
	
	MAX = 2**(n-1) - 1
	MIN = -2**(n)
	if input_data > MAX:  
		return MAX
	elif input_data < MIN:
		return MIN
	else:
		return input_data


def robotization(input_tuple, BLOCKSIZE): 
	'''
	Parameters : 
	BLOCKSIZE : size of the block, type int
	input_string : input tuple of audio data of size BLOCKSIZE, type int
	
	Returns: 
	output_block : list of output data. type int 
	
	Brief: 
	Converts the input_string into robotized output_block
	'''
	
	#input_tuple = struct.unpack('h' * BLOCKSIZE * 2, input_string)
	output_block = [0 for n in range(0, 2* BLOCKSIZE)]

    spect = np.fft.fft(input_tuple)
	output = np.fft.ifft(np.absolute(spect))
	for n in range(0,len(output)):
        output_block[n] = clip_n(output[n], 16)
		# output_block[n] = output[n]
	#output_string = struct.pack('h' * 2 *  BLOCKSIZE, *output_block)	
	return output_block	

def whisperisation(input_tuple, BLOCKSIZE): 
	'''
	Parameters : 
	BLOCKSIZE : size of the block, type int
	input_string : input tuple of audio data of size BLOCKSIZE, type int
	
	Returns: 
	output_block : list of output data. type int 
	
	Brief: 
	Converts the input_string into whisperization output_block
	'''
	
	output_block = [0 for n in range(0, BLOCKSIZE)]
	
	random_phase = 2 * cmath.pi * random.random()
	random_complex = cmath.cos(random_phase) + (cmath.sin(random_phase))j
	
	spect = np.fft.fft(input_tuple)
	output = np.fft.ifft(np.absolute(spect) * random_complex)
	
	for n in range(0,len(output)):
		output_block[n] = clip_n(output[n], 16)
	
	return output_block	
	

def vibrato(BLOCKSIZE):
	for n in range(0, BLOCKSIZE):
        
    # Get previous and next buffer values (since kr is fractional)
    # Processing for left channel
        kr_prev = int(math.floor(kr))               
        kr_next = kr_prev + 1
        frac = kr - kr_prev    # 0 <= frac < 1
        if kr_next >= buffer_MAX:
            kr_next = kr_next - buffer_MAX
    

        # Compute output value using interpolation
        output_value_L = (1-frac) * buffer[kr_prev] + frac * buffer[kr_next]

        # Update buffer (pure delay)
        buffer[kw] = input_value[n]

        # Increment read index
        kr = kr + 1 + W * math.sin( 2 * math.pi * f0 * n / RATE )
            # Note: kr is fractional (not integer!)

        # Ensure that 0 <= kr < buffer_MAX
        if kr >= buffer_MAX:
            # End of buffer. Circle back to front.
            kr = 0

        # Increment write index    
        kw = kw + 1
        if kw == buffer_MAX:
            # End of buffer. Circle back to front.
            kw = 0
        
        # Processing for Right channel     
        kr_prev_R = int(math.floor(kr_R))               
        kr_next_R = kr_prev_R + 1
        frac_R = kr_R - kr_prev_R    # 0 <= frac < 1
        if kr_next_R >= buffer_MAX_R:
            kr_next_R = kr_next_R - buffer_MAX_R
    

        # Compute output value using interpolation
        output_value_R = (1-frac_R) * buffer_R[kr_prev_R] + frac_R * buffer_R[kr_next_R]

        # Update buffer (pure delay)
        buffer_R[kw] = input_value[n]

        # Increment read index
        kr_R = kr_R + 1 + W_R * math.sin( 2 * math.pi * f0_R * n / RATE )
        # Note: kr is fractional (not integer!)

        # Ensure that 0 <= kr < buffer_MAX
        if kr_R >= buffer_MAX_R:
            # End of buffer. Circle back to front.
            kr_R = 0

        # Increment write index    
        kw_R = kw_R + 1
        if kw_R == buffer_MAX_R:
            # End of buffer. Circle back to front.
            kw_R = 0    

        # clip and put output values in two channels
        output_block[2*n] = clip16(output_value_L)
        output_block[2*n + 1] = clip16(output_value_R)


def butter_bandpass(data, lowcut, highcut, fs, order):
	nyq = 0.5 * fs
	low = lowcut / nyq
	high = highcut / nyq
	b, a = butter(order, [low, high], btype='band')
	y = lfilter(b, a, data)
	return y


		
	
	
