'''
This file contains modules for different effects and tools to modilfy or filter 
input stream of audio. This file is a part of DSP final project. 
'''
# 
# Created by 
# Drumil Mahajan, New York University, School of Engineering, 
# Class of 2017. 

	
	
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


def robotization(input_string, BLOCKSIZE): 
	'''
	Parameters : 
	BLOCKSIZE : size of the block, type int
	input_string : input string of audio data of size BLOCKSIZE, type string
	
	Returns: 
	output_string : robotized version of input_string , type string 
	
	Brief: 
	Converts the input_string into robotzed output_stirng 
	'''
	input_tuple = struct.unpack('h' * BLOCKSIZE * 2, input_string)

    spect = np.fft.fft(input_tuple)
	output = np.fft.ifft(np.absolute(spect))
	for n in range(0,len(output)):
        output_block[n] = clip_n(output[n], 16)
		# output_block[n] = output[n]
	output_string = struct.pack('h' * 2 *  BLOCKSIZE, *output_block)	
	return output_string	

def whisperisation(input_stream): 

def vibrato(): 

def band_pass(self, low, high): 

def butter_bandpass(self,lowcut, highcut, fs, order):
	nyq = 0.5 * fs
	low = lowcut / nyq
	high = highcut / nyq
	b, a = butter(order, [low, high], btype='band')
	y = lfilter(b, a, data)
	return y


def butter_bandpass_filter(self, data, lowcut, highcut, fs, order=5):
	
	return y
		
	
	
