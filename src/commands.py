from subprocess import call
from subprocess import Popen


def reboot():
    call(["adb", "reboot"])

def rebootrecovery():
    call(["adb", "reboot", "recovery"])

def rebootfastboot():
    call(["adb", "reboot", "fastboot"])

def logcat():
    call(["adb", "logcat"])

def getstatedevice():
    call(["adb", "get-state"])

def getsn():
    call(["adb", "get-serialno"])

def startserver():
    call(["adb", "start-server"])

def killserver():
    call(["adb", "kill-server"])

def reconnecthost():
    call(["adb", "reconnect"])

def reconnectdevice():
    call(["adb", "reconnect", "device"])

def reconnectoffline():
    call(["adb", "reconnect", "offline"])
    
def remount():
    call(["adb", "remount"])
    
def root():
    call(["adb", "root"])
    
def rebootbootloader():
    call(["adb", "reboot", "bootloader"])
    
def devices():
    call(["adb", "devices"])

# Shell

def shell():
    Popen(["adb", "shell"])
    
def androidversion():
    Popen(["adb", "shell", "getprop", "ro.build.version.release"])
    
def getapps():
    Popen(["adb", "shell", "list", "packages", "-r"])

## Commands that have arguments
def install(arg):
    call(["adb", "install", arg])
    
def pull(arg):
    call(["adb", "pull", arg])
    
def push(arg, arg2):
    call(["adb", "push", arg, arg2])
    
def sideload(arg):
    call(["adb", "sideload", arg])

def uninstall(arg):
    call(["adb", "uninstall", arg])

# Fastboot button commands
def fastboot_devices():
    Popen(["fastboot", "devices"])
    
def fastboot_reboot():
    Popen(["fastboot", "reboot"])
    
def fastboot_reboot_recovery():
    Popen(["fastboot", "reboot", "recovery"])
    
def fastboot_unlock():
    Popen(["fastboot", "flashing", "unlock"])
    
def fastboot_lock():
    Popen(["fastboot", "flashing", "lock"])
    
def fastboot_critical_unlock():
    Popen(["fastboot", "flashing", "unlock_critical"])
    
def fastboot_critical_lock():
    Popen(["fastboot", "flashing", "lock_critical"])
