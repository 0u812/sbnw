# SBNW: A Network Viewer for SBML

## Introduction
SBNW is a network viewer which supports autolayout of models. Uses libSBML for reading/writing models.

## Download

The latest release can be downloaded at https://github.com/0u812/sbnw/releases.

## Test Cases

The SBML [test models](https://github.com/0u812/sbnw/releases/download/1.2.4/testcases.zip) used to develop this tool are available for download from the releases page as well.

## Online Documentation

Online C API documentation (via Doxygen) can be found at http://0u812.github.io/sbnw/docs. Python documentation can be found at http://0u812.github.io/sbnw/sphinx.


## How to compile the library

 * Install the latest version of <a href="http://sourceforge.net/projects/sbml/files/libsbml/">libSBML</a> or build it from source (tested with 5.6, 5.8, 5.10, 5.11).
 * **NOTE**: If you install a pre-built binary of libSBML then you must compile SBNW with the same version of Visual Studio as used to build libSBML (2010 at the time of writing).
 * Clone the latest revision of the <a href="https://github.com/0u812/sbnw">master branch</a> to Documents\sbnw via git. In the Documents folder, run `git clone https://github.com/0u812/sbnw.git`
 * Download and instsall <a href="http://www.cmake.org/">CMake</a> (compatible with major version 2 or 3).
 * Open CMake and select Documents\sbnw as the source directory.
 * Select Documents\sbnw-build (or choose a directory at will) as the build directory.
 * Click configure & generate via CMake, choosing a generator that matches the required configuration (32-bit x86 is recommended on Windows; on Linux the default generator is sufficient).
 * Using CMake, set the `LIBSBML_DIR` variable to point to the directory where libSBML is installed/downloaded. Click configure & generate again.
 * **NOTE**: In order to statically link to libSBML, specify `SBNW_LINK_TO_STATIC_LIBSBML=ON`. Otherwise, the libSBML DLLs must be in the PATH to run any compiled code.
 * On Windows, open the generated .sln in Visual Studio, and change the configuration to "Release"; on Linux/Mac simply run make -j4 install from the build directory.
 * *(This step was previously used to instruct the user to set the MSVC runtime library. It is now set automatically through CMake. This placeholder serves as a reminder in case this solution breaks at some point.)*
 * **Windows Specific:** In Visual Studio, right click on the INSTALL target and select build. SBNW will be installed to the location stored in CMAKE_INSTALL_PREFIX (ensure your user has write access).

## Using the Tellurium Plugin

The network viewer is available as a plugin in Tellurium. Simply switch to the network viewer tab, open a model from the [test cases](https://github.com/0u812/sbnw/releases/download/1.2.4/testcases.zip) (e.g. BorisEJB.xml), and enter the following code:

```
# The nwed module is used to communicate with the plugin
import nwed
# Get the current model
sbmlstr = nwed.getsbml()
# Print the SBML
print(sbmlstr)
# Load the SBML back into the network viewer
nwed.setsbml(sbmlstr)
```

![Usage example](http://0u812.github.io/sbnw/hosted/img/usage_ex.png)

## Using the Library (C API)

The C API is exposed via graphfab/autolayoutc_api.h.  There is an example in sandbox/basic that demonstrates all the functionality needed to get the layout working:

```
        // type to store layout info
        gf_layoutInfo* l;

        // load the model
        gf_SBMLModel* mod = gf_loadSBMLbuf(buf);

        // options for layout algo
        fr_options opt;

        // read layout info from the model
        l = gf_processLayout(mod);

        // randomize node positions
        gf_randomizeLayout(l);

        // do layout algo
        opt.k = 20.;
        opt.boundary = 1;
        opt.mag = 0;
        opt.grav = 0.;
        opt.baryx = opt.baryy = 500.;
        opt.autobary = 1;
        gf_doLayoutAlgorithm(opt, l);

        // save layout information to new SBML file
        gf_writeSBMLwithLayout(outfile, mod, l);

        // run destructors on the model
        gf_freeSBMLModel(mod);

        // run destructors on the layout
        gf_freeLayoutInfo(l);
```