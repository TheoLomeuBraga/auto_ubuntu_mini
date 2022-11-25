import psutil

import os

pakage_manager_add_repository_command = "sudo apt-get install software-properties-common;sudo add-apt-repository "

aditional_repositorys = []

pakage_manager_update_repository_command = "sudo apt update"

pakage_manager_instalation_command = "sudo apt install"

pakages = ["xorg ","firefox","wicd","neofetch","htop","nano","gnome-software","discover"]

final_commands = []

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
    if power == 0:
            pakages += ["slim" ,"icewm","thunar"]
            final_commands += ["sudo slim"]
    elif power == 1:
            #pakages += ["slim" ,"lxde"]
            #final_commands += ["sudo slim"]
            pakages += ["slim" ,"lxqt","openbox"]
            final_commands += ["sudo slim"]
    elif power == 2:
            pakages += ["sddm" ,"xfce4"]
            final_commands += ["sudo sddm"]
    elif power == 3:
            pakages += ["sddm" ,"cinnamon-desktop-environment"]
            aditional_repositorys += ["universe"]
            final_commands += ["sudo sddm"]
    elif power == 4:
            pakages += ["sddm" ,"kde-full"]
            final_commands += ["sudo sddm"]
    

def install():
    global pakages,final_commands,aditional_repositorys

    #add repositorys
    for i in aditional_repositorys :
        os.system(pakage_manager_add_repository_command + " " + i)
        print("runing: ",pakage_manager_add_repository_command + " " + i)
    
    

    #updating pakage manager
    print("runing: ",pakage_manager_update_repository_command)
    os.system(pakage_manager_update_repository_command)

    #install pakages
    command_install_pakages = pakage_manager_instalation_command
    for i in pakages :
        command_install_pakages += " " + i
    print("runing: ",command_install_pakages)
    os.system(command_install_pakages)

    

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

