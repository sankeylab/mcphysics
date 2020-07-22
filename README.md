# McPhysics
This is a library of tools spefically aimed at the McGill undergraduate physics labs, namely PHYS 439/469 at the moment. It can be thought of as an augmentation of the [Spinmob](https://github.com/Spinmob/spinmob/wiki) library, which provides general-purpose, broadly applicable data handling, plotting, fitting, graphical interface, and other analysis tools. 

If you have installed McPhysics as described below, you do not need to also install Spinmob. You should, however, read the [Spinmob](https://github.com/Spinmob/spinmob/wiki), which provides a lot of information about automated fitting and data handling.

## Recommended installation method

1. Download and install [Anaconda Python 3](https://www.anaconda.com/distribution/) or [Miniconda Python 3](https://docs.conda.io/en/latest/miniconda.html). See additional instructions below for OSX.

2. From the Anaconda Prompt (or system terminal, depending on your installation options), install the requisite packages available in the conda repository:
   ```
   conda install numpy scipy imageio matplotlib pyqtgraph spyder pyopengl
   ```

3. Install spinmob and mcphysics via pip:
   ```
   pip install spinmob mcphysics pyvisa
   ```

4. Open Spyder and start playing. Example script:
   ```
   import mcphysics
   mcphysics.playground.fitting_statistics_demo()
   ```

## OSX Notes
You may need to tell your system where the `Anaconda3/bin` folder is located manually. A method that worked is to create a text file named `.bash_profile` in your home directory, and add the line `export PATH="/path/to/Anaconda3/bin:$PATH"`, replacing `/path/to` with the appropriate path. Log out and back in, and the terminal should now "know about" `conda` and `pip`.

## Upgrading
To upgrade to the latest stable versions,
   ```
   pip install mcphysics spinmob --upgrade --no-cache-dir
   ```

## Accessing VISA instruments
To access instruments (see below) you will also need a VISA driver, such as Rhode & Schwartz VISA or National Instruments VISA. I recommend [Rhode & Schwarz](https://www.rohde-schwarz.com/ca/driver-pages/remote-control/3-visa-and-tools_231388.html).

## Accessing an ADALM2000
To access the ADALM2000, you will need to install [libiio](https://github.com/analogdevicesinc/libiio) and [libm2k (with python bindings!)](https://github.com/analogdevicesinc/libm2k). On Windows, this is a matter of running two installers. On Linux (and probably osx), we are required to manually compile the libm2k library, so a specific version of these may be required, if this is the case, the McPhysics library will complain and tell you which version is required when you try to access the device.

## Organization
The McPhysics library is organized heirarchically, and you should use Spyder's code completion suggestions to navigate it. You can also type `<ctrl>-i` while your cursor is beside an object to access its documentation. Below is a list of the existing functionality. For more information, please visit our (growing) [wiki](https://github.com/Spinmob/mcphysics/wiki).

### mcphysics.data
 * __load_chn():__ Loads a Maestro .Chn file, returning a [spinmob databox](https://github.com/Spinmob/spinmob/wiki/2.-Data-Handling).
 * __load_chns():__ Load multiple .Chn files, returning a list of [spinmob databoxes](https://github.com/Spinmob/spinmob/wiki/2.-Data-Handling).
 * __plot_chn_files():__ Quick function for analyzing / plotting multiple .Chn files on the same axes.
 * __load_image():__ Loads an image file (jpg, png, etc...), returning 3d numpy array (1 dimension for x, 1 dimension for y, and 1 for the color channel).
 * __load_images():__ Loads multiple images, returning a list of such arrays.
 
 ### mcphysics.functions
  * __em_gaussian():__ Exponentially modified Gaussian probability density function.
  * __erfcx():__ A scaled complementary error function.
  * __reduced_chi2():__ Reduced chi^2 probability density function.
  * __voigt():__ Voigt probability density function.
 
 ### mcphysics.instruments
  * __[adalm2000()](https://github.com/Spinmob/mcphysics/wiki/instruments.adalm2000()):__ Graphical interface for the ADALM2000.
  * __adalm2000_api():__ Lower level, non-graphical interface for the ADALM2000.
  * __[sillyscope()](https://github.com/Spinmob/mcphysics/wiki/instruments.sillyscope()):__ Semi-unified graphical interface for interacting with an assortment of Rigol and Tektronix sillyscopes.
  * __sillyscope_api():__ Lower level, non-graphical interface for the same sillyscopes.
  * __keithley_dmm():__ Graphical interface for our the Keithley digital multimeters (currently 199).
  * __keithley_dmm_api():__ Lower level, non-graphical interface for the DMM.
  
 ### mcphysics.playground
  * __fitting_statistics_demo():__ Graphical fake data generator and fitter. Useful for visualizing fit statistics.
  * __plot_and_integrate_reduced_chi2():__ Plots the reduced chi^2 distribution for the specified degrees of freedom, then numerically integrates it. This is useful if you want to know how reasonable a given value of chi^2 is.
