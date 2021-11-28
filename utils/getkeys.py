import win32api as wapi

keyList = [" ", "W", "A", "S", "D", "O", "P"]

def key_check():
    keys = [key for key in keyList if wapi.GetAsyncKeyState(ord(key))]
    if 'P' in keys:   return 'P'
    elif 'O' in keys: return 'O'
    elif 'W' in keys: return 'W'
    elif 'A' in keys: return 'A'
    elif 'S' in keys: return 'S'
    elif 'D' in keys: return 'D'
    elif ' ' in keys: return ' '
    else:             return 'none'
