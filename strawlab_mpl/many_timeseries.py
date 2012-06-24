#!/usr/bin/env python
import numpy as np

class ManyTimeseries:
    def __init__(self, ax, times, ys, show=['all','mean'], opts=None):
        # TODO: handle missing data and non-perfectly aligned data.
        for showi in show:
            assert showi in ['all','mean','std']

        if opts is None:
            opts = {}

        self.default_opts = {
            'all': dict(lw=0.2, color='k', alpha=0.6 ),
            'std': dict(alpha=0.4, facecolor='red', edgecolor='none'),
            'mean': dict(lw=2, color='red' ),
            'global': dict(),
            }

        if 'all' in show:
            # plot individual traces before the rest
            kwargs = self._getopts(opts,'all')
            for ysi in ys:
                ax.plot( times, ysi, **kwargs)
        if 'mean' in show or 'std' in show:
            meany = np.mean( ys, axis=0 )
            if 'std' in show:
                # plot std before mean so it is behind
                kwargs = self._getopts(opts,'std')
                stdy = np.std( ys, axis=0 )
                ax.fill_between( times, meany+stdy, meany-stdy, **kwargs)
            if 'mean' in show:
                kwargs = self._getopts(opts,'mean')
                ax.plot( times, meany, **kwargs)

    def _getopts(self,opts,name):
        result = {}
        # apply the defaults first
        result.update( self.default_opts['global'] )
        result.update( self.default_opts[name] )

        # then apply the options passed on this run
        result.update( opts.get('global',{}) )
        result.update( opts.get(name, {}) )
        return result

    def finalize(self):
        return
