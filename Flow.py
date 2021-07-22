##################################################
## The premise of Flow Free is simple: draw a path
## connecting two dots of the same color without #
## crossing itself or another path. Every 24-hour
## period, a new set of puzzles becomes available
## to you as "Daily Challenges." After a few days
## of this, I started recording some data just for
## fun. I recorded both the number of line      ##
## segments necessary to complete the puzzles and
## the side lengths of the aforementioned puzzles,
## which are all square. The resultant data     ##
## consists of two values, segment count and side
## length, separated by a space, like so: "13 6".
## This program parses the data into two lists, ##
## "lines" and "dim", and does some neat stuff  ##
## with these two lists. Also, I added          ##
## "embroidery" work to the code because I got  ##
## bored messing around in Matplotlib and thought
## the octothorpes looked festive as they're red #
## in my IDE.                                   ##
##################################################
##                    WTFPL                     ##
##################################################
##               [NAME REDACTED]                ##
##################################################
##                                              ##
import math                                     ##
from numpy import log, polyfit as plyft         ##
from matplotlib import style, pyplot as plt, \
image as mpimg                                  ##
##                                              ##
def example(): #example of a Flow game          ##
##                                              ##
    fig2 = plt.gcf()                            ##
    fig2.canvas.set_window_title('Example')     ##
    plt.imshow(mpimg.imread('Flow.png')), \
plt.figure(), plt.show(block = False)           ##
##                                              ##
def parser(): #parses data from Flow.txt        ##
##                                              ##
    global segments, side_lengths, lines        ##
##                                              ##
    Flow_txt = open('Flow.txt','r').read().split()
    lines = [int(i) for i in [Flow_txt for \
Flow_txt in Flow_txt]]                          ##
    segments, side_lengths = lines[::2], \
lines[1::2]                                     ##
##                                              ##
def counters(): #counts instances of list values #
##                                              ##
    global segments_count, side_lengths_count   ##
##                                              ##
    segments_count, side_lengths_count = \
[[i, segments.count(i)] for i in set(segments)], \
[[i, side_lengths.count(i)] for i in \
set(side_lengths)]                              ##
##                                              ##
example(), parser(), counters()                 ##
##                                              ##
segments.sort(), side_lengths.sort()            ##
##                                              ##
def best_log_fit(): #logarithmic equation fit   ##
##                                              ##
    global fit                                  ##
##                                              ##
    fit = plyft(log(side_lengths), segments, 1) ##
##                                              ##
best_log_fit()                                  ##
##                                              ##
style.use('ggplot')                             ##
##                                              ##
segment_sum, side_lengths_sum = sum(segments), \
sum(side_lengths)                               ##
##                                              ##
Euler_difference = abs(math.e - segment_sum / \
side_lengths_sum)                               ##
Euler_difference_percentage = Euler_difference / \
math.e * 100                                    ##
##                                              ##
def Flow_plot(): #plots data and log fit        ##
##                                              ##
    fig1 = plt.gcf()                            ##
    fig1.canvas.set_window_title('Plot')        ##
    plt.scatter(side_lengths, segments, color = \
'#003F72')                                      ##
    plt.plot(side_lengths, fit[0] * \
log(side_lengths) + fit[1])                     ##
    plt.show(block = False)                     ##
##                                              ##
Flow_plot()                                     ##
##                                              ##
print(f"Number of games played: \
{int(len(lines) / 2)}\n\nDifference between \
Euler's number and average\nnumber of lines per \
side length: {round(Euler_difference, 15)}\n\n\
That's about a \
{round(Euler_difference_percentage, 2)}% error.")
##                                              ##
##################################################
## I was going to add a program that would      ##
## simulate games of Flow Free and record similar
## data automatically, but I did some research, ##
## and found only implementations that use AI,  ##
## which is way out of the scope of this project #
## and my capabilities. Also, Matplotlib is really
## confusing. Is it just me or is it really     ##
## convoluted? Overall, I want to add some more ##
## functionality to it, like auto-updating from ##
## the Google Keep document, but I'm kind of over
## it . Maybe I'll add some more to it next year.
## Anyway, have a happy holiday season!         ##
##                      v                       ##
##                     >X<                      ##
##                      A                       ##
##                     d$b                      ##
##                   .d\$$b.                    ##
##                 .d$i$$\$$b.                  ##
##                    d$$@b                     ##
##                   d\$$$ib                    ##
##                 .d$$$\$$$b                   ##
##               .d$$@$$$$\$$ib.                ##
##                   d$$i$$b                    ##
##                  d\$$$$@$b                   ##
##               .d$@$$\$$$$$@b.                ##
##             .d$$$$i$$$\$$$$$$b.              ##
##                     ###                      ##
##                     ###                      ##
##                     ###                      ##
##################################################
