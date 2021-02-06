import cairo

print ("Cairo Version " + cairo.cairo_version_string());


test_surface = cairo.ImageSurface(cairo.FORMAT_A1, 1024,1024);
test_context = cairo.Context(test_surface);

test_context.scale(1024,1024);
test_context.set_line_width(0.01);



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
        pointsx = [];
        pointsy = [];
        pointsx.append(p0x);
        pointsy.append(p0y);
        while t <= 1:
            q0_x_temp = t * (p1x - p0x);
            q0_y_temp = t * (p1y - p0y);
            q1_x_temp = t * (p2x - p1x);
            q1_y_temp = t * (p2y - p1y);
            b1_x = abs( t * (q1_x_temp - q0_x_temp));
            b1_y = abs(t * (q1_y_temp - q0_y_temp));
            # throw away values not inside the ranges of the interpolations of q0,q1
            if ((b1_x >= q0_x_temp) or (b1_x <= q1_x_temp) and ((b1_y >= q0_y_temp) or (b1_y <= q0_y_temp))):
                     pointsx.append(b1_x)
                     pointsy.append(b1_y)
            t = t + 0.1;

        for i in (range(len(pointsx))):
                 try:
                    test_context.move_to(pointsx[i],pointsy[i]);
                    test_context.line_to(p1x,p1y);
                    test_context.move_to(pointsx[i+1],pointsy[i+1]);
                    test_context.line_to(pointsx[i],pointsy[i]);
                    print("writing from " + str(pointsx[i]) + "," + str(pointsy[i]) + " to " + str(pointsx[i + 1]) + "," + str(pointsy[i + 1]));
                    test_context.stroke();
                    test_surface.write_to_png("curve.png");
                 except IndexError:
                          pass;





test_context.set_source_rgb(0.1,0.2,0);
#linear_bezier(0,0,1,1,0.50);
quadratic_bezier(0.2,0.3,1,1,0.41,0.91,0.2);
test_surface.finish()

