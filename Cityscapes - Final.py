
#-----Statement of Authorship----------------------------------------#
#
#  This is an individual assessment item.  By submitting this
#  code I agree that it represents my own work.  I am aware of
#  the University rule that a student must not act in a manner
#  which constitutes academic dishonesty as stated and explained
#  in QUT's Manual of Policies and Procedures, Section C/5.3
#  "Academic Integrity" and Section E/2.1 "Student Code of Conduct".
#
#    Student no: N10269142
#    Student name: Anna Nguyen
#
#  NB: Files submitted without a completed copy of this statement
#  will not be marked.  All files submitted will be subjected to
#  software plagiarism analysis using the MoSS system
#  (http://theory.stanford.edu/~aiken/moss/).
#
#--------------------------------------------------------------------#



#-----Assignment Description-----------------------------------------#
#
#  CITYSCAPES
#
#  This assignment tests your skills at defining functions, processing
#  data stored in lists and efficiently repeating multiple actions in
#  order to display a complex visual image.  The incomplete
#  Python script below is missing a crucial function, "build_city".
#  You are required to complete this function so that when the
#  program is run it draws a city whose plan is determined by
#  randomly-generated data stored in a list which specifies what
#  style of building to erect on particular sites.  See the
#  instruction sheet accompanying this file for full details.
#
#  Note that this assignment is in two parts, the second of which
#  will be released only just before the final deadline.  This
#  template file will be used for both parts and you will submit
#  your final solution as a single Python 3 file, whether or not you
#  complete both parts of the assignment.
#
#--------------------------------------------------------------------#  



#-----Preamble-------------------------------------------------------#
#
# This section imports necessary functions and defines constant
# values used for creating the drawing canvas.  You should not change
# any of the code in this section.
#

# Import the functions needed to complete this assignment.  You
# should not need to use any other modules for your solution.  In
# particular, your solution must not rely on any non-standard Python
# modules that need to be installed separately, because the markers
# may not have access to such modules.

from turtle import *
from math import *

# Define constant values used in the main program that sets up
# the drawing canvas.  Do not change any of these values.

canvas_height = 700 # pixels
canvas_width = 1100 # pixels
grass_depth = 95 # vertical depth of the "grass", in pixels
half_width = canvas_width // 2 # maximum x coordinate in either direction
grid_font = ('Arial', 10, 'normal') # font for drawing the grid
grid_size = 50 # gradations for the x and y scales shown on the screen
offset = 5 # offset of the x-y coordinates from the screen's edge, in pixels
max_height = canvas_height - grass_depth # maximum positive y coordinate
max_building_height = 575 # city ordinance maximum building height
site_width = 240 # maximum width of a building site

# Define the locations of building sites approved by the
# city council (arranged from back to front)
sites = [['Site 1', [-225, 0]],
         ['Site 2', [25, 0]],
         ['Site 3', [275, 0]],
         ['Site 4', [-375, -25]],
         ['Site 5', [-125, -25]],
         ['Site 6', [125, -25]],
         ['Site 7', [375, -25]],
         ['Site 8', [-275, -50]],
         ['Site 9', [-25, -50]],
         ['Site 10', [225, -50]]]

#
#--------------------------------------------------------------------#



#-----Functions for Creating the Drawing Canvas----------------------#
#
# The functions in this section are called by the main program to
# manage the drawing canvas for your image.  You should not change
# any of the code in this section.
#

# Set up the canvas and draw the background for the overall image.
# By default the drawing grid is displayed - call the function
# with False as the argument to prevent this.
def create_drawing_canvas(show_grid = True):

    # Set up the drawing canvas with coordinate (0, 0) in the
    # "grass" area
    setup(canvas_width, canvas_height)
    setworldcoordinates(-half_width, -grass_depth, half_width, max_height)

    # Draw as fast as possible
    tracer(False)

    # Make the sky blue
    bgcolor('sky blue')

    # Draw the "grass" as a big green rectangle (overlapping the
    # edge of the drawing canvas slightly)
    overlap = 25 # pixels
    penup()
    goto(-(half_width + overlap), -(grass_depth + overlap)) # bottom-left
    fillcolor('pale green')
    begin_fill()
    setheading(90) # face north
    forward(grass_depth + overlap * 2)
    right(90) # face east
    forward(canvas_width + overlap * 2)
    right(90) # face south
    forward(grass_depth + overlap * 2)
    end_fill()

    # Draw a nice warm sun peeking into the image at the top left
    penup()
    goto(-canvas_width // 2, canvas_height - grass_depth)
    pencolor('yellow')
    dot(350)

    # Draw a big fluffy white cloud in the sky
    goto(canvas_width // 3, canvas_height - grass_depth - 100)
    pencolor('white')
    dot(200)
    setheading(200)
    forward(100)
    dot(180)
    setheading(0)
    forward(200)
    dot(160)

    # Optionally draw x coordinates along the bottom of the
    # screen (to aid debugging and marking)
    pencolor('black')
    if show_grid:
        for x_coord in range(-half_width + grid_size, half_width, grid_size):
            goto(x_coord, -grass_depth + offset)
            write('| ' + str(x_coord), font = grid_font)

    # Optionally draw y coordinates on the left-hand edge of
    # the screen (to aid debugging and marking)
    if show_grid:
        for y_coord in range(-grid_size, max_height, grid_size):
            goto(-half_width + offset, y_coord - offset)
            write(y_coord, font = grid_font)
        goto(-half_width + offset, max_building_height - 5)
        write('Maximum allowed building height', font = grid_font)

    # Optionally mark each of the building sites approved by
    # the city council
    if show_grid:
        for site_name, location in sites:
            goto(location)
            dot(5)
            goto(location[0] - (site_width // 2), location[1])
            setheading(0)
            pendown()
            forward(site_width)
            penup()
            goto(location[0] - 40, location[1] - 17)
            write(site_name + ': ' + str(location), font = grid_font)
     
    # Reset everything ready for the student's solution
    pencolor('black')
    width(1)
    penup()
    home()
    tracer(True)


# End the program and release the drawing canvas.
# By default the cursor (turtle) is hidden when the program
# ends - call the function with False as the argument to
# prevent this.
def release_drawing_canvas(hide_cursor = True):
    tracer(True) # ensure any drawing in progress is displayed
    if hide_cursor:
        hideturtle()
    done()
    
#
#--------------------------------------------------------------------#



#-----Test Data for Use During Code Development----------------------#
#
# The "fixed" data sets in this section are provided to help you
# develop and test your code.  You can use them as the argument to
# the build_city function while perfecting your solution.  However,
# they will NOT be used to assess your program.  Your solution will
# be assessed using the random_plan function appearing below.  Your
# program must work correctly for any data set generated by the
# random_plan function.
#
# Each of the data sets below is a list specifying a set of
# buildings to be erected.  Each specification consists of the
# following parts:
#
# a) The site on which to erect the building, from Site 1 to 10.
# b) The style of building to be erected, from style 'A' to 'D'.
# c) The number of floors to be constructed, from 1 to 10.
# d) An extra value, either 'X' or 'O', whose purpose will be
#    revealed only in Part B of the assignment.  You should
#    ignore it while completing Part A.
#

# Each of these data sets draws just one building in each of the
# four styles
fixed_plan_1 = [[1, 'A', 6, 'O']]
fixed_plan_2 = [[2, 'B', 7, 'O']]
fixed_plan_3 = [[3, 'C', 5, 'O']]
fixed_plan_4 = [[4, 'D', 4, 'O']]
fixed_plan_5 = [[1, 'A', 9, 'X']]
fixed_plan_6 = [[2, 'B', 2, 'X']]
fixed_plan_7 = [[3, 'C', 3, 'X']]
fixed_plan_8 = [[4, 'D', 6, 'X']]

# Each of the following data sets draws just one style of
# building but at three different sizes, including the maximum
# (so that you can check your building's maximum height against
# the height limit imposed by the city council)
fixed_plan_9 = [[1, 'A', 10, 'O'], [2, 'A', 5, 'O'], [3, 'A', 1, 'O']]
fixed_plan_10 = [[1, 'B', 10, 'O'], [2, 'B', 5, 'O'], [3, 'B', 1, 'O']]
fixed_plan_11 = [[1, 'C', 10, 'O'], [2, 'C', 5, 'O'], [3, 'C', 1, 'O']]
fixed_plan_12 = [[1, 'D', 10, 'O'], [2, 'D', 5, 'O'], [3, 'D', 1, 'O']]
fixed_plan_13 = [[1, 'A', 10, 'X'], [2, 'A', 5, 'X'], [3, 'A', 1, 'X']]
fixed_plan_14 = [[1, 'B', 10, 'X'], [2, 'B', 5, 'X'], [3, 'B', 1, 'X']]
fixed_plan_15 = [[1, 'C', 10, 'X'], [2, 'C', 5, 'X'], [3, 'C', 1, 'X']]
fixed_plan_16 = [[1, 'D', 10, 'X'], [2, 'D', 5, 'X'], [3, 'D', 1, 'X']]

# Each of the following data sets draws a complete cityscape
# involving each style of building at least once. There is
# no pattern to them, they are simply specific examples of the
# kind of data returned by the random_plan function which will be
# used to assess your solution. Your program must work for any value
# that can be returned by the random_plan function, not just these
# fixed data sets.
fixed_plan_17 = \
         [[1, 'D', 2, 'O'],
          [2, 'B', 7, 'O'],
          [5, 'C', 6, 'O'],
          [6, 'A', 4, 'O']]
fixed_plan_18 = \
         [[1, 'D', 6, 'O'],
          [3, 'C', 5, 'O'],
          [4, 'B', 3, 'O'],
          [9, 'A', 9, 'O'],
          [10, 'D', 2, 'O']]
fixed_plan_19 = \
         [[5, 'C', 6, 'O'],
          [6, 'B', 9, 'O'],
          [7, 'A', 5, 'O'],
          [8, 'A', 7, 'O'],
          [9, 'D', 4, 'O']]
fixed_plan_20 = \
         [[1, 'A', 4, 'O'],
          [2, 'B', 4, 'O'],
          [3, 'A', 5, 'O'],
          [4, 'D', 7, 'O'],
          [10, 'B', 10, 'O']]
fixed_plan_21 = \
         [[1, 'B', 6, 'O'],
          [3, 'A', 4, 'O'],
          [4, 'C', 4, 'O'],
          [6, 'A', 8, 'O'],
          [8, 'C', 7, 'O'],
          [9, 'B', 5, 'O'],
          [10, 'D', 3, 'O']]
fixed_plan_22 = \
         [[1, 'A', 10, 'O'],
          [2, 'A', 9, 'O'],
          [3, 'C', 10, 'O'],
          [4, 'B', 5, 'O'],
          [5, 'B', 7, 'O'],
          [6, 'B', 9, 'O'],
          [7, 'C', 2, 'O'],
          [8, 'C', 4, 'O'],
          [9, 'A', 6, 'O'],
          [10, 'D', 7, 'O']]
fixed_plan_23 = \
         [[3, 'A', 8, 'O'],
          [4, 'C', 8, 'O'],
          [5, 'B', 4, 'O'],
          [6, 'D', 5, 'O'],
          [7, 'C', 5, 'X'],
          [8, 'A', 3, 'X'],
          [9, 'D', 2, 'X']]
fixed_plan_24 = \
         [[2, 'C', 3, 'O'],
          [3, 'B', 1, 'O'],
          [4, 'C', 3, 'X'],
          [5, 'C', 1, 'O'],
          [6, 'D', 2, 'O'],
          [7, 'B', 1, 'O'],
          [8, 'D', 2, 'O'],
          [9, 'C', 7, 'O'],
          [10, 'A', 1, 'X']]
fixed_plan_25 = \
         [[1, 'B', 7, 'X'],
          [3, 'C', 1, 'O'],
          [6, 'D', 3, 'O'],
          [7, 'A', 7, 'O'],
          [8, 'D', 3, 'X'],
          [9, 'C', 7, 'O'],
          [10, 'C', 9, 'X']]
fixed_plan_26 = \
         [[1, 'A', 6, 'O'],
          [2, 'A', 2, 'O'],
          [3, 'A', 9, 'X'],
          [4, 'D', 1, 'X'],
          [5, 'C', 7, 'O'],
          [6, 'D', 6, 'O'],
          [7, 'B', 5, 'O'],
          [8, 'A', 1, 'O'],
          [9, 'D', 10, 'X'],
          [10, 'A', 6, 'O']]
 
#
#--------------------------------------------------------------------#



#-----Function for Assessing Your Solution---------------------------#
#
# The function in this section will be used to mark your solution.
# Do not change any of the code in this section.
#
# The following function creates a random data set specifying a city
# to be built.  Your program must work for any data set returned by
# this function.  The results returned by calling this function will
# be used as the argument to your build_city function during marking.
# For convenience during code development and marking this function
# also prints the plan for the city to be built to the shell window.
#

def random_plan(print_plan = True):
    building_probability = 70 # percent
    option_probability = 20 # percent
    from random import randint, choice
    # Create a random list of building instructions
    city_plan = []
    for site in range(1, len(sites) + 1): # consider each building site
        if randint(1, 100) <= building_probability: # decide whether to build here
            style = choice(['A', 'B', 'C', 'D']) # choose building style
            num_floors = randint(1, 10) # choose number of floors
            if randint(1, 100) <= option_probability: # decide on option's value
                option = 'X'
            else:
                option = 'O'
            city_plan.append([site, style, num_floors, option])
    # Optionally print the result to the shell window
    if print_plan:
        print('\nBuildings to be constructed\n' +
              '(site, style, no. floors, option):\n\n',
              str(city_plan).replace('],', '],\n '))
    # Return the result to the student's build_city function
    return city_plan

#
#--------------------------------------------------------------------#



#-----Student's Solution---------------------------------------------#
#  Complete the assignment by replacing the dummy function below with
#  your own "build_city" function.
# num_floors; style [building style]

#develop function for each building style
#function for drawing windows

def windows(win_side, win_top, spacing, window_colour, frame_colour):
##prepare to draw window filling
    setheading(90) 
    color(window_colour)
    pencolor(frame_colour)
    pendown()
    begin_fill()
    #draw window 
    for window_color in range(2):
        forward(win_side)
        right(90)
        forward(win_top)
        right(90)
    end_fill()
    penup()
    #prepare to draw next window
    setheading(0)
    forward(spacing + win_top)

def floor(floor_length, floor_height, floor_colour, outline_colour):
    #prepare to draw floor from the middle
    setheading(180)
    color(floor_colour)
    pencolor(outline_colour)
    pensize(1.5)
    pendown() 
    begin_fill() 
    #draw floor
    forward(floor_length/2) 
    right(90)
    for floor in range(2):
        forward(floor_height) 
        right(90)
        forward(floor_length)
        right(90)
    end_fill()
    penup()
    #move back to starting position
    setheading(0) 
    forward(floor_length/2)

def fencing(colour, frame_height, frame_top, floorlength):
##positino to draw first piece of fencing
    forward(frame_top)
    #prepare to draw fence
    color(colour)
    pendown()
    setheading(90)
   #draw first piece of the fence
    for first_piece in range(2):
       forward(frame_height)
       right(90)
       forward(frame_top)
       right(90)
   #position to draw main fencing
    setheading(0)
    forward(frame_top)
    #draw main fencing
    for frame in range(floorlength//frame_top):
      setheading(90) 
      forward(frame_height) 
      right(90)
      forward(frame_top) 
      right(90)
      forward(frame_height) 
    setheading(90)
    #draw last piece of the fence
    for last_piece in range(2):
        forward(frame_height)
        right(90)
        forward(frame_top)
        right(90)
    penup()

def sign(sign_side, sign_top, sign_colour, outline_colour):
    #prepare to draw sign
    color(sign_colour)
    pencolor(outline_colour)
    pendown()
    pensize(1.5)
    begin_fill()
    #draw sign
    setheading(180)
    forward(sign_top/2)
    for sign in range(2):
        right(90)
        forward(sign_side)
        right(90)
        forward(sign_top)
    backward(sign_top)
    end_fill()
    penup()
    
def cross(cross_side = 10):
    #position to draw cross
    forward(25)
    setheading(90)
    forward(cross_side)
    #prepare to draw cross
    color("red")
    pendown()
    begin_fill()
    #draw cross
    setheading(180)
    forward(cross_side/2)
    for cross in range(4):
        right(90)
        forward(cross_side)
        left(90)
        forward(cross_side)
        right(90)
        forward(cross_side)
    end_fill()
    penup()

def floor_roof(floor_length, fill_colour, outline_colour):
   #prepare to draw
   pendown()
   setheading(180)
   pencolor(outline_colour)
   fillcolor(fill_colour)
   begin_fill()
   #draw top and side of floor roof
   forward((floor_length + 20)/2)
   left(135)
   forward(15)
   left(45)
   #draw bottom and side of floor roof
   pencolor(fill_colour)
   forward(floor_length)
   left(45)
   pencolor(outline_colour)
   forward(15)
   left(135)
   forward((floor_length + 20)/2)
   end_fill()
   penup()

def arch(bottom_length, side_length, fill_colour, outline_colour):
#prepare to draw arch
   pendown()
   setheading(0)
   pencolor(outline_colour)
   fillcolor(fill_colour)
   begin_fill()
   #draw arch
   forward(bottom_length)
   left(90)
   forward(side_length)
   circle(bottom_length, extent = 180)
   forward(side_length)
   left(90)
   forward(bottom_length)
   end_fill()
   penup()
    
def ConstructionSign(sign_side = 70, sign_length = 200, draw = False):
    if draw == True:
        #position to draw
        setheading(90)
        pendown()
        forward(15)
        #draw sign
        sign(70, 200, "Yellow", "Black")
        #position for sign writing
        forward(sign_length - 22) 
        setheading(90)
        forward(70/10)
        #write 'Under Construction' on sign
        pencolor('black')
        write('Under Construction', font =("Arial", 13, "bold"))
        penup()
        #position to draw top section of sign
        setheading(90)
        forward(25)
        setheading(0)
        forward(80 - 3)
        sign(25, 180, "Black", "Black")
        #position for sign writing
        forward(130)
        #write 'Caution' on sign
        pencolor("Yellow")
        write('CAUTION', font=("Arial", 15, "bold"))
        penup()
    
def Hospital(num_floors, floor_length = 240,
              floor_height = 50, sign_side = 50):
##draw ground floor
    floor(floor_length, floor_height, "light grey", "dark grey")
    #position to draw door for ground floor
    backward(10)
    #draw [25 x 20 pixel] door using windows function
    windows(25, 20, 0, "brown", "black")
    #move back to center
    penup()
    backward(10)
    setheading(90)
    forward(floor_height)
##draw additional floors given by instructions in random plan
    for floors in range(num_floors):
        floor(floor_length, floor_height, "LightGrey", "DarkGrey")
        #position to draw windows
        setheading(180)
        forward((floor_length/2) - 10) 
        setheading(90)
        forward(floor_height/5)
        #draw row of [30 x 20 pixel] windows
        for window in range(11):
            windows(30, 20, 0, "LightBlue", "Cornflower Blue")
        #reposition to draw next floor
        penup()
        forward((floor_length/2) - ((floor_length/2) - 10))
        setheading(90)
        forward(floor_height - (floor_height/5))
        setheading(180)
        forward(floor_length/2)
        
def ClockTower(num_floors, floor_length = 105, floor_height = 50,
              large_engrave = 30):
##draw floors given by instructions in random plan
    for floors in range(num_floors):
        floor(floor_length, floor_height,
              "BlanchedAlmond", "BurlyWood")
    ##position to start small engravings
        setheading(180)
        small_engrave = large_engrave / 6 
        forward((floor_length/2) - small_engrave)
        setheading(90)
        forward(small_engrave)
        #prepare to draw small engravings
        pensize(0.5)
        #draw small engravings [5 x 5 pixels] using windows function
        for small_engravings in range(10):
            windows(small_engrave, small_engrave,
                    5, "Tan", "DarkGoldenrod")
    ##reposition to draw larger engravings
        penup()
        setheading(90)
        forward(small_engrave * 2)
        setheading(180)
        forward(floor_length - (small_engrave))
        #draw large engravings [30 x 5 pixels] using windows function 
        for large_engravings in range(10):
            windows(large_engrave, small_engrave, 5,
                    "Tan", "DarkGoldenrod")
        #reposition to draw next floor
        penup()
        setheading(90)
        forward(large_engrave + small_engrave)
        setheading(180)
        forward(floor_length/2)
#roof piece for Building B 
def ClockTowerPiece(outer_display = 50, draw = False):
    if draw == True:
        #draw outer clock display [50 x 50 pixels] using floor function
        floor(outer_display, outer_display,
              "BlanchedAlmond", "BurlyWood")
    ##prepare to draw inner clock display
        setheading(180)
        inner_display = outer_display - 20
        forward(inner_display/2)
        setheading(90)
        forward(10)
        #draw inner clock display [30 x 30 pixels] using windows function
        windows(inner_display, inner_display, 0,
                "BurlyWood", "DarkGoldenrod")
    ##position to draw clock face
        setheading(180)
        forward(inner_display/2)
        setheading(90)
        #prepare clock
        pencolor("white")
        fillcolor("white")
        begin_fill()
        pendown()
        setheading(0)
        #draw clock
        circle((inner_display/2) - 1)
        end_fill()
    ##prepare to draw clock hands
        long_hand = 10    
        penup()
        pencolor("black")
        setheading(90)
        forward(inner_display/2) #move to center of clock
        #draw long hand
        pendown()
        forward(long_hand)
        backward(long_hand)
        penup()
        right(90)
        #draw short hand
        pendown()
        forward(long_hand - 2)
        penup()
    ##position to draw roof
        backward(long_hand - 2)
        setheading(90)
        forward(outer_display/2)
        setheading(180)
        roof_angle = 135
        #prepare to draw roof
        pendown()
        pencolor("Sienna")
        fillcolor("DarkGoldenrod")
        begin_fill()
        #draw roof
        forward(outer_display)
        right(roof_angle)
        forward(70)
        right(roof_angle - 45)
        forward(70)
        right(roof_angle)
        forward(outer_display)
        end_fill()
        penup()

#function to draw building style C - Hotel
def Hotel(num_floors, floorheight = 50, door_top = 20,
          floorlength = 120, window_height = 30):
    from random import choice
##draw ground floor
    groundfloor = 200 #pixels
    floor(groundfloor, floorheight, "LightSteelBlue", "SteelBlue")
    #position to draw doors
    setheading(180)
    forward(15)
    for main_doorway in range(2):
        #draw 2 [25 x 15 pixel] doors using windows function
        windows(25, (door_top - 5), 0, "Silver", "DarkGray")
    #reposition to center
    setheading(90)
    forward(10)
    left(90)
    forward(door_top - 5)
    #position for windows to be drawn
    forward(groundfloor/2 - 10)
    for ground_windows1 in range(3):
        windows(window_height, door_top, 0, "LightBlue", "Cornflower Blue")
    penup()
    forward((door_top - 5)* 4)
    for ground_windows2 in range(3):
        windows(window_height, door_top, 0, "LightBlue", "Cornflower Blue")
    #reposition to draw other floors
    penup()
    forward(10)
    setheading(90)
    forward(40)
    setheading(180)
    forward(groundfloor/2)
#import choice to choose between colours
    from random import choice
##additonal floors given by instructions in random plan
    for floors in range(num_floors):
        #position to draw first floor component
        forward(floorlength/2)
        #floor colour choices
        floor_choices = ["LightSteelBlue", "Thistle"]
        floor_color = choice(floor_choices)
        #choose appropriate outline colour for floor
        if floor_color == "LightSteelBlue":
            floor_outline = "SteelBlue"
        else:
            floor_outline = "Plum"
    ##draw floors - broken into two components of different colour
        for floor_components in range(2):
            floor(floorlength, floorheight, floor_color, floor_outline)
            #reposition to draw foor
            setheading(180)
            forward((floorlength/2) - 10)
            #draw door using windows function
            windows(window_height, door_top, 0, "Peru", "Sienna")
            #reposition to draw windows
            forward(15)
            setheading(90)
            forward(floorheight/4)
            #draw windows
            for floor_windows in range(3):
                windows(25, door_top, 0, "LightBlue", "Cornflower Blue")
            #reposition to draw next floor component
            setheading(270)
            forward(floorheight/4)
            setheading(0)
            forward((floorlength/2) + 15)
            #change floor colour for new component
            if floor_color == "LightSteelBlue":
                floor_color = "Thistle"
                floor_outline = "Plum"
            else:
                floor_color = "LightSteelBlue"
                floor_outline = "SteelBlue"
    ##reposition to draw fencing
        setheading(180)
        forward((floorlength*2) + (floorlength/2))
        #draw fencing
        fencing("Lavender", 10, 15, (floorlength*2))
        #prepare to draw next floor
        forward(floorheight)
        setheading(180)
        forward(floorlength)
#roof piece for Hotel Building
def HotelRoofPiece(star_side = 15, floorlength = 120, draw = False):
    if draw == True:
    ##position to draw row of stars for roof piece
        forward(floorlength - 20)
        setheading(90)
        forward(star_side * 2)
        #draw 5 stars in a row
        for star in range(5):
            #prepare to draw star
            angle = 120
            setheading(angle/2)
            fillcolor("Yellow")
            pencolor("Black")
            pendown()
            begin_fill()
            #draw star segments 5 times
            for star_segment in range(5):
                forward(star_side)
                right(angle)
                forward(star_side)
                right(72 - angle)
            end_fill()
            penup()
            #position for next star
            setheading(0)
            forward(star_side * 3)
    ##position to draw roof
        backward(star_side * 2)
        setheading(90)
        forward(star_side)
        setheading(180)
        #prepare to draw roof
        pendown()
        fillcolor("MediumSlateBlue")
        pencolor("SlateBlue")
        begin_fill()
        #draw roof
        forward(star_side * 13)
        right(155)
        forward(110)
        right(50)
        forward(110)
        end_fill()
        penup()
        
#function to draw Building D
def BuildingD(num_floors, floor_length = 120, floor_height = 50):
##draw floors 
    for floors in range(num_floors):
        floor(floor_length, floor_height, "Azure", "SlateGray")
        #position to top of floor
        setheading(90)
        forward(floor_height)
        #draw roof for floor
        floor_roof(120, "LightSlateGray", "SlateGray")
        #position to draw arches for doors and windows
        left(90)
        forward(floor_height - 5)
        #draw arches 
        arch(10, 15, "DimGray", "DimGray")
        #reposition to draw next floors
        setheading(90)
        forward(45)
#roof piece for Building D
def BuildingDRoofPiece(draw = False, floor_length = 90, floor_height = 40):
    if draw == True:
       #draw floor
       floor(floor_length, floor_height, "Azure", "SlateGray")
       #position to draw arches
       setheading(90)
       forward(5)
       arch(20, 10, "DimGray", "DimGray")
       #go to top of floor
       setheading(90)
       forward(45)
       pendown()
       fillcolor()
       begin_fill()
       #draw roofs
       floor_roof(floor_length, "LightSlateGray", "SlateGray")
       setheading(90)
       forward(10)
       floor_roof((floor_length - 30), "LightSlateGray", "SlateGray")

# Erect buildings as per the provided city plan
def build_city(fixed_plan_5):
    for plan in fixed_plan_5:
        #starting position in sites list
        position = 0 
        if plan[0] == 1:
            #go to site 1
            goto(sites[position][1])
            #building choices 
            if plan[1] == 'A':
                #draw building with specified stories, excluding ground floor
                Hospital(plan[2] - 1)
                #if construction not completed, include sign
                if plan[3] == 'X':
                    ConstructionSign(draw = True)
                else: #draw building with roof piece 
                    sign(50, 50, "Gainsboro", "Gray")
                    cross()
            elif plan[1] == 'B':
                #draw building with specified stories
                ClockTower(plan[2])
                #if construction completed, draw roof piece
                if plan[3] == 'O':
                    ClockTowerPiece(draw = True)
                else: #draw construction sign
                    ConstructionSign(draw = True)
            elif plan[1] == 'C':
                Hotel(plan[2] - 1)
                if plan[3] == 'X':
                    ConstructionSign(draw = True)
                else:
                    HotelRoofPiece(draw = True)
            else:
                BuildingD(plan[2])
                if plan[3] == 'O':
                    BuildingDRoofPiece(draw = True)
                else:
                    ConstructionSign(draw = True)
        #for other buildings not built on site 1
        else:
            #change position according to site number on plan
            position = position + (plan[0] - 1)
            #go to specified site
            goto(sites[position][1])
            #building choices
            if plan[1] == 'A':
                Hospital(plan[2] - 1)
                if plan[3] == 'O':
                    sign(50, 50, "Gainsboro", "Gray")
                    cross()
                else:
                    ConstructionSign(draw = True)
            elif plan[1] == 'B':
                ClockTower(plan[2])
                if plan[3] == 'X':
                    ConstructionSign(draw = True)
                else:
                    ClockTowerPiece(draw = True)
            elif plan[1] == 'C':
                Hotel(plan[2] - 1)
                if plan[3] == 'O':
                    HotelRoofPiece(draw = True)
                else:
                    ConstructionSign(draw = True)
            else:
                BuildingD(plan[2])
                if plan[3] == 'X':
                    ConstructionSign(draw = True)
                else:
                    BuildingDRoofPiece(draw = True)

#
#--------------------------------------------------------------------#



#-----Main Program---------------------------------------------------#
#
# This main program sets up the background, ready for you to start
# building your city.  Do not change any of this code except
# as indicated by the comments marked '*****'.
#

# Set up the drawing canvas
# ***** Change the default argument to False if you don't want to
# ***** display the coordinates and building sites
create_drawing_canvas()

# Control the drawing speed
# ***** Modify the following argument if you want to adjust
# ***** the drawing speed
speed('slow')

# Decide whether or not to show the drawing being done step-by-step
# ***** Set the following argument to False if you don't want to wait
# ***** while the cursor moves around the screen
tracer(False)

# Give the drawing canvas a title
# ***** Replace this title with your name and/or a description of
# ***** your city
title("Anna Nguyen")

### Call the student's function to build the city
### ***** While developing your program you can call the build_city
### ***** function with one of the "fixed" data sets, but your
### ***** final solution must work with "random_plan()" as the
### ***** argument to the build_city function.  Your program must
### ***** work for any data set that can be returned by the
### ***** random_plan function.
##build_city(fixed_plan_11) # <-- used for code development only, not marking
build_city(random_plan()) # <-- used for assessment

# Exit gracefully
# ***** Change the default argument to False if you want the
# ***** cursor (turtle) to remain visible at the end of the
# ***** program as a debugging aid
release_drawing_canvas()

#
#--------------------------------------------------------------------#

