.. SBNW: a layout engine for SBML

libSBNW Documentation
====================================

Contents:

Example 1: Basic Usage

   Load the model

   >>> model = sbnw.loadsbml('/path/to/sbnw/testcases/twocompsys-ex.xml')
   >>> layout = model.layout
   >>> canvas = layout.canvas

   Access the network from the layout

   >>> network = layout.network

   Shrink or enlarge a network so that it fits within a window

   >>> layout.fitwindow(0,0,300,300)

   Access the node coordinates

   >>> for node in network.nodes:
   >>>   print(node.centroid)

Example 2: Add layout information to an SBML model

   Load the model

   >>> model = sbnw.loadsbml('/path/to/sbnw/testcases/ant_power_law_sbml.xml')
   >>> layout = model.layout
   >>> canvas = layout.canvas
   >>> network = layout.network

   Randomize the initial configuration and run the FR algorithm

   >>> network.randomize(canvas)
   >>> network.autolayout()

   Shrink or enlarge a network so that it fits within a window

   >>> layout.fitwindow(0,0,300,300)

   Override SBML level/version if desired

   >>> model.level = 3
   >>> model.version = 1

   Save the model to an SBML file

   >>> model.save('/path/to/output.xml')

API Documentation

.. currentmodule:: sbnw

.. autosummary::
   :nosignatures:
   :toctree: generated/

   loadsbml
   point
   network
   layout
   canvas
   node
   compartment
   reaction
   transform

Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`

