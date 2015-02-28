.. Graphfab: a layout engine for SBML

Graphfab Documentation
====================================

Contents:

.. toctree::
   :maxdepth: 2

.. automodule:: graphfab
    :members:

This here's the doc

.. py:function:: enumerate(sequence[, start=0])

   Return an iterator that yields tuples of an index and an item of the
   *sequence*. (And so on.)
   
   Load the model
   
   >>> model = graphfab.loadsbml('/home/wisp/stuff/SauroLab/develop/graphfab-snake/testcases/twocompsys-ex.xml')
   >>> layout = model.layout
   
   Access the API to obtain the network parameters
   
   >>> network = layout.network
   >>> canvas = layout.canvas
   
   Randomize the initial configuration and run the FR algorithm
   
   >>> network.randomize(canvas)
   >>> network.autolayout()
   
   Shrink or enlarge a network so that it fits within a window
   
   >>> layout.fitwindow(0,0,300,300)

Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`

