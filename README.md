<div align='right'></div># PHYS227 CW 8

**Author(s):** Michael Seaman, Taylor Patti, Austin Ayers, Chinmai Raman, Andrew Malfavon

[![Build Status](https://travis-ci.org/chapman-phys227-2016s/cw-8-YOURTEAM.svg?branch=master)](https://travis-ci.org/chapman-phys227-2016s/cw-8-YOURTEAM)

**Due date:** 2016/04/12

## Specification

Complete the following exercises from the primary textbook, placing your solutions into separate files. In each file, write the solution as a callable function, so that you can write suitable test functions that demonstrate correct output using the nose framework. GitHub will automatically run your tests on every commit, indicating any failures via the Travis framework with build status above.

1. p.508, 8.15. Work this short problem together to make sure you all understand how it works.
1. If you have not, read Section 8.6 and 8.7 of the textbook for background information. Focus in particular on the implementations on p.495 of ```walk2D.py``` and its vectorized version on p.497 of ```walk2Dv.py```. Note that the output is a sequence of .pdf files that you can later collect into animated gifs using the bash command ```convert -delay 50 -loop 0 tmp_*.pdf walk.gif``` in the Terminal, which uses the ImageMagick file conversion suite in linux. The delay parameter specifies frame delay in milliseconds. The loop parameter of 0 specifies an infinite number of loops for the gif.
1. p.514, 8.33, in ```walk2D_class.py```. Be sure to split the parts sensibly among your group, and be sure to implement your code so it works properly with the Travis testing framework. Create an animated gif for each random walk demonstration, and load them into your example notebook as images in Markdown cells. When checking files into git, do not check in the temporary frames used to create the animated gifs. Only check in the completed gif files.

To cleanly present your work, create a Jupyter notebook ```cw8.ipynb``` that imports each of your python files as modules and demonstrates the functionality. The notebook should be formatted professionally using Markdown headings, including your name and a brief description of each homework section. 

## Assessment

_\<Analyze what you found useful about this assignment in your own words. Include any lingering questions or comments that you may have.\>_

## Honor Pledge

I pledge that all the work in this repository is my own with only the following exceptions:

* Content of starter files supplied by the instructor;
* Code borrowed from another source, documented with correct attribution in the code and summarized here.

Signed,

 Michael Seaman, Taylor Patti, Austin Ayers, Chinmai Raman, Andrew Malfavon
