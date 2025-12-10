from src import commands
import threading

def run_command_threaded(command_func, *args):

    thread = threading.Thread(target=command_func, args=args)
    thread.start()

# ADB Scripting
def reboot():
    run_command_threaded(commands.reboot)

def rebootrecovery():
    run_command_threaded(commands.rebootrecovery)

def rebootfastboot():
    run_command_threaded(commands.rebootfastboot)

def rebootbootloader():
    run_command_threaded(commands.rebootbootloader)

def getstatedevice():
    run_command_threaded(commands.getstatedevice)

def getsn():
    run_command_threaded(commands.getsn)

def root():
    run_command_threaded(commands.root)

# ADB Debugging & Internal Debugging
def logcat():
    run_command_threaded(commands.logcat)

def startserver():
    run_command_threaded(commands.startserver)

def killserver():
    run_command_threaded(commands.killserver)

def reconnecthost():
    run_command_threaded(commands.reconnecthost)

def reconnectdevice():
    run_command_threaded(commands.reconnectdevice)

def reconnectoffline():
    run_command_threaded(commands.reconnectoffline)

def devices():
    run_command_threaded(commands.devices)

# App Installation & File Transfer
def install(arg):
    run_command_threaded(commands.install, arg)

def push(arg, arg2):
    run_command_threaded(commands.push, arg, arg2)

def pull(arg):
    run_command_threaded(commands.pull, arg)

def remount():
    run_command_threaded(commands.remount)

def sideload(arg):
    run_command_threaded(commands.sideload, arg)

# Shell
def shell():
    run_command_threaded(commands.shell)

def uninstall(arg):
    run_command_threaded(commands.uninstall, arg)

def getapps():
    run_command_threaded(commands.getapps)

def androidversion():
    run_command_threaded(commands.androidversion)

# Fastboot section
def fastboot_devices():
    run_command_threaded(commands.fastboot_devices)

def fastboot_reboot():
    run_command_threaded(commands.fastboot_reboot)

def fastboot_reboot_recovery():
    run_command_threaded(commands.fastboot_reboot_recovery)

def fastboot_unlock():
    run_command_threaded(commands.fastboot_unlock)

def fastboot_lock():
    run_command_threaded(commands.fastboot_lock)

def fastboot_critical_unlock():
    run_command_threaded(commands.fastboot_critical_unlock)

def fastboot_critical_lock():
    run_command_threaded(commands.fastboot_critical_lock)
