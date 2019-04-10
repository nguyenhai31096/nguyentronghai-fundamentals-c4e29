def is_inside(point=[], rectangle=[]):
    point_coordinates_x = point[0]
    rectangle_coordinates_x = rectangle[0]
    point_coordinates_y = point[1]
    rectangle_coordinates_y = rectangle[1]
    width_retangle = rectangle[2]
    height_retangle = rectangle[3]
    if point_coordinates_x in range ( rectangle_coordinates_x, rectangle_coordinates_x + width_retangle ):
        if point_coordinates_y in range (rectangle_coordinates_y, rectangle_coordinates_y + height_retangle):
            return True
    else:
        return False
#test_case:
check_this_point = is_inside([100, 100],[140, 60, 100, 100])
if check_this_point == True:
    print("true")
else:
    print("false") 

