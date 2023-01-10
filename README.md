## XRD Simulation of Interfaces in HCP Crystals

Personal project based on my MSc project (2017-2019). Converting hcp3d MATLAB scripts to Python. See github.com/loraran/hcp3d (XRD Simulation of Interfaces in HCP Crystals).

###### Last Update (10 Jan 2023): _Create README file with basic file descriptions._

A research paper was published using results obtained from the original MATLAB scripts. You can find it here:

>[_Retrieving the configuration of grain boundary structure in polycrystalline materials by extraordinary X-ray reflection analysis_](https://doi.org/10.1107/S1600576720007803)
<br>L. Aarão-Rodrigues, A. Isaac, R. B. Figueiredo and A. Malachias - _J. Appl. Cryst._ (2020). **53**, 1006-1014

---

### Simulation Routines

* `main.py` - hcp3d_py main script. Executes all relevant scripts, calling functions in the correct order.
* `lattice.py` - Crystal lattice assembly. Defines lattice parameters and matrix size, sets up a spherical matrix.
* `projections.py` - Generates specified projections of the matrix created by `lattice`: (100), (110).
* Collection of functions that perform progressive rotation and cutting of the projected matrices:
  * **_[TO-DO]_** `progressive_cuts/alpha.py` - Progressive rotation, cutting and assembly of _out-of-plane_ α-type interfaces.
  * **_[TO-DO]_** `progressive_cuts/beta.py` - Progressive rotation, cutting and assembly of _out-of-plane_ β-type interfaces.
  * **_[TO-DO]_** `progressive_cuts/gamma_z.py` - Progressive rotation, cutting and assembly of _out-of-plane_ γ-type interfaces.
  * **_[TO-DO]_** `progressive_cuts/gamma_x.py` - Progressive rotation, cutting and assembly of _in-plane_ γ-type interfaces.
* **_[TO-DO]_** `fft_out_of_plane.py` - Fast-Fourier Transform of assembled out-of-plane lattices α, β and γ. Varies Miller index ℓ with 0.006 steps.
* Collection of functions that perform Fast-Fourier Transform of assembled lattices γ (in-plane):
  * **_[TO-DO]_** `fft_in_plane/fft_h.py` - Varies Miller index h with 0.006 steps.
  * **_[TO-DO]_** `fft_in_plane/fft_k.py` - Varies Miller index k with 0.006 steps.
  * **_[TO-DO]_** `fft_in_plane/fft_hk.py` - Varies Miller indexes h and k with 0.006 steps.
* **_[TO-DO]_** `stacking_fault.py` - Main script to execute the simulation and calculation of FFT in simulated stacking faults (see next item).
* **_[TO-DO]_** `hcp3d_stack` - Collection of functions that create and assemble lattices with different types of stacking faults:
  * **_[TO-DO]_** `_abb.py` - Stacking faults in which the ABAB registry along the c (00L) axis is replaced by ABBA stackings.
  * **_[TO-DO]_** `_abc.py` - Stacking faults in which the ABAB registry along the c (00L) axis is replaced by ABCAB stackings.
  
### **_[TO-DO]_** Extraction of Atom Matrix Figures for POV-Ray™
>The [_Persistence of Vision Raytracer™_](http://www.povray.org/) (_POV-Ray™_) is a tool for producing high-quality computer graphics. POV-Ray is a free and open-source software with source code available under the AGPLv3.

* Collection of scripts to assist the creation on images to better illustrate relevant assembled lattices (all atom positions are preserved). They create _.pov_ files to be visualized in POV-Ray.

### **_[TO-DO]_** Data Retrieval
