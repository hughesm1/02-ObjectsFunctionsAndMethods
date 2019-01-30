# """
# This module lets you experience the POWER of FUNCTIONS and PARAMETERS.
#
# Authors: David Mutchler, Vibha Alangar, Matt Boutell, Dave Fisher,
#          Aaron Wilkin, their colleagues, and Marcus Hughes-Oliver.
# """  # DONE: 1. PUT YOUR NAME IN THE ABOVE LINE.
#
# import rosegraphics as rg
#
#
# def main():
#     """
#     Calls the other functions in this module to test and/or demonstrate them.
#     """
#     drawing_speed = 10  # Bigger numbers mean faster drawing
#     window = rg.TurtleWindow()
#     window.tracer(drawing_speed)
#
#     # -------------------------------------------------------------------------
#     # When the _TODO_s ask you to test YOUR code,
#     # comment-out the following two statements and replace them
#     # by calls to   better_draw_circles   et al as needed.
#     # -------------------------------------------------------------------------
#     #draw_circles(rg.Point(100, 50))
#     #draw_circles(rg.Point(-200, 0))
#     #better_draw_circles(rg.Point(100, 50), 20)
#     #better_draw_circles(rg.Point(-200, 0), 5)
#     #even_better_draw_circles(rg.Point(100,50), 20, 7, 'blue', 3)
#     #even_better_draw_circles(rg.Point(-200,0), 5, 20, 'purple', 2)
#
#     draw_circles(rg.Point(150, 0))
#     draw_circles(rg.Point(-150, 0))
#     even_better_draw_circles(rg.Point(0, 150), 15, 10, 'red', 3)
#     even_better_draw_circles(rg.Point(0, -150), 15, 10, 'blue', 3)
#     window.update()
#     window.close_on_mouse_click()
#
#
# ###############################################################################
# # DONE: 2.
# #   First, RUN this program.  You will see that it draws concentric circles
# #   whose radii vary by 15.
# #
# #   Next, READ:
# #     -- main.
# #          Note that it  constructs a TurtleWindow and then calls the function
# #             draw_circles
# #          twice, sending   draw_circles  one Point the first time
# #          and another Point the second time.
# #     -- The function  draw_circles  is defined immediately below this _TODO_.
# #            Be sure that you understand its code!  Ask questions as needed!
# #
# #   After you have done the above, change the above _TODO_ to DONE
# #   and continue to the next _TODO_ below.
# #
# ###############################################################################
#
#
# def draw_circles(point):
#     """
#     Constructs a SimpleTurtle, then uses the SimpleTurtle to draw 10 circles
#     such that:
#       -- Each is centered at the given Point, and
#       -- They have radii:  15  30  45  60  75  ..., respectively.
#     """
#     turtle = rg.SimpleTurtle()
#
#     # -------------------------------------------------------------------------
#     # Draw circles centered at the given Point, by telling the SimpleTurtle to:
#     #  Step 1: Go to the given Point and point east (towards the right).
#     #  Step 2: Go 15 pixels DOWN, with its Pen up.
#     #          Then draw a radius R circle.
#     #    Note: The circle will be centered at the given Point,
#     #    because of the way that the SimpleTurtle  draw_circle  method works.
#     #  Step 3: Repeat Step 2, but using 30 pixels instead of 15, in both places
#     #  Step 4: Repeat Step 2, but using 45 pixels instead of 15
#     #  Step 5: Repeat Step 2, but using 60 pixels instead of 15
#     #    etc.
#     # -------------------------------------------------------------------------
#
#     turtle.pen_up()
#     turtle.go_to(point)
#     turtle.set_heading(0)  # Point "east" (towards the right)
#
#     for k in range(1, 11):  # k becomes 1, 2, 3, ... 10
#
#         turtle.pen_up()
#
#         # Go DOWN 15 pixels, ending up pointing east again
#         turtle.right(90)
#         turtle.forward(15)
#         turtle.left(90)
#
#         turtle.pen_down()
#         turtle.draw_circle(15 * k)  # Radius 15, 30, 45, 60, ...
#
#
# ###############################################################################
# # DONE: 3a.
# #   The function
# #       better_draw_circles
# #   defined below this _TODO_ starts out exactly the same as the code for
# #       draw_circles
# #   that you read above.
# #
# #   Your job is to make
# #       better_draw_circles
# #   "better" than   draw_circles   by adding a PARAMETER for the amount
# #   by which the radii of the concentric circles increase, as described below.
# #
# #   The new   better_draw_circles   function can do the same  thing as
# #   the   draw_circles  function, but additionally allows for the radii to
# #   vary by ANY desired amount.  Hence, the new version will be MORE POWERFUL.
# #
# #   So, modify the   better_draw_circles   function defined BELOW so that
# #   it has a single ADDITIONAL PARAMETER that is the amount
# #   by which the radii of the circles increase.
# #
# #   For example, if that new parameter is given the value 15,
# #   then the circles should have radii:  15  30  45  60  75 ..., respectively,
# #   just as in   draw_circles.  But if that new parameter is given the value 3,
# #   then the circles should have radii:  3  6  9  12  15  18 ..., respectively.
# #
# # DONE: 3b.
# #   In   main  at the place indicated, comment-out the two existing calls
# #   to  draw_circles  and add at least two calls to the improved
# #   better_draw_circles  function, to TEST that your modified code is correct
# #   and does indeed allow for different amounts by which the radii can vary.
# #
# # #############################################################################
#
#
# def better_draw_circles(point, radius):
#     """
#     Starts out the same as the   draw_circles   function defined ABOVE.
#     You Will make it an IMPROVED, MORE POWERFUL function per the above _TODO_.
#     """
#     turtle = rg.SimpleTurtle()
#     turtle.pen_up()
#     turtle.go_to(point)
#     turtle.set_heading(0)  # Point "east" (towards the right)
#
#     for k in range(1, 11):  # k becomes 1, 2, 3, ... 10
#
#         turtle.pen_up()
#
#         # Go DOWN 15 pixels, ending up pointing east again
#         turtle.right(90)
#         turtle.forward(radius)
#         turtle.left(90)
#
#         turtle.pen_down()
#         turtle.draw_circle(radius * k)  # Radius 15, 30, 45, 60, ...
#
#
# ###############################################################################
# # DONE: 4a.
# #   In the previous _TODO_, you made a MORE POWERFUL version
# #   of   draw_circles   by introducing a new PARAMETER for the amount
# #   by which the radii of the concentric circles increase.
# #
# #   In this _TODO_, you will implement a function called
# #      even_better_draw_circles
# #   that has FIVE parameters, for:
# #     -- The center of the concentric circles (as it started with)
# #     -- The amount by which the radii vary (as you did above)
# #     -- The number of concentric circles drawn
# #     -- The pen color of each of the concentric circles
# #     -- The pen thickness of each of the concentric circles
# #
# #   Hence, this   even_better_draw_circles   function will be
# #   even more POWERFUL than the previous functions,
# #   in that it can draw LOTS of different kinds of circles.
# #
# #   Start by copy-and-pasting the code from   better_draw_circles  above
# #   to the body of the   even_better_draw_circles   function defined below.
# #   Then add parameters and modify the code to make them work!
# #
# # DONE: 4b.
# #   In   main  at the place indicated, comment-out the existing calls
# #   to  better_draw_circles  and add at least two calls to the improved
# #   even_better_draw_circles  function, to TEST that your modified code is
# #   correct and does indeed use its parameters per their descriptions above.
# #
# ###############################################################################
#
# def even_better_draw_circles(point, radius, number, color, thick):
#     """ An improved version of draw_circles, per the _TODO_ above. """
#     # READ the above _TODO_ and then copy-paste code from better_circles here:
#     turtle = rg.SimpleTurtle()
#     turtle.pen_up()
#     turtle.go_to(point)
#     turtle.set_heading(0)  # Point "east" (towards the right)
#
#     for k in range(1, number):  # k becomes 1, 2, 3, ... 10
#
#         turtle.pen = rg.Pen(color, thick)
#         turtle.pen_up()
#
#         # Go DOWN 15 pixels, ending up pointing east again
#         turtle.right(90)
#         turtle.forward(radius)
#         turtle.left(90)
#
#         turtle.pen_down()
#         turtle.draw_circle(radius * k)  # Radius 15, 30, 45, 60, ...
#
#
# ###############################################################################
# # DONE: 5.
# #
# # Finally, comment-out the existing calls to  even_better_draw_circles  and
# # add code in   main  to draw various circles that form a BEAUTIFUL picture!
# ###############################################################################
#
#
# # -----------------------------------------------------------------------------
# # Calls  main  to start the ball rolling.
# # -----------------------------------------------------------------------------
# main()

import rosegraphics as rg


def main():
    # window = draw_window()
    xs = []
    os = []
    count = 0
    county = 0
    q = 0
    l = 0
    g = 0
    w = 0
    d = 0
    z = 0
    window = rg.RoseWindow(600, 600)

    draw_thing(window)
    while True:
        x = XX(window)
        xs = xs + [x]
        o = OO(window)
        os = os + [o]
        for k in range(len(xs)):
            if xs[k] == 1:
                q = q + 1
                if q == 1:
                    count = count + 1
            if xs[k] == 4:
                l = l + 1
                if l == 1:
                    count = count + 1
            if xs[k] == 7:
                g = g + 1
                if g == 1:
                    count = count + 1
        if count == 3:
            print('game over, square wins')
            window.close_on_mouse_click()
            break
        for k in range(len(os)):
            if os[k] == 1:
                w = w + 1
                if w == 1:
                    county = county + 1
            if os[k] == 4:
                d = d + 1
                if d == 1:
                    county = county + 1
            if os[k] == 7:
                z = z + 1
                if z == 1:
                    county = county + 1
        if county == 3:
            print('game over, O wins')
            window.close_on_mouse_click()
            break




def draw_window():
    window = rg.RoseWindow(600, 600)

    window.render()
    window.close_on_mouse_click()
    return window


def XX(window):
    x_mark = int(input('Where would you like to put your mark? number 1-9, 4 is on the next line and so forth'))
    if x_mark == 1:
        square = rg.Square(rg.Point(120, 100), 90)
        square.attach_to(window)
        window.render()
    elif x_mark == 2:
        square = rg.Square(rg.Point(300, 100), 90)
        square.attach_to(window)
        window.render()
    elif x_mark == 3:
        square = rg.Square(rg.Point(500, 100), 90)
        square.attach_to(window)
        window.render()
    elif x_mark == 4:
        square = rg.Square(rg.Point(120, 220), 90)
        square.attach_to(window)
        window.render()
    elif x_mark == 5:
        square = rg.Square(rg.Point(300, 220), 90)
        square.attach_to(window)
        window.render()
    elif x_mark == 6:
        square = rg.Square(rg.Point(500, 220), 90)
        square.attach_to(window)
        window.render()
    elif x_mark == 7:
        square = rg.Square(rg.Point(120, 450), 90)
        square.attach_to(window)
        window.render()
    elif x_mark == 8:
        square = rg.Square(rg.Point(300, 450), 90)
        square.attach_to(window)
        window.render()
    elif x_mark == 9:
        square = rg.Square(rg.Point(500, 450), 90)
        square.attach_to(window)
        window.render()
    return x_mark

def OO(window):
    o_mark = int(input('Where would you like to put your mark? number 1-9, 4 is on the next line and so forth'))
    if o_mark == 1:
        square = rg.Circle(rg.Point(120, 100), 90 // 2)
        square.attach_to(window)
        window.render()
    elif o_mark == 2:
        square = rg.Circle(rg.Point(300, 100), 90//2)
        square.attach_to(window)
        window.render()
    elif o_mark == 3:
        square = rg.Circle(rg.Point(500, 100), 90//2)
        square.attach_to(window)
        window.render()
    elif o_mark == 4:
        square = rg.Circle(rg.Point(120, 220), 90//2)
        square.attach_to(window)
        window.render()
    elif o_mark == 5:
        square = rg.Circle(rg.Point(300, 220), 90//2)
        square.attach_to(window)
        window.render()
    elif o_mark == 6:
        square = rg.Circle(rg.Point(500, 220), 90//2)
        square.attach_to(window)
        window.render()
    elif o_mark == 7:
        square = rg.Circle(rg.Point(120, 450), 90//2)
        square.attach_to(window)
        window.render()
    elif o_mark == 8:
        square = rg.Circle(rg.Point(300, 450), 90//2)
        square.attach_to(window)
        window.render()
    elif o_mark == 9:
        square = rg.Circle(rg.Point(500, 450), 90//2)
        square.attach_to(window)
        window.render()
    return o_mark


def draw_thing(window):

    start_l = rg.Point(200, 50)
    end_l = rg.Point(200, 500)
    start_r = rg.Point(400, 50)
    end_r = rg.Point(400, 500)
    start_t = rg.Point(50, 150)
    end_t = rg.Point(550, 150)
    start_b = rg.Point(50, 350)
    end_b = rg.Point(550, 350)
    line_l = rg.Line(start_l, end_l)
    line_l.attach_to(window)
    line_r = rg.Line(start_r, end_r)
    line_r.attach_to(window)
    line_t = rg.Line(start_t, end_t)
    line_t.attach_to(window)
    line_b = rg.Line(start_b, end_b)
    line_b.attach_to(window)
    window.render()
    return window
main()