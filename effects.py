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
	

def vibrato():


def butter_bandpass(data, lowcut, highcut, fs, order):
	nyq = 0.5 * fs
	low = lowcut / nyq
	high = highcut / nyq
	b, a = butter(order, [low, high], btype='band')
	y = lfilter(b, a, data)
	return y


		
	
	
