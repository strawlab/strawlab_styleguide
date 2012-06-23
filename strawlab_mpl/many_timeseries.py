#!/usr/bin/env python
import numpy as np

class ManyTimeseries:
    def __init__(self,ax, times, ys, show=['all','mean']):
        # TODO: handle missing data, custom plotting options for colors, etc.
        for showi in show:
            assert showi in ['all','mean','std']
        if 'all' in show:
            # plot individual traces before the rest
            for ysi in ys:
                ax.plot( times, ysi, lw=0.2, color='k', alpha=0.6 )
        if 'mean' in show or 'std' in show:
            meany = np.mean( ys, axis=0 )
            if 'std' in show:
                # plot std before mean
                stdy = np.std( ys, axis=0 )
                ax.fill_between( times, meany+stdy, meany-stdy, alpha=0.4,
                                 facecolor='red', edgecolor='none')
            if 'mean' in show:
                ax.plot( times, meany, lw=2, color='red' )

    def finalize(self):
        return
