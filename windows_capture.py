import win32gui, win32ui, win32con
import numpy as np
from ctypes import windll
class WindowCapture:
    def __init__(self, window_name):
        # find the handle for the window we want to capture
        self.hwnd = win32gui.FindWindow(None, window_name)
        if not self.hwnd:
            raise Exception('Window not found: {}'.format(window_name))
    def screenshot(self):
        left, top, right, bottom = win32gui.GetClientRect(self.hwnd)

        # w = right - left
        # h = bottom - top
        # hwnd_dc = win32gui.GetWindowDC(self.hwnd)
        # mfc_dc = win32ui.CreateDCFromHandle(hwnd_dc)
        # save_dc = mfc_dc.CreateCompatibleDC()
        # bitmap = win32ui.CreateBitmap()
        # bitmap.CreateCompatibleBitmap(mfc_dc, w, h)
        # save_dc.SelectObject(bitmap)
        # # If Special K is running, this number is 3. If not, 1
        # result = windll.user32.PrintWindow(self.hwnd, save_dc.GetSafeHdc(), 3)
        # bmpinfo = bitmap.GetInfo()
        # bmpstr = bitmap.GetBitmapBits(True)
        # img = np.frombuffer(bmpstr, dtype=np.uint8).reshape((bmpinfo["bmHeight"], bmpinfo["bmWidth"], 4))
        # img = img[...,: 3]
        # img = np.ascontiguousarray(img)# make image C_CONTIGUOUS and drop alpha channel
        # win32gui.DeleteObject(bitmap.GetHandle())
        # save_dc.DeleteDC()
        # mfc_dc.DeleteDC()
        # win32gui.ReleaseDC(self.hwnd, hwnd_dc)
        return self.capture_image(left, top, right, bottom)
    

    def capture_image(self, left, top, right, bottom):
        w = right - left
        h = bottom - top
        hwnd_dc = win32gui.GetWindowDC(self.hwnd)
        mfc_dc = win32ui.CreateDCFromHandle(hwnd_dc)
        save_dc = mfc_dc.CreateCompatibleDC()
        bitmap = win32ui.CreateBitmap()
        bitmap.CreateCompatibleBitmap(mfc_dc, w, h)
        save_dc.SelectObject(bitmap)
        # If Special K is running, this number is 3. If not, 1
        result = windll.user32.PrintWindow(self.hwnd, save_dc.GetSafeHdc(), 3)
        bmpinfo = bitmap.GetInfo()
        bmpstr = bitmap.GetBitmapBits(True)
        img = np.frombuffer(bmpstr, dtype=np.uint8).reshape((bmpinfo["bmHeight"], bmpinfo["bmWidth"], 4))
        img = img[...,: 3]
        img = np.ascontiguousarray(img)# make image C_CONTIGUOUS and drop alpha channel
        win32gui.DeleteObject(bitmap.GetHandle())
        save_dc.DeleteDC()
        mfc_dc.DeleteDC()
        win32gui.ReleaseDC(self.hwnd, hwnd_dc)
        return img 
    
    
   