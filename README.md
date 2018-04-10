# bokeh_intro

This repo provides a script and two Jupyter Notebooks which provide a simple intro to using [bokeh][bokeh-home]. Portions were presented originally at the 2017 Oct 28 Data Science with Python [meetup event][meetup-event].

## Contents:
* **compare_matplotlib.py** -- sample script comparing the basic plotting syntax of matplotlib vs bokeh
* **Compare_Matplotlib.ipynb** -- (same as previous, except in a Jupyter Notebook)
* **Sum_of_Squared_Errors.ipynb** -- Jupyter Notebook illustrating bokeh + ipywidgets

## Requirements:

* Python 3
* conda

Easiest to install both via [Anaconda][anaconda-download].

## Usage

The notebooks in this repo can be run in the same virtual environment used in the [bokeh_wrap][bokeh_wrap] repo. Follow the instructions there for creating the environment and using it as a kernel in Jupyter Notebook.

Even if you do not create the specific virtual enviroment from that repo, most likely the widgets in notebook **Sum_of_Squared_Errors.ipynb** will work just fine in your global Python 3 environment, if you are using a recently updated Anaconda installation.

You can run the script with:

    (bokeh_wrap) $ python3 compare_matplotlib.py

I find that some quirk with the graphics backend requires that I minimize or move my terminal window to actually see the plot window.

Alternately or instead of that script, start a Jupyter Notebook server:

    (bokeh_wrap) $ jupyter notebook

and run notebook **Compare_Matplotlib.ipynb**.

The other notebook **Sum_of_Squared_Errors.ipynb** provides an example of combining bokeh with ipywidgets to make a plot which illustrates the concept of adjusting a function's parameters to fit data points. (It is not intended as providing an actual recommended method for fitting points; its purpose is to show how ipywidgets can be used in a bokeh plot).


[anaconda-download]: https://www.anaconda.com/download/
[bokeh-home]: https://bokeh.pydata.org/en/latest/
[bokeh_wrap]: https://github.com/dpshenoy/bokeh_wrap
[meetup-event]: https://www.meetup.com/League-of-Extraordinary-Algorithms/events/244101320/