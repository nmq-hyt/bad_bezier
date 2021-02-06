import cairo

print ("Cairo Version " + cairo.cairo_version_string());


test_surface = cairo.ImageSurface(cairo.FORMAT_A1, 1024,1024);
test_context = cairo.Context(test_surface);

test_context.scale(1024,1024);
test_context.set_line_width(0.007);



# linear_bezier
# draws a striaght line between two points, p0 and p0
# t is not strictly necessary here, but the orignal
# bezier function produces a point in space, ranging 0 <= t <= 1
def linear_bezier(p0x,p0y,p1x,p1y,t):
         test_context.move_to(p0x,p0y);
         tx = t * (p1x - p0x);
         ty = t * (p1y - p0y);
         test_context.line_to(tx,ty);
         test_context.stroke();
         test_surface.write_to_png("line.png");

# quadratic_bezier
# draws a series of points which are interpolations between p0 and p2, from p1, the control node
# p0 x,y values are the start
# p2 x,y values are the end
# the control point is p1, x,y
# t is default zero, to run through the entire curve process
# with t incremented by 0.1 each time 


def quadratic_bezier(p0x,p0y,p1x,p1y,p2x,p2y,t):
# lists of computed x, y points,
# which represent points in space which follow the curve of the line
         # it turns out my original code was actually correct, and that i had understood the question
         # but I'm not familar with computer graphics, and kept messing up the lines (by projecting them from the wrong angle, etc)
        tsquare = t * t;
        pointsx = [];
        pointsy = [];
     
        while t <= 1:
                 qx = (p1x + ((p0x + ((p0x * tsquare) - (2 * t * p0x)))) - ((p1x + (p1x * tsquare) - (2 * t * p1x))) + (tsquare * (p2x - p1x)));
                 qy = (p1y + ((p0y + ((p0y * tsquare) - (2 * t * p0y)))) - ((p1y + (p1y * tsquare) - (2 * t * p1y))) + (tsquare * (p2y - p1y)));
                 if ((qx >= p0x) or (qx <= p2x) and ((qy >= p0y) or (qy <= p2y))):
                          pointsx.append(qx);
                          pointsy.append(qy);
                 t = t + 0.1;
        for i in (range(len(pointsx))):
                 try:
                    test_context.line_to(pointsx[i],pointsy[i]);
                    test_context.line_to(p1y,p1x);
                    test_context.move_to(pointsx[i+1],pointsy[i+1]);
                    test_context.line_to(pointsx[i],pointsy[i]);
                    print("writing from " + str(pointsx[i]) + "," + str(pointsy[i]) + " to " + str(pointsx[i + 1]) + "," + str(pointsy[i + 1]));
                    test_context.stroke();
                    test_surface.write_to_png("curve.png");
                 except IndexError:
                          pass;


test_context.set_source_rgb(0.1,0.2,0);
#linear_bezier(0,0,1,1,0.50);
quadratic_bezier(0.21,0.51,0.55,0,0.3,0.81,0);


test_surface.finish()

