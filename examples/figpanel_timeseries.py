#!/usr/bin/env python
import numpy as np
import os, sys
import strawlab_mpl.defaults as smd; smd.setup_defaults()
from strawlab_mpl.many_timeseries import ManyTimeseries
from strawlab_mpl.spines import spine_placer, auto_reduce_spine_bounds

import matplotlib.pyplot as plt
import matplotlib.ticker as mticker

def make_many_timeseries_figure():
    # Generate some fake data in 4 timeseries
    times = np.arange( 0, 200.0, 0.01 )
    nt = len(times)
    ys = []
    for i in range(4):
        ys.append( np.sin( times*2*np.pi*0.02 + i*20 ) + 0.13*np.random.randn(nt) )

    # Build a figure and place a two axes instances in it.
    fig = plt.figure(figsize=(8,6))
    ax1 = fig.add_subplot(2,1,1)
    ax2 = fig.add_subplot(2,1,2)

    # Use our helper function to plot the multiple timeseries.
    mts1 = ManyTimeseries( ax1, times, ys, show=['all','mean'] )

    # Use our helper function to plot the multiple timeseries.
    mts2 = ManyTimeseries( ax2, times, ys, show=['mean','std'] )

    # Locate the axes spines.
    spine_placer(ax1, location='left' )
    spine_placer(ax2, location='left,bottom' )

    # Finalize the plots (stuff that can only be done
    # after the spines are placed).
    mts1.finalize()
    mts2.finalize()

    # Add standard axis labels.
    ax1.set_ylabel('y1 value (units)')
    ax2.set_ylabel('y2 value (units)')
    ax2.set_xlabel('time (seconds)')

    # Now, add a final few touchups.
    ax1.yaxis.set_major_locator( mticker.MaxNLocator(nbins=4) )
    ax1.set_xticks([])
    ax2.yaxis.set_major_locator( mticker.MaxNLocator(nbins=4) )
    auto_reduce_spine_bounds( ax1 )
    auto_reduce_spine_bounds( ax2 )

    fig.tight_layout()
    return fig

if __name__=='__main__':
    np.random.seed(3) # ensure that example always looks the same
    fig = make_many_timeseries_figure()
    if 0:
        plt.show()
    if 1:
        fname = 'panel_timeseries.svg'
        fig.savefig(fname)
        print 'saved',fname
