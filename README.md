# A mathematical function to find the best seat in a movie theater

Based on an argument with my sister, I decided to make a python function to calculate the best place to sit in a movie theater

<hr>

## The Function itself

The function is given by:


	function best-seat(width-of-screen, distance-of-screen-from-seats-first-row-of-seats):
		peripheral-view = 114
		distance-from-screen = cot(peripheral-view) * width-of-screen/2
		best-possible-seat = distance-from-screen - distance-between-screen-and-first-row

		return ceil(best-possible-seat)


<hr>

## Example

An Example of this can be found here:

![example-view](https://github.com/v2thegreat/a-mathematical-function-to-find-the-best-seat-in-a-movie-theater/blob/master/images/theater%20view.png)


###### Here:


* `Screen width` is `14 seats`
*	`distance between screen and first row` is `1 seat` (marked as `x`)
* `best seat` is what we need to find

Throwing this into the best-seat function, we find that the best seat is going to be `5th Row`

Sometimes, it might be a good idea to sit a little closer, which is why the 4th row is marked too

It's also assumed that the middle seats are the best, so I won't return that

<hr>

## Installation

Simply ensure that Python (doesn't matter if 2 or 3) is installed. To check if it is correctly installed, type `python` in the command prompt/terminal

<hr>

## Running the function

In the same directory as the rest of the module, simply type: `python main.py`, and enter the needed information
