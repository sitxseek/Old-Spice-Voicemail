'''
    File name: voicemail.py
    Author: Yangzong Guo
    Date created: 11/30/2016
    Date last modified: 12/04/2016
    Python Version: 3.5.2
'''
import urllib.request
import os
import getopt, sys
import platform
#added a comment (practicing git)
#counts the number of digits in a string
def numOfDigits(inputString):
    count = 0
    for n in inputString:
        if n.isdigit():
            count += 1
    return count

#checks if a string contains letters
def hasLetters(inputString):
    return any(c.isalpha() for c in inputString)

#checking if program is running on Mac or Windows
platform = platform.system() #platform == 'Darwin' if running on a Mac

#checking for command line arguments.. go into 'if' when one or more arguments detected
if len(sys.argv) > 1:
    gender = ''
    number = ''
    greeting = []
    digits = []
    reason = []
    ending = []
    fname = ''
    #read command line args
    myopts, args = getopt.getopt(sys.argv[1:],"g:n:r:e:o:")
    #o == option
    #a == argument passed to the o
    for o, a in myopts:
        if o == '-g':
            gender = a
        elif o == '-n':
            number = a
            for x in a:
                #if x is a digit, add filename to digits list
                if x.isdigit():
                    digits.append(x + ".mp3")
        elif o == '-r':
            #if gender is male, add nonoptional greetings to greeting list and non optional reason to reason list
            if gender == 'm' or gender == 'male':
                greeting.append("m-b1-hello.mp3")
                greeting.append("m-b2-have_dialed.mp3")
                reason.append("m-r0-cannot_come_to_phone.mp3")
                #add specified reasons to reason list
                for x in a:
                    if x == "1":
                        reason.append("m-r1-building.mp3")
                    elif x == "2":
                        reason.append("m-r2-cracking_walnuts.mp3")
                    elif x == "3":
                        reason.append("m-r3-polishing_monocole.mp3")
                    elif x == "4":
                        reason.append("m-r4-ripping_weights.mp3")
            #if gender is female, add nonoptional greetings to greeting list and non optional reason to reason list
            elif gender == 'f' or gender == 'female':
                greeting.append("f-b1-hello_caller.mp3")
                greeting.append("f-b2-lady_at.mp3")
                reason.append("f-r0.1-unable_to_take_call.mp3")
                reason.append("f-r0.2-she_is_busy.mp3")
                #add specified reasons to reason list
                for x in a:
                    if x == "1":
                        reason.append("f-r1-ingesting_old_spice.mp3")
                    elif x == "2":
                        reason.append("f-r2-listening_to_reading.mp3")
                    elif x == "3":
                        reason.append("f-r3-lobster_dinner.mp3")
                    elif x == "4":
                        reason.append("f-r4-moon_kiss.mp3")
                    elif x == "5":
                        reason.append("f-r5-riding_a_horse.mp3")

        elif o == '-e':
            if gender == 'm' or gender == 'male':
                #adding specified male endings to ending list
                for x in a:
                    if x == "1":
                        ending.append("m-e1-horse.mp3")
                    elif x == "2":
                        ending.append("m-e2-jingle.mp3")
                    elif x == "3":
                        ending.append("m-e3-on_phone.mp3")
                    elif x == "4":
                        ending.append("m-e4-swan_dive.mp3")
                    elif x == "5":
                        ending.append("m-e5-voicemail.mp3")
                #ending.append("m-leave_a_message.mp3")
            elif gender == 'f' or gender == 'female':
                #adding specified female endings to ending list
                for x in a:
                    if x == "1":
                        ending.append("f-e1-she_will_get_back_to_you.mp3")
                    elif x == "2":
                        ending.append("f-e2-thanks_for_calling.mp3")
        elif o == '-o':
            #settings output filename
            fname = a
#if no command line arguments were detected, enter 'else' condition
else:
    #restart program until the user confirms settings
    confirmed = False
    while not confirmed:
        #asking user for gender preference and phone number
        gender = input("Would you like the male or female voice?(male/female): ")
        #ask the user again if he/she enters something else
        while gender != 'male' and gender != 'female' and gender != 'm' and gender != 'f':
            gender = input("Please enter 'male' or 'female': ")

        number = input("Enter your phone number: ")
        #ask user again if phone number contains letters
        while hasLetters(number) or not number or numOfDigits(number) != 10:
            number = input("Please enter a valid phone number (e.g 555-555-5555): ")

        greeting = []
        digits = []
        reason = []
        ending = []
        #looping through the phone number and extracting only the digits
        for x in number:
            #if character is a number, append to the list digits
            if x.isdigit():
                digits.append(x + ".mp3")

        #asking user to choose the reasons and endings they want based on specified gender
        if gender == "male" or gender == 'm':
            #adding non optional greeting mp3 files to list greeting and reason mp3 files to reason list
            greeting.append("m-b1-hello.mp3")
            greeting.append("m-b2-have_dialed.mp3")
            reason.append("m-r0-cannot_come_to_phone.mp3")
            print(
            "[1] Building\n"
            "[2] Cracking walnuts\n"
            "[3] Polishing monocole\n"
            "[4] Ripping weights"
            )
            reasons = input("Enter the reasons you want in your voice mail (numbers 1-4): ")
            #make sure reasons only contains numbers between 1-4
            while hasLetters(reasons) or '5' in reasons or '6' in reasons or '7' in reasons or '8' in reasons or '9' in reasons or '0' in reasons or not reasons:
                reasons = input("Please only enter numbers between 1-4: ")
            #appending the mp3 filenames to reason list
            for num in reasons:
                if num == "1":
                    reason.append("m-r1-building.mp3")
                elif num == "2":
                    reason.append("m-r2-cracking_walnuts.mp3")
                elif num == "3":
                    reason.append("m-r3-polishing_monocole.mp3")
                elif num == "4":
                    reason.append("m-r4-ripping_weights.mp3")

            print(
            "[1] Horse\n"
            "[2] Jingle\n"
            "[3] On phone\n"
            "[4] Swan dive\n"
            "[5] Voicemail"
            )
            endings = input("Enter the endings you want in your voice mail (numbers 1-5): ")
            #make sure endings only contains numbers between 1-5
            while hasLetters(endings) or '6' in endings or '7' in endings or '8' in endings or '9' in endings or '0' in endings or not endings:
                endings = input("Please only enter numbers between 1-5: ")
            #appending to mp3 filenames to ending list
            for num in endings:
                if num == "1":
                    ending.append("m-e1-horse.mp3")
                elif num == "2":
                    ending.append("m-e2-jingle.mp3")
                elif num == "3":
                    ending.append("m-e3-on_phone.mp3")
                elif num == "4":
                    ending.append("m-e4-swan_dive.mp3")
                elif num == "5":
                    ending.append("m-e5-voicemail.mp3")
            #print summary
            print(
            "Your settings\n"
            "Gender: " + gender + "\n"
            "Number: " + number + "\n"
            "Reasons: " + reasons + "\n"
            "Endings: " + endings
            )
            #ask user for confirmation. If user types "yes", exit the while loop
            confirmation = input("Confirm these settings?(yes/no): ")
            if confirmation == "yes":
                confirmed = True
            else:
                confirmed = False
        #female option
        elif gender == 'female' or gender == 'f':
            #adding non optional greeting mp3 files to greeting list and reason mp3 files to reason list
            greeting.append("f-b1-hello_caller.mp3")
            greeting.append("f-b2-lady_at.mp3")
            reason.append("f-r0.1-unable_to_take_call.mp3")
            reason.append("f-r0.2-she_is_busy.mp3")
            print(
            "[1] Ingesting old spice\n"
            "[2] listening to reading\n"
            "[3] Lobster dinner\n"
            "[4] Moon kiss\n"
            "[5] Riding a horse"
            )
            reasons = input("Enter the reasons you want in your voice mail (numbers 1-5): ")
            #make sure reasons only contains numbers between 1-5
            while hasLetters(reasons) or '6' in reasons or '7' in reasons or '8' in reasons or '9' in reasons or '0' in reasons or not reasons:
                reasons = input("Please only enter numbers between 1-5: ")
            #appending to mp3 filenames to reason list
            for num in reasons:
                if num == "1":
                    reason.append("f-r1-ingesting_old_spice.mp3")
                elif num == "2":
                    reason.append("f-r2-listening_to_reading.mp3")
                elif num == "3":
                    reason.append("f-r3-lobster_dinner.mp3")
                elif num == "4":
                    reason.append("f-r4-moon_kiss.mp3")
                elif num == "5":
                    reason.append("f-r5-riding_a_horse.mp3")

            print(
            "[1] She will get back to you\n"
            "[2] Thanks for calling"
            )
            endings = input("Enter the endings you want in your voice mail (numbers 1-2): ")
            #make sure endings only contains numbers between 1-2
            while hasLetters(endings) or '3' in endings or '4' in endings or '5' in endings or '6' in endings or '7' in endings or '8' in endings or '9' in endings or '0' in endings or not endings:
                endings = input("Please only enter numbers between 1-2: ")
            #appending mp3 filenames to ending list
            for num in endings:
                if num == "1":
                    ending.append("f-e1-she_will_get_back_to_you.mp3")
                elif num == "2":
                    ending.append("f-e2-thanks_for_calling.mp3")
            #printing summary
            print(
            "Your settings\n"
            "Gender: " + gender + "\n"
            "Number: " + number + "\n"
            "Reasons: " + reasons + "\n"
            "Endings: " + endings
            )
            #ask user for confirmation. If user types "yes", exit while loop
            confirmation = input("Confirm these settings?(yes/no): ")
            if confirmation == "yes" or confirmation == 'y':
                confirmed = True
            else:
                confirmed = False

    #asking user for filename
    fname = input("What do you want the file to be called? ")


#combining the greeting mp3 files into one string. Also downloading the mp3 files at the same time
greetingCommand = ""
for num in greeting:
    #Mac option
    if platform == 'Darwin':
        try:
            #retrieving 'num', which is a string for the mp3 filename and naming it 'num'
            urllib.request.urlretrieve('http://www-bcf.usc.edu/~chiso/itp125/project_version_1/' + num, num)
            #concatenating 'num' with 'greetingCommand'
            greetingCommand = greetingCommand + num + " "
        except urllib.error.HTTPError as err:
            print(error.code)
    #Windows option
    else:
        try:
            urllib.request.urlretrieve('http://www-bcf.usc.edu/~chiso/itp125/project_version_1/' + num, num)
            greetingCommand = greetingCommand + num + " + "
        except urllib.error.HTTPError as err:
            print(error.code)

#truncating extra space and plus sign for windows greeting
if platform != 'Darwin':
    greetingCommand = greetingCommand[:-2]

#concatenating the digit mp3 files into one string. Also downloading the mp3 files at the same time
digitCommand = ""
for num in digits:
    if platform == 'Darwin':
        try:
            urllib.request.urlretrieve('http://www-bcf.usc.edu/~chiso/itp125/project_version_1/' + num, num)
            digitCommand = digitCommand + num + " "
        except urllib.error.HTTPError as err:
            print(error.code)
    else:
        try:
            urllib.request.urlretrieve('http://www-bcf.usc.edu/~chiso/itp125/project_version_1/' + num, num)
            digitCommand = digitCommand + num + " + "
        except urllib.error.HTTPError as err:
            print(error.code)

#truncating extra space and plus sign for windows greeting
if platform != 'Darwin':
    digitCommand = digitCommand[:-2]

#concatenating the reason mp3 files into one string. Also downloading the mp3 files at the same time
reasonCommand = ""
for num in reason:
    if platform == 'Darwin':
        try:
            urllib.request.urlretrieve('http://www-bcf.usc.edu/~chiso/itp125/project_version_1/' + num, num)
            reasonCommand = reasonCommand + num + " "
        except urllib.error.HTTPError as err:
            print(err.code)
    else:
        try:
            urllib.request.urlretrieve('http://www-bcf.usc.edu/~chiso/itp125/project_version_1/' + num, num)
            reasonCommand = reasonCommand + num + " + "
        except urllib.error.HTTPError as err:
            print(error.code)

#truncating extra space and plus sign for windows greeting
if platform != 'Darwin':
    reasonCommand = reasonCommand[:-2]

#concatenating the ending mp3 files into one string. Also downloading the mp3 files at the same time
endingCommand = ""
for num in ending:
    if platform == 'Darwin':
        try:
            urllib.request.urlretrieve('http://www-bcf.usc.edu/~chiso/itp125/project_version_1/' + num, num)
            endingCommand = endingCommand + num + " "
        except urllib.error.HTTPError as err:
            print(error.code)
    else:
        try:
            urllib.request.urlretrieve('http://www-bcf.usc.edu/~chiso/itp125/project_version_1/' + num, num)
            endingCommand = endingCommand + num + " + "
        except urllib.error.HTTPError as err:
            print(error.code)

#truncating extra space and plus sign for windows greeting
if platform != 'Darwin':
    endingCommand = endingCommand[:-2]

#combining mp3 using the strings generated above
if platform == 'Darwin':
    os.system("cat " + str(greetingCommand) + str(digitCommand) + str(reasonCommand) + str(endingCommand) + "> " + str(fname) + ".mp3")
else:
    os.system("copy /b " + str(greetingCommand) + str(digitCommand) + str(reasonCommand) + str(endingCommand) + "c:\\" + str(fname) + ".mp3")

#removing mp3 files
for n in greeting:
    os.remove(n)

for n in reason:
    os.remove(n)

for n in digits:
    #in case there are multiple instances of a same digit, check if the digit has been removed already
    if os.path.exists(str(n)):
        os.remove(n)

for n in ending:
    os.remove(n)

#writing list of mp3 files to mp3list.txt
try:
    #appending to file. Will create mp3list.txt if it does not exist
    with open("mp3list.txt", "a") as myfile:
        myfile.write(str(gender) + " " + str(number) + " " + str(digitCommand) + str(greetingCommand) + str(reasonCommand) + str(endingCommand) + '\n' + '\n')
except IOError:
    print("Unable to write to file.")
