plotting
========

The basic idea behind our plots is that we want them to convey the
most information in the simplest, most intuitive way possible. `Edward
Tufte's works <http://www.edwardtufte.com/tufte/books_vdqi>`_ are
great inspiration here.

There is no completely automated way to make such plots, but the
**strawlab_mpl** package contains various utilities that make this
easier when using `matplotlib <http://matplotlib.sourceforge.net>`_.

Example 1 - category scatter plot
---------------------------------

Let's take a look at an example. We'll use a relatively simple
category scatter plot showing the distribution of samples from three
categories. A simple plot done with matplotlib would look like the
plot on the left. On the right is an example with much better style.

.. image:: images/bad_good.png

Example 2 - timeseries data
---------------------------

Our second example is timeseries data. The top plot shows three
individual trials (in grey) and the mean (in red). The bottom plot
shows the mean (red line) in a shaded region denoting the standard
deviation. These are both good ways to convey the mean response while
still showing some of the underlying variation.

.. image:: images/panel_timeseries.png

