import numpy as np

def get_data(f_name):
	# f_name should be one of ['IBD_off_nonshifted.npy', 
	#						   'IBD_on_nonshifted.npy',
	#						   'IBD_sim_signal_nonshifted.npy',
	#						   'IBD_off_shifted.npy',
	#						   'IBD_on_shifted.npy']
	return np.load(f_name)