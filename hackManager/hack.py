import winappdbg
import os


__website__ = "FindADownload.net"
__author__ = "David Almendarez"
__version__ = "1.0"
__date__ = "09/21/2014"


class Hack(object):
    """Base class utilized to make hack development for any type of game/software easy."""
    
    def __init__(self, processName=None):
        """
        i = Hack(process_name).
        ########################
        If no process is supplied, then you do \
        
        i = Hack().findProcess()
        print i.running

        to get the current running processes.
        """
        
        self.module_base_dict = {}
        self.name = processName
        self.threads = {}
        self.hwnd = None
        self.base_address = None
        self.running = []
        if processName is not None:
            self.findProcess(processName)
            self.getBaseAddress()

    def __repr__(self):
        return "<Hack instance: %s>" %str(self.name)

    def get_threads(self):
        """
        Get running thread list.
        You can call .suspend(), .resume(), .kill(), .name(), \
        .set_name(), .is_hidden(), .set_process(), etc.
        Check out http://winappdbg.sourceforge.net/doc/v1.4/reference/winappdbg.system.Thread-class.html for more info.
        """
        process = self.hwnd 
        for thread in process.iter_threads():
            self.threads[str(thread.get_tid())] = thread

    @classmethod
    def change_window_title(cls, title, new_title):
        """
        Change the specified window's title to the new_title. \
        (title, new_title).

        This is a class-method.

        i.e.: Hack.change_window_title('Cheat Engine 6.1', 'Undetected CE')
        """
        try:
            _window = winappdbg.System.find_window(windowName=title)
        except:
            _window = None
            
        if _window:
            _window.set_text(new_title)
            return _window
        
        return False

    def findProcess(self, processName=None):
        """
        If a processName is not passed, then it will return the list of running processes.
        Do NOT call this method(function) directly. It is called by the __init__ class method.
        If you want to list all running process do the following:
        ins = Hack()
        print ins.running
        """
        system = winappdbg.System()
        for process in system:
            if process.get_filename() is not None:
                name = process.get_filename().split("\\")[-1]
                if processName is None:
                    self.running.append((name, process.get_pid()))
                else:
                    if name == processName:
                        self.hwnd = process
                        break;
                
    def getBaseAddress(self):
        """
        Get our processes base_address & its DLL's base_addresses too. \
        Stored in module_base_dict global variable.
        """
        process = self.hwnd

        if process is None:
            raise ValueError, "Could not find process."
            
        bits = process.get_bits()
        for module in process.iter_modules():
            if module.get_filename().split("\\")[-1] == self.name:
                self.base_address = module.get_base()
                #self.base_address = winappdbg.HexDump.address( module.get_base(), bits )
            else:
                module_name = os.path.basename(module.get_filename())
                self.module_base_dict[module_name] = module.get_base()

    def read(self, address, length):
        """
        Read process memory. (memory_adress, data_length). \
        i.e.: (0x40000000, 4)
        """
        process = self.hwnd
        data = process.read( address, length )
        return data

    def write(self, address, data):
        "Write to process memory. (memory_address, data2write)"""
        process = self.hwnd
        writen = process.write( address, data )
        return 1

    def load_dll(self, filename):
        """Inject filename.dll into our process. (filename)"""
        process = self.hwnd
        process.inject_dll( filename )
        return True

