import win32api,win32gui,win32con
from keyboardData import VK_CODE
from time import sleep
class Click:
    def __init__(self,windowsname):
        self.windowsname = windowsname

    def gethwid(self):
        hwid = win32gui.FindWindow('LDPlayerMainFrame',self.windowsname)
        childs = win32gui.FindWindowEx(hwid,None,'RenderWindow','TheRender')
        return childs
    
    def get_hwids(self, window_title, level=1):
        hwid = win32gui.FindWindow(None, self.windowsname)
        sub_window_handle = self.find_window_by_title(hwid, window_title)
        parent_window_handle = []
        parent_window_handle.append(sub_window_handle)
        temp = sub_window_handle
        for _ in range(level+1):
            parent_window = self.find_parent_window(temp)
            parent_window_handle.append(parent_window)
            temp = parent_window
        return parent_window_handle

    def get_nox_player_windows(self, level=1):
        hwid = win32gui.FindWindow(None, "NoxPlayer")
        sub_window_handle = self.find_window_by_title(hwid, "sub")
        parent_window_handle = []
        temp = sub_window_handle
        for _ in range(level):
            parent_window = self.find_parent_window(temp)
            parent_window_handle.append(parent_window)
            temp = parent_window
        return parent_window_handle
    
    def getfirefoxid(self):
        hwid = win32gui.FindWindow('MozillaWindowClass',self.windowsname)
        return hwid
    
    def getchromeid(self):
        hwid = win32gui.FindWindow('Chrome_WidgetWin_1',self.windowsname)
        return hwid      
    
    # def control_click(self,hwid,x,y):
    #     l_param = win32api.MAKELONG(x,y)
    #     win32gui.SendMessage(hwid,win32con.WM_LBUTTONDOWN,win32con.MK_LBUTTON,l_param)
    #     win32gui.SendMessage(hwid,win32con.WM_LBUTTONUP,win32con.MK_LBUTTON,l_param)
        # Constants for Windows messages
        
    def click(self, hwnd, x, y):
        lParam = win32api.MAKELONG(x, y)
        win32gui.SendMessage(hwnd, win32con.WM_LBUTTONDOWN, win32con.MK_LBUTTON, lParam)
        win32gui.SendMessage(hwnd, win32con.WM_LBUTTONUP, None, lParam)
        
    def send_key(self,hwid,key, hold_duration=0):
        keycode = VK_CODE[key]
        #OX70 คือ F11 เอามาจาก 
        #http://www.kbdedit.com/manual/low_level_vk_list.html
        win32api.SendMessage(hwid, win32con.WM_KEYDOWN,keycode, 0)
        sleep(hold_duration)
        win32api.SendMessage(hwid, win32con.WM_KEYUP,keycode, 0)

        # win32api.SendMessage(hwid, win32con.WM_KEYDOWN,win32con.VK_RETURN, 0)
        # win32api.SendMessage(hwid, win32con.WM_KEYUP,win32con.VK_RETURN, 0)

        # win32api.PostMessage(hwid, win32con.WM_KEYDOWN, win32con.VK_RETURN, 0)
        # win32api.PostMessage(hwid, win32con.WM_CHAR, ord('\r'), 0)
        # win32api.PostMessage(hwid, win32con.WM_KEYUP, win32con.VK_RETURN, 0) 
        
    def send_input(self,hwid, msg):
        for c in msg:
            if c == "\n":
                win32api.SendMessage(hwid, win32con.WM_KEYDOWN, win32con.VK_RETURN, 0)
                win32api.SendMessage(hwid, win32con.WM_KEYUP, win32con.VK_RETURN, 0)
            else:
                win32api.SendMessage(hwid, win32con.WM_CHAR, ord(c), 0)   
            
            
    def drag_and_drop(self,hwid, start_x, start_y, end_x, end_y):
        WM_LBUTTONDOWN = 0x0201
        WM_LBUTTONUP = 0x0202
        WM_MOUSEMOVE = 0x0200
        # Convert coordinates to Windows format
        start_x = int(start_x)
        start_y = int(start_y)
        end_x = int(end_x)
        end_y = int(end_y)

        start_point = win32api.MAKELONG(start_x, start_y)
        end_point = win32api.MAKELONG(end_x, end_y)
        # Simulate left button down event
        win32api.PostMessage(hwid, WM_LBUTTONDOWN, win32con.MK_LBUTTON, start_point)
        # Simulate mouse movement while dragging
        win32api.PostMessage(hwid, WM_MOUSEMOVE, 0, end_point)
        # Simulate left button up event
        win32api.PostMessage(hwid, WM_LBUTTONUP, 0, end_point)

    # Function to simulate click-and-hold
    def click_and_hold(self,hwid, position, hold_duration=0.1):
        WM_LBUTTONDOWN = 0x0201
        WM_LBUTTONUP = 0x0202
        # Convert coordinates to Windows format
        x, y = position
        point = win32api.MAKELONG(x, y)
        # Simulate left button down event
        win32api.PostMessage(hwid, WM_LBUTTONDOWN, win32con.MK_LBUTTON, point)
        # Hold the click for the specified duration
        #sleep(hold_duration)
        # Simulate left button up event
        #win32api.PostMessage(hwnd, WM_LBUTTONUP, 0, point)    
    # Function to simulate click-and-hold with mouse movement
    def click_hold_and_move(self,hwnd, start_x, start_y, end_x, end_y, duration, hold):
        WM_LBUTTONDOWN = 0x0201
        WM_LBUTTONUP = 0x0202
        WM_MOUSEMOVE = 0x0200
        # Convert coordinates to Windows format
        start_x = int(start_x)
        start_y = int(start_y)
        end_x = int(end_x)
        end_y = int(end_y)

        start_point = win32api.MAKELONG(start_x, start_y)
        end_point = win32api.MAKELONG(end_x, end_y)
        # Simulate left button down event
        win32api.PostMessage(hwnd, WM_LBUTTONDOWN, win32con.MK_LBUTTON, start_point)
        # Calculate the distance to move
        dx = end_x - start_x
        dy = end_y - start_y
        # Calculate the number of steps for mouse movement
        num_steps = max(abs(dx), abs(dy))
        # Calculate the delay between each step
        delay = duration / num_steps
        # Perform mouse movement
        for step in range(1, num_steps + 1):
            # Calculate the intermediate position
            x = start_x + int(dx * step / num_steps)
            y = start_y + int(dy * step / num_steps)
            point = win32api.MAKELONG(x, y)
            # Simulate mouse movement
            win32api.PostMessage(hwnd, WM_MOUSEMOVE, 0, point)
            # Delay between each step
            sleep(delay)
        # Simulate left button up event
        sleep(hold)
        win32api.PostMessage(hwnd, WM_LBUTTONUP, 0, end_point)

    def find_window_by_title(self, hwnd, title):
        if win32gui.GetWindowText(hwnd) == title:
            return hwnd
        else:
            child_windows = []
            win32gui.EnumChildWindows(hwnd, lambda hwnd, param: param.append(hwnd), child_windows)
            for child in child_windows:
                result = self.find_window_by_title(child, title)
                if result:
                    return result
        return None

    def find_parent_window(self, hwnd):
        current_window_title = win32gui.GetWindowText(hwnd)
        parent_window_handle = win32gui.GetParent(hwnd)
        if parent_window_handle:
            parent_window_title = win32gui.GetWindowText(parent_window_handle)
            print(f"Parent of '{current_window_title}' is '{parent_window_title}' (Handle: {parent_window_handle})")
            return parent_window_handle
        return 0      