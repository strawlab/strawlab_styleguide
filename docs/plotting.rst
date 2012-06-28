plotting
========

The basic idea behind our plots is that we want them to convey the
most information in the simplest, most intuitive way possible. Edward
Tufte's works are great inspiration here.

There is no completely automated way to make such plots, but the
**strawlab_mpl** package contains various utilities that make this
easier when using `Matplotlib <http://matplotlib.sourceforge.net>`_.

.. image:: images/panel_scatter.png

Let's take the plot above as an example. This shows the distribution
of samples from three categories. A simple plot done with Matplotlib would look like this.

.. image:: images/scatter_bad.png
