import ctypes
import os

strCurPath = os.path.dirname(__file__)

# if target has dependency dll, load it before target dll
# ctypes.CDLL(os.path.join(strCurPath, "cpprest141_2_10.dll"))
lib = ctypes.CDLL(os.path.join(strCurPath, "test_hello_world.dll"))

hello_world_func = lib.TestFunctionHelloWorld
hello_world_func.argtypes = None
hello_world_func.restype = None  

def hello_world():
    hello_world_func()