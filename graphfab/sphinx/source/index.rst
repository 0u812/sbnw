.. SBNW: a layout engine for SBML

libSBNW Documentation
====================================

Contents:

Example 1: Basic Usage

   Import the module

   >>> import sbnw

   Load an SBML model

   >>> model = sbnw.loadsbml('twocompsys-ex.xml') # included in the test cases

   Shrink or enlarge a network so that it fits within a window

   >>> model.network.fitwindow(0,0,300,300)

   Access the node coordinates

   >>> for node in model.network.nodes:
   >>>   print(node.centroid)

Example 2: Add layout information to an SBML model

   Import the module

   >>> import sbnw

   Load an SBML model

   >>> model = sbnw.loadsbml('ant_power_law_sbml.xml') # included in the test cases

   Randomize the initial configuration and run the FR algorithm

   >>> model.network.randomize(canvas)
   >>> model.network.autolayout()

   Shrink or enlarge a network so that it fits within a window

   >>> model.network.fitwindow(0,0,300,300)

   Override SBML level/version if desired

   >>> model.level = 3
   >>> model.version = 1

   Save the model to an SBML file

   >>> model.save('output.xml')

API Documentation

.. currentmodule:: sbnw

.. autosummary::
   :toctree: generated/

.. rubric:: Functions
.. autosummary::
   :toctree: generated/

   loadsbml
   arrowpoly
   arrowpoly_filled
   narrow_styles
   get_arrow_style
   set_arrow_style

.. rubric:: Classes
.. autosummary::
   :toctree: generated/

   sbmlmodel
   point
   network
   node
   compartment
   reaction
   transform

Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`

