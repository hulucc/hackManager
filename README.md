# hackManager

***

> Process memory hacking made easy.


Requirements: Python 2.6 or 2.7(recommended).

Dependencies: Ctypes, Winappdbg(http://winappdbg.sourceforge.net/Downloads.html)

PyPi Installation (Optional): `pip install hackManager`


> hackManager was created to streamline the process of hack creation. You can create quick, powerful hacks in Python with a few lines of code. 

> **Note:** You can also create anti-hacking software with this library.

Here are a few working examples below:


#####Kernel / DLL Hooking

    from hackManager.hack import Hack


    def sendto(event, ra, s, buf, length, flags, to, tolength):
        data = event.get_process().peek(buf, length)
        print "Send: " + data + "\n"


    h = Hack("rust_server.exe")
    h.add_hook("ws2_32.dll", "sendto", sendto)
    h.hook()
    h.safe_exit()

> You can hook onto Kernel and DLL functions within' a process. In this example, we hook onto RUST's(game) Dedicated Server and hook onto its WinSock SendTo DLL function calls. This allows us to sniff(analyze) process-specific traffic. This requires a little research on your part though. For example, you need to know what parameters the DLL functions require. You can easily pull this up on Google Search by typing something like, i.e: "WinSock sendto msdn". The Microsoft Developer Network is fulled with tons of documentation for its DLLs like Winsock. In this example, I referenced the following documentation:
http://msdn.microsoft.com/en-us/library/windows/desktop/ms740148%28v=vs.85%29.aspx

> You can add as many hooks as you want, for the same DLL or different ones. Simply call the class-method `add_hook(DLL_Name, DLL_Function, function_handler)`.


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
    Hack.change_window_title("Cheat Engine 6.1", "Changed")
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

####Accessing and modifying data structures
> Most games and computer software come with structures that group data together. These structures can be accessed with hackManager and even modified! 

    from hackManager.hack import Hack
    import ctypes
    
    # Winsock sockaddr structure. Documented at:   
    # http://msdn.microsoft.com/en-us/library/windows/desktop/ms740496%28v=vs.85%29.aspx
    
    class sockaddr(ctypes.Structure):
        _fields_ = [
            ("sa_family", ctypes.c_ushort),
            ("sa_data", ctypes.c_char * 14),
        ]
        
    def sendto(event, ra, s, buf, length, flags, to, tolength):
        p = event.get_process()
        data = p.peek(buf, length)
        to_struct = p.read_structure(to, sockaddr)
        print "BUFFER DATA: " + repr(data) + "\n"
        print "ACCESSING SPECIFIC STRUCTURE sa_data field:", repr(to_struct.sa_data)
        print "PEEKING WHOLE STRUCTURE DATA:", repr(p.peek(to, tolength))
    
    game = Hack("game.exe")
    h.add_hook("ws2_32.dll", "sendto", sendto)
    h.hook()
    h.safe_exit()
    
> In this example we are hooking on the game's Winsock sendto DLL function and accessing its Structure directly via `ctypes`. We are also accessing the data directly via `peek`. Both methods work great, however, if you want to access Structure fields in a clean manner, the `ctypes` approach is preferred.
    
####Retrieving and interacting with running threads
> You can retrieve the list of the processes running threads with the `Hack.get_threads()` class-method. You can use this to your advantage to supervise the amount of threads your processes currently has running and to analyze them individually. Remember that hackManager is built on top of `winappdbg`, thus you are able to execute thread-related class-method like, i.e: `thread_instance.set_name()`, `thread_instance.is_hidden()`, `thread_instance.set_process()`, `thread_instance.kill()`, `thread_instance.name()`, `thread_instance.resume()`, `thread_instance.suspend()`, to name a few. 
> When you call `Hack.get_threads()`, the list of threads are stored on your `Hack()` instances `thread` global variable. Thus you can access it with `Hack_instance.threads`. It's stored as a dictionary. The thread id's being the keys for the dictionary.
> Check the `winappdbg` documentation for more information regarding iteraction with threads. Remember: hackManager returns `winappdbg.Thread` instances.

    from hackManager.hack import Hack
    
    h = Hack("game.exe")
    h.get_threads()
    print h.threads # returns dictionary, with the keys being the individual threads id's.

####Retrieving the list of imported DLLs(libraries).
> You can retrieve the list of loaded(imported) DLLs(libraries) within' the process by accessing the `module_base_dict` global variable. The `module_base_dict` is a dictionary with the keys being the module names and the values being their base address.

    from hackManager.hack import Hack
    
    h = Hack("game.exe")
    print h.module_base_dict


####Retrieving list of running processes
> You can retrieve the list of currently running processes by not supplying a target process name within' your `Hack()` instance. Then you access the list by calling `Hack_instance.running`.

    from hackManager.hack import Hack
    
    h = Hack()
    print h.running
