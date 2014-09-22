# hackManager

***

> Process memory hacking made easy.


Requirements: Python 2.5, 2.6 or 2.7(recommended).

Dependencies: Ctypes, Winappdbg

PyPi Installation (Optional): `pip install hackManager`


> hackManager was created to streamline the process of hack creation. You can create quick, powerful hacks in Python with a few lines of code. 

> **Note:** You can also create anti-hacking software with this library.

Here are a few working examples below:

#####Call of Duty Black Ops 2 - No Recoil

    from hackManager.hack import Hack
    
    BLACKOPS_NORECOIL = 0x004AF328
    
    cheat_engine = Hack.change_window_title("Cheat Engine 6.1", "Changed")
    target = "t6mp.exe"
    instance = Hack(target)
    instance.findProcess()
    print instance.read(BLACKOPS_NORECOIL, 1)
