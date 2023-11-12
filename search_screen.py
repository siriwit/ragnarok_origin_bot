import cv2 as cv
import numpy as np
import sys

class Classbot:
    TRACKBAR_WINDOW = "Trackbars"
    def __init__(self, main_img, temp_img="", window_name="ROO Bot"):
        self.tempimg = temp_img
        self.mainimg = main_img
        self.image_to_draw_path = None
        self.window_name = window_name
        if temp_img != "":
            self.tempimg = cv.imread(temp_img,cv.IMREAD_ANYCOLOR)
       
        
    def search(self,threshold=0.9, debug=False, image_path=""):
        self.image_to_draw_path = image_path
        result = cv.matchTemplate(self.mainimg,self.tempimg,cv.TM_CCOEFF_NORMED)    
        _,_,_,_ = cv.minMaxLoc(result)
        locations = np.where(result >= threshold)
        locations= list(zip(*locations[::-1]))
        height = self.tempimg.shape[0]
        width =  self.tempimg.shape[1]
        rectangles =[]
        for loc in locations:
            rect = (int(loc[0]),int(loc[1]),width,height)
            rectangles.append(rect)
            rectangles.append(rect)
        
        rectangles,_ =cv.groupRectangles(rectangles,groupThreshold=1,eps=0.2)
        
        if debug:
            mytxt = image_path.split('/')[-1]
            self.draw_debug_rect(f"Finding {mytxt}", 60, 80, 10, 10, show_text=True, show_rect=False, show_marker=False, show_finding_image=True)
            if len(rectangles):
                for (x,y,w,h) in rectangles:
                    self.draw_debug_rect(mytxt, x, y, w, h)
            else:
                self.show_image()

        return rectangles
    

    def draw_debug_rect(
            self, text, 
            x, y, width, height,
            font=cv.FONT_ITALIC, 
            fontsize=0.8, 
            color=(255,0,255),
            show_text=True,
            show_rect=True,
            show_marker=True,
            show_finding_image=True):
        topleft = (x, y)
        bottomright = (x + width, y + height)
        centerx = x + int(width / 2)
        centery = y +int(height / 2)
        position = (topleft[0],topleft[1]-10)
        point = []
        point.append((centerx,centery))
        if show_text:
            cv.putText(self.mainimg, text, position, font, fontsize, color, thickness=2)
        if show_rect:
            cv.rectangle(self.mainimg,topleft,bottomright,color=(255,0,255),thickness=2,lineType=cv.LINE_8)
        if show_marker:
            cv.drawMarker(self.mainimg,(centerx,centery),color=(0,255,0),thickness=2,markerSize=40,markerType=cv.MARKER_CROSS)
        if show_finding_image and self.image_to_draw_path is not None:
            x_offset = 80
            y_offset = 100
            image_to_draw = cv.imread(self.image_to_draw_path)
            image_to_draw_height = image_to_draw.shape[0]
            image_to_draw_width = image_to_draw.shape[1]
            image_to_draw_topleft = (x_offset, y_offset)
            image_to_draw_bottomright = (x_offset + image_to_draw_width, y_offset + image_to_draw_height)
            draw_x = x_offset+image_to_draw_width
            draw_y = y_offset+image_to_draw_height
            self.mainimg[y_offset:draw_y, x_offset:draw_x] = image_to_draw
            cv.rectangle(self.mainimg, image_to_draw_topleft, image_to_draw_bottomright, color=(255,0,255), thickness=2, lineType=cv.LINE_8)
        self.show_image()


    def show_image(self):
        cv.imshow(f"{self.window_name} Debugging",self.mainimg)
        if cv.waitKey(1) == ord('q'):
            cv.destroyAllWindows()
            sys.exit(0)


    def getcolor(self,x,y,color="0x000000"):
        ##define status
        status = False 
        ## return b g r from x y[y,x]
        b,g,r = self.mainimg[y,x]
        #sumvalue from r g b
        sumvalue = self.mainimg[y,x].sum()
     
        ## change to r g b
        value = '%02x%02x%02x' % (r, g, b)
        ## upper 
        value =value.upper()
        ## add 0x autoitinfo
        value = '0x' + value
        ### if to return
        if value == color:
            status = True
        return status,sumvalue
    
    def draw_rectangles(self, haystack_img, rectangles):
        # these colors are actually BGR
        line_color = (0, 255, 0)
        line_type = cv.LINE_4

        for (x, y, w, h) in rectangles:
            # determine the box positions
            top_left = (x, y)
            bottom_right = (x + w, y + h)
            # draw the box
            cv.rectangle(haystack_img, top_left, bottom_right, line_color, lineType=line_type)

        return haystack_img

    # given a list of [x, y] positions and a canvas image to draw on, return an image with all
    # of those click points drawn on as crosshairs
    def draw_crosshairs(self, haystack_img, points):
        # these colors are actually BGR
        marker_color = (255, 0, 255)
        marker_type = cv.MARKER_CROSS

        for (center_x, center_y) in points:
            # draw the center point
            cv.drawMarker(haystack_img, (center_x, center_y), marker_color, marker_type)

        return haystack_img

    # create gui window with controls for adjusting arguments in real-time
    def init_control_gui(self):
        cv.namedWindow(self.TRACKBAR_WINDOW, cv.WINDOW_NORMAL)
        cv.resizeWindow(self.TRACKBAR_WINDOW, 350, 700)

        # required callback. we'll be using getTrackbarPos() to do lookups
        # instead of using the callback.
        def nothing(position):
            pass

        # create trackbars for bracketing.
        # OpenCV scale for HSV is H: 0-179, S: 0-255, V: 0-255
        cv.createTrackbar('HMin', self.TRACKBAR_WINDOW, 0, 179, nothing)
        cv.createTrackbar('SMin', self.TRACKBAR_WINDOW, 0, 255, nothing)
        cv.createTrackbar('VMin', self.TRACKBAR_WINDOW, 0, 255, nothing)
        cv.createTrackbar('HMax', self.TRACKBAR_WINDOW, 0, 179, nothing)
        cv.createTrackbar('SMax', self.TRACKBAR_WINDOW, 0, 255, nothing)
        cv.createTrackbar('VMax', self.TRACKBAR_WINDOW, 0, 255, nothing)
        # Set default value for Max HSV trackbars
        cv.setTrackbarPos('HMax', self.TRACKBAR_WINDOW, 179)
        cv.setTrackbarPos('SMax', self.TRACKBAR_WINDOW, 255)
        cv.setTrackbarPos('VMax', self.TRACKBAR_WINDOW, 255)

        # trackbars for increasing/decreasing saturation and value
        cv.createTrackbar('SAdd', self.TRACKBAR_WINDOW, 0, 255, nothing)
        cv.createTrackbar('SSub', self.TRACKBAR_WINDOW, 0, 255, nothing)
        cv.createTrackbar('VAdd', self.TRACKBAR_WINDOW, 0, 255, nothing)
        cv.createTrackbar('VSub', self.TRACKBAR_WINDOW, 0, 255, nothing)

    # returns an HSV filter object based on the control GUI values
    def get_hsv_filter_from_controls(self):
        # Get current positions of all trackbars
        hsv_filter = HsvFilter()
        hsv_filter.hMin = cv.getTrackbarPos('HMin', self.TRACKBAR_WINDOW)
        hsv_filter.sMin = cv.getTrackbarPos('SMin', self.TRACKBAR_WINDOW)
        hsv_filter.vMin = cv.getTrackbarPos('VMin', self.TRACKBAR_WINDOW)
        hsv_filter.hMax = cv.getTrackbarPos('HMax', self.TRACKBAR_WINDOW)
        hsv_filter.sMax = cv.getTrackbarPos('SMax', self.TRACKBAR_WINDOW)
        hsv_filter.vMax = cv.getTrackbarPos('VMax', self.TRACKBAR_WINDOW)
        hsv_filter.sAdd = cv.getTrackbarPos('SAdd', self.TRACKBAR_WINDOW)
        hsv_filter.sSub = cv.getTrackbarPos('SSub', self.TRACKBAR_WINDOW)
        hsv_filter.vAdd = cv.getTrackbarPos('VAdd', self.TRACKBAR_WINDOW)
        hsv_filter.vSub = cv.getTrackbarPos('VSub', self.TRACKBAR_WINDOW)
        return hsv_filter

    # given an image and an HSV filter, apply the filter and return the resulting image.
    # if a filter is not supplied, the control GUI trackbars will be used
    def apply_hsv_filter(self, original_image, hsv_filter=None):
        # convert image to HSV
        hsv = cv.cvtColor(original_image, cv.COLOR_BGR2HSV)

        # if we haven't been given a defined filter, use the filter values from the GUI
        if not hsv_filter:
            hsv_filter = self.get_hsv_filter_from_controls()

        # add/subtract saturation and value
        h, s, v = cv.split(hsv)
        s = self.shift_channel(s, hsv_filter.sAdd)
        s = self.shift_channel(s, -hsv_filter.sSub)
        v = self.shift_channel(v, hsv_filter.vAdd)
        v = self.shift_channel(v, -hsv_filter.vSub)
        hsv = cv.merge([h, s, v])

        # Set minimum and maximum HSV values to display
        lower = np.array([hsv_filter.hMin, hsv_filter.sMin, hsv_filter.vMin])
        upper = np.array([hsv_filter.hMax, hsv_filter.sMax, hsv_filter.vMax])
        # Apply the thresholds
        mask = cv.inRange(hsv, lower, upper)
        result = cv.bitwise_and(hsv, hsv, mask=mask)

        # convert back to BGR for imshow() to display it properly
        img = cv.cvtColor(result, cv.COLOR_HSV2BGR)

        return img

    # apply adjustments to an HSV channel
    # https://stackoverflow.com/questions/49697363/shifting-hsv-pixel-values-in-python-using-numpy
    def shift_channel(self, c, amount):
        if amount > 0:
            lim = 255 - amount
            c[c >= lim] = 255
            c[c < lim] += amount
        elif amount < 0:
            amount = -amount
            lim = amount
            c[c <= lim] = 0
            c[c > lim] -= amount
        return c        
        
        

