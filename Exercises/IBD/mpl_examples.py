import matplotlib.pyplot as plt
import numpy as np

#-------------------------------------------------------------------------------

# Greeting yee enlightened folk! Welcome to the 21st century, where there is no 
# capital ```T``` in sight. Congratulations on leaving the dark ages of years 
# gone past with TBrowsers. This file gives some that can either be copied or 
# imported directly into analysis scripts to make typical HEP plots. Enjoy!

#-------------------------------------------------------------------------------

def plot_histogram(xs, x_range, n_bins, x_label, y_label, cumulative_and_normalise=False):
	
	# Plot a histogram of the distribution of xs. xs can be any iterable 
	# container, e.g. python list, 1D numpy array etc. x_range should be a 
	# tuple/list with two entries (xlow, xup), and the labels should be strings.

	# For the general use case, better to avoid the global plt. methods,
	# even though the code is a little longer.
	fig, ax = plt.subplots() 

	# Fig is a canvas, ax is an object that occupies part of that canvas with a plot.
	ax.hist(xs, range = x_range, bins = n_bins, 
		cumulative = cumulative_and_normalise, normed = cumulative_and_normalise)
	

	# Just the esthetics ----------------
	ax.set_xlabel(x_label)
	ax.set_ylabel(y_label)
	ax.grid(True)
	ax.set_xlim(x_range) # For consistency.

	# Pop up.
	return ax


#-------------------------------------------------------------------------------

def plot_histograms(xs_set, x_range, n_bins, x_label, y_label, legend_labels, 
	cumulative_and_normalise=False):

	# Plot the histograms of the distribution of xs_set. xs[i] can be any iterable 
	# container, e.g. python list, 1D numpy array etc. x_range should be a 
	# tuple/list with two entries (xlow, xup), and the labels should be strings.
	# xs_set should be a list of iterables.

	fig, ax = plt.subplots() 
	for i in range(len(xs_set)):
		# Use the histtype='step' flag to have just the edges of the bins.
		ax.hist(xs_set[i], range = x_range, bins = n_bins, label = legend_labels[i],
			cumulative = cumulative_and_normalise, normed = cumulative_and_normalise,
			histtype='step', lw = 2)
	

	# Just the esthetics ----------------
	ax.set_xlabel(x_label)
	ax.set_ylabel(y_label)
	ax.legend(loc = 'lower right', prop={'size':11})
	ax.grid(True)
	ax.set_xlim(x_range)

	return ax


#-------------------------------------------------------------------------------

def plot_bar_stack(all_bin_heights, bin_edges, x_range, x_label, y_label, legend_labels):

	# Plot the stacked histograms of the xs_set. xs[i] can be any iterable 
	# container, e.g. python list, 1D numpy array etc. x_range should be a 
	# tuple/list with two entries (xlow, xup), and the labels should be strings.
	# xs_set should be a list of iterables.

	cols = ['b', 'r', 'g', 'y']
	fig, ax = plt.subplots() 
	xs_prev = np.zeros(len(all_bin_heights[0]))
	for iHist in range(len(all_bin_heights)):
		ax.bar(bin_edges[0:-1], all_bin_heights[iHist], bin_edges[1] - bin_edges[0], 
			    bottom = xs_prev, label = legend_labels[iHist], facecolor = cols[iHist])
		
		xs_prev += all_bin_heights[iHist]
	

	# Just the esthetics ----------------
	ax.set_xlabel(x_label)
	ax.set_ylabel(y_label)
	ax.legend(loc = 'upper right', prop={'size':11})
	ax.grid(True)
	ax.set_ylim(bottom=0)
	ax.set_xlim(x_range)

	return ax


#-------------------------------------------------------------------------------

def scatter_plot(all_xs, all_ys, x_range, y_range, x_label, y_label, legend_labels):

	# Plot a scatter plot. all_xs and all_ys can be tuples of different sets of 
	# co-ordinates (e.g. a set for signal, a set for background), and each is 
	# put on a subplot in a single row.
	fig = plt.figure(figsize=[15.5,6])

	axs = []

	for i in range(len(all_xs)): 
		ax = plt.subplot(1, len(all_xs), i)
		ax.scatter(all_xs[i], all_ys[i], label = legend_labels[i])

		# Just the esthetics ----------------
		ax.set_xlabel(x_label)
		ax.set_ylabel(y_label)

		ax.grid(True)
		ax.set_ylim(y_range)
		ax.set_xlim(x_range)
		axs.append(ax)

	return axs


#-------------------------------------------------------------------------------
