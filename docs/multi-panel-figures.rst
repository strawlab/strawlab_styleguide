multi panel figures
===================

Most figures in most papers often have many panels. Regenerating a
single panel within a multi-panel figure can be cumbersome if it means
every minor change need the entire figure to be remade manually. For
this reason, I suggest automating the construction of such multi-panel
figures so they can be re-built whenever a constituent panel
changes. The `svg_stack <https://github.com/astraw/svg_stack.git>`_
library serves this purpose when used with .svg figure files. It
strives to make the output compatible with further editing by
`Inkscape <http://inkscape.org>`_.

Consequently, the workflow in our lab consists of:

 1. rendering intermediate panels to the .svg format
 2. compose these panels into a figure using svg_stack
 3. (if necessary) manual editing of the final figure with Inkscape
 4. export from Inkscape into the required target format (.png or .pdf, typically)

rendering to svg with matplotlib
--------------------------------

I have two main tips to make nice SVG files with matplotlib.

First is to adjust font settings so that the fonts are rendered as SVG
strings (rather than converting the text into paths). I also prefer
the fonts Arial and Times New Roman to the matplotlib defaults. This
can be done with::

    import strawlab_mpl.defaults as smd
    smd.setup_defaults()

Under the hood, the important parts of the above are::

    rcParams = matplotlib.rcParams
    rcParams['svg.fonttype'] = 'none' # No text as paths. Assume font installed.

    rcParams['font.serif'] = ['Times New Roman']
    rcParams['font.sans-serif'] = ['Arial']
    rcParams['font.family'] = 'sans-serif'

The second tip for nice svg files is to let matplotlib convert any
elements with many data into a raster plot. This dramatically
decreases file size and rendering work. Doing this is very simple --
include a "rasterize=True" kwarg when calling your relevant
matmplotlib command::

    ax.plot( giant_array_of_x_values,
             giant_array_of_y_values,
             rasterize=True)


compose these panels into a figure using svg_stack
--------------------------------------------------

svg_stack is meant for composing multiple elements into a bigger
page. The `instructions included with svg_stack
<https://github.com/astraw/svg_stack.git>`_ are recommended to get you
started.


export from Inkscape into the desired format
--------------------------------------------

Inkscape can be scripted to export files at the command line. For
example, this will render a .png file of <INPUT_FILENAME>::

    inkscape -f <INPUT_FILENAME> --export-dpi=90  --export-background=white --export-png=OUTPUT_FILENAME
