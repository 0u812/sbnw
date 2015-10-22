/*== SAGITTARIUS =====================================================================
 * Copyright (c) 2012, Jesse K Medley
 * All rights reserved.

 * Redistribution and use in source and binary forms, with or without
 * modification, are permitted provided that the following conditions are met:
    * Redistributions of source code must retain the above copyright
      notice, this list of conditions and the following disclaimer.
    * Redistributions in binary form must reproduce the above copyright
      notice, this list of conditions and the following disclaimer in the
      documentation and/or other materials provided with the distribution.
    * Neither the name of The University of Washington nor the
      names of its contributors may be used to endorse or promote products
      derived from this software without specific prior written permission.

 * THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND
 * ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
 * WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
 * DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDERS OR ANYONE DISTRIBUTING THE SOFTWARE
 * BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL 
 * DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
 * LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND
 * ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
 * (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS
 * SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
 */

//== FILEDOC =========================================================================

/** @file autolayout.h
 * @brief SBML layout interface in C
  */

//== BEGINNING OF CODE ===============================================================

#ifndef __SBNW_AUTOLAYOUT_H_
#define __SBNW_AUTOLAYOUT_H_

//== INCLUDES ========================================================================

#include "graphfab/core/SagittariusCore.h"
#include "graphfab/sbml/autolayoutSBML.h"
#include "graphfab/sbml/layout.h"
#include "graphfab/layout/fr.h"

#endif


///*! \mainpage libSBNW
// *
// * \section intro_sec Introduction
// *
// * libSBNW is a SBML compliant layout generation program.
// *
//
// Example:
//
// \code
//
//       #include "autolayoutc_api.h"
//
//       //...
//
//       // type to store layout info
//       gf_layoutInfo* l;
//
//
//       // load the model
//       gf_SBMLModel* mod = gf_loadSBMLbuf(buf);
// 
//
//       // options for layout algo
//       fr_options opt;
//
//
//       // read layout info from the model
//       l = gf_processLayout(mod);
//
//
//       // randomize node positions
//       gf_randomizeLayout(l);
//
//       // do layout algo
//       opt.k = 20.;
//       opt.boundary = 1;
//       opt.mag = 0;
//       opt.grav = 0.;
//       opt.baryx = opt.baryy = 500.;
//       opt.autobary = 1;
//       gf_doLayoutAlgorithm(opt, l);
//
//       // save layout information to new SBML file
//       gf_writeSBMLwithLayout(outfile, mod, l);
//
//
//       // run destructors on the model
//       gf_freeSBMLModel(mod);
//
//
//       // run destructors on the layout
//       gf_freeLayoutInfo(l);
//
// \endcode
//
// * \section install_sec Installation
// *
// * Installation documentation is provided at https://github.com/0u812/sbnw.


// \defgroup C_API All external C Methods

// \defgroup C_Internal Internal C Methods

//
//*/
//
