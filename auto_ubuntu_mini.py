import psutil

import os

<<<<<<< HEAD
pakage_manager_add_repository_command = "sudo apt-get install software-properties-common;sudo add-apt-repository "

aditional_repositorys = []

pakage_manager_update_repository_command = "sudo apt update"

pakage_manager_instalation_command = "sudo apt install"

pakages = ["xorg ","firefox","wicd","neofetch","htop","nano","gnome-software","discovery"]

final_commands = []
=======

final_comand = "sudo reboot"
>>>>>>> 840d0fc57aeff0e9b40839fe409c1e41cb0b940f

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
    if RAM > 3.8 and CPUs >= 4:
        power = 3
    if RAM > 7.8 and CPUs >= 8:
        power = 4
    
    
    
    print("power is: ",power)





def select_best_ui():
    global power,pakages,final_commands,aditional_repositorys
    match power:
        case 0:
            pakages += ["slim" ,"icewm","thunar"]
            final_commands += ["sudo slim"]
        case 1:
            pakages += ["slim" ,"lxde"]
            final_commands += ["sudo slim"]
        case 2:
            pakages += ["sddm" ,"xfce4"]
            final_commands += ["sudo sddm"]
        case 3:
            pakages += ["sddm" ,"cinnamon-desktop"]
            aditional_repositorys += ["ppa:embrosyn/cinnamon"]
            final_commands += ["sudo sddm"]
        case 4:
            pakages += ["sddm" ,"kde-full"]
            final_commands += ["sudo sddm"]

def install():
    global pakages,final_commands,aditional_repositorys

    #add repositorys
    command_add_repository = pakage_manager_add_repository_command
    for i in aditional_repositorys :
        command_add_repository += " " + i
    print("runing: ",command_add_repository)
    os.system(command_add_repository)

    #install pakages
    command_install_pakages = pakage_manager_instalation_command
    for i in pakages :
        command_install_pakages += " " + i
    print("runing: ",command_install_pakages)
    os.system(command_install_pakages)

    #updating pakage manager
    print("runing: ",pakage_manager_update_repository_command)
    os.system(pakage_manager_update_repository_command)

    #run final comands
    for i in final_commands :
        print("runing: ",i)
        os.system(i)
    
    
    
    

    
    

def want_continue():
    repos = ""
    for i in aditional_repositorys :
        repos += " " + i
    print("you will add this repositorys: ",repos)

    paks = ""
    for i in pakages :
        paks += " " + i
    print("you will add this pakages: ",paks)

    proceed = input("you will proceed with the installation y/n \n")
    if proceed == "y" or proceed == "Y":
        install()



def get_pc_info():
    get_CPUs()
    get_RAM()
    define_power()
    input("press enter to continue\n")

def make_instalation():
    get_CPUs()
    get_RAM()
    define_power()
    select_best_ui()
    want_continue()
    
    

#get_pc_info()
make_instalation()
input("press enter to continue\n")

