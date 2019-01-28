import ctypes
dll=ctypes.cdll.LoadLibrary("F:\\ykq\P\\ConsoleApplication1\\Release\\ConsoleApplication1.dll")
# dll.c_t.restype = ctypes.c_char_p
# print(dll.add(1,3))
# print(dll.c_t().decode('utf-8'))
# dll.display.restype = ctypes.c_char
dll.display()


