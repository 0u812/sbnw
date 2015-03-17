.. SBNW: a layout engine for SBML

SBNW Documentation
====================================

Contents:

.. toctree::
   :maxdepth: 2

.. automodule:: graphfab
    :members:

SBNW Usage Example
   
   Load the model
   
   >>> model = graphfab.loadsbml('/path/to/sbnw/testcases/twocompsys-ex.xml')
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

