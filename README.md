# hackManager

***

> Process memory hacking made easy.


Requirements: Python 2.6 or 2.7(recommended).

Dependencies: Ctypes, Winappdbg(http://winappdbg.sourceforge.net/Downloads.html)

PyPi Installation (Optional): `pip install hackManager`


> hackManager was created to streamline the process of hack creation. You can create quick, powerful hacks in Python with a few lines of code. 

> **Note:** You can also create anti-hacking software with this library.

Here are a few working examples below:

#####Call of Duty Black Ops 2(PC) - No Recoil

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

#####Creating test apps for testing hacks
> The purpose of test apps is to learn how to read data structures and access their individual attributes, i.e.: "health", "name", "position", "level", etc.

    from hackManager.test import Test
    
    class Player(Test):
        def __init__(self, name, **kwargs):
            Test.__init__(self, name, **kwargs)
            
    # mainloop_check(attr="health") will output the value of health every second.
    Player(name="Charlie", health=100).mainloop_check(attr="health")

I recommend py2exe to compile python scripts to Windows executables.
(http://www.py2exe.org/)
