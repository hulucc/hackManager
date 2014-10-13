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

    # Absolute memory address
    BLACKOPS_RECOIL_ADDRESS = 0x004AF328
    # You can also supply the base address and a offset like, i.e.:
    # BLACKOPS_RECOIL_ADDRESS = instance.base_address + 0xAF328

    # No recoil value
    BLACKOPS_NO_RECOIL_VALUE = 117

    target = "t6mp.exe"
    instance = Hack(target)
    instance.findProcess()
    # main modules base address (0x400000)
    print instance.base_address
    # instance.read_char(BLACKOPS_RECOIL_ADDRESS) returns the following:
    # ( value, label )
    #
    # label is: t6mp.exe(base address) + offset
    print instance.read_char(BLACKOPS_RECOIL_ADDRESS)
    # update value with 117(NO RECOIL VALUE)
    instance.write_char(BLACKOPS_RECOIL_ADDRESS, BLACKOPS_NO_RECOIL_VALUE)

> Singleplayer & Multiplayer hack that removes every weapons recoil effect.

#####Changing Cheat Engine's Title

    from hackManager.hack import Hack
    cheat_engine = Hack.change_window_title("Cheat Engine 6.1", "Changed")
> This allows us to use Cheat Engine to find memory addresses without it being detected.

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
