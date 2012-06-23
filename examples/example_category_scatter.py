#!/usr/bin/env python
import numpy as np
import os, sys
import strawlab_mpl.defaults as smd; smd.setup_defaults()
from strawlab_mpl.category_scatter import CategoryScatter
from strawlab_mpl.spines import spine_placer, auto_reduce_spine_bounds

import matplotlib.pyplot as plt
import matplotlib.ticker as mticker

def make_category_scatter_figure():
    # Generate some fake data in 3 categories.
    categories = [('a',np.random.randn( 15 )),
                  ('b',np.random.randn( 16 )+0.6),
                  ('c',np.random.randn( 20 )-0.8),
                  ]

    # Build a figure and place a single axes instance in it.
    fig = plt.figure(figsize=(4,3))
    ax1 = fig.add_subplot(1,1,1)

    # Use our helper function to do the category scatter plot.
    cs = CategoryScatter( ax1, categories )

    # Locate the axes spines on the left and bottom.
    spine_placer(ax1, location='left,bottom' )

    # Finalize the category scatter plot (stuff that can only be done
    # after the spines are placed).
    cs.finalize()

    # Add standard y label.
    ax1.set_ylabel('y value (units)')

    # Now, add a final few touchups.
    ax1.spines['bottom'].set_color('none') # don't draw bottom spine
    ax1.yaxis.set_major_locator( mticker.MaxNLocator(nbins=4) )
    auto_reduce_spine_bounds( ax1 )

    fig.tight_layout()
    return fig

if __name__=='__main__':
    np.random.seed(3) # ensure that example always looks the same
    fig = make_category_scatter_figure()
    if 0:
        plt.show()
    if 1:
        # Saving as .svg will allow opening and editing in Inkscape.
        fname = 'scat.svg'
        fig.savefig(fname)
        print 'saved',fname
