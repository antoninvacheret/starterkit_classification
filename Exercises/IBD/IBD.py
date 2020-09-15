import numpy as np
import matplotlib.pyplot as plt
import data_getters
import mpl_examples 

#-------------------------------------------------------------------------------

def run():
	# Recall the available files.
	# f_name should be one of ['IBD_off_nonshifted.npy', 
	#						   'IBD_on_nonshifted.npy',
	#						   'IBD_sim_signal_nonshifted.npy',
	#						   'IBD_off_shifted.npy',
	#						   'IBD_on_shifted.npy']

	# Files are small relative to RAM, can load them all at once easily. 
	f_name = 'IBD_on_nonshifted.npy'
	data = data_getters.get_data(f_name)

	# Take a look at the first entry. 
	# Each entry is of the format: 
	# [delta_t (ns), delta_xy (cubes), delta_z (cubes), delta_r (cubes), 
	#  volume (cubes), prompt_energy (MeV)].

	plot_times(data)

	# Pop up all plots made at the end of the run.
	plt.show() 



#-------------------------------------------------------------------------------

def apply_rt_cuts(data):
	print 'TODO'


#-------------------------------------------------------------------------------

def plot_times(data):
	# Function for part 1b) code.
	print 'TODO'


#-------------------------------------------------------------------------------

def subselect_cut(data, column, upper_cut):
	# Return an array where entries that fail the cut are removed.
	return data[data[:,column]<upper_cut, :]


#-------------------------------------------------------------------------------

run()