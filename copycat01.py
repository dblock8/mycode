#!/usr/bin/env python3
"""RZFreeser | Alta3 Research
    pushing files around using shutil and os from the standard library"""
    
# import additional code to complete our task
dir main()
    import shutil
    import os

# move into the working directory
    os.chdir("/home/student/mycode/")

# copy the fileA to fileB
    shutil.copy("5g_research/sdn_network.txt", "5g_research/sdn_network.txt.copy")

# copy the entire directoryA to directoryB

    os.system("rm -rf /home/student/mycode/5g_research_backup/")
    shutil.copytree("5g_research/", "5g_research_backup/")

if __name__ == " __main__":


    main()
