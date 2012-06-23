def spine_placer( ax, location='left,bottom' ):
    expected_locations = ['left','right','top','bottom']

    locations = location.split(',')
    for loc in locations: # loc in ['left','right','top','bottom']
        if loc not in expected_locations:
            raise ValueError('unexpected spine location: %s'%loc)

    for loc, spine in ax.spines.items(): #loc in ['left','right','top','bottom']
        if loc not in expected_locations:
            raise ValueError('unexpected spine location: %s'%loc)
        if loc in locations:
            spine.set_position( ('outward',10) ) # outward by 10 points
        else:
            spine.set_color('none') # don't draw spine

    if ('left' in locations) and (not 'right' in locations):
        ax.yaxis.set_ticks_position('left')
    elif ('right' in locations) and (not 'left' in locations):
        ax.yaxis.set_ticks_position('right')

    if ('bottom' in locations) and (not 'top' in locations):
        ax.xaxis.set_ticks_position('bottom')
    elif ('top' in locations) and (not 'bottom' in locations):
        ax.xaxis.set_ticks_position('top')

def auto_reduce_spine_bounds( ax ):
    yticks = ax.get_yticks()
    y0, y1 = ax.viewLim.intervaly
    ymin = min(y0,y1)
    ymax = max(y0,y1)
    good_cond = (yticks >= ymin) & (yticks <= ymax)
    yticks = yticks[good_cond]
    if len(yticks):
        ax.spines['left'].set_bounds( yticks[0], yticks[-1] )
        ax.spines['right'].set_bounds( yticks[0], yticks[-1] )


    xticks = ax.get_xticks()
    x0, x1 = ax.viewLim.intervalx
    xmin = min(x0,x1)
    xmax = max(x0,x1)
    good_cond = (xticks >= xmin) & (xticks <= xmax)
    xticks = xticks[good_cond]
    if len(xticks):
        ax.spines['top'].set_bounds( xticks[0], xticks[-1] )
        ax.spines['bottom'].set_bounds( xticks[0], xticks[-1] )
