#!/usr/bin/env python
import numpy as np

class CategoryScatter:
    def __init__(self,ax, categories, xscatter=0.5):
        self.xticks = []
        self.xticklabels = []
        self.ax = ax
        for xval, (name, yvals) in enumerate( categories ):
            n = len(yvals)
            xvals = xval*np.ones( (n,) )
            xvals += xscatter*np.random.uniform( size=n ) - xscatter*0.5
            self.ax.plot( xvals, yvals, 'o', alpha=0.3, mec='none' )
            self.xticks.append( xval )
            self.xticklabels.append( name )

    def finalize(self):
        self.ax.set_xticks( self.xticks )
        self.ax.set_xticklabels( self.xticklabels )
