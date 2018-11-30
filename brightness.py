import wmi

def br(num):
    brightness = num
    c = wmi.WMI(namespace="wmi")
    method = c.WmiMonitorBrightnessMethods()[0]
    method.WmiSetBrightness(brightness, 0)

num = input("Enter brightness percentage: ")
br(num)
