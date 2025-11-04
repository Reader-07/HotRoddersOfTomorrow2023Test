# This is the worst code you will ever see. I did this with basically zero knowledge of python and only some HTML knowledge. Good luck.
# A lot of this is only working based in luck and random redundancies.
# At least I changed it so the questions ping off a function instead of repeating the question code for every if statement.
# Well... now I understand my question code quite well from that. So much time wasted. It looked advanced though.
import random
# Setting up variables. While statements will loop until wanted. Amounts will be set to start.
again = "Y"
start = "Y"
state_id = "Y"
correct = 0
wrong = 0
amount = 0
question = "Y"
# The basic question format which will be called upon.
def ask_question():
    global amount; global correct; global wrong
    if true_ans_letter == "a":
        true_ans_word = ans_a
    elif true_ans_letter == "b":
        true_ans_word = ans_b
    elif true_ans_letter == "c":
        true_ans_word = ans_c
    elif true_ans_letter == "d":
        true_ans_word = ans_d
    print(f"{question}\n a) {ans_a}\n b) {ans_b}\n c) {ans_c}\n d) {ans_d}\n"); amount += 1
    ans = "Y"
    while ans == "Y":
        user_ans = input("What is your answer? ")
        if user_ans.lower().strip() == true_ans_letter.lower().strip() or user_ans.lower().strip() == true_ans_word.lower().strip():
            print("\nCorrect!"); correct += 1
            ans = "X"
        elif user_ans.lower().strip() == "":
            print("\nPlease answer. It helps your learning.")
            continue
        # Mild, vary basic easter egg.
        elif user_ans.lower().strip() == "404":
            print("Error 404: Answer not found.")
            continue
        else:
            print(f"\nSorry! The correct answer was {true_ans_word}."); wrong += 1
            ans = "X"
#The beginning interface for the user to set their settings.
while start == "Y":
    start = input("Would you like to (s)tart or read the (i)nstructions? ")
    # The user has selected to enter into instructions.
    if start.lower().strip() == "instructions" or start.lower().strip() == "i":
        print("\033c")
        print("You will get a randomly generated question from the 2023 Hot Rodders of Tomorrow Dual National Championship Test Study Guide.\n"
        "When you get your question, all you need to do is type your answer as either the letter (i.e. 'a') or as the words (i.e. 'Push Rod').\n"
        "The system shouldn't be case sensitive so you don't need to worry about capitalization but you will need to worry about spelling.\n"
        "I have made the executive decision to remove periods unless there are multiple sentences in each answer so that there is less of a chance to get a false negative.\n"
        "However, make sure to type either only the letter or word.\n"
        "The test guide has spelling errors in it which I have decided to include into this program.\n"
        "However, I have gone through many sleep-deprived revsions of this code, so there are a large amount that come from me.\n"
        "Everything else should be intuitive so have fun studying!\n"
        "If you have any issues, email me at xxxxxxxxxxxxxxx or put an issue in my GitHub at Reader-07. I might update it... eventually.\n")
        start = "Y"
    # The user has selected to start the setup.
    elif start.lower().strip() == "start" or start.lower().strip() == "s":
        print("\nStarting...")
        while state_id == "Y":
            print("Would you like to have the questions stay on the screen or dissapear after you continue?\n")
            state = input("(S)tay/(D)issapear: ")
            # Setting up the state of the finished questions.
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
        # Clears the terminal when ran. Activated when user has selected dissapear in setup.
        print("\033c")
    print(f"You have completed {amount} questions this session. \n")
    # Identifies which question gets selected.
    rand_int = random.randint(1,173)
    print(f"\nHere is question #{rand_int}:\n")
# All questions require six variables ("question", "ans_a", "ans_b", "ans_c", "ans_d", and "true_ans_letter") and one function call ("ask question()").
# This method slightly adds more lines, but it makes it much more readable than sticking all variables on one line.
# Questions 1 through 14, any driopped component that hits the floor, tool pan, or tray will be considered a dropped penalty.
    if rand_int == 1:
        question = "Which dropped component will be a 15 second penalty?"
        ans_a = "Push Rod"
        ans_b = "Cylinder Head Gasket"
        ans_c = "Head Fastener(s) (wiped & reoiled)"
        ans_d = "Lifter"
        true_ans_letter = "d"
        ask_question()
    elif rand_int == 2:
        question = "Which dropped component will be a 2 minute penalty?"
        ans_a = "Cylinder Head Gasket"
        ans_b = "Air Cleaner"
        ans_c = "Lifter"
        ans_d = "Water Pump"
        true_ans_letter = "b"
        ask_question()
    elif rand_int == 3:
        question = "Which dropped component wil NOT be a 2 minute penalty?"
        ans_a = "Timing Chain and/or Timing Gear"
        ans_b = "Valve Cover"
        ans_c = "Spark Plug"
        ans_d = "Timing Cover"
        true_ans_letter = "a"
        ask_question()
    elif rand_int == 4:
        question = "Which dropped component will be a 5 minute penalty?"
        ans_a = "Valve Cover"
        ans_b = "Oil Pan"
        ans_c = "Distibutor"
        ans_d = "Timing Chain Cover"
        true_ans_letter = "a"
        ask_question()
    elif rand_int == 5:
        question = "Which dropped component will be a 10 minute penalty?"
        ans_a = "Cylinder Head"
        ans_b = "Exhaust Header"
        ans_c = "Distibutor"
        ans_d = "Oil Pump"
        true_ans_letter = "a"
        ask_question()
    elif rand_int == 6:
        question = "Which dropped component will be a 5 minute penalty?"
        ans_a = "a) Rocker Arm"
        ans_b = "Oil Pan"
        ans_c = "Rod Bearing Half"
        ans_d = "Intake Manifold"
        true_ans_letter = "d"
        ask_question()
    elif rand_int == 7:
        questions = "Which dropped component will be a 5 minute penalty?"
        ans_a = "Oil Pan"
        ans_b = "Cylinder Head"
        ans_c = "Air Cleaner"
        ans_d = "Exhaust Header"
        true_ans_letter = "d"
        ask_question()
    elif rand_int == 8:
        question = "Which dropped component will be a 1 minute penalty?"
        ans_a = "Rod Bearing Half"
        ans_b = "Oil Pump Nut"
        ans_c = "Cylinder Head Gasket"
        ans_d = "Oil Filter"
        true_ans_letter = "c"
        ask_question()
    elif rand_int == 9:
        question = "Which dropped component will be a 15 second penalty?"
        ans_a = "Camshaft Bolts"
        ans_b = "Lifter Bars"
        ans_c = "Spark Plug"
        ans_d = "Oil Filter"
        true_ans_letter = "d"
        ask_question()
    elif rand_int == 10:
        question = "If a Valve Cover T-Handle is dropped during competition, what will be the penalty time for each occurence?"
        ans_a = "15 seconds"
        ans_b = "1 minute"
        ans_c = "2 minutes"
        ans_d = "Not a penalty"
        true_ans_letter = "a"
        ask_question()
    elif rand_int == 11:
        question = "If a Distributor Cap is dropped during competition, what will be the penalty time for each occurence?"
        ans_a = "2 minutes"
        ans_b = "5 minutes"
        ans_c = "10 minutes"
        ans_d = "15 minutes"
        true_ans_letter = "a"
        ask_question()
    elif rand_int == 12:
        question = "If a Water Pump is dropped during competition, what will be the penalty time for each occurence?"
        ans_a = "30 seconds"
        ans_b = "1 minute"
        ans_c = "2 minutes"
        ans_d = "5 minutes"
        true_ans_letter = "d"
        ask_question()
    elif rand_int == 13:
        question = "If an Oil Pump Drive is dropped during competition, what will be the penalty time for each occurence?"
        ans_a = "15 seconds"
        ans_b = "1 minute"
        ans_c = "2 minutes"
        ans_d = "5 minutes"
        true_ans_letter = "a"
        ask_question()
    elif rand_int == 14:
        question = "If a Spark Plug is dropped during competition, what will be the penalty time for each occurence?"
        ans_a = "30 seconds"
        ans_b = "1 minute"
        ans_c = "2 minutes"
        ans_d = "3 minutes"
        true_ans_letter = "c"
        ask_question()
# Questions 15 through 66 are either True or False.
    elif rand_int == 15:
        question = "Brake cleaners and carb cleaners are banned. Only Non-Toxic cleaners that are approved in writing by Rodney Bingham may be used."
        ans_a = "True"
        ans_b = "False"
        ans_c = ""
        ans_d = ""
        true_ans_letter = "a"
        ask_question()
    elif rand_int == 16:
        question = "When de-torqueing the oil pump nut, a pry bar is NOT necessary."
        ans_a = "True"
        ans_b = "False"
        ans_c = ""
        ans_d = ""
        true_ans_letter = "b"
        ask_question()
    elif rand_int == 17:
        question = "Tools, components, or fasteners may be placed in mouth."
        ans_a = "True"
        ans_b = "False"
        ans_c = ""
        ans_d = ""
        true_ans_letter = "b"
        ask_question()
    elif rand_int == 18:
        question = "ALL fasteners and washers must be removed from all component except cylinder heads center washer."
        ans_a = "True"
        ans_b = "False"
        ans_c = ""
        ans_d = ""
        true_ans_letter = "a"
        ask_question()
    elif rand_int == 19:
        question = "During the disassembly phase, multiple rod caps may be loosened and/or removed at a single time."
        ans_a = "True"
        ans_b = "False"
        ans_c = ""
        ans_d = ""
        true_ans_letter = "b"
        ask_question()
    elif rand_int == 20:
        question = "Header gaskets must be removed from the engine and placed on the bench."
        ans_a = "True"
        ans_b = "False"
        ans_c = ""
        ans_d = ""
        true_ans_letter = "a"
        ask_question()
    elif rand_int == 21:
        question = "Valve cover gaskets must be removed from the engine and placed on the bench."
        ans_a = "True"
        ans_b = "False"
        ans_c = ""
        ans_d = ""
        true_ans_letter = "b"
        true_ans_word = ans_b
        ask_question()
    elif rand_int == 22:
        question = "Water pump gasket must be removed from the engine and placed on the bench."
        ans_a = "True"
        ans_b = "False"
        ans_c = ""
        ans_d = ""
        true_ans_letter = "b"
        ask_question()
    elif rand_int == 23:
        question = "Timing chain cover gasket must NOT be removed from the engine an placed on the bench."
        ans_a = "True"
        ans_b = "False"
        ans_c = ""
        ans_d = ""
        true_ans_letter = "a"
        ask_question()
    elif rand_int == 24:
        question = "Cylinder head bolts are NOT required to be oiled at the bench."
        ans_a = "True"
        ans_b = "False"
        ans_c = ""
        ans_d = ""
        true_ans_letter = "b"
        ask_question()
    elif rand_int == 25:
        question = "Oil filter gasket must be oiled at the bench."
        ans_a = "True"
        ans_b = "False"
        ans_c = ""
        ans_d = ""
        true_ans_letter = "a"
        ask_question()
    elif rand_int == 26:
        question = "Only one piston and rod assembly are to be installed at a time."
        ans_a = "True"
        ans_b = "False"
        ans_c = ""
        ans_d = ""
        true_ans_letter = "a"
        ask_question()
    elif rand_int == 27:
        question = "Lifter guides may NOT be installed until ALL lifters have been installed."
        ans_a = "True"
        ans_b = "False"
        ans_c = ""
        ans_d = ""
        true_ans_letter = "a"
        ask_question()
    elif rand_int == 28:
        question = "With the number one piston at Top Dead Center on compression stroke, intake valve #1 is adjusted."
        ans_a = "True"
        ans_b = "False"
        ans_c = ""
        ans_d = ""
        true_ans_letter = "a"
        ask_question()
    elif rand_int == 29:
        question = "When a rod cap with bearing is dropped, it does NOT need to be wiped and re-oiled at the bench."
        ans_a = "True"
        ans_b = "False"
        ans_c = ""
        ans_d = ""
        true_ans_letter = "b"
        ask_question()
    elif rand_int == 30:
        question = "Any dropped component that hits the floor, tool pan, or tray will be considered a dropped item. A dropped Timing Cover will NOT be a 2 minute penalty?"
        ans_a = "True"
        ans_b = "False"
        ans_c = ""
        ans_d = ""
        true_ans_letter = "b"
        ask_question()
    elif rand_int == 31:
        question = "Any dropped component that hits the floor, tool pan, or tray will be considered a dropped item."
        ans_a = "True"
        ans_b = "False"
        ans_c = ""
        ans_d = ""
        true_ans_letter = "a"
        ask_question()
    elif rand_int == 32:
        question = "Stripped spark plug holes will be a 15 minute penalty."
        ans_a = "True"
        ans_b = "False"
        ans_c = ""
        ans_d = ""
        true_ans_letter = "a"
        ask_question()
    elif rand_int == 33:
        question = "Broken piston rings will be a 5 minute penalty."
        ans_a = "True"
        ans_b = "False"
        ans_c = ""
        ans_d = ""
        true_ans_letter = "a"
        ask_question()
    elif rand_int == 34:
        question = "During the assembly phase, the oil filter is torqued at 100 in/lbs."
        ans_a = "True"
        ans_b = "False"
        ans_c = ""
        ans_d = ""
        true_ans_letter = "b"
        ask_question()
    elif rand_int == 35:
        question = "When removing the piston and rod assembly, rod bolt protectors must be used."
        ans_a = "True"
        ans_b = "False"
        ans_c = ""
        ans_d = ""
        true_ans_letter = "a"
        ask_question()
    elif rand_int == 36:
        question = "A torque wrench may be used as a breaker bar."
        ans_a = "True"
        ans_b = "False"
        ans_c = ""
        ans_d = ""
        true_ans_letter = "b"
        ask_question()
    elif rand_int == 37:
        question = "Headers must be torqued hand tight outside-in with a 3/8 in wrench."
        ans_a = "True"
        ans_b = "False"
        ans_c = ""
        ans_d = ""
        true_ans_letter = "b"
        ask_question()
    elif rand_int == 38:
        question = "Distributor hold-down must be torqued hand tight with a 9/16 in wrench."
        ans_a = "True"
        ans_b = "False"
        ans_c = ""
        ans_d = ""
        true_ans_letter = "a"
        ask_question()
    elif rand_int == 39:
        question = "Cam gear must be torqued 100 in/lbs with a clockwise pattern."
        ans_a = "True"
        ans_b = "False"
        ans_c = ""
        ans_d = ""
        true_ans_letter = "b"
        ask_question()
    elif rand_int == 40:
        question = "Harmonic balancer must be torqued 50 ft/lbs with a torque stick."
        ans_a = "True"
        ans_b = "False"
        ans_c = ""
        ans_d = ""
        true_ans_letter = "b"
        ask_question()
    elif rand_int == 41:
        question = "Intake manifold must be torqued hand tight with a 3/8 in wrench."
        ans_a = "True"
        ans_b = "False"
        ans_c = ""
        ans_d = ""
        true_ans_letter = "a"
        ask_question()
    elif rand_int == 42:
        question = "Piston rod assembly must be torqued 15 ft/lbs then 35 ft/lbs."
        ans_a = "True"
        ans_b = "False"
        ans_c = ""
        ans_d = ""
        true_ans_letter = "b"
        ask_question()
    elif rand_int == 43:
        question = "Oil filter is torqued hand tight."
        ans_a = "True"
        ans_b = "False"
        ans_c = ""
        ans_d = ""
        true_ans_letter = "a"
        ask_question()
    elif rand_int == 44:
        question = "Speed Sleeves do NOT require a piston installer."
        ans_a = "True"
        ans_b = "False"
        ans_c = ""
        ans_d = ""
        true_ans_letter = "a"
        ask_question()
    elif rand_int == 45:
        question = "All tools and trays must be placed on the bench at the start of the competition, at the end of disassembly phase, and at the end of assembly phase."
        ans_a = "True"
        ans_b = "False"
        ans_c = ""
        ans_d = ""
        true_ans_letter = "a"
        ask_question()
    elif rand_int == 46:
        question = "Band and Plier style ring compressors only do NOT require a piston installer."
        ans_a = "True"
        ans_b = "False"
        ans_c = ""
        ans_d = ""
        true_ans_letter = "b"
        ask_question()
    elif rand_int == 47:
        questtion = "Rod Bearing Halves, Oil Filter gasket, Rocker arm pivot balls, and Pushrod seats are the components that must be lubricated and called out to the judge's attention."
        ans_a = "True"
        ans_b = "False"
        ans_c = ""
        ans_d = ""
        true_ans_letter = "a"
        ask_question()
    elif rand_int == 48:
        question = "Distributor MUST only be in place before oil pan has been installed."
        ans_a = "True"
        ans_b = "False"
        ans_c = ""
        ans_d = ""
        true_ans_letter = "b"
        ask_question()
    elif rand_int == 49:
        question = "Cylinder head fastener(s) must be wiped and re-oiled at the bench after it has been dropped."
        ans_a = "True"
        ans_b = "False"
        ans_c = ""
        ans_d = ""
        true_ans_letter = "a"
        ask_question()
    elif rand_int == 50:
        question = "Tempering and annealing are ways to harden or soften metal."
        ans_a = "True"
        ans_b = "False"
        ans_c = ""
        ans_d = ""
        true_ans_letter = "a"
        ask_question()
    elif rand_int == 51:
        question = "Most aluminum heads require valve guide inserts to support valve stem."
        ans_a = "True"
        ans_b = "False"
        ans_c = ""
        ans_d = ""
        true_ans_letter = "a"
        ask_question()
    elif rand_int == 52:
        question = "When the Check Engine Light comes on a vehicle's dashboard, it means the engine is too old and needs replaced."
        ans_a = "True"
        ans_b = "False"
        ans_c = ""
        ans_d = ""
        true_ans_letter = "b"
        ask_question()
    elif rand_int == 53:
        question = "The vehicle's air filter cleans the air for the engine."
        ans_a = "True"
        ans_b = "False"
        ans_c = ""
        ans_d = ""
        true_ans_letter = "a"
        ask_question()
    elif rand_int == 54:
        question = "Most vehicles' exhaust system consists of the following items: exhaust manifold, exhaust pipe, catalytic converter, muffler and tail pipe."
        ans_a = "True"
        ans_b = "False"
        ans_c = ""
        ans_d = ""
        true_ans_letter = "a"
        ask_question()
    elif rand_int == 55:
        question = "Radiators are heat exchangers to keep the engine cool by circulating engine coolant through the engine block."
        ans_a = "True"
        ans_b = "False"
        ans_c = ""
        ans_d = ""
        true_ans_letter = "a"
        ask_question()
    elif rand_int == 56:
        question = "On October 1, 1908, the first production Model T Ford is completed at the company's Piquette Avenue plant in Detroit."
        ans_a = "True"
        ans_b = "False"
        ans_c = ""
        ans_d = ""
        true_ans_letter = "a"
        ask_question()
    elif rand_int == 57:
        question = "Henry Ford and William Durant founded the Chevrolet Motor Company."
        ans_a = "True"
        ans_b = "False"
        ans_c = ""
        ans_d = ""
        true_ans_letter = "b"
        ask_question()
    elif rand_int == 58:
        question = "The surface on the crankshaft which rests in the block is called main journal."
        ans_a = "True"
        ans_b = "False"
        ans_c = ""
        ans_d = ""
        true_ans_letter = "a"
        ask_question()
    elif rand_int == 59:
        question = "VIN stands for Vehicle Identification Number."
        ans_a = "True"
        ans_b = "False"
        ans_c = ""
        ans_d = ""
        true_ans_letter = "a"
        ask_question()
    elif rand_int == 60:
        question = "ICM stands for Ignition Control Module."
        ans_a = "True"
        ans_b = "False"
        ans_c = ""
        ans_d = ""
        true_ans_letter = "a"
        ask_question()
    elif rand_int == 61:
        question = "SEMA stands for Special Equipment Market Assistance."
        ans_a = "True"
        ans_b = "False"
        ans_c = ""
        ans_d = ""
        true_ans_letter = "b"
        ask_question()
    elif rand_int == 62:
        question = "ECM stands for Engine Control Mpoule."
        ans_a = "True"
        ans_b = "False"
        ans_c = ""
        ans_d = ""
        true_ans_letter = "a"
        ask_question()
    elif rand_int == 63:
        question = "TDC does not stand for Top Dead Center."
        ans_a = "True"
        ans_b = "False"
        ans_c = ""
        ans_d = ""
        true_ans_letter = "b"
        ask_question()
    elif rand_int == 64:
        question = "PRI stands for Performance Racing Industry."
        ans_a = "True"
        ans_b = "False"
        ans_c = ""
        ans_d = ""
        true_ans_letter = "a"
        ask_question()
    elif rand_int == 65:
        question = "FPR stands for Fuel Pump Regulator."
        ans_a = "True"
        ans_b = "False"
        ans_c = ""
        ans_d = ""
        true_ans_letter = "a"
        ask_question()
    elif rand_int == 66:
        question = "The main purpose for having a harmonic balancer is to absorb the vibration from the combustion."
        ans_a = "True"
        ans_b = "False"
        ans_c = ""
        ans_d = ""
        true_ans_letter = "a"
        ask_question()
# Questions 67 through 77 will be automotive acronyms.
    elif rand_int == 67:
        question = "What does ABS stand for?"
        ans_a = "Anti-Backfire System"
        ans_b = "All Brake System"
        ans_c = "Anti-lock Brake System"
        ans_d = "Alternator Body Sensor"
        true_ans_letter = "c"
        ask_question()
    elif rand_int == 68:
        question = "What does ASE satnd for?"
        ans_a = "Automotive Service Education"
        ans_b = "Automotive Service Excellence"
        ans_c = "Automatic Sensor Equipment"
        ans_d = "American Service Excellence"
        true_ans_letter = "b"
        ask_question()
    elif rand_int == 69:
        question = "What does BCM stand for?"
        ans_a = "Body Connector Mass"
        ans_b = "Brake Control Module"
        ans_c = "Beyond Capability of Maintenance"
        ans_d = "Body Control Module"
        true_ans_letter = "d"
        ask_question()
    elif rand_int == 70:
        question = "What does TPS stand for?"
        ans_a = "Throttle Position Sensor"
        ans_b = "Technical Program System"
        ans_c = "Torque Pistons to Specification"
        ans_d = "Throttle Position System"
        true_ans_letter = "a"
        ask_question()
    elif rand_int == 71:
        question = "What does SEMA stand for?"
        ans_a = "Specialized Engine Machining Authority"
        ans_b = "Squirrels Eat My Acorns"
        ans_c = "Supercharged Engine Management Advisory"
        ans_d = "Specialty Equipment Marketing Association."
        true_ans_letter = "d"
        ask_question()
    elif rand_int == 72:
        question = "What does WOT stand for?"
        ans_a = "Weapons Operation Training"
        ans_b = "Weight On Transmission"
        ans_c = "Wide Open Throttle"
        ans_d = "Width Of Throttle"
        true_ans_letter = "c"
    elif rand_int == 73:
        question = "What does DLC stand for?"
        ans_a = "Digital Link Converter"
        ans_b = "Data Link Connector"
        ans_c = "Data Length Convertor"
        ans_d = "Data Link Convertor"
        true_ans_letter = "b"
        ask_question()
    elif rand_int == 74:
        question = "What Does MAF stand for?"
        ans_a = "Muffler Air Filter"
        ans_b = "Manifold Air Flow"
        ans_c = "Market Automotive Foundation"
        ans_d = "Mass Airflow"
        true_ans_letter = "d"
        ask_question()
    elif rand_int == 75:
        question = "What does DVOM stand for?"
        ans_a = "Digital Volt-Ohmmeter"
        ans_b = "Digital Viscosity Meter"
        ans_c = "Data Volt Ohm Meter"
        ans_d = "Digital Volt Ohm Module"
        true_ans_letter = "a"
        ask_question()
    elif rand_int == 76:
        question = "What does GND stand for?"
        ans_a = "General Notes Dated"
        ans_b = "Ground"
        ans_c = "General Data"
        ans_d = "None of the above"
        true_ans_letter = "b"
        ask_question()
    elif rand_int == 77:
        question = "What does PCV stand for?"
        ans_a = "Permanent Virtual Current"
        ans_b = "Poly Vinyl Color"
        ans_c = "Premature Ventilation Current"
        ans_d = "Positive Crankcase Ventilation"
        true_ans_letter = "d"
        ask_question()
# Questions 78 through 92 will have torque specifications. Please select the correct amount of torque.
    elif rand_int == 78:
        question = "There is a two-step torque sequence for the Cylinder Heads fasteners. What are the correct amounts?"
        ans_a = "15 ft/lbs and 30 ft/lbs"
        ans_b = "25 ft/lbs and 40 ft/lbs"
        ans_c = "25 ft/lbs and 50 ft/lbs"
        ans_d = "25 in/lbs and 50 in/lbs"
        true_ans_letter = "c"
        ask_question()
    elif rand_int == 79:
        question = "There will be a two-step torque sequence for Rod Nuts, what is the correct amount?"
        ans_a = "10 ft/lbs and 20 ft/lbs"
        ans_b = "15 ft/lbs and 25 ft/lbs"
        ans_c = "15 ft/lbs and 30 ft/lbs"
        ans_d = "10 ft/lbs and 35 ft/lbs"
        true_ans_letter = "c"
        ask_question()
    elif rand_int == 80:
        question = "There is a one-step torque sequence for the Cam Gear bolts. What is the correct amount?"
        ans_a = "100 in/lbs"
        ans_b = "15 ft/lbs"
        ans_c = "Hand Tight"
        ans_d = "100 ft/lbs"
        true_ans_letter = "a"
        ask_question()
    elif rand_int == 81:
        question = "There is a one-step torque sequence for the Oil Pump. What is the correct amount?"
        ans_a = "50 in/lbs"
        ans_b = "50 ft/lbs"
        ans_c = "75 in/lbs"
        ans_d = "100 in/lbs"
        true_ans_letter = "b"
        ask_question()
    elif rand_int == 82:
        question = "There is a one-step torque sequence for the Headers bolts. What is the correct amount?"
        ans_a = "Hand Tight"
        ans_b = "100 in/lbs"
        ans_c = "50 in/lbs"
        ans_d = "15 ft/lbs"
        true_ans_letter = "a"
        ask_question()
    elif rand_int == 83:
        question = "There is a one-step torque sequence for the Valve Cover. What is the correct amount?"
        ans_a = "100 in/lbs"
        ans_b = "75 in/lbs"
        ans_c = "50 in/lbs"
        ans_d = "Hand Tight"
        true_ans_letter = "d"
        ask_question()
    elif rand_int == 84:
        question = "There is a one-step torque sequence for the Spark Plugs. What is the correct amount?"
        ans_a = "Hand Tight"
        ans_b = "50 in/lbs"
        ans_c = "75 in/lbs"
        ans_d = "100 in/lbs"
        true_ans_letter = "d"
        ask_question()
    elif rand_int == 85:
        question = "There is a one-step torque sequence for the Water Pump bolts. What is the correct amount?"
        ans_a = "25 in/lbs"
        ans_b = "25 ft/lbs"
        ans_c = "50 ft/lbs"
        ans_d = "75 ft/lbs"
        true_ans_letter = "b"
        ask_question()
    elif rand_int == 86:
        question = "There is a one-step torque sequence for the Starter. What is the correct amount?"
        ans_a = "15 ft/lbs"
        ans_b = "25 in/lbs"
        ans_c = "50 in/lbs"
        ans_d = "100 in/lbs"
        true_ans_letter = "a"
        ask_question()
    elif rand_int == 87:
        question = "There is a one-step torque sequence for the Carburetor fasteners. What is the correct amount?"
        ans_a = "25 in/lbs"
        ans_b = "Hand Tight"
        ans_c = "75 in/lbs"
        ans_d = "50 in/lbs"
        true_ans_letter = "b"
        ask_question()
    elif rand_int == 88:
        question = "There is a one-step torque sequence for the Timing Chain Cover bolts. What is the correct amount?"
        ans_a = "Hand Tight"
        ans_b = "100 in/lbs"
        ans_c = "75 in/lbs"
        ans_d = "50 in/lbs"
        true_ans_letter = "d"
        ask_question()
    elif rand_int == 89:
        question = "The Oil Pan has two different size fasteners. The rail fasteners are 5/16 inch and the corner fasteners are 3/8 inch. There is a one-step torque sequence for the Oil Pan's Corner fastener's (3/8 inch). What is the correct amount?"
        ans_a = "25 in/lbs"
        ans_b = "50 in /lbs"
        ans_c = "75 in/lbs"
        ans_d = "100 in/lbs"
        true_ans_letter = "c"
        ask_question()
    elif rand_int == 90:
        question = "The Oil Pan has two different size fasteners. The rail fasteners are 5/16 inch and the corner fasteners are 3/8 inch. There is a one-step torque sequence for the Oil Pan's Rail fastener's (5/16 inch). What is the correct amount?"
        ans_a = "25 in/lbs"
        ans_b = "50 in /lbs"
        ans_c = "75 in/lbs"
        ans_d = "100 in/lbs"
        true_ans_letter = "b"
        ask_question()
    elif rand_int == 91:
        question = "There is a one-step torque sequence for the following items. Which part is NOT torqued hand tight."
        ans_a = "Harmonic Balancer Adapter"
        ans_b = "Distributor Hold-down"
        ans_c = "Intake Manifold"
        ans_d = "Oil Filter"
        true_ans_letter = "a"
        ask_question()
    elif rand_int == 92:
        question = "There is a one-step torque sequence for the Roller Lifter Spider Hold Down bolts. What is the correct amount?"
        ans_a = "Hand Tight"
        ans_b = "25 in/lbs"
        ans_c = "50 in/lbs"
        ans_d = "100 in/lbs"
        true_ans_letter = "d"
        ask_question()
# Questions 93 through 98 will be on pry bar requirements.
    elif rand_int == 93:
        question = "During the Disassembly Phase, when is it required to use a pry bar?"
        ans_a = "De-torque of rod nuts"
        ans_b = "De-torque cam gear bolts"
        ans_c = "Removing pistons"
        ans_d = "Removing timing chain"
        true_ans_letter = "b"
        ask_question()
    elif rand_int == 94:
        question = "During the assembly phase, when is NOT required to use a pry bar?"
        ans_a = "Torque of rod nut"
        ans_b = "Hand starting and snugging the oil pump nut"
        ans_c = "Torque of cam gear bolts"
        ans_d = "Torque of harmonic balancer"
        true_ans_letter = "a"
        ask_question()
    elif rand_int == 95:
        question = "During the Disassembly Phase, when is it required to use a pry bar?"
        ans_a = "De-torque/removal of oil pump"
        ans_b = "De-torque cylinder heads"
        ans_c = "Removal of lifters"
        ans_d = "Removal of oil pan"
        true_ans_letter = "a"
        ask_question()
    elif rand_int == 96:
        question = "During the Assembly Phase, when is it required to use a pry bar?"
        ans_a = "Hand start/Snugg of the oil pump nut"
        ans_b = "Torque of rod nuts"
        ans_c = "Installing pistons"
        ans_d = "Installing cylinder heads"
        true_ans_letter = "a"
        ask_question()
    elif rand_int == 97:
        question = "During the Assembly Phase, when is it required to use a pry bar?"
        ans_a = "Torque of cylinder heads"
        ans_b = "Torque of timing chain cover"
        ans_c = "Torque of oil pan"
        ans_d = "Torque of cam gear bolts"
        true_ans_letter = "d"
        ask_question()
    elif rand_int == 98:
        question = "During the Assembly Phase, when is it NOT required to use a pry bar?"
        ans_a = "Torque of harmonic balancer bolt"
        ans_b = "Torque of the oil pump nut"
        ans_c = "De-Torque of the harmonic balancer bolt"
        ans_d = "None of the Above"
        true_ans_letter = "c"
        ask_question()
    elif rand_int == 99:
        question = "How many fasteners does the Oil Pan have?"
        ans_a = "17"
        ans_b = "16"
        ans_c = "15"
        ans_d = "19"
        true_ans_letter = "a"
        ask_question()
    elif rand_int == 100:
        question = "How many fasteners does one Cylinder Head have?"
        ans_a = "15"
        ans_b = "17"
        ans_c = "18"
        ans_d = "16"
        true_ans_letter = "b"
        ask_question()
    elif rand_int == 101:
        question = "How many fasteners does Timing Cover have?"
        ans_a = "9"
        ans_b = "10"
        ans_c = "8"
        ans_d = "11"
        true_ans_letter = "b"
        ask_question()
# Questions 102 through 137 will be on the 2023 Hot Rodders of Tomorrow Rulebook. Please answer correctly.
    elif rand_int == 102:
        question = "According to the 2023 Hot Rodders of Tomorrow Rule Book, Which tool is NOT approved?"
        ans_a = "Torque Sticks"
        ans_b = "Screw Driver"
        ans_c = "Speed Handle"
        ans_d = "Wobble Extensions"
        true_ans_letter = "a"
        ask_question()
    elif rand_int == 103:
        question = "According to the 2023 Hot Rodders of Tomorrow Rule Book, Which tool is NOT approved?"
        ans_a = '12" Breaker Bar'
        ans_b = "Ratchet Wrench"
        ans_c = "Speed Handle"
        ans_d = "Needle Nose Pliers"
        true_ans_letter = "b"
        ask_question()
    elif rand_int == 104:
        question = "According to the 2023 Hot Rodders of Tomorrow Rule Book, Which tool is approved?"
        ans_a = "Yankee type Screw Drivers"
        ans_b = "Grip Enhancers"
        ans_c = "Rolling Carts or Trays"
        ans_d = "Open and combination wrenches"
        true_ans_letter = "d"
        ask_question()
    elif rand_int == 105:
        question = "According to the 2023 Hot Rodders of Tomorrow Rule Book, Which tool is approved?"
        ans_a = "T-Bars"
        ans_b = "Yankee type screw drivers"
        ans_c = "Magnetic Tray(s)"
        ans_d = 'Spark Plug Socket Longer than 4"'
        true_ans_letter = "c"
        ask_question()
    elif rand_int == 106:
        question = "Before the engine is completely assembled, the valve train must be properly adjusted. Which component must NOT be installed before beginning the valve adjustment"
        ans_a = "Valve Covers"
        ans_b = "Piston and Rod Assembly"
        ans_c = "Timing Chain and Gears"
        ans_d = "Cylinder Heads"
        true_ans_letter = "a"
        ask_question()
    elif rand_int == 107:
        question = "Before the engine is completely assembled, the valve train must be properly adjusted. Which component must be installed before beginning the valve adjustment"
        ans_a = "Intake Manifold"
        ans_b = "Headers"
        ans_c = "Spark Plugs"
        ans_d = "Lifters"
        true_ans_letter = "d"
        ask_question()
    elif rand_int == 108:
        question = "All engine components must be removed separately. Which component will remain on the Cylinder Head?"
        ans_a = "Lifters"
        ans_b = "Intake Valves"
        ans_c = "Rocker Arms"
        ans_d = "Rocker Arm Nuts"
        true_ans_letter = "b"
        ask_question()
    elif rand_int == 109:
        question = "All engine components must be removed separately. Which component will remain on the Cylinder Head?"
        ans_a = "Head Bolts"
        ans_b = "Push Rods"
        ans_c = "Spark Plugs"
        ans_d = "Valve Springs"
        true_ans_letter = "d"
        ask_question()
    elif rand_int == 110:
        question = "With the number one piston at Top Dead Center (TDC) on Compression Stroke, which exhaust valve is adjusted?"
        ans_a = "#1"
        ans_b = "#2"
        ans_c = "#5"
        ans_d = "#6"
        true_ans_letter = "a"
        ask_question()
    elif rand_int == 111:
        question = "With the number one piston at Top Dead Center (TDC) on Compression Stroke, which intake valve is adjusted?"
        ans_a = "#8"
        ans_b = "#7"
        ans_c = "#6"
        ans_d = "#4"
        true_ans_letter = "b"
        ask_question()
    elif rand_int == 112:
        question = "With the number one piston at Top Dead Center (TDC) on Exhaust Stroke, which intake valve is adjusted?"
        ans_a = "#1"
        ans_b = "#2"
        ans_c = "#3"
        ans_d = "#5"
        true_ans_letter = "c"
        ask_question()
    elif rand_int == 113:
        question = "With the number one piston at Top Dead Center (TDC) on Compression Stroke, which intake valve is adjusted?"
        ans_a = "#3"
        ans_b = "#5"
        ans_c = "#6"
        ans_d = "None of the Above"
        true_ans_letter = "b"
        ask_question()
    elif rand_int == 114:
        question = "With the number one piston at Top Dead Center (TDC) on Exhaust Stroke, which exhaust valve is adjusted?"
        ans_a = "#2"
        ans_b = "#5"
        ans_c = "#6"
        ans_d = "All of the Above"
        true_ans_letter = "d"
        ask_question()
    elif rand_int == 115:
        question = "With the number one piston at Top Dead Center (TDC) on Exhaust Stroke, which exhaust valve is adjusted?"
        ans_a = "#1"
        ans_b = "#7"
        ans_c = "#3"
        ans_d = "#8"
        true_ans_letter = "b"
        ask_question()
    elif rand_int == 116:
        question = "Which fastener can a speed wrench be used on during assembly phase?"
        ans_a = "Oil Pan Nuts"
        ans_b = "Valve Cover Fasteners"
        ans_c = "Rocker Arm Nuts"
        ans_d = "Water Pump Bolts"
        true_ans_letter = "a"
        ask_question()
    elif rand_int == 117:
        question = "Which fastener can a speed wrench NOT be used in during the assembly phase?"
        ans_a = "Rocker Arm Nuts"
        ans_b = "Timing Cover Bolts"
        ans_c = "Oil Pan Nuts"
        ans_d = "Cylinder Head Bolts"
        true_ans_letter = "a"
        ask_question()
    elif rand_int == 118:
        question = "Team members use a torque wrnech to torque cylinder head bolts in the proper sequence. What is the meaning of torque?"
        ans_a = "Applied twisting force to an object"
        ans_b = "Tightening the fastener"
        ans_c = "Scale to measure weight"
        ans_d = "All of the above"
        true_ans_letter = "a"
        ask_question()
    elif rand_int == 119:
        question = "Why does torque matter?"
        ans_a = "To ensure that the fastener is snugged"
        ans_b = "To make sure each fastener is tightened correctly"
        ans_c = "To make sure the fasteners gets the proper stretch"
        ans_d = "None of the above"
        true_ans_letter = "c"
        ask_question()
    elif rand_int == 120:
        question = "Why are torque patterns required?"
        ans_a = "To distribute the gasket evenly to prevent gaps/wrinkles"
        ans_b = "Torqueing will look neat with the pattern"
        ans_c = "To make sure every fastener is NOT torqued"
        ans_d = "Prevent a fastener from cracking"
        true_ans_letter = "a"
        ask_question()
    elif rand_int == 121:
        question = "Which of the following gasket must be removed from the engine and placed on the bench?"
        ans_a = "Oil Pan Gasket"
        ans_b = "Carburetor Gasket"
        ans_c = "Valve Cover Gasket"
        ans_d = "Timing Chain Cover Gasket"
        true_ans_letter = "a"
        ask_question()
    elif rand_int == 122:
        question = "Which of the following gaskets must NOT be removed from the component/engine?"
        ans_a = "Header Gasket"
        ans_b = "Intake Gasket"
        ans_c = "Oil Pan Gasket"
        ans_d = "Carburetor Gasket"
        true_ans_letter = "d"
        ask_question()
    elif rand_int == 123:
        question = "Which of the following gasket must be removed from the engine/component and placed on the bench?"
        ans_a = "Water Pump Gasket"
        ans_b = "Cylinder Head Gasket"
        ans_c = "Timing Chain Cover Gasket"
        ans_d = "Valve Cover Gasket"
        true_ans_letter = "b"
        ask_question()
    elif rand_int == 124:
        question = 'A 12" or longer breaker bar or ratchet must be used to de-torque the following fasteners:'
        ans_a = "Head Nut/Bolts"
        ans_b = "Oil Pump Nut"
        ans_c = "Harmonic Balancer Bolt"
        ans_d = "All of The Above"
        true_ans_letter = "d"
        ask_question()
    elif rand_int == 125:
        question = "If a team damages or loses a component or fastener, the coach may call a timeout and request a replacement component of fastener. What is the penalty time for each occurence?"
        ans_a = "1 Minute"
        ans_b = "2 Minutes"
        ans_c = "4 Minutes"
        ans_d = "6 Minutes"
        true_ans_letter = "a"
        ask_question()
    elif rand_int == 126:
        question = "Torque wrenches may NOT be placed on the following area(s):"
        ans_a = "Padded Tray"
        ans_b = "On The Floor"
        ans_c = "On The Bench"
        ans_d = "None of the Above"
        true_ans_letter = "b"
        ask_question()
    elif rand_int == 127:
        question = "During the assembly phase, how many degrees apart do the piston rings get clocked at?"
        ans_a = "90 Degrees"
        ans_b = "45 Degrees"
        ans_c = "180 Degrees"
        ans_d = "360 Degrees"
        true_ans_letter = "c"
        ask_question()
    elif rand_int == 128:
        question = "When installing the piston and rod assembly, what is the purpose for using rod bolt protectors?"
        ans_a = "Protect the Rod bolts from falling"
        ans_b = "Protect the rod bearings from being damaged"
        ans_c = "Protect cylinder walls and crack journals from being scratched"
        ans_d = "Protect the piston skirt from cracking"
        true_ans_letter = "c"
        ask_question()
    elif rand_int == 129:
        question = "Why is it required to clock the piston rings at 180 degrees?"
        ans_a = "To keep the gaps away from each other"
        ans_b = "To keep anti-freeze out of the combustion chamber"
        ans_c = "To keep oil from bypassing into the combustion chamber easily"
        ans_d = "To prevent water from bypassing into the combustion chamber"
        true_ans_letter = "c"
        ask_question()
    elif rand_int == 130:
        question = "During competition, why is it required to wear helmets and safety glasses?"
        ans_a = "Helmets are worn to prevent neck injury. Safety glasses are worn to prevent facial injury"
        ans_b = "Helmets are worn to protect your head from injury. Safety glasses are worn to protect your eyes from injury"
        ans_c = "Helmets and safety glasses are worn to remind the students that they are competing."
        ans_d = "Helmets are worn to protect your head from injury. Safety glasses are worn to provoke your eyes from injury."
        true_ans_letter = "b"
        ask_question()
    elif rand_int == 131:
        question = "Why is it required to hand start all fasteners?"
        ans_a = "Prevents threads from stripping/cross threading"
        ans_b = "Confirms that the team has all of the correct fasteners"
        ans_c = "To ensure proper alignmnet of the component"
        ans_d = "All of the above"
        true_ans_letter = "d"
        ask_question()
    elif rand_int == 132:
        question = "During competition in the disassembly phase, why is it required to do 5 full turns on the balancer puller bolts?"
        ans_a = "On an engine that the balancer is not honed, you would have to turn at least 5 full turns to remove the balancer from the crankshaft"
        ans_b = "To make sure the bolts are engaged"
        ans_c = "To prevent the threads from falling"
        ans_d = "None of the above"
        true_ans_letter = "a"
        ask_question()
    elif rand_int == 133:
        question = 'What is the significance of putting the timing gears "dot to dot"?'
        ans_a = "The crankshaft will be at 180 degrees"
        ans_b = "The camshaft will be at the right position to install pistons"
        ans_c = "The camshaft and the crankshaft will have the correct timing"
        ans_d = "All of the above"
        true_ans_letter = "c"
        ask_question()
    elif rand_int == 134:
        question = "When removing pistons and the rod assembly, where must the rod cap and piston NOT be placed once it has been removed?"
        ans_a = "Piston Rack"
        ans_b = "Tray"
        ans_c = "Bench"
        ans_d = "Floor"
        true_ans_letter = "d"
        ask_question()
    elif rand_int == 135:
        question = "Students and instructors must be how many yards away from the event before using any tobacco or electronic smoking products?"
        ans_a = "50 yards"
        ans_b = "75 yards"
        ans_c = "100 yards"
        ans_d = "25 yards"
        true_ans_letter = "c"
        ask_question()
    elif rand_int == 136:
        question = "Torque wrenches may NOT be placed on the following area(s):"
        ans_a = "Padded Tray"
        ans_b = "On The Floor"
        ans_c = "On The Bench"
        ans_d = "None of the Above"
        true_ans_letter = "b"
        ask_question()
    elif rand_int == 137:
        question = "What is the maximum amount of torque wrenches that will be allowed to have on the bench during competition?"
        ans_a = "2"
        ans_b = "3"
        ans_c = "4"
        ans_d = "6"
        true_ans_letter = "d"
        ask_question()
    elif rand_int == 138:
        question = "What is a protective device that will allow opening and closing when current draw becomes excessive?"
        ans_a = "Fuse"
        ans_b = "Circuit Breaker"
        ans_c = "Insulator"
        ans_d = "Fusable Link"
        true_ans_letter = "b"
        ask_question()
    elif rand_int == 139:
        question = "What is a special calibrated wire installed into a harness that is designed to protect the circuit from an overload?"
        ans_a = "Circuit Breaker Wire"
        ans_b = "Fuse"
        ans_c = "Fusible Link"
        ans_d = "Insulator"
        true_ans_letter = "c"
        ask_question()
    elif rand_int == 140:
        question = "What is made of plastic, rubber, and ceramics that can resist the flow of electricity?"
        ans_a = "Circuit Breaker"
        ans_b = "Fuse"
        ans_c = "Insulator"
        ans_d = "Fusable Link"
        true_ans_letter = "c"
        ask_question()
    elif rand_int == 141:
        question = "What is the movement of electrons from atom to atom called?"
        ans_a = "Fuse"
        ans_b = "Electricity"
        ans_c = "Current"
        ans_d = "Voltage"
        true_ans_letter = "b"
        ask_question()
    elif rand_int == 142:
        question = "What is the flow of electrons called?"
        ans_a = "Current"
        ans_b = "Circuit"
        ans_c = "Voltage"
        ans_d = "Ground"
        true_ans_letter = "a"
        ask_question()
    elif rand_int == 143:
        question = "What is needed to control the flow of current in a circuit?"
        ans_a = "Fuse"
        ans_b = "Current"
        ans_c = "Circuit"
        ans_d = "Voltage"
        true_ans_letter = "d"
        ask_question()
    elif rand_int == 144:
        question = "What protects a circuit against damage caused by a short circuit?"
        ans_a = "Series Circuit"
        ans_b = "Current"
        ans_c = "Fuse"
        ans_d = "Ground"
        true_ans_letter = "c"
        ask_question()
# Use Ohm's Law for questions 145 through 148. Please answer correctly.
    elif rand_int == 145:
        question = "If a circuit has 12 volts and 2 Ohms, what is the current in this circuit?"
        ans_a = "24 amps"
        ans_b = "4 amps"
        ans_c = "8 amps"
        ans_d = "6 amps"
        true_ans_letter = "d"
        ask_question()
    elif rand_int == 146:
        question = "If a ciruit has 12 volts and 2 amps, what is the resistance in this circuit?"
        ans_a = "24 ohms"
        ans_b = "6 ohms"
        ans_c = "4 ohms"
        ans_d = "8 ohms"
        true_ans_letter = "b"
        ask_question()
    elif rand_int == 147:
        question = "If a circuit had 3 amps and 2 ohms, what is the voltage in this circuit?"
        ans_a = "6 volts"
        ans_b = "3 volts"
        ans_c = "3 volts"
        ans_d = "6.2 volts"
        true_ans_letter = "a"
        ask_question()
    elif rand_int == 148:
        question = "If a ciruit has 12 amps and 6 ohms, what is the voltage in this circuit?"
        ans_a = "2 volts"
        ans_b = "18 volts"
        ans_c = "72 volts"
        ans_d = "6 volts"
        true_ans_letter = "c"
        ask_question()
    elif rand_int == 149:
        question = "The power in watts is equal to the voltage in volts, times the current in amps. If a circuit has 12 volts and 3 amps, what is the power in this circuit?"
        ans_a = "3 watts"
        ans_b = "4 watts"
        ans_c = "15 watts"
        ans_d = "36 watts"
        true_ans_letter = "d"
        ask_question()
    elif rand_int == 150:
        question = "The power in watts is equal to the voltage in volts, times the current in amps. If a circuit has 6 volts and 2 amps, what is the power in this circuit?"
        ans_a = "3 watts"
        ans_b = "4 watts"
        ans_c = "8 watts"
        ans_d = "12 watts"
        true_ans_letter = "d"
        ask_question()
    elif rand_int == 151:
        question = "The power in watts is equal to the voltage in volts, times the current in amps. If a circuit has 11volts and 3 amps, what is the power in this circuit?"
        ans_a = "33 watts"
        ans_b = "14 watts"
        ans_c = "9 watts"
        ans_d = "4 watts"
        true_ans_letter = "a"
        ask_question()
# Questions 152 through 172 will be on General Automotive. Please answer correctly.
    elif rand_int == 152:
        question = "Building an engine to an exacting set of specifications is called:"
        ans_a = "Balancing"
        ans_b = "Decking"
        ans_c = "Blueprinting"
        ans_d = "None of the above"
        true_ans_letter = "c"
        ask_question()
    elif rand_int == 153:
        question = "Align boring is done:"
        ans_a = "To make crankshaft parallel to camshaft"
        ans_b = "To correct cylinder out of round"
        ans_c = "To correct cylinder taper"
        ans_d = "All of the above"
        true_ans_letter = "a"
        ask_question()
    elif rand_int == 154:
        question = "When applying cross hatch to a cylinder you would use a:"
        ans_a = "Bench grinder"
        ans_b = "File"
        ans_c = "Emery cloth"
        ans_d = "Hone"
        true_ans_letter = "d"
        ask_question()
    elif rand_int == 155:
        question = "Why are main bearings made of soft metal?"
        ans_a = "To accept dirt"
        ans_b = "Soft to conform to crankshaft journal"
        ans_c = "All of the above"
        ans_d = "None of the above"
        true_ans_letter = "c"
        ask_question()
    elif rand_int == 156:
        question = "What is used to measure a cylinder bore accurately?"
        ans_a = "Micrometer"
        ans_b = "Gauge"
        ans_c = "Dial-Bore Gauge"
        ans_d = "None of the above"
        true_ans_letter = "c"
        ask_question()
    elif rand_int == 157:
        question = "To measure piston to valve clearance you would use:"
        ans_a = "CC burette"
        ans_b = "Modeling clay"
        ans_c = "Dial bore guage"
        ans_d = "Deck gauge"
        true_ans_letter = "b"
        ask_question()
    elif rand_int == 158:
        question = "The tool used to measure crankshaft main journal taper is a _______________."
        ans_a = "Dial bore gauge"
        ans_b = "Micrometer"
        ans_c = "Telescoping gauge"
        ans_d = "Dial indicator"
        true_ans_letter = "b"
        ask_question()
    elif rand_int == 159:
        question = "What is the firing order for an in-line four cylinder?"
        ans_a = "3-2-4-1"
        ans_b = "4-3-2-1"
        ans_c = "1-3-4-2"
        ans_d = "2-4-3-1"
        true_ans_question = "c"
        ask_question()
    elif rand_int == 160:
        question = "1,8,4,3,6,5,7,2 is the_______ of a small block Chevy 350?"
        ans_a = "Intake torque sequence"
        ans_b = "Cylinder head trque sequence"
        ans_c = "Rod cap torque sequence"
        ans_d = "Firing order"
        true_ans_letter = "d"
        ask_question()
    elif rand_int == 161:
        question = "If the air-fuel mixture in a engine is too rich, what is the air-fuel ratio?"
        ans_a = "14:1"
        ans_b = "10:1"
        ans_c = "28:2"
        ans_d = "17:1"
        true_ans_letter = "b"
        ask_question()
    elif rand_int == 162:
        question = "What is the main function of an intake manifold?"
        ans_a = "Distribute carbon monoxide equally to the cylinders"
        ans_b = "Distribute air and fuel equally to the cylinders"
        ans_c = "Clean the air before it mixes with the fuel"
        ans_d = "Distribute air into each cylinder head"
        true_ans_letter = "b"
        ask_question()
    elif rand_int == 163:
        question = "White smoke is coming from the tail pipe? What would cause this?"
        ans_a = "Defective water pump"
        ans_b = "Thermostat is stuck open"
        ans_c = "Coolant leaking into the combustion chamber"
        ans_d = "Restrictions in the cooling system"
        true_ans_letter = "c"
        ask_question()
    elif rand_int == 164:
        question = "How often do you need to change most vehicles' engine oil?"
        ans_a = "3,000 Miles"
        ans_b = "30,000 Miles"
        ans_c = "3 Weeks"
        ans_d = "300 Miles"
        true_ans_letter = "a"
        ask_question()
    elif rand_int == 165:
        question = 'In 10W-30 Motor oil, what does the "W" stand for stand for?'
        ans_a = "West"
        ans_b = "Winter"
        ans_c = "Weight"
        ans_d = "Width"
        true_ans_letter = "b"
        ask_question()
    elif rand_int == 166:
        question = "The effect of having excess camber is?"
        ans_a = "Uneven tire wear"
        ans_b = "Even tire wear"
        ans_c = "Increases a smooth ride"
        ans_d = "Decreases tire wear"
        true_ans_letter = "a"
        ask_question()
    elif rand_int == 167:
        question = "The difference between DOT 3 and DOT 4 brake fluids is?"
        ans_a = "DOT 4 fluid has a higher boiling point than DOT 3"
        ans_b = "DOT 3 fluid has a higher boiling point than DOT 4 fluid"
        ans_c = "DOT 3 fluid has a higher viscosity than DOT 4 fluid"
        ans_d = "DOT 4 fluid has a higher viscosity than DOT 3 fluid"
        true_ans_letter = "a"
        ask_question()
    elif rand_int == 168:
        question = "What is the main reason(s) for a cooling system in the engine?"
        ans_a = "Remove unwanted heat"
        ans_b = "Maintain operating temp"
        ans_c = "Bring engine up to operating temp"
        ans_d = "All of the above"
        true_ans_letter = "d"
        ask_question()
    elif rand_int == 169:
        question = "Please define the following vocabulary word: Aerodynamics"
        ans_a = "A device for measuring mechanical air force"
        ans_b = "Created when a vehicle corners that tends to push a vehicle sideways"
        ans_c = "The amount the intake amnifold can filter"
        ans_d = "The study of the effects of air resistance and lift on vehicles"
        true_ans_letter = "d"
        ask_question()
    elif rand_int == 170:
        question = "Please define the following vocabulary word: Air Capacity"
        ans_a = "The amount the intake manifold can filter"
        ans_b = "The volume displaced on intake strokes during each crankshaft revolution"
        ans_c = "The maesurement of effectiveness of a machine's energy and power"
        ans_d = "A device for measuring mechanical air force"
        true_ans_letter = "b"
        ask_question()
    elif rand_int == 171:
        question = "Technician A says nitrous oxide is a fuel. Technician B says nitrous oxide is flammable. Who is correct?"
        ans_a = "Technician A"
        ans_b = "Technician B"
        ans_c = "Both Technicians A and B"
        ans_d = "Neither Technician A nor B"
        true_ans_letter = "d"
        ask_question()
    elif rand_int == 172:
        question = "Technician A says stroke impacts the compression ratio. Technician B says the head gasket thickness impacts the compression ratio. Who is correct?"
        ans_a = "Technician A"
        ans_b = "Technician B"
        ans_c = "Both Technicians A and B"
        ans_d = "Neither Technician A nor B"
        true_ans_letter = "c"
        ask_question()
# After this, to 236, the questions should use pictures to help you identify tools and items. I don't know how to add pictures in.
# Perhaps with more time. This is just a passion project to create skills after all.
    elif rand_int == 173:
        question = "I can't really put the identification section in this, but you will study it right?\nIt is questions 173 to 236 in your packet.\nMaybe when I have the time, I will then add in these questions."
        ans_a = "Yes"
        ans_b = "No"
        ans_c = ""
        ans_d = ""
        true_ans_letter = "a"
        ask_question()
    # The catch-all for if the generator somehow returns a question outside the parameters. It shouldn't, but just in case.
    else:
        print("Sorry, your number has not been programmed yet. How did you get here? The program shouldn't let you get here.")
    # The code that gets called for the user to get their score if they want it. I put it like this so it is easier to change the scoring system as wanted.
    def track_score():
        score_lock = "Y"
        while score_lock == "Y":
            print(f"\nGood job! You have worked on {amount} questions this session!")
            show_score = input("\nWould you like to see your current score? Y/N ")
            # User decides to get their score.
            if show_score.lower().strip() == "y" or show_score.lower().strip() == "yes":
                print(f"You have {wrong} questions wrong and {correct} questions right.\nThis causes you to have a score of {(correct / amount) * 100}%.")
                score_lock = "X"
                continue
            # User decides to skip their score.
            elif show_score.lower().strip() == "n" or show_score.lower().strip() == "no":
                score_lock = "X"
                continue
            # User fails to enter a proper answer.
            else:
                print("Please enter 'Yes' or 'No'. You can also use 'Y' or 'N'.")
    # Calls the score function every ten questions up to 200.
    if amount == 10 or amount == 20 or amount == 30 or amount == 40 or amount == 50 or amount == 60 or amount == 70 or amount == 80 or amount == 90 or amount == 100 or amount == 110 or amount == 120 or amount == 130 or amount == 140 or amount == 150 or amount == 160 or amount == 170 or amount == 180 or amount == 190 or amount == 200:
        # Gives a special message for reaching 200 questions.
        if amount == 200:
            print("\nGood job! You have correctly solved 200 questions this session!\n This is the final progress check for the system! Incredible!")
        track_score()
    cont = "Y"
    # Allows the user to decide of they want to do another question or exit the program.
    while cont == "Y":
        again = input("\nContinue? Y/N: ")
        if again.lower().strip() == "y" or again.lower().strip() == "yes":
            cont = "X"
            continue
        elif again.lower().strip() == "n" or again.lower().strip() == "no":
            exit()
            break
        else:
            print("Please enter 'Yes' or 'No'. You can also use 'Y' or 'N'.")