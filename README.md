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
    
    BLACKOPS2_RECOIL_ADDRESS = 0x004AF328
    BLACKOPS2_NORECOIL_VALUE = 167
    
    target = "t6mp.exe"
    instance = Hack(target)
    instance.findProcess()
    instance.write(BLACKOPS2_RECOIL_ADDRESS, BLACKOPS2_NORECOIL_VALUE)
> Singleplayer & Multiplayer hack that removes every weapons recoil effect.

#####Changing Cheat Engine's Title

    from hackManager.hack import Hack
    cheat_engine = Hack.change_window_title("Cheat Engine 6.1", "Changed")
> This allows use to use Cheat Engine to find memory addresses without it being detected.
