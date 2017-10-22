## For 2017 Oct 28 Data Science with Python [meetup event](https://www.meetup.com/League-of-Extraordinary-Algorithms/events/244101320/)

### Contents:
* **Compare_Matplotlib.ipynb** -- Jupyter Notebook comparing the basic plotting syntax of matplotlib vs bokeh
* **Sum_of_Squared_Errors.ipynb** -- Jupyter Notebook illustrating bokeh + ipywidgets
* **countries-compare/** -- a sample bokeh server app

These examples assume you are running Python 3.5 or 3.6, and have installed the standard data analysis packages numpy and pandas. 
These examples were created using bokeh version 0.12.10, although version 0.12.9 should work too.
PyData [recommends installing bokeh via Anaconda](https://bokeh.pydata.org/en/latest/docs/installation.html#package-installs). 
At the time of this writing the latest version of bokeh available via Anaconda ([with the conda-forge channel added 
to your conda config](https://conda-forge.org/#about)) is version 0.12.9:

    $ conda search bokeh | grep -E "0.12.9|0.12.10"
                                0.12.9                   py27_0  conda-forge
                             *  0.12.9                   py35_0  conda-forge
                                0.12.9                   py36_0  conda-forge

If you want the latest version 0.12.10, [use pip](https://bokeh.pydata.org/en/latest/docs/installation.html#package-installs):

    $ pip search bokeh | grep 0.12.10
    bokeh (0.12.10)              - Interactive plots and applications in the browser from Python

    $ pip install bokeh     # will automatically install the latest available version

For running **Sum_of_Squared_Errors.ipynb** you will also need to have installed: 

    $ pip list | grep -E "ipyw|widg"
    ipywidgets                         6.0.0
    widgetsnbextension                 2.0.0

To run the **countries-compare** app:

    $ bokeh serve countries-compare

Then browse to localhost:5006 to use the app. To stop the bokeh server use Ctrl-C (Cmd-C on Mac).