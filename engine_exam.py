# This is the worst code you will ever see. I did this with basically zero knowledge of python and only some HTML knowledge. Good luck.
# A lot of this is only working based in luck and random redundancies.
import random
again = "Y"
start = "Y"
state_id = "Y"
correct = 0
while start == "Y":
    start = input("Would you like to (s)tart or read the (i)nstructions? ")
    if start.lower().strip() == "instructions" or start.lower().strip() == "i":
        print("\033c")
        print("You will get a randomly generated question from the 2023 Hot Rodders of Tomorrow Dual National Championship Test Study Guide.\n"
        "When you get your question, all you need to do is type your answer as either the letter (i.e. 'a') or as the words (i.e. 'Push Rod').\n"
        "The system shouldn't be case sensitive so you don't need to worry about capitalization but you will need to worry about spelling.\n"
        "I have made the executive decision to remove periods unless there are multiple sentences in each answer so that there is less of a chance to get a false negative.\n"
        "However, make sure to type either only the letter or word.\n"
        "The test guide has spelling errors in it which I have decided to include into this program.\n"
        "Everything else should be intuitive so have fun studying!\n"
        "If you have any issues, email me at xxxxxxxxxxxxxxx and I will respond eventually.\n")
        start = "Y"
    elif start.lower().strip() == "start" or start.lower().strip() == "s":
        print("\nStarting...")
        while state_id == "Y":
            print("Would you like to have the questions stay on the screen or dissapear after you continue?\n")
            state = input("(S)tay/(D)issapear: ")
            if state.lower().strip() == "d" or state.lower().strip() == "dissapear":
                state == "d"
                state_id == "d"
                break
            elif state.lower().strip() == "s" or state.lower().strip() == "stay":
                state_id == "s"
                break
            else: 
                print("Please select (s)tay or (d)issapear.")
        break
    else:
        print("Please enter either 'start' or 'instructions'. (S or I also work.)")
        start = "Y"
print("\033c")
while again == "Y" or "y":
    if state == "d":
        print("\033c")
    rand_int = random.randint(1,173)
    print(f"\nHere is question #{rand_int}:\n")
# Questions 1 through 14, any driopped component that hits the floor, tool pan, or tray will be considered a dropped penalty.
    if rand_int == 1:
        print("Which dropped component will be a 15 second penalty?\n a) Push Rod\n b) Cylinder Head Gasket\n c) Head Fastener(s) (wiped & reoiled)\n d) Lifter\n")
        ans = input("What is your answer? ")
        if ans.lower().strip() == "a" or ans.lower().strip() == "push rod":
            print("\nCorrect!"); correct += 1
        else:
            print("\nSorry! The correct answer was Push Rod.")
    elif rand_int == 2:
        print("Which dropped component will be a 2 minute penalty?\n a) Cylinder Head Gasket\n b) Air Cleaner\n c) Lifter\n d) Water Pump\n")
        ans = input("What is your answer? ")
        if ans.lower().strip() == "b" or ans.lower().strip() == "air cleaner":
            print("\nCorrect!"); correct += 1
        else:
            print("\nSorry! The correct answer was Air Cleaner.")
    elif rand_int == 3:
        print("Which dropped component wil NOT be a 2 minute penalty?\n a) Timing Chain and/or Timing Gear\n b) Valve Cover\n c) Spark Plug\n Timing Cover\n")
        ans = input("What is your answer? ")
        if ans.lower().strip() == "timing chain and/or timing gear" or ans.lower().strip() == "a":
            print("\nCorrect!"); correct += 1
        else:
            print("\nSorry! The correct answer was Timing Chain and/or Timing Gear.")
    elif rand_int == 4:
        print("Which dropped component will be a 5 minute penalty?\n a) Valve Cover\n b) Oil Pan\n c) Distibutor\n d) Timing Chain Cover\n")
        ans = input("What is your answer? ")
        if ans.lower().strip() == "distributor" or ans.lower().strip() == "c":
            print("\nCorrect!"); correct += 1
        else:
            print("\nSorry! The correct answer was Distributor.")
    elif rand_int == 5:
        print("Which dropped component will be a 10 minute penalty?\n a) Cylinder Head\n b) Exhaust Header\n c) Distibutor\n d) Oil Pump\n")
        ans = input("What is your answer? ")
        if ans.lower().strip() == "cylinder head" or ans.lower().strip() == "a":
            print("\nCorrect!"); correct += 1
        else:
            print("\nSorry! The correct answer was Cylinder Head.")
    elif rand_int == 6:
        print("Which dropped component will be a 5 minute penalty?\n a) Rocker Arm\n b) Oil Pan\n c) Rod Bearing Half\n d) Intake Manifold\n")
        ans = input("What is your answer? ")
        if ans.lower().strip() == "intake manifold" or ans.lower().strip() == "d":
            print("\nCorrect!"); correct += 1
        else:
            print("\nSorry! The correct answer was Intake Manifold.")
    elif rand_int == 7:
        print("Which dropped component will be a 5 minute penalty?\n a) Oil Pan\n b) Cylinder Head\n c) Air Cleaner\n d) Exhaust Header\n")
        ans = input("What is your answer? ")
        if ans.lower().strip() == "exhaust header" or ans.lower().strip() == "d":
            print("\nCorrect!"); correct += 1
        else:
            print("\nSorry! The correct answer was Exhaust Header.")
    elif rand_int == 8:
        print("Which dropped component will be a 1 minute penalty?\n a) Rod Bearing Half\n b) Oil Pump Nut\n c) Cylinder Head Gasket\n d) Oil Filter\n")
        ans = input("What is your answer? ")
        if ans.lower().strip() == "cylinder head gasket" or ans.lower().strip() == "c":
            print("\nCorrect!"); correct += 1
        else:
            print("\nSorry! The correct answer was Cylinder Head Gasket.")
    elif rand_int == 9:
        print("Which dropped component will be a 15 second penalty?\n a) Camshaft Bolts\n b) Lifter Bars\n c) Spark Plug\n d) Oil Filter\n")
        ans = input("What is your answer? ")
        if ans.lower().strip() == "d" or ans.lower().strip() == "oil filter":
            print("\nCorrect!"); correct += 1
        else:
            print("\nSorry! The correct answer was Oil Filter.")
    elif rand_int == 10:
        print("If a Valve Cover T-Handle is dropped during competition, what will be the penalty time for each occurence?\n a) 15 seconds\n b) 1 minute\n c) 2 minutes\n d) Not a penalty\n")
        ans = input("What is your answer? ")
        if ans.lower().strip() == "a" or ans.lower().strip() == "15 seconds":
            print("\nCorrect!"); correct += 1
        else:
            print("\nSorry! The correct answer was 15 seconds.")
    elif rand_int == 11:
        print("If a Distributor Cap is dropped during competition, what will be the penalty time for each occurence?\n a) 2 minutes\n b) 5 minutes\n c) 10 minutes\n d) 15 minutes\n")
        ans = input("What is your answer? ")
        if ans.lower().strip() == "a" or ans.lower().strip() == "2 minutes":
            print("\nCorrect!"); correct += 1
        else:
            print("\nSorry! The correct answer was 2 minutes.")
    elif rand_int == 12:
        print("If a Water Pump is dropped during competition, what will be the penalty time for each occurence?\n a) 30 seconds\n b) 1 minute\n c) 2 minutes\n d) 5 minutes\n")
        ans = input("What is your answer? ")
        if ans.lower().strip() == "d" or ans.lower().strip() == "5 minutes":
            print("\nCorrect!"); correct += 1
        else:
            print("\nSorry! The correct answer was 5 minutes.")
    elif rand_int == 13:
        print("If an Oil Pump Drive is dropped during competition, what will be the penalty time for each occurence?\n a) 15 seconds\n b) 1 minute\n c) 2 minutes\n d) 5 minutes\n")
        ans = input("What is your answer? ")
        if ans.lower().strip() == "a" or ans.lower().strip() == "15 seconds":
            print("\nCorrect!"); correct += 1
        else:
            print("\nSorry! The correct answer was 15 seconds.")
    elif rand_int == 14:
        print("If a Spark Plug is dropped during competition, what will be the penalty time for each occurence?\n a) 30 seconds\n b) 1 minute\n c) 2 minutes\n d) 3 minutes\n")
        ans = input("What is your answer? ")
        if ans.lower().strip() == "c" or ans.lower().strip() == "2 minutes":
            print("\nCorrect!"); correct += 1
        else:
            print("\nSorry! The correct answer was 2 minutes.")
# Questions 15 through 66 are either True or False.
    elif rand_int == 15:
        print("Brake cleaners and carb cleaners are banned. Only Non-Toxic cleaners that are approved in writing by Rodney Bingham may be used.\n a) True\n b) False\n")
        ans = input("What is your answer? ")
        if ans.lower().strip() == "a" or ans.lower().strip() == "true":
            print("\nCorrect!"); correct += 1
        else:
            print("\nSorry! The correct answer was True.")
    elif rand_int == 16:
        print("When de-torqueing the oil pump nut, a pry bar is NOT necessary.\n a) True\n b) False\n")
        ans = input("What is your answer? ")
        if ans.lower().strip() == "b" or ans.lower().strip() == "false":
            print("\nCorrect!"); correct += 1
        else:
            print("\nSorry! The correct answer was False.")
    elif rand_int == 17:
        print("Tools, components, or fasteners may be placed in mouth.\n a) True\n b) False\n")
        ans = input("What is your answer? ")
        if ans.lower().strip() == "b" or ans.lower().strip() == "false":
            print("\nCorrect!"); correct += 1
        else:
            print("\nSorry! The correct answer was False.")
    elif rand_int == 18:
        print("ALL fasteners and washers must be removed from all component except cylinder heads center washer.\n a) True\n b) False\n")
        ans = input("What is your answer? ")
        if ans.lower().strip() == "a" or ans.lower().strip() == "True":
            print("\nCorrect!"); correct += 1
        else:
            print("\nSorry! The correct answer was True.")
    elif rand_int == 19:
        print("During the disassembly phase, multiple rod caps may be loosened and/or removed at a single time.\n a) True\n b) False\n")
        ans = input("What is your answer? ")
        if ans.lower().strip() == "b" or ans.lower().strip() == "False":
            print("\nCorrect!"); correct += 1
        else:
            print("\nSorry! The correct answer was False.")
    elif rand_int == 20:
        print("Header gaskets must be removed from the engine and placed on the bench.\n a) True\n b) False\n")
        ans = input("What is your answer? ")
        if ans.lower().strip() == "a" or ans.lower().strip() == "true":
            print("\nCorrect!"); correct += 1
        else:
            print("\nSorry! The correct answer was True.")
    elif rand_int == 21:
        print("Valve cover gaskets must be removed from the engine and placed on the bench.\n a) True\n b) False\n")
        ans = input("What is your answer? ")
        if ans.lower().strip() == "b" or ans.lower().strip() == "false":
            print("\nCorrect!"); correct += 1
        else:
            print("\nSorry! The correct answer was False.")
    elif rand_int == 22:
        print("Water pump gasket must be removed from the engine and place don the bench.\n a) True\n b) False\n")
        ans = input("What is your answer? ")
        if ans.lower().strip() == "b" or ans.lower().strip() == "false":
            print("\nCorrect!"); correct += 1
        else:
            print("\nSorry! The correct answer was False.")
    elif rand_int == 23:
        print("Timing chain cover gasket must NOT be removed from the engine an placed on the bench.\n a) True\n b) False\n")
        ans = input("What is your answer? ")
        if ans.lower().strip() == "a" or ans.lower().strip() == "true":
            print("\nCorrect!"); correct += 1
        else:
            print("\nSorry! The correct answer was True.")
    elif rand_int == 24:
        print("Cylinder head bolts are NOT required to be oiled at the bench.\n a) True\n b) False\n")
        ans = input("What is your answer? ")
        if ans.lower().strip() == "b" or ans.lower().strip() == "false":
            print("\nCorrect!"); correct += 1
        else:
            print("\nSorry! The correct answer was False.")
    elif rand_int == 25:
        print("Oil filter gasket must be oiled at the bench.\n a) True\n b) False\n")
        ans = input("What is your answer? ")
        if ans.lower().strip() == "a" or ans.lower().strip() == "true":
            print("\nCorrect!"); correct += 1
        else:
            print("\nSorry! The correct answer was True.")
    elif rand_int == 26:
        print("Only one piston and rod assembly are to be installed at a time.\n a) True\n b) False\n")
        ans = input("What is your answer? ")
        if ans.lower().strip() == "a" or ans.lower().strip() == "true":
            print("\nCorrect!"); correct += 1
        else:
            print("\nSorry! The correct answer was True.")
    elif rand_int == 27:
        print("Lifter guides may NOT be installed until ALL lifters have been installed.\n a) True\n b) False\n")
        ans = input("What is your answer? ")
        if ans.lower().strip() == "a" or ans.lower().strip() == "true":
            print("\nCorrect!"); correct += 1
        else:
            print("\nSorry! The correct answer was True.")
    elif rand_int == 28:
        print("With the number one piston at Top Dead Center on compression stroke, intake valve #1 is adjusted.\n a) True\n b) False\n")
        ans = input("What is your answer? ")
        if ans.lower().strip() == "a" or ans.lower().strip() == "true":
            print("\nCorrect!"); correct += 1
        else:
            print("\nSorry! The correct answer was False.")
    elif rand_int == 29:
        print("When a rod cap with bearing is dropped, it does NOT need to be wiped and re-oiled at the bench.\n a) True\n b) False\n")
        ans = input("What is your answer? ")
        if ans.lower().strip() == "b" or ans.lower().strip() == "false":
            print("\nCorrect!"); correct += 1
        else:
            print("\nSorry! The correct answer was False.")
    elif rand_int == 30:
        print("Any dropped component that hits the floor, tool pan, or tray will be considered a dropped item. A dropped Timing Cover will NOT be a 2 minute penalty?\n a) True\n b) False\n")
        ans = input("What is your answer? ")
        if ans.lower().strip() == "b" or ans.lower().strip() == "False":
            print("\nCorrect!"); correct += 1
        else:
            print("\nSorry! The correct answer was False.")
    elif rand_int == 31:
        print("Any dropped component that hits the floor, tool pan, or tray will be considered a dropped item.\n a) True\n b) False\n")
        ans = input("What is your answer? ")
        if ans.lower().strip() == "a" or ans.lower().strip() == "true":
            print("\nCorrect!"); correct += 1
        else:
            print("\nSorry! The correct answer was True.")
    elif rand_int == 32:
        print("Stripped spark plug holes will be a 15 minute penalty.\n a) True\n b) False\n")
        ans = input("What is your answer? ")
        if ans.lower().strip() == "a" or ans.lower().strip() == "true":
            print("\nCorrect!"); correct += 1
        else:
            print("\nSorry! The correct answer was True.")
    elif rand_int == 33:
        print("Broken piston rings will be a 5 minute penalty.\n a) True\n b) False\n")
        ans = input("What is your answer? ")
        if ans.lower().strip() == "a" or ans.lower().strip() == "true":
            print("\nCorrect!"); correct += 1
        else:
            print("\nSorry! The correct answer was True.")
    elif rand_int == 34:
        print("During the assembly phase, the oil filter is torqued at 100 in/lbs.\n a) True\n b) False\n")
        ans = input("What is your answer? ")
        if ans.lower().strip() == "b" or ans.lower().strip() == "false":
            print("\nCorrect!"); correct += 1
        else:
            print("\nSorry! The correct answer was False.")
    elif rand_int == 35:
        print("When removing the piston and rod assembly, rod bolt protectors must be used.\n a) True\n b) False\n")
        ans = input("What is your answer? ")
        if ans.lower().strip() == "a" or ans.lower().strip() == "true":
            print("\nCorrect!"); correct += 1
        else:
            print("\nSorry! The correct answer was True.")
    elif rand_int == 36:
        print("A torque wrench may be used as a breaker bar.\n a) True\n b) False\n")
        ans = input("What is your answer? ")
        if ans.lower().strip() == "b" or ans.lower().strip() == "false":
            print("\nCorrect!"); correct += 1
        else:
            print("\nSorry! The correct answer was False.")
    elif rand_int == 37:
        print("Headers must be torqued hand tight outside-in with a 3/8 in wrench.\n a) True\n b) False\n")
        ans = input("What is your answer? ")
        if ans.lower().strip() == "b" or ans.lower().strip() == "false":
            print("\nCorrect!"); correct += 1
        else:
            print("\nSorry! The correct answer was False.")
    elif rand_int == 38:
        print("Distributor hold-down must be torqued hand tight with a 9/16 in wrench.\n a) True\n b) False\n")
        ans = input("What is your answer? ")
        if ans.lower().strip() == "a" or ans.lower().strip() == "true":
            print("\nCorrect!"); correct += 1
        else:
            print("\nSorry! The correct answer was True.")
    elif rand_int == 39:
        print("Cam gear must be torqued 100 in/lbs with a clockwise pattern.\n a) True\n b) False\n")
        ans = input("What is your answer? ")
        if ans.lower().strip() == "b" or ans.lower().strip() == "false":
            print("\nCorrect!"); correct += 1
        else:
            print("\nSorry! The correct answer was False.")
    elif rand_int == 40:
        print("Harmonic balancer must be torqued 50 ft/lbs with a torque stick.\n a) True\n b) False\n")
        ans = input("What is your answer? ")
        if ans.lower().strip() == "b" or ans.lower().strip() == "false":
            print("\nCorrect!"); correct += 1
        else:
            print("\nSorry! The correct answer was False.")
    elif rand_int == 41:
        print("Intake manifold must be torqued hand tight with a 3/8 in wrench.\n a) True\n b) False\n")
        ans = input("What is your answer? ")
        if ans.lower().strip() == "a" or ans.lower().strip() == "true":
            print("\nCorrect!"); correct += 1
        else:
            print("\nSorry! The correct answer was True.")
    elif rand_int == 42:
        print("Piston rod assembly must be torqued 15 ft/lbs then 35 ft/lbs.\n a) True\n b) False\n")
        ans = input("What is your answer? ")
        if ans.lower().strip() == "b" or ans.lower().strip() == "false":
            print("\nCorrect!"); correct += 1
        else:
            print("\nSorry! The correct answer was False.")
    elif rand_int == 43:
        print("Oil filter is torqued hand tight.\n a) True\n b) False\n")
        ans = input("What is your answer? ")
        if ans.lower().strip() == "a" or ans.lower().strip() == "true":
            print("\nCorrect!"); correct += 1
        else:
            print("\nSorry! The correct answer was True.")
    elif rand_int == 44:
        print("Speed Sleeves do NOT require a piston installer.\n a) True\n b) False\n")
        ans = input("What is your answer? ")
        if ans.lower().strip() == "a" or ans.lower().strip() == "true":
            print("\nCorrect!"); correct += 1
        else:
            print("\nSorry! The correct answer was True.")
    elif rand_int == 45:
        print("All tools and trays must be placed on the bench at the start of the competition, at the end of disassembly phase, and at the end of assembly phase.\n a) True\n b) False\n")
        ans = input("What is your answer? ")
        if ans.lower().strip() == "a" or ans.lower().strip() == "true":
            print("\nCorrect!"); correct += 1
        else:
            print("\nSorry! The correct answer was True.")
    elif rand_int == 46:
        print("Band and Plier style ring compressors only do NOT require a piston installer.\n a) True\n b) False\n")
        ans = input("What is your answer? ")
        if ans.lower().strip() == "b" or ans.lower().strip() == "false":
            print("\nCorrect!"); correct += 1
        else:
            print("\nSorry! The correct answer was False.")
    elif rand_int == 47:
        print("Rod Bearing Halves, Oil Filter gasket, Rocker arm pivot balls, and Pushrod seats are the components that must be lubricated and called out to the judge's attention.\n a) True\n b) False\n")
        ans = input("What is your answer? ")
        if ans.lower().strip() == "a" or ans.lower().strip() == "true":
            print("\nCorrect!"); correct += 1
        else:
            print("\nSorry! The correct answer was True.")
    elif rand_int == 48:
        print("Distributor MUST only be in place before oil pan has been installed.\n a) True\n b) False\n")
        ans = input("What is your answer? ")
        if ans.lower().strip() == "b" or ans.lower().strip() == "false":
            print("\nCorrect!"); correct += 1
        else:
            print("\nSorry! The correct answer was False.")
    elif rand_int == 49:
        print("Cylinder head fastener(s) must be wiped and re-oiled at the bench after it has been dropped.\n a) True\n b) False\n")
        ans = input("What is your answer? ")
        if ans.lower().strip() == "a" or ans.lower().strip() == "true":
            print("\nCorrect!"); correct += 1
        else:
            print("\nSorry! The correct answer was True.")
    elif rand_int == 50:
        print("Tempering and annealing are ways to harden or soften metal.\n a) True\n b) False\n")
        ans = input("What is your answer? ")
        if ans.lower().strip() == "a" or ans.lower().strip() == "true":
            print("\nCorrect!"); correct += 1
        else:
            print("\nSorry! The correct answer was True.")
    elif rand_int == 51:
        print("Most aluminum heads require valve guide inserts to support valve stem.\n a) True\n b) False\n")
        ans = input("What is your answer? ")
        if ans.lower().strip() == "a" or ans.lower().strip() == "true":
            print("\nCorrect!"); correct += 1
        else:
            print("\nSorry! The correct answer was True.")
    elif rand_int == 52:
        print("When the Check Engine Light comes on a vehicle's dashboard, it means the engine is too old and needs replaced.\n a) True\n b) False\n")
        ans = input("What is your answer? ")
        if ans.lower().strip() == "b" or ans.lower().strip() == "false":
            print("\nCorrect!"); correct += 1
        else:
            print("\nSorry! The correct answer was False.")
    elif rand_int == 53:
        print("The vehicle's air filter cleans the air for the engine.\n a) True\n b) False\n")
        ans = input("What is your answer? ")
        if ans.lower().strip() == "a" or ans.lower().strip() == "true":
            print("\nCorrect!"); correct += 1
        else:
            print("\nSorry! The correct answer was True.")
    elif rand_int == 54:
        print("Most vehicles' exhaust system consists of the following items: exhaust manifold, exhaust pipe, catalytic converter, muffler and tail pipe.\n a) True\n b) False\n")
        ans = input("What is your answer? ")
        if ans.lower().strip() == "a" or ans.lower().strip() == "true":
            print("\nCorrect!"); correct += 1
        else:
            print("\nSorry! The correct answer was True.")
    elif rand_int == 55:
        print("Radiators are heat exchangers to keep the engine cool by circulating engine coolant through the engine block.\n a) True\n b) False\n")
        ans = input("What is your answer? ")
        if ans.lower().strip() == "a" or ans.lower().strip() == "true":
            print("\nCorrect!"); correct += 1
        else:
            print("\nSorry! The correct answer was True.")
    elif rand_int == 56:
        print("On October 1, 1908, the first production Model T Ford is completed at the company's Piquette Avenue plant in Detroit.\n a) True\n b) False\n")
        ans = input("What is your answer? ")
        if ans.lower().strip() == "a" or ans.lower().strip() == "true":
            print("\nCorrect!"); correct += 1
        else:
            print("\nSorry! The correct answer was True.")
    elif rand_int == 57:
        print("Henry Ford and William Durant founded the Chevrolet Motor Company.\n a) True\n b) False\n")
        ans = input("What is your answer? ")
        if ans.lower().strip() == "b" or ans.lower().strip() == "false":
            print("\nCorrect!"); correct += 1
        else:
            print("\nSorry! The correct answer was False.")
    elif rand_int == 58:
        print("The surface on the crankshaft which rests in the block is called main journal.\n a) True\n b) False\n")
        ans = input("What is your answer? ")
        if ans.lower().strip() == "a" or ans.lower().strip() == "true":
            print("\nCorrect!"); correct += 1
        else:
            print("\nSorry! The correct answer was True.")
    elif rand_int == 59:
        print("VIN stands for Vehicle Identification Number.\n a) True\n b) False\n")
        ans = input("What is your answer? ")
        if ans.lower().strip() == "a" or ans.lower().strip() == "true":
            print("\nCorrect!"); correct += 1
        else:
            print("\nSorry! The correct answer was True.")
    elif rand_int == 60:
        print("ICM stands for Ignition Control Module.\n a) True\n b) False\n")
        ans = input("What is your answer? ")
        if ans.lower().strip() == "a" or ans.lower().strip() == "true":
            print("\nCorrect!"); correct += 1
        else:
            print("\nSorry! The correct answer was True.")
    elif rand_int == 61:
        print("SEMA stands for Special Equipment Market Assistance.\n a) True\n b) False\n")
        ans = input("What is your answer? ")
        if ans.lower().strip() == "b" or ans.lower().strip() == "false":
            print("\nCorrect!"); correct += 1
        else:
            print("\nSorry! The correct answer was False.")
    elif rand_int == 62:
        print("ECM stands for Engine Control Mpoule.\n a) True\n b) False\n")
        ans = input("What is your answer? ")
        if ans.lower().strip() == "a" or ans.lower().strip() == "true":
            print("\nCorrect!"); correct += 1
        else:
            print("\nSorry! The correct answer was True.")
    elif rand_int == 63:
        print("TDC does not stand for Top Dead Center.\n a) True\n b) False\n")
        ans = input("What is your answer? ")
        if ans.lower().strip() == "b" or ans.lower().strip() == "false":
            print("\nCorrect!"); correct += 1
        else:
            print("\nSorry! The correct answer was False.")
    elif rand_int == 64:
        print("PRI stands for Performance Racing Industry.\n a) True\n b) False\n")
        ans = input("What is your answer? ")
        if ans.lower().strip() == "a" or ans.lower().strip() == "true":
            print("\nCorrect!"); correct += 1
        else:
            print("\nSorry! The correct answer was True.")
    elif rand_int == 65:
        print("FPR stands for Fuel Pump Regulator.\n a) True\n b) False\n")
        ans = input("What is your answer? ")
        if ans.lower().strip() == "a" or ans.lower().strip() == "true":
            print("\nCorrect!"); correct += 1
        else:
            print("\nSorry! The correct answer was True.")
    elif rand_int == 66:
        print("The main purpose for having a harmonic balancer is to absorb the vibration from the combustion.\n a) True\n b) False\n")
        ans = input("What is your answer? ")
        if ans.lower().strip() == "a" or ans.lower().strip() == "true":
            print("\nCorrect!"); correct += 1
        else:
            print("\nSorry! The correct answer was True.")
# Questions 67 through 77 will be automotive acronyms.
    elif rand_int == 67:
        print("What does ABS stand for?\n a) Anti-Backfire System\n b) All Brake System\n c) Anti-lock Brake System\n d) Alternator Body Sensor\n")
        ans = input("What is your answer? ")
        if ans.lower().strip() == "c" or ans.lower().strip() == "anti-lock brake system":
            print("\nCorrect!"); correct += 1
        else:
            print("\nSorry! The correct answer was Anti-lock Brake System.")
    elif rand_int == 68:
        print("What does ASE satnd for?\n a) Automotive Service Education\n b) Automotive Service Excellence\n c) Automatic Sensor Equipment\n d) American Service Excellence\n")
        ans = input("What is your answer? ")
        if ans.lower().strip() == "b" or ans.lower().strip() == "automotive service excellence":
            print("\nCorrect!"); correct += 1
        else:
            print("\nSorry! The correct answer was Automotive Service Excellence.")
    elif rand_int == 69:
        print("What does BCM stand for?\n a) Body Connector Mass\n b) Brake Control Module\n c) Beyond Capability of Maintenance\n d) Body Control Module\n")
        ans = input("What is your answer? ")
        if ans.lower().strip() == "d" or ans.lower().strip() == "body control module":
            print("\nCorrect!"); correct += 1
        else:
            print("\nSorry! The correct answer was Body Control Module.")
    elif rand_int == 70:
        print("What does TPS stand for?\n a) Throttle Position Sensor\n b) Technical Program System\n c) Torque Pistons to Specification\n d) Throttle Position System\n")
        ans = input("What is your answer? ")
        if ans.lower().strip() == "a" or ans.lower().strip() == "throttle position sensor":
            print("\nCorrect!"); correct += 1
        else:
            print("\nSorry! The correct answer was Throttle Position Sensor.")
    elif rand_int == 71:
        print("What does SEMA stand for?\n a) Specialized Engine Machining Authority\n b) Squirrels Eat My Acorns\n c) Supercharged Engine Management Advisory\n d) Specialty Equipment Marketing Association.\n")
        ans = input("What is your answer? ")
        if ans.lower().strip() == "d" or ans.lower().strip() == "specialty equipment marketing association":
            print("\nCorrect!"); correct += 1
        else:
            print("\nSorry! The correct answer was Specialty Equipment Marketing Association.")
    elif rand_int == 72:
        print("What does WOT stand for?\n a) Weapons Operation Training\n b) Weight On Transmission\n c) Wide Open Throttle\n d) Width Of Throttle\n")
        ans = input("What is your answer? ")
        if ans.lower().strip() == "c" or ans.lower().strip() == "wide open throttle":
            print("\nCorrect!"); correct += 1
        else:
            print("\nSorry! The correct answer was Wide Open Throttle.")
    elif rand_int == 73:
        print("What does DLC stand for?\n a) Digital Link Converter\n b) Data Link Connector\n c) Data Length Convertor\n d) Data Link Convertor\n")
        ans = input("What is your answer? ")
        if ans.lower().strip() == "b" or ans.lower().strip() == "data link connector":
            print("\nCorrect!"); correct += 1
        else:
            print("\nSorry! The correct answer was Data Link Connector.")
    elif rand_int == 74:
        print("What Does MAF stand for?\n a) Muffler Air Filter\n b) Manifold Air Flow\n c) Market Automotive Foundation\n d) Mass Airflow\n")
        ans = input("What is your answer? ")
        if ans.lower().strip() == "d" or ans.lower().strip() == "mass airflow":
            print("\nCorrect!"); correct += 1
        else:
            print("\nSorry! The correct answer was Mass Airflow.")
    elif rand_int == 75:
        print("What does DVOM stand for?\n a) Digital Volt-Ohmmeter\n b) Digital Viscosity Meter\n c) Data Volt Ohm Meter\n d) Digital Volt Ohm Module\n")
        ans = input("What is your answer? ")
        if ans.lower().strip() == "a" or ans.lower().strip() == "digital volt-ohmmeter":
            print("\nCorrect!"); correct += 1
        else:
            print("\nSorry! The correct answer was Digital Volt-Ohmmeter.")
    elif rand_int == 76:
        print("What does GND stand for?\n a) General Notes Dated\n b) Ground\n c) General Data\n d) None of the above\n")
        ans = input("What is your answer? ")
        if ans.lower().strip() == "b" or ans.lower().strip() == "ground":
            print("\nCorrect!"); correct += 1
        else:
            print("\nSorry! The correct answer was Ground.")
    elif rand_int == 77:
        print("What does PCV stand for?\n a) Permanent Virtual Current\n b) Poly Vinyl Color\n c) Premature Ventilation Current\n d) Positive Crankcase Ventilation\n")
        ans = input("What is your answer? ")
        if ans.lower().strip() == "d" or ans.lower().strip() == "positive crankcase ventilation":
            print("\nCorrect!"); correct += 1
        else:
            print("\nSorry! The correct answer was Positive Crankcase Ventilation.")
#Questions 78 through 92 will have torque specifications. Please select the correct amount of torque.
    elif rand_int == 78:
        print("There is a two-step torque sequence for the Cylinder Heads fasteners. What are the correct amounts?\n a) 15 ft/lbs and 30 ft/lbs\n b) 25 ft/lbs and 40 ft/lbs\n c) 25 ft/lbs and 50 ft/lbs\n d) 25 in/lbs and 50 in/lbs\n")
        ans = input("What is your answer? ")
        if ans.lower().strip() == "c" or ans.lower().strip() == "25 ft/lbs and 50 ft/lbs":
            print("\nCorrect!"); correct += 1
        else:
            print("\nSorry! The correct answer was 25 ft/lbs and 50 ft/lbs.")
    elif rand_int == 79:
        print("There will be a two-step torque sequence for Rod Nuts, what is the correct amount?\n a) 10 ft/lbs and 20 ft/lbs\n b) 15 ft/lbs and 25 ft/lbs\n c) 15 ft/lbs and 30 ft/lbs\n d) 10 ft/lbs and 35 ft/lbs\n")
        ans = input("What is your answer? ")
        if ans.lower().strip() == "c" or ans.lower().strip() == "15 ft/lbs and 30 ft/lbs":
            print("\nCorrect!"); correct += 1
        else:
            print("\nSorry! The correct answer was 15 ft/lbs and 30 ft/lbs.")
    elif rand_int == 80:
        print("There is a one-step toque sequence for the Cam Gear bolts. What is the correct amount?\n a) 100 in/lbs\n b) 15 ft/lbs\n c) Hand Tight\n d) 100 ft/lbs\n")
        ans = input("What is your answer? ")
        if ans.lower().strip() == "a" or ans.lower().strip() == "100 in/lbs":
            print("\nCorrect!"); correct += 1
        else:
            print("\nSorry! The correct answer was 100 in/lbs.")
    elif rand_int == 81:
        print("There is a one-step torque sequence for the Oil Pump. What is the correct amount?\n a) 50 in/lbs\n b) 50 ft/lbs\n c) 75 in/lbs\n d) 100 in/lbs\n")
        ans = input("What is your answer? ")
        if ans.lower().strip() == "b" or ans.lower().strip() == "50 ft/lbs":
            print("\nCorrect!"); correct += 1
        else:
            print("\nSorry! The correct answer was 50 ft/lbs.")
    elif rand_int == 82:
        print("There is a one-step torque sequence for the Headers bolts. What is the correct amount?\n a) Hand Tight\n b) 100 in/lbs\n c) 50 in/lbs\n d) 15 ft/lbs\n")
        ans = input("What is your answer? ")
        if ans.lower().strip() == "a" or ans.lower().strip() == "hand tight":
            print("\nCorrect!"); correct += 1
        else:
            print("\nSorry! The correct answer was Hand Tight.")
    elif rand_int == 83:
        print("There is a one-step torque sequence for the Valve Cover. What is the correct amount?\n a) 100 in/lbs\n b) 75 in/lbs\n c) 50 in/lbs\n d) Hand Tight\n")
        ans = input("What is your answer? ")
        if ans.lower().strip() == "d" or ans.lower().strip() == "hand tight":
            print("\nCorrect!"); correct += 1
        else:
            print("\nSorry! The correct answer was Hand Tight.")
    elif rand_int == 84:
        print("There is a one-step torque sequence for the Spark Plugs. What is the correct amount?\n a) Hand Tight\n b) 50 in/lbs\n c) 75 in/lbs\n d) 100 in/lbs\n")
        ans = input("What is your answer? ")
        if ans.lower().strip() == "d" or ans.lower().strip() == "100 in/lbs":
            print("\nCorrect!"); correct += 1
        else:
            print("\nSorry! The correct answer was 100 in/lbs.")
    elif rand_int == 85:
        print("There is a one-step torque sequence for the Water Pump bolts. What is the correct amount?\n a) 25 in/lbs\n b) 25 ft/lbs\n c) 50 ft/lbs\n d) 75 ft/lbs\n")
        ans = input("What is your answer? ")
        if ans.lower().strip() == "b" or ans.lower().strip() == "25 ft/lbs":
            print("\nCorrect!"); correct += 1
        else:
            print("\nSorry! The correct answer was 25 ft/lbs.")
    elif rand_int == 86:
        print("There is a one-step torque sequence for the Starter. What is the correct amount?\n a) 15 ft/lbs\n b) 25 in/lbs\n c) 50 in/lbs\n d) 100 in/lbs\n")
        ans = input("What is your answer? ")
        if ans.lower().strip() == "a" or ans.lower().strip() == "15 ft/lbs":
            print("\nCorrect!"); correct += 1
        else:
            print("\nSorry! The correct answer was 15 ft/lbs.")
    elif rand_int == 87:
        print("There is a one-step torque sequence for the Carburetor fasteners. What is the correct amount?\n a) 25 in/lbs\n b) Hand Tight\n c) 75 in/lbs\n d) 50 in/lbs\n")
        ans = input("What is your answer? ")
        if ans.lower().strip() == "b" or ans.lower().strip() == "hand tight":
            print("\nCorrect!"); correct += 1
        else:
            print("\nSorry! The correct answer was Hand Tight.")
    elif rand_int == 88:
        print("There is a one-step torque sequence for the Timing Chain Cover bolts. What is the correct amount?\n a) Hand Tight\n b) 100 in/lbs\n c) 75 in/lbs\n d) 50 in/lbs\n")
        ans = input("What is your answer? ")
        if ans.lower().strip() == "d" or ans.lower().strip() == "50 in/lbs":
            print("\nCorrect!"); correct += 1
        else:
            print("\nSorry! The correct answer was 50 in/lbs.")
    elif rand_int == 89:
        print("The Oil Pan has two different size fasteners. The rail fasteners are 5/16 inch and the corner fasteners are 3/8 inch. There is a one-step torque sequence for the Oil Pan's Corner fastener's (3/8 inch). What is the correct amount?\n a) 25 in/lbs\n b) 50 in /lbs\n c) 75 in/lbs\n d) 100 in/lbs\n")
        ans = input("What is your answer? ")
        if ans.lower().strip() == "c" or ans.lower().strip() == "75 in/lbs":
            print("\nCorrect!"); correct += 1
        else:
            print("\nSorry! The correct answer was 75 in/lbs.")
    elif rand_int == 90:
        print("The Oil Pan has two different size fasteners. The rail fasteners are 5/16 inch and the corner fasteners are 3/8 inch. There is a one-step torque sequence for the Oil Pan's Rail fastener's (5/16 inch). What is the correct amount?\n a) 25 in/lbs\n b) 50 in /lbs\n c) 75 in/lbs\n d) 100 in/lbs\n")
        ans = input("What is your answer? ")
        if ans.lower().strip() == "b" or ans.lower().strip() == "50 in/lbs":
            print("\nCorrect!"); correct += 1
        else:
            print("\nSorry! The correct answer was 50 in/lbs.")
    elif rand_int == 91:
        print("There is a one-step torque sequence for the following items. Which part is NOT torqued hand tight.\n a) Harmonic Balancer Adapter\n b) Distributor Hold-down\n c) Intake Manifold\n d) Oil Filter\n")
        ans = input("What is your answer? ")
        if ans.lower().strip() == "a" or ans.lower().strip() == "harmonic balancer adapter":
            print("\nCorrect!"); correct += 1
        else:
            print("\nSorry! The correct answer was Harmonic Balancer Adapter.")
    elif rand_int == 92:
        print("There is a one-step torque sequence for the Roller Lifter Spider Hold Down bolts. What is the correct amount?\n a) Hand Tight\n b) 25 in/lbs\n c) 50 in/lbs\n d) 100 in/lbs\n")
        ans = input("What is your answer? ")
        if ans.lower().strip() == "d" or ans.lower().strip() == "100 in/lbs":
            print("\nCorrect!"); correct += 1
        else:
            print("\nSorry! The correct answer was 100 in/lbs.")
# Questions 93 through 98 will be on pry bar requirements.
    elif rand_int == 93:
        print("During the Disassembly Phase, when is it required to use a pry bar?\n a) De-torque of rod nuts\n b) De-torque cam gear bolts\n c) Removing pistons\n d) Removing timing chain\n")
        ans = input("What is your answer? ")
        if ans.lower().strip() == "b" or ans.lower().strip() == "de-torque cam gear bolts":
            print("\nCorrect!"); correct += 1
        else:
            print("\nSorry! The correct answer was De-torque cam gear bolts.")
    elif rand_int == 94:
        print("During the assemblt phase, when is NOT required to use a pry bar?\n a) Torque of rod nut\n b) Hand starting and snugging the oil pump nut\n c) Torque of cam gear bolts\n d) Torque of harmonic balancer\n")
        ans = input("What is your answer? ")
        if ans.lower().strip() == "a" or ans.lower().strip() == "torque of rod nuts":
            print("\nCorrect!"); correct += 1
        else:
            print("\nSorry! The correct answer was Torque of rod nuts.")
    elif rand_int == 95:
        print("During the Disassembly Phase, when is it required to use a pry bar?\n a) De-torque/removal of oil pump\n b) De-torque cylinder heads\n c) Removal of lifters\n d) Removal of oil pan\n")
        ans = input("What is your answer? ")
        if ans.lower().strip() == "a" or ans.lower().strip() == "de-torque/removal of oil pump":
            print("\nCorrect!"); correct += 1
        else:
            print("\nSorry! The correct answer was De-torque/removal of oil pump.")
    elif rand_int == 96:
        print("During the Assembly Phase, when is it required to use a pry bar?\n a) Hand start/Snugg of the oil pump nut\n b) Torque of rod nuts\n c) Installing pistons\n d) Installing cylinder heads\n")
        ans = input("What is your answer? ")
        if ans.lower().strip() == "a" or ans.lower().strip() == "hand start/snugg of the oil pump nut":
            print("\nCorrect!"); correct += 1
        else:
            print("\nSorry! The correct answer was Hand start/Snugg of the oil pump nut.")
    elif rand_int == 97:
        print("During the Assembly Phase, when is it required to use a pry bar?\n a) Torque of cylinder heads\n b) Torque of timing chain cover\n c) Torque of oil pan\n d) Torque of cam gear bolts\n")
        ans = input("What is your answer? ")
        if ans.lower().strip() == "d" or ans.lower().strip() == "torque of cam gear bolts":
            print("\nCorrect!"); correct += 1
        else:
            print("\nSorry! The correct answer was Torque of cam gear bolts.")
    elif rand_int == 98:
        print("During the Assembly Phase, when is it NOT required to use a pry bar?\n a) Torque of harmonic balancer bolt\n b) Torque of the oil pump nut\n c) De-Torque of the harmonic balancer bolt\n d) None of the Above\n")
        ans = input("What is your answer? ")
        if ans.lower().strip() == "c" or ans.lower().strip() == "de-torque of the harmonic balancer bolt":
            print("\nCorrect!"); correct += 1
        else:
            print("\nSorry! The correct answer was De-Torque of the harmonic balancer bolt.")
    elif rand_int == 99:
        print("How many fasteners does the Oil Pan have?\n a) 17\n b) 16\n c) 15\n d) 19\n")
        ans = input("What is your answer? ")
        if ans.lower().strip() == "a" or ans.lower().strip() == "17":
            print("\nCorrect!"); correct += 1
        else:
            print("\nSorry! The correct answer was 17.")
    elif rand_int == 100:
        print("How many fasteners does one Cylinder Head have?\n a) 15\n b) 17\n c) 18\n d) 16\n")
        ans = input("What is your answer? ")
        if ans.lower().strip() == "b" or ans.lower().strip() == "17":
            print("\nCorrect!"); correct += 1
        else:
            print("\nSorry! The correct answer was 17.")
    elif rand_int == 101:
        print("How many fasteners does Timing Cover have?\n a) 9\n b) 10\n c) 8\n d) 11\n")
        ans = input("What is your answer? ")
        if ans.lower().strip() == "b" or ans.lower().strip() == "10":
            print("\nCorrect!"); correct += 1
        else:
            print("\nSorry! The correct answer was 10.")
# Questions 102 through 137 will be on the 2023 Hot Rodders of Tomorrow Rulebook. Please answer correctly.
    elif rand_int == 102:
        print("According to the 2023 Hot Rodders of Tomorrow Rule Book, Which tool is NOT approved?\n a) Torque Sticks\n b) Screw Driver\n c) Speed Handle\n d) Wobble Extensions\n")
        ans = input("What is your answer? ")
        if ans.lower().strip() == "a" or ans.lower().strip() == "torque sticks":
            print("\nCorrect!"); correct += 1
        else:
            print("\nSorry! The correct answer was Torque Sticks.")
    elif rand_int == 103:
        print('According to the 2023 Hot Rodders of Tomorrow Rule Book, Which tool is NOT approved?\n a) 12" Breaker Bar\n b) Ratchet Wrench\n c) Speed Handle\n d) Needle Nose Pliers\n')
        ans = input("What is your answer? ")
        if ans.lower().strip() == "b" or ans.lower().strip() == "ratchet wrench":
            print("\nCorrect!"); correct += 1
        else:
            print("\nSorry! The correct answer was Ratchet Wrench.")
    elif rand_int == 104:
        print("According to the 2023 Hot Rodders of Tomorrow Rule Book, Which tool is approved?\n a) Yankee type Screw Drivers\n b) Grip Enhancers\n c) Rolling Carts or Trays\n d) Oppen and combination wrenches\n")
        ans = input("What is your answer? ")
        if ans.lower().strip() == "d" or ans.lower().strip() == "open and combination wrenches":
            print("\nCorrect!"); correct += 1
        else:
            print("\nSorry! The correct answer was Open and combination wrenches.")
    elif rand_int == 105:
        print('According to the 2023 Hot Rodders of Tomorrow Rule Book, Which tool is approved?\n a) T-Bars\n b) Yankee type screw drivers\n c) Magnetic Tray(s)\n d) Spark Plug Socket Longer than 4"')
        ans = input("What is your answer? ")
        if ans.lower().strip() == "c" or ans.lower().strip() == "magnetic tray(s)":
            print("\nCorrect!"); correct += 1
        else:
            print("\nSorry! The correct answer was Magnetic Tray(s).")
    elif rand_int == 106:
        print("Before the engine is completely assembled, the valve train must be properly adjusted. Which component must NOT be installed before beginning the valve adjustment\n a) Valve Covers\n b) Piston and Rod Assembly\n c) Timing Chain and Gears\n d) Cylinder Heads\n")
        ans = input("What is your answer? ")
        if ans.lower().strip() == "a" or ans.lower().strip() == "valve covers":
            print("\nCorrect!"); correct += 1
        else:
            print("\nSorry! The correct answer was Valve Covers.")
    elif rand_int == 107:
        print("Before the engine is completely assembled, the valve train must be properly adjusted. Which component must be installed before beginning the valve adjustment\n a) Intake Manifold\n b) Headers\n c) Spark Plugs\n d) Lifters\n")
        ans = input("What is your answer? ")
        if ans.lower().strip() == "d" or ans.lower().strip() == "lifters":
            print("\nCorrect!"); correct += 1
        else:
            print("\nSorry! The correct answer was Lifters.")
    elif rand_int == 108:
        print("All engine components must be removed separately. Which component will remain on the Cylinder Head?\n a) Lifters\n b) Intake Valves\n c) Rocker Arms\n d) Rocker Arm Nuts\n")
        ans = input("What is your answer? ")
        if ans.lower().strip() == "b" or ans.lower().strip() == "intake valves":
            print("\nCorrect!"); correct += 1
        else:
            print("\nSorry! The correct answer was Intake Valves.")
    elif rand_int == 109:
        print("All engine components must be removed separately. Which component will remain on the Cylinder Head?\n a) Head Bolts\n b) Push Rods\n c) Spark Plugs\n d) Valve Springs\n")
        ans = input("What is your answer? ")
        if ans.lower().strip() == "d" or ans.lower().strip() == "valve springs":
            print("\nCorrect!"); correct += 1
        else:
            print("\nSorry! The correct answer was Valve Springs.")
    elif rand_int == 110:
        print("With the number one piston at Top Dead Center (TDC) on Compression Stroke, which exhaust valve is adjusted?\n a) #1\n b) #2\n c) #5\n d) #6\n")
        ans = input("What is your answer? ")
        if ans.lower().strip() == "a" or ans.lower().strip() == "#1":
            print("\nCorrect!"); correct += 1
        else:
            print("\nSorry! The correct answer was #1.")
    elif rand_int == 111:
        print("With the number one piston at Top Dead Center (TDC) on Compression Stroke, which intake valve is adjusted?\n a) #8\n b) #7\n c) #6\n d) #4\n")
        ans = input("What is your answer? ")
        if ans.lower().strip() == "b" or ans.lower().strip() == "#7":
            print("\nCorrect!"); correct += 1
        else:
            print("\nSorry! The correct answer was #7.")
    elif rand_int == 112:
        print("With the number one piston at Top Dead Center (TDC) on Exhaust Stroke, which intake valve is adjusted?\n a) #1\n b) #2\n c) #3\n d) #5\n")
        ans = input("What is your answer? ")
        if ans.lower().strip() == "c" or ans.lower().strip() == "#3":
            print("\nCorrect!"); correct += 1
        else:
            print("\nSorry! The correct answer was #3.")
    elif rand_int == 113:
        print("With the number one piston at Top Dead Center (TDC) on Compression Stroke, which intake valve is adjusted?\n a) #3\n b) #5\n c) #6\n d) None of the Above\n")
        ans = input("What is your answer? ")
        if ans.lower().strip() == "b" or ans.lower().strip() == "#5":
            print("\nCorrect!"); correct += 1
        else:
            print("\nSorry! The correct answer was #5.")
    elif rand_int == 114:
        print("With the number one piston at Top Dead Center (TDC) on Exhaust Stroke, which exhaust valve is adjusted?\n a) #2\n b) #5\n c) #6\n d) All of the Above\n")
        ans = input("What is your answer? ")
        if ans.lower().strip() == "d" or ans.lower().strip() == "all of the above":
            print("\nCorrect!"); correct += 1
        else:
            print("\nSorry! The correct answer was All of the Above.")
    elif rand_int == 115:
        print("With the number one piston at Top Dead Center (TDC) on Exhaust Stroke, which exhaust valve is adjusted?\n a) #1\n b) #7\n c) #3\n d) #8\n")
        ans = input("What is your answer? ")
        if ans.lower().strip() == "b" or ans.lower().strip() == "#7":
            print("\nCorrect!"); correct += 1
        else:
            print("\nSorry! The correct answer was #7.")
    elif rand_int == 116:
        print("Which fastener can a speed wrench be used on during assembly phase?\n a) Oil Pan Nuts\n b) Valve Cover Fasteners\n c) Rocker Arm Nuts\n d) Water Pump Bolts\n")
        ans = input("What is your answer? ")
        if ans.lower().strip() == "a" or ans.lower().strip() == "oil pan nuts":
            print("\nCorrect!"); correct += 1
        else:
            print("\nSorry! The correct answer was Oil Pan Nuts.")
    elif rand_int == 117:
        print("Which fastener can a speed wrench NOT be used in during the assembly phase?\n a) Rocker Arm Nuts\n b) Timing Cover Bolts\n c) Oil Pan Nuts\n d) Cylinder Head Bolts\n")
        ans = input("What is your answer? ")
        if ans.lower().strip() == "a" or ans.lower().strip() == "rocker arm nuts":
            print("\nCorrect!"); correct += 1
        else:
            print("\nSorry! The correct answer was Rocker Arm Nuts.")
    elif rand_int == 118:
        print("Team members use a torque wrnech to torque cylinder head bolts in the proper sequence. What is the meaning of torque?\n a) Applied twisting force to an object\n b) Tightening the fastener\n c) Scale to measure weight\n d) All of the above\n")
        ans = input("What is your answer? ")
        if ans.lower().strip() == "a" or ans.lower().strip() == "applied twisting force to an object":
            print("\nCorrect!"); correct += 1
        else:
            print("\nSorry! The correct answer was Applied twisting force to an object.")
    elif rand_int == 119:
        print("Why does torque matter?\n a) To ensure that the fastener is snugged\n b) To make sure each fastener is tightened correctly\n c) To make sure the fasteners gets the proper stretch\n d) None of the above\n")
        ans = input("What is your answer? ")
        if ans.lower().strip() == "c" or ans.lower().strip() == "to make sure the fasteners gets the proper stretch":
            print("\nCorrect!"); correct += 1
        else:
            print("\nSorry! The correct answer was To make sure the fasteners gets the proper stretch.")
    elif rand_int == 120:
        print("Why are torque patterns required?\n a) To distribute the gasket evenly to prevent gaps/wrinkles\n b) Torqueing will look neat with the pattern\n c) To make sure every fastener is NOT torqued\n d) Prevent a fastener from cracking\n")
        ans = input("What is your answer? ")
        if ans.lower().strip() == "a" or ans.lower().strip() == "to distrubute the gasket evenly to prvent gaps/wrinkles":
            print("\nCorrect!"); correct += 1
        else:
            print("\nSorry! The correct answer was To distribute the gasket evenly to prevent gaps/wrinkles.")
    elif rand_int == 121:
        print("Which of the following gasket must be removed from the engine and placed on the bench?\n a) Oil Pan Gasket\n b) Carburetor Gasket\n c) Valve Cover Gasket\n d) Timing Chain Cover Gasket\n")
        ans = input("What is your answer? ")
        if ans.lower().strip() == "a" or ans.lower().strip() == "oil pan gasket":
            print("\nCorrect!"); correct += 1
        else:
            print("\nSorry! The correct answer was Oil Pan Gasket.")
    elif rand_int == 122:
        print("Which of the following gaskets must NOT be removed from the component/engine?\n a) Header Gasket\n b) Intake Gasket\n c) Oil Pan Gasket\n d) Carburetor Gasket\n")
        ans = input("What is your answer? ")
        if ans.lower().strip() == "d" or ans.lower().strip() == "carburetor gasket":
            print("\nCorrect!"); correct += 1
        else:
            print("\nSorry! The correct answer was Carburetor Gasket.")
    elif rand_int == 123:
        print("Which of the following gasket must be removed from the engine/component and placed on the bench?\n a) Water Pump Gasket\n b) Cylinder Head Gasket\n c) Timing Chain Cover Gasket\n d) Valve Cover Gasket\n")
        ans = input("What is your answer? ")
        if ans.lower().strip() == "b" or ans.lower().strip() == "cylinder head gasket":
            print("\nCorrect!"); correct += 1
        else:
            print("\nSorry! The correct answer was Cylinder Head Gasket.")
    elif rand_int == 124:
        print('A 12" or longer breaker bar or ratchet must be used to de-torque the following fasteners:\n a) Head Nut/Bolts\n b) Oil Pump Nut\n c) Harmonic Balancer Bolt\n d) All of The Above\n')
        ans = input("What is your answer? ")
        if ans.lower().strip() == "d" or ans.lower().strip() == "all of the above":
            print("\nCorrect!"); correct += 1
        else:
            print("\nSorry! The correct answer was All of The Above.")
    elif rand_int == 125:
        print("If a team damages or loses a component or fastener, the coach may call a timeout and request a replacement component of fastener. What is the penalty time for each occurence?\n a) 1 Minute\n b) 2 Minutes\n c) 4 Minutes\n d) 6 Minutes\n")
        ans = input("What is your answer? ")
        if ans.lower().strip() == "a" or ans.lower().strip() == "1 minute":
            print("\nCorrect!"); correct += 1
        else:
            print("\nSorry! The correct answer was 1 Minute.")
    elif rand_int == 126:
        print("Torque wrenches may NOT be placed on the following area(s):\n a) Padded Tray\n b) On The Floor\n c) On The Bench\n d) None of the Above\n")
        ans = input("What is your answer? ")
        if ans.lower().strip() == "b" or ans.lower().strip() == "on the floor":
            print("\nCorrect!"); correct += 1
        else:
            print("\nSorry! The correct answer was On The Floor.")
    elif rand_int == 127:
        print("During the assembly phase, how many degrees apart do the piston rings get clocked at?\n a) 90 Degrees\n b) 45 Degrees\n c) 180 Degrees\n d) 360 Degrees\n")
        ans = input("What is your answer? ")
        if ans.lower().strip() == "c" or ans.lower().strip() == "180 degrees":
            print("\nCorrect!"); correct += 1
        else:
            print("\nSorry! The correct answer was 180 Degrees.")
    elif rand_int == 128:
        print("When installing the piston and rod assembly, what is the purpose for using rod bolt protectors?\n a) Protect the Rod bolts from falling\n b) Protect the rod bearings from being damaged\n c) Protect cylinder walls and crack journals from being scratched\n d) Protect the piston skirt from cracking\n")
        ans = input("What is your answer? ")
        if ans.lower().strip() == "c" or ans.lower().strip() == "protect cylinder walls and crank journals from being scratched":
            print("\nCorrect!"); correct += 1
        else:
            print("\nSorry! The correct answer was Protect cylinder walls and crank journals from being scratched.")
    elif rand_int == 129:
        print("Why is it required to clock the piston rings at 180 degrees?\n a) To keep the gaps away from each other\n b) To keep anti-freeze out of the combustion chamber\n c) To keep oil from bypassing into the combustion chamber easily\n d) To prevent water from bypassing into the combustion chamber\n")
        ans = input("What is your answer? ")
        if ans.lower().strip() == "c" or ans.lower().strip() == "to keep oil from bypassing into the combustion chamber easily":
            print("\nCorrect!"); correct += 1
        else:
            print("\nSorry! The correct answer was To keep oil from bypassing into the combustion chamber easily.")
    elif rand_int == 130:
        print("During competition, why is it required to wear helmets and safety glasses?\n a) Helmets are worn to prevent neck injury. Safety glasses are worn to prevent facial injury\n b) Helmets are worn to protect your head from injury. Safety glasses are worn to protect your eyes from injury\n c) Helmets and safety glasses are worn to remind the students that they are competing.\n d) Helmets are worn to protect your head from injury. Safety glasses are worn to provoke your eyes from injury.\n")
        ans = input("What is your answer? ")
        if ans.lower().strip() == "b" or ans.lower().strip() == "helmets are worn to protect your head from injury. safety glasses are worn to protect your eyes from injury":
            print("\nCorrect!"); correct += 1
        else:
            print("\nSorry! The correct answer was Helmets are worn to protect your head from injury. Safety glasses are worn to protect your eyes from injury.")
    elif rand_int == 131:
        print("Why is it required to hand start all fasteners?\n a) Prevents threads from stripping/cross threading\n b) Confirms that the team has all of the correct fasteners\n c) To ensure proper alignmnet of the component\n d) All of the above\n")
        ans = input("What is your answer? ")
        if ans.lower().strip() == "d" or ans.lower().strip() == "all of the above":
            print("\nCorrect!"); correct += 1
        else:
            print("\nSorry! The correct answer was All of the above.")
    elif rand_int == 132:
        print("During competition in the disassembly phase, why is it required to do 5 full turns on the balancer puller bolts?\n a) On an engine that the balancer is not honed, you would have to turn at least 5 full turns to remove the balancer from the crankshaft\n b) To make sure the bolts are engaged\n c) To prevent the threads from falling\n d) None of the above\n")
        ans = input("What is your answer? ")
        if ans.lower().strip() == "a" or ans.lower().strip() == "on an engine that the balancer is not honed, you would have to turn at least 5 full turns to remove the balancer from the crankshaft":
            print("\nCorrect!"); correct += 1
        else:
            print("\nSorry! The correct answer was On an engine that the balancer is not honed, you would have to turn at least 5 full turns to remove the balancer from the crankshaft.")
    elif rand_int == 133:
        print('What is the significance of putting the timing gears "dot to dot"?\n a) The crankshaft will be at 180 degrees\n b) The camshaft will be at the right position to install pistons\n c) The camshaft and the crankshaft will have the correct timing\n d) All of the above\n')
        ans = input("What is your answer? ")
        if ans.lower().strip() == "c" or ans.lower().strip() == "the camshaft and the crankshaft will have the correct timing":
            print("\nCorrect!"); correct += 1
        else:
            print("\nSorry! The correct answer was The camshaft and the crankshaft will have the correct timing.")
    elif rand_int == 134:
        print("When removing pistons and the rod assembly, where must the rod cap and piston NOT be place donce it has been removed?\n a) Piston Rack\n b) Tray\n c) Bench\n d) Floor\n")
        ans = input("What is your answer? ")
        if ans.lower().strip() == "d" or ans.lower().strip() == "floor":
            print("\nCorrect!"); correct += 1
        else:
            print("\nSorry! The correct answer was Floor.")
    elif rand_int == 135:
        print("Students and instructors must be how many yards away from the event before using any tobacco or electronic smoking products?\n a) 50 yards\n b) 75 yards\n c) 100 yards\n d) 25 yards\n")
        ans = input("What is your answer? ")
        if ans.lower().strip() == "c" or ans.lower().strip() == "100 yards":
            print("\nCorrect!"); correct += 1
        else:
            print("\nSorry! The correct answer was 100 yards.")
    elif rand_int == 136:
        print("Torque wrenches may NOT be placed on the following area(s):\n a) Padded Tray\n b) On The Floor\n c) On The Bench\n d) None of the Above\n")
        ans = input("What is your answer? ")
        if ans.lower().strip() == "b" or ans.lower().strip() == "on the floor":
            print("\nCorrect!"); correct += 1
        else:
            print("\nSorry! The correct answer was On The Floor.")
    elif rand_int == 137:
        print("What is the maximum amount of torque wrenches that will be allowed to have on the bench during competition?\n a) 2\n b) 3\n c) 4\n d) 6\n")
        ans = input("What is your answer? ")
        if ans.lower().strip() == "d" or ans.lower().strip() == "6":
            print("\nCorrect!"); correct += 1
        else:
            print("\nSorry! The correct answer was 6.")
    elif rand_int == 138:
        print("What is a protective device that will allow opening and closing when current draw becomes excessive?\n a) Fuse\n b) Circuit Breaker\n c) Insulator\n d) Fusable Link\n")
        ans = input("What is your answer? ")
        if ans.lower().strip() == "b" or ans.lower().strip() == "circuit breaker":
            print("\nCorrect!"); correct += 1
        else:
            print("\nSorry! The correct answer was Circuit Breaker.")
    elif rand_int == 139:
        print("What is a special calibrated wire installed into a harness that is designed to protect the circuit from an overload?\n a) Circuit Breaker Wire\n b) Fuse\n c) Fusible Link\n d) Insulator\n")
        ans = input("What is your answer? ")
        if ans.lower().strip() == "c" or ans.lower().strip() == "fusible link":
            print("\nCorrect!"); correct += 1
        else:
            print("\nSorry! The correct answer was Fusible Link.")
    elif rand_int == 140:
        print("What is made of plastic, rubber, and ceramics that can resist the flow of electricity?\n a) Circuit Breaker\n b) Fuse\n c) Insulator\n d) Fusable Link\n")
        ans = input("What is your answer? ")
        if ans.lower().strip() == "c" or ans.lower().strip() == "insulator":
            print("\nCorrect!"); correct += 1
        else:
            print("\nSorry! The correct answer was Insulator.")
    elif rand_int == 141:
        print("What is the movement of electrons from atom to atom called?\n a) Fuse\n b) Electricity\n c) Current\n d) Voltage\n")
        ans = input("What is your answer? ")
        if ans.lower().strip() == "b" or ans.lower().strip() == "electricity":
            print("\nCorrect!"); correct += 1
        else:
            print("\nSorry! The correct answer was Electricity.")
    elif rand_int == 142:
        print("What is the flow of electrons called?\n a) Current\n b) Circuit\n c) Voltage\n d) Ground\n")
        ans = input("What is your answer? ")
        if ans.lower().strip() == "a" or ans.lower().strip() == "current":
            print("\nCorrect!"); correct += 1
        else:
            print("\nSorry! The correct answer was Current.")
    elif rand_int == 143:
        print("What is needed to control the flow of current in a circuit?\n a) Fuse\n b) Current\n c) Circuit\n d) Voltage\n")
        ans = input("What is your answer? ")
        if ans.lower().strip() == "d" or ans.lower().strip() == "voltage":
            print("\nCorrect!"); correct += 1
        else:
            print("\nSorry! The correct answer was Voltage.")
    elif rand_int == 144:
        print("What protects a circuit against damage caused by a short circuit?\n a) Series Circuit\n b) Current\n c) Fuse\n d) Ground\n")
        ans = input("What is your answer? ")
        if ans.lower().strip() == "c" or ans.lower().strip() == "fuse":
            print("\nCorrect!"); correct += 1
        else:
            print("\nSorry! The correct answer was Fuse.")
# Use Ohm's Law for Questions 145 through 148. Please answer correctly.
    elif rand_int == 145:
        print("If a circuit has 12 volts and 2 Ohms, what is the current in this circuit?\n a) 24 amps\n b) 4 amps\n c) 8 amps\n d) 6 amps\n")
        ans = input("What is your answer? ")
        if ans.lower().strip() == "d" or ans.lower().strip() == "6 amps":
            print("\nCorrect!"); correct += 1
        else:
            print("\nSorry! The correct answer was 6 amps.")
    elif rand_int == 146:
        print("If a ciruit has 12 volts and 2 amps, what is the resistance in this circuit?\n a) 24 ohms\n b) 6 ohms\n c) 4 ohms\n 8 ohms\n")
        ans = input("What is your answer? ")
        if ans.lower().strip() == "b" or ans.lower().strip() == "6 ohms":
            print("\nCorrect!"); correct += 1
        else:
            print("\nSorry! The correct answer was 6 ohms.")
    elif rand_int == 147:
        print("If a circuit had 3 amps and 2 ohms, what is the voltage in this circuit?\n a) 6 volts\n b) 3 volts\n c) 3 volts\n d) 6.2 volts\n")
        ans = input("What is your answer? ")
        if ans.lower().strip() == "a" or ans.lower().strip() == "6 volts":
            print("\nCorrect!"); correct += 1
        else:
            print("\nSorry! The correct answer was 6 volts.")
    elif rand_int == 148:
        print("If a ciruit has 12 amps and 6 ohms, what is the voltage in this circuit?\n a) 2 volts\n b) 18 volts\n c) 72 volts\n d) 6 volts\n")
        ans = input("What is your answer? ")
        if ans.lower().strip() == "c" or ans.lower().strip() == "72 volts":
            print("\nCorrect!"); correct += 1
        else:
            print("\nSorry! The correct answer was 72 volts.")
    elif rand_int == 149:
        print("The power in watts is equal to the voltage in volts, times the current in amps. If a circuit has 12 volts and 3 amps, what is the power in this circuit?\n a) 3 watts\n b) 4 watts\n c) 15 watts\n d) 36 watts\n")
        ans = input("What is your answer? ")
        if ans.lower().strip() == "d" or ans.lower().strip() == "36 watts":
            print("\nCorrect!"); correct += 1
        else:
            print("\nSorry! The correct answer was 36 watts.")
    elif rand_int == 150:
        print("The power in watts is equal to the voltage in volts, times the current in amps. If a circuit has 6 volts and 2 amps, what is the power in this circuit?\n a) 3 watts\n b) 4 watts\n c) 8 watts\n d) 12 watts\n")
        ans = input("What is your answer? ")
        if ans.lower().strip() == "d" or ans.lower().strip() == "12 watts":
            print("\nCorrect!"); correct += 1
        else:
            print("\nSorry! The correct answer was 12 watts.")
    elif rand_int == 151:
        print("The power in watts is equal to the voltage in volts, times the current in amps. If a circuit has 11volts and 3 amps, what is the power in this circuit?\n a) 33 watts\n b) 14 watts\n c) 9 watts\n d) 4 watts\n")
        ans = input("What is your answer? ")
        if ans.lower().strip() == "a" or ans.lower().strip() == "33 watts":
            print("\nCorrect!"); correct += 1
        else:
            print("\nSorry! The correct answer was 33 watts.")
# Questions 152 through 172 will be on General Automotive. Please answer correctly.
    elif rand_int == 152:
        print("Building an engine to an exacting set of specifications is called:\n a) Balancing\n b) Decking\n c) Blueprinting\n d) None of the above\n")
        ans = input("What is your answer? ")
        if ans.lower().strip() == "c" or ans.lower().strip() == "blueprinting":
            print("\nCorrect!"); correct += 1
        else:
            print("\nSorry! The correct answer was Blueprinting.")
    elif rand_int == 153:
        print("Align boring is done:\n a) To make crankshaft parallel to camshaft\n b) To correct cylinder out of round\n c) To correct cylinder taper\n d) All of the above\n")
        ans = input("What is your answer? ")
        if ans.lower().strip() == "a" or ans.lower().strip() == "to make crankshaft parallel to camshaft":
            print("\nCorrect!"); correct += 1
        else:
            print("\nSorry! The correct answer was To make crankshaft parallel to camshaft.")
    elif rand_int == 154:
        print("When applying cross hatch to a cylinder you would use a:\n a) Bench grinder\n b) File\n c) Emery cloth\n d) Hone\n")
        ans = input("What is your answer? ")
        if ans.lower().strip() == "d" or ans.lower().strip() == "hone":
            print("\nCorrect!"); correct += 1
        else:
            print("\nSorry! The correct answer was Hone.")
    elif rand_int == 155:
        print("Why are main bearings made of soft metal?\n a) To accept dirt\n b) Soft to conform to crankshaft journal\n c) All of the above\n d) None of the above\n")
        ans = input("What is your answer? ")
        if ans.lower().strip() == "c" or ans.lower().strip() == "all of the above":
            print("\nCorrect!"); correct += 1
        else:
            print("\nSorry! The correct answer was All of the above.")
    elif rand_int == 156:
        print("What is used to measure a cylinder bore accurately?\n a) Micrometer\n b) Gauge\n c) Dial-Bore Gauge\n d) None of the above\n")
        ans = input("What is your answer? ")
        if ans.lower().strip() == "c" or ans.lower().strip() == "dial-bore gauge":
            print("\nCorrect!"); correct += 1
        else:
            print("\nSorry! The correct answer was Dial-Bore Gauge.")
    elif rand_int == 157:
        print("To measure piston to valve clearance you would use:\n a) CC burette\n b) Modeling clay\n c) Dial bore guage\n d) Deck gauge\n")
        ans = input("What is your answer? ")
        if ans.lower().strip() == "b" or ans.lower().strip() == "modeling clay":
            print("\nCorrect!"); correct += 1
        else:
            print("\nSorry! The correct answer was Modeling clay.")
    elif rand_int == 158:
        print("The tool used to measure crankshaft main journal taper is a _______________.\n a) Dial bore gauge\n b) Micrometer\n c) Telescoping gauge\n d) Dial indicator\n")
        ans = input("What is your answer? ")
        if ans.lower().strip() == "b" or ans.lower().strip() == "micrometer":
            print("\nCorrect!"); correct += 1
        else:
            print("\nSorry! The correct answer was Micrometer.")
    elif rand_int == 159:
        print("What is the firing order for an in-line four cylinder?\n a) 3-2-4-1\n b) 4-3-2-1\n c) 1-3-4-2 d) 2-4-3-1\n")
        ans = input("What is your answer? ")
        if ans.lower().strip() == "c" or ans.lower().strip() == "1-3-4-2":
            print("\nCorrect!"); correct += 1
        else:
            print("\nSorry! The correct answer was 1-3-4-2.")
    elif rand_int == 160:
        print("1,8,4,3,6,5,7,2 is the_______ of a small block Chevy 350?\n a) Intake torque sequence\n b) Cylinder head trque sequence\n c) Rod cap torque sequence\n d) Firing order\n")
        ans = input("What is your answer? ")
        if ans.lower().strip() == "d" or ans.lower().strip() == "firing order":
            print("\nCorrect!"); correct += 1
        else:
            print("\nSorry! The correct answer was Firing order.")
    elif rand_int == 161:
        print("If the air-fuel mixture in a engine is too rich, what is the air-fuel ratio?\n a) 14:1\n b) 10:1\n c) 28:2\n d) 17:1\n")
        ans = input("What is your answer? ")
        if ans.lower().strip() == "b" or ans.lower().strip() == "10:1":
            print("\nCorrect!"); correct += 1
        else:
            print("\nSorry! The correct answer was 10:1.")
    elif rand_int == 162:
        print("What is the main function of an intake manifold?\n a) Distribute carbon monoxide equally to the cylinders\n b) Distribute air and fuel equally to the cylinders\n c) Clean the air before it mixes with the fuel\n d) Distribute air into each cylinder head\n")
        ans = input("What is your answer? ")
        if ans.lower().strip() == "b" or ans.lower().strip() == "distribute air and fuel equally to the cylinders":
            print("\nCorrect!"); correct += 1
        else:
            print("\nSorry! The correct answer was Distribute air and fuel equally to the cylinders.")
    elif rand_int == 163:
        print("White smoke is coming from the tail pipe? What would cause this?\n a) Defective water pump\n b) Thermostat is stuck open\n c) Coolant leaking into the combustion chamber\n d) Restrictions in the cooling system\n")
        ans = input("What is your answer? ")
        if ans.lower().strip() == "c" or ans.lower().strip() == "coolant leaking into the combustion chamber":
            print("\nCorrect!"); correct += 1
        else:
            print("\nSorry! The correct answer was Coolant leaking into the combustion chamber.")
    elif rand_int == 164:
        print("How often do you need to change most vehicles' engine oil?\n a) 3,000 Miles\n b) 30,000 Miles\n c) 3 Weeks\n d) 300 Miles\n")
        ans = input("What is your answer? ")
        if ans.lower().strip() == "a" or ans.lower().strip() == "3,000 miles":
            print("\nCorrect!"); correct += 1
        else:
            print("\nSorry! The correct answer was 3,000 Miles.")
    elif rand_int == 165:
        print('In 10W-30 Motor oil, what does the "W" stand for stand for?\n a) West\n b) Winter\n c) Weight\n d) Width\n')
        ans = input("What is your answer? ")
        if ans.lower().strip() == "b" or ans.lower().strip() == "winter":
            print("\nCorrect!"); correct += 1
        else:
            print("\nSorry! The correct answer was Winter.")
    elif rand_int == 166:
        print("The effect of having excess camber is?\n a) Uneven tire wear\n b) Even tire wear\n c) Increases a smooth ride\n d) Decreases tire wear\n")
        ans = input("What is your answer? ")
        if ans.lower().strip() == "a" or ans.lower().strip() == "uneven tire wear":
            print("\nCorrect!"); correct += 1
        else:
            print("\nSorry! The correct answer was Uneven tire wear.")
    elif rand_int == 167:
        print("The difference between DOT 3 and DOT 4 brake fluids is?\n a) DOT 4 fluid has a higher boiling point than DOT 3\n b) DOT 3 fluid has a higher boiling point than DOT 4 fluid\n c) DOT 3 fluid has a higher viscosity than DOT 4 fluid\n d) DOT 4 fluid has a higher viscosity than DOT 3 fluid\n")
        ans = input("What is your answer? ")
        if ans.lower().strip() == "a" or ans.lower().strip() == "dot 4 fluid has a higher boiling point than dot 3 fluid":
            print("\nCorrect!"); correct += 1
        else:
            print("\nSorry! The correct answer was DOT 4 fluid has a higher boiling point than DOT 3 fluid.")
    elif rand_int == 168:
        print("What is the main reason(s) for a cooling system in the engine?\n a) Remove unwanted heat\n b) Maintain operating temp\n c) Bring engine up to operating temp\n d) All of the above\n")
        ans = input("What is your answer? ")
        if ans.lower().strip() == "d" or ans.lower().strip() == "all of the above":
            print("\nCorrect!"); correct += 1
        else:
            print("\nSorry! The correct answer was All of the above.")
    elif rand_int == 169:
        print("Please define the following vocabulary word: Aerodynamics\n a) A device for measuring mechanical air force\n b) Created when a vehicle corners that tends to push a vehicle sideways\n c) The amount the intake amnifold can filter\n d) The study of the effects of air resistance and lift on vehicles\n")
        ans = input("What is your answer? ")
        if ans.lower().strip() == "d" or ans.lower().strip() == "the study of the effects of air resistance and lift on vehicles":
            print("\nCorrect!"); correct += 1
        else:
            print("\nSorry! The correct answer was The study of the effects of air resistance and lift on vehicles.")
    elif rand_int == 170:
        print("Please define the following vocabulary word: Air Capacity\n a) The amount the intake manifold can filter\n b) The volume displaced on intake strokes during each crankshaft revolution\n c) The maesurement of effectiveness of a machine's energy and power\n d) A device for measuring mechanical air force\n")
        ans = input("What is your answer? ")
        if ans.lower().strip() == "b" or ans.lower().strip() == "the volume displaced on intake strokes during each crankshaft revolution":
            print("\nCorrect!"); correct += 1
        else:
            print("\nSorry! The correct answer was The volume displaced on intake strokes during each crankshaft revolution.")
    elif rand_int == 171:
        print("Technician A says nitrous oxide is a fuel. Technician B says nitrous oxide is flammable. Who is correct?\n a) Technician A\n b) Technician B\n c) Both Technicians A and B\n d) Neither Technician A nor B\n")
        ans = input("What is your answer? ")
        if ans.lower().strip() == "d" or ans.lower().strip() == "neither technician a nor b":
            print("\nCorrect!"); correct += 1
        else:
            print("\nSorry! The correct answer was Neither Technician A nor B.")
    elif rand_int == 172:
        print("Technician A says stroke impacts the compression ratio. Technician B says the head gasket thickness impacts the compression ratio. Who is correct?\n a) Technician A\n b) Technician B\n c) Both Technicians A and B\n d) Neither Technician A nor B\n")
        ans = input("What is your answer? ")
        if ans.lower().strip() == "c" or ans.lower().strip() == "both technician a and b":
            print("\nCorrect!"); correct += 1
        else:
            print("\nSorry! The correct answer was Both Technician A and B.")
# After this, to 236, the questions should use pictures to help you identify tools and items. I don't know how to add pictures in.
    elif rand_int == 173:
        print("I can't really put the identification section in this, but you will study it right? (Yes or No)\n It is questions 173 to 236.")
        ans = input("What is your answer? ")
        if ans.lower().strip() == "yes":
            print("\nCorrect!"); correct += 1
        else:
            print("\nSorry! The correct answer was Yes.")
    else:
        print("Sorry, your number has not been programmed yet. How did you get here?")
    if correct == 10:
        print("\nCongrats! You have correctly solved 10 questions this session!")
    if correct == 20:
        print("\nCongrats! You have correctly solved 20 questions this session!")
    if correct == 30:
        print("\nCongrats! You have correctly solved 30 questions this session!")
    if correct == 40:
        print("\nCongrats! You have correctly solved 40 questions this session!")
    if correct == 50:
        print("\nCongrats! You have correctly solved 50 questions this session!")
    if correct == 60:
        print("\nCongrats! You have correctly solved 60 questions this session!")
    if correct == 70:
        print("\nCongrats! You have correctly solved 70 questions this session!")
    if correct == 80:
        print("\nCongrats! You have correctly solved 80 questions this session!")
    if correct == 90:
        print("\nCongrats! You have correctly solved 90 questions this session!")
    if correct == 100:
        print("\nCongrats! You have correctly solved 100 questions this session!")
    cont = "Y"
    while cont == "Y":
        again = input("\nContinue? Y/N: ")
        if again.lower().strip() == "y" or again.lower().strip() == "yes":
            cont = "X"
            continue
        elif again.lower().strip() == "n" or again.lower().strip() == "no":
            exit()
            break
        else:
            print("Please enter yes or no.")