import os

logo2 = """
                                                                                                            
                            ................................   .,%%%%,... ..................................
                            .... ..............................,&%&&&@%,....................................
                            .......(,,,,,.......................*%%&(*@*,.....................,..,,%(*&&,...
                            ....#***(@@(*,..,....................(*(#%#,...................,,*#@@@&@@@@%##,,
                            ...,,#&@@@@@@@@@%**,,,,,,,,**%&@@@@%(%@@&%//&@@@@@@@&%%%%%%%&&@@@@@@@@&(//**,,,.
                            ....,,,,,**(@@@@@@@@@@@@@@@@@@@@@&&@@@@&&(#@@@@@@&@%@@@@@@@@@@@@@@(/*,,,,.......
                            ..........,,,,**/(&@@@@@@@@@((//*&@@@@@@@&&@&@&@@&(/////////****,,,,............
                            ................,,,,,,,,,,,,,,,,.*@@@@@@@@@@@@@@@/*,,...........................
                            ..................................#&@@@@@@@@@@&@&*,,............................
                                                    ........,%@@@@@@@@@@@@/,,....                         
                                                    ......,.,&@@@@@&@&@@&#*,,....                         
                                                    ....,,.,%&&@@@@@@@@@&(*,,....                         
                                                    ..,,&%/@@@@@@@@@@@@@@@@*,,...                         
                                                    ,,,,(&@&&@@@@@@@@@@@@&(*,,...                         
                                                    ,,.*&@#&@@&&@@@&@@@@@%@%,,,..                         
                                                    ..,%%/&#@&@@@@@@@@&&%/@&@*,,.                         
                                                    .,.*//@#@@@@@@@@@@@@&/@/&*,,.                         
"""

logo = """
        ::::::::::: ::::::::::: ::::    ::::  ::::::::::        ::::::::  :::            :::      ::::::::      :::     :::::::::  
            :+:         :+:     +:+:+: :+:+:+ :+:              :+:    :+: :+:          :+: :+:   :+:    :+:    :+:      :+:    :+: 
            +:+         +:+     +:+ +:+:+ +:+ +:+              +:+        +:+         +:+   +:+  +:+          +:+ +:+   +:+    +:+ 
            +#+         +#+     +#+  +:+  +#+ +#++:++#         +#++:++#++ +#+        +#++:++#++: +#++:++#++  +#+  +:+   +#++:++#:  
            +#+         +#+     +#+       +#+ +#+                     +#+ +#+        +#+     +#+        +#+ +#+#+#+#+#+ +#+    +#+ 
            #+#         #+#     #+#       #+# #+#              #+#    #+# #+#        #+#     #+# #+#    #+#       #+#   #+#    #+# 
            ###     ########### ###       ### ##########        ########  ########## ###     ###  ########        ###   ###    ### 
"""

Directories = ["1. Games", "2. Game Launchers", "3. Coding", "4. Other Applications", "5. Virtual Machines", "6. Common Websites ;)"] # You can change these to the numbers and names of ur wanted directories
Commands = ["exit - Exits the terminal", "back - Goes to the previous directory"]

def RunSelectAndPrintInDir(category, put_ur_list_here):
    print(f"\nChoose a {category} to open!")
    index = 1

    for item in os.listdir():
        new_index = str(index) + ". "
        new_name = ""

        for char in item:
            if char != ".":
                new_name += char
            else:
                break

        print(new_index, new_name)

        put_ur_list_here.append(item)


        index += 1


def OpenChosenIndexInDir(index, needed_dir, directory):
    for item in needed_dir:
        if needed_dir.index(item) + 1 == index:
            new_name = ""

            for char in needed_dir[index - 1]:
                if char != ".":
                    new_name += char
                else:
                    break


            print(f"You've chosen: {new_name}")
            os.system(f"{directory}\\{item}")
        else:
            pass

isRunning = True

while isRunning:
    print(f"{logo2}\n{logo}")
    print("What directory would u like to visit?")

    for epik_dir in Directories:
        print(epik_dir)

    FirstDir = input("\n")

    try:
        FirstDir = int(FirstDir)
    except:
        FirstDir = FirstDir

    if isinstance(FirstDir, str) and FirstDir == "help":
        for command in Commands:
            print(command)

    if FirstDir == 1:
        os.chdir(r"DIRECTORY1_PATH_HERE") # PUT UR DIRECTORY HERE

        Directory = os.getcwd()
        Games = []

        RunSelectAndPrintInDir("game", Games)
        
        Chosen_Game = int(input("\n"))
        OpenChosenIndexInDir(Chosen_Game, Games, Directory)

    elif FirstDir == 2:
        os.chdir(r"DIRECTORY1_PATH_HERE") # PUT UR DIRECTORY HERE

        Launchers = []
        Directory = os.getcwd()

        RunSelectAndPrintInDir("game launcher", Launchers)

        Chosen_Launcher = int(input("\n"))
        OpenChosenIndexInDir(Chosen_Launcher, Launchers, Directory)

    elif FirstDir == 3:
        os.chdir(r"DIRECTORY1_PATH_HERE") # PUT UR DIRECTORY HERE

        IDEs = []
        Directory = os.getcwd()

        RunSelectAndPrintInDir("IDE", IDEs)

        Chosen_IDE = int(input("\n"))
        OpenChosenIndexInDir(Chosen_IDE, IDEs, Directory)

    elif FirstDir == 4:
        os.chdir(r"DIRECTORY1_PATH_HERE") # PUT UR DIRECTORY HERE

        Other_Apps = []
        Direct = os.getcwd()

        RunSelectAndPrintInDir("application", Other_Apps)

        Chosen_APP = int(input("\n"))
        OpenChosenIndexInDir(Chosen_APP, Other_Apps, Direct)

    elif FirstDir == 5:
        os.chdir(r"DIRECTORY1_PATH_HERE") # PUT UR DIRECTORY HERE

        VMS = []
        Direct = os.getcwd()
        RunSelectAndPrintInDir("virutal machine", VMS)

        Chosen_VM = int(input("\n"))
        OpenChosenIndexInDir(Chosen_VM, VMS, Direct)

    elif FirstDir == 6:
        print("\nChoose a webpage!")

        with open(r"PUT_THE_PATH_TO_UR_TXT_FILE_CONTAINING_UR_WEBSITES") as file: # PUT A PATH TO A TXT FILE CONTAINING WEBSITES U WANT TO VISIT
            index = 1
            tbl = []

            for website in file:
                website = website.strip()
                new_index = str(index) + ". "
                print(new_index, website)

                tbl.append(website)
                index += 1

            Chosen_Webpage = int(input("\n"))

            for site in tbl:
                if tbl.index(site) == Chosen_Webpage - 1:
                    os.system(f"start {tbl[(Chosen_Webpage or site) - 1]}")
                    print(f"Opening page: {tbl[(Chosen_Webpage or site) - 1]}")



    Re_Run = str(input("\nWould u like to go again? Type 'Y' or 'N'\n")).lower()
    
    if Re_Run[0] == "y":
        os.system("cls")
    else:
        isRunning = False

