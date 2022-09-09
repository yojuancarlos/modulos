import os
import time

path = "C:\pruebas\carpeta1"
ti_m = os.path.getmtime(path)
m_ti = time.ctime(ti_m)
print( f" was last modified at {m_ti}")