import psutil
import os

final_comand = "sudo reboot"

CPUs = 0
def get_CPUs():
    global CPUs
    CPUs = psutil.cpu_count()
    print("you have: ",CPUs," CPU cores")

RAM = 0.0
def get_RAM():
    global RAM,CPUs
    RAM = psutil.virtual_memory().total / 1000000000
    print("memory ran total size is: ",RAM," GB")

power = 0
def define_power():
    global RAM,CPUs,power
    print("defining power")
    if RAM > 0.8:
        power = 1
    if RAM > 1.8 and CPUs >= 2:
        power = 2
    
    
    
    
    print("power is: ",power)

def install_basics():
    print("instaling basic pakages")
    os.system("sudo apt install xorg firefox wicd ")

def install_extras():
    print("instaling extra pakages")
    os.system("sudo apt install gnome-software discovery ")

def install_best_ui():
    global power
    match power:
        case 1:
            os.system("sudo apt install slim lxde")
            final_comand = "sudo slim"
        case 2:
            os.system("sudo apt install sddm xfce4")
            final_comand = "sudo sddm"
        case 3:
            os.system("sudo apt install sddm kde-full")
            final_comand = "sudo sddm"

def get_pc_info():
    get_CPUs()
    get_RAM()
    define_power()
    input("press enter to continue")

def make_instalation():
    get_CPUs()
    get_RAM()
    define_power()
    install_basics()
    install_best_ui()
    os.system(final_comand)
    



get_pc_info()
#make_instalation()



