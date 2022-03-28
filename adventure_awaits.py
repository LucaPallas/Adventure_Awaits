import sys

# Used the name 'ascii_wizard' rather than just 'wizard' to more accurately describe what the function is about.
# Used a function to do this as there are two places the ascii_art wizard would have been placed so by doing it as a function it reduces repeated code.
def ascii_wizard():

    # Used 'format' as it accurately describes what the contained constants do. Alternatives could be 'style' or 'font'.
    # Used a class to contain all the relevant formating strings to make adding colours or styles to string outputs easier without having to remeber the string values and repeating code.
    class format:

    # Used constants as these should not change throught the code and used the colour/format names as easiest to use. 'END' could alternatively be called 'CLEAR'.
        DARKCYAN = "\033[36m"
        PURPLE = "\033[95m"
        BLUE = "\033[94m"
        RED = "\033[91m"
        YELLOW = "\033[93m"
        GREEN = "\033[92m"
        BOLD = "\033[1m"
        UNDERLINE = "\033[4m"
        END = "\033[0m"

    # Used 'ascii_art' instead of 'message' as it hold strings specifically relating to the ascii art required in the project, rather than a general string text.
    ascii_art = format.PURPLE
    ascii_art += format.BOLD
    ascii_art += "\n                         ______\n"
    ascii_art += "                       .'* *.'\n"
    ascii_art += "                    __/_*_*(_\n"
    ascii_art += "                   / _______ \ \n"
    ascii_art += "                  _\_)/___\(_/_\n"
    ascii_art += "                 / _((\O O/))_ \ \n"
    ascii_art += "                 \ \())(-)(()/ /\n"
    ascii_art += "                  ' \(((()))/ '\n"
    ascii_art += "                 / ' \)).))/ ' \ \n"
    ascii_art += "               (   ( .;''';. .'  )\n"
    ascii_art += "               _\"__ /    )\ __\"/_\n"
    ascii_art += "                 \/  \   ' /  \/\n"
    ascii_art += "                  .'  '...' ' )\n"
    ascii_art += "                   / /  |  \ \ \n"
    ascii_art += "                  / .   .   . \ \n"
    ascii_art += "                 /   .     .   \ \n"
    ascii_art += "                /   /   |   \   \ \n"
    ascii_art += "             .'   /    b    '.  '.\n"
    ascii_art += "         _.-'    /     Bb     '-. '-._\n"
    ascii_art += "     _.-'       |      BBb       '-.  '-.\n"
    ascii_art += "    (___________\____.dBBBb.________)____)\n"
    ascii_art += format.END

    # Used imported method sys.stdout.write() instead of print() function as it is more efficient to use the imported method than to use the funtion plus have control over whether a new line is added or not.
    sys.stdout.write(ascii_art)

# Used 'display _list' as it most accurately describes the functions purpose. Alternative could be 'show_list'.
# Used as a function to reduce code repeat when wanting to display the contents of a list/lists.
def display_list(list:list):

    # Used 'format' as it accurately describes what the contained constants do. Alternatives could be 'style' or 'font'.
    # Used a class to contain all the relevant formating strings to make adding colours or styles to string outputs easier without having to remeber the string values and repeating code.
    class format:

    # Used constants as these should not change throught the code and used the colour/format names as easiest to use. 'END' could alternatively be called 'CLEAR'.
        DARKCYAN = "\033[36m"
        PURPLE = "\033[95m"
        BLUE = "\033[94m"
        RED = "\033[91m"
        YELLOW = "\033[93m"
        GREEN = "\033[92m"
        BOLD = "\033[1m"
        UNDERLINE = "\033[4m"
        END = "\033[0m"

    # Used 'index' as it is the list's index that the number is referencing. An alternative could be 'i' but it's not as informative.
    index = 0

    # Used while (index < len(list)) because the amount of records that will be in the list is unknown.
    # Used a while loop instead of a for loop, as for loops were outside the scopeof this projects functional requirements.
    while (index < len(list)):

        # Used 'record' as most accurate description, seeing as the variable will hold the record contained at that particular index. 'item' could also be used but less accurate.
        record = list[index]

        # Used 'message' rather than 'output' to make it a bit more descriptive of what the output is, which is a message to the user.
        message = format.RED
        message += record + "\n"
        message += format.END

        # Used imported method sys.stdout.write() instead of print() function as it is more efficient to use the imported method than to use the funtion plus have control over whether a new line is added or not.
        sys.stdout.write(message)
        index += 1

    

# Used 'select_reward' as the user gets to pick what type of reward they are getting e.g. Sword of Fire or Curse of Slow. An alternative name could be 'get_item_name', but that doesn't work as well for the Curses/Blessings.
# Used this as a function to reduce repeated code and increase reusability, as it allows for the program to be expanded to include more reward types through the 'type' parameter (.g. Necklace, Axe etc). This could have been called something more specific like 'weapon' but then would not allow for rewards such as armor or curses accurately. This function also allows the user to input the descriptor (e.g. Sword of 'Fire'), after which the full reward name is added to both the 'rewards' and 'total_rewards' lists, all while avoiding repeated code.
def select_reward(message_in:str, type:str, rewards:list, total_rewards:list):

    # Used 'message' rather than 'output' to make it a bit more descriptive of what the output is, which is a message to the user.
    message = message_in
    message += type
    message += " of _____ (Enter "
    message += type
    message += " type): "

    # Used imported method sys.stdout.write() instead of print() function as it is more efficient to use the imported method than to use the funtion plus have control over whether a new line is added or not.
    sys.stdout.write(message)

    # Used 'reward' as it describes what is being held in the variable well. Alternative could have been 'item' but as there are also Curses and Blessings, it didn't fit as well.
    reward = type 
    reward+= " of " 
    reward+=  sys.stdin.readline().strip()

    # Used to add string held in 'reward' to list 'rewards'.
    rewards.append(reward)

    # Used to add string held in 'reward' to list 'total_rewards'.
    total_rewards.append(reward)

    return rewards, total_rewards

# Used 'error_message' as it accurately describes the meaning of the function. 'display_error' would be a possible alternative.
# Used a function as error/exception handling was outside of the projects scope, so by providing a message letting the user know why they have missed out on a section due to incorrect input is the best alternative to doing so. 
# Had it take in parameters for the choice for which incorrect input was taken and the 'name' variable to increase the reusability.
# ** Note: due to note having input validation within the scope of this project, 'error_message()' will only trigger for the int and float variable 'if-elif-else' statements when the value does not fit the conditions. If it is instead a string/letter/symbol the program will simply freeze. **
def error_message(choice:str, name:str):

    # Used 'message' rather than 'output' to make it a bit more descriptive of what the output is, which is a message to the user.
    message = "\nSorry "
    message += name
    message += " but you have entered an invalid response for "
    message += choice
    message += ".\n"
    message += "For this section no items or spells will be rewarded.\n"

    # Used imported method sys.stdout.write() instead of print() function as it is more efficient to use the imported method than to use the funtion plus have control over whether a new line is added or not.
    sys.stdout.write(message)

# Used 'end_game' as it is used whn the user decides to end the game. Alternatives could be 'end_story' or 'final_message'.
# Used function because eventhough the code is not repeated as it provides a neat and efficient way to both display the records from 'total_rewards' along with the exit message, whilst also containg the code to see if the user wannts to play.
def end_game(name:str)->str:

    # Used 'message' rather than 'output' to make it a bit more descriptive what the output is, which is a message to the user.
    message = "\nWould you like to go on another adventure "
    message += name
    message += "? (Enter yes or no): "

    # Used imported method sys.stdout.write() instead of print() function as it is more efficient to use the imported method than to use the funtion plus have control over whether a new line is added or not.
    sys.stdout.write(message)
    
    # Used 'response' rather than 'reply' as the variable is containing the users response to the question asked, though 'reply' could also work.
    response = sys.stdin.readline().strip()

    # Used an 'if-else' statement as it is the easiest way to determine whether the user whichs to continue. The other alternative of a 'while' loop doesn't really work as this funtion already exists within a 'while' loop and we don't need it to repeat at least once.
    # Used 'if  (response == "yes" or response == "Yes" or response == "Y" or response == "y")' as it allows for a few combinations of respones a user may input to signify 'yes'. The response 'yes' is used as that is the condition used in the 'while' loop, so it makes more sense to check for that than for 'no'.
    if (response == "yes" or response == "Yes" or response == "Y" or response == "y"):

        # Used 'response_out' rather than just 'output' as it more accurately describes that it is an output tied with the external variable 'response'.
        response_out = "yes"

    # Used this to that any 'response' other than those given in the 'if' statement would trigger 'response_out' to be set to 'no' which would cause the external 'while' loop to be exited. 'response_out' doesn't need to be set to 'no', just set to a string value thats not 'yes', but 'no' is the most logical value to use, and makes debugging/variable tracking easier to follow.
    else:
        response_out = "no"

    return response_out

# Used 'main' as even though not a requirement for the main function to be called 'main' in Python, it generally is in other langages and wanted to keep with that convention.
def main():

    # Used 'rewards' as a plural of the variable 'reward' which are added into the list. Alternative could have been 'item/items' but as there are also Curses and Blessings, so that didn't fit as well.
    rewards = []

    # Used 'totsl_rewards' as it holds all the rewards the user collects before deciding to no longer continue their adventure. Alternative could have been 'item/tota;_items' but as there are also Curses and Blessings, so that didn't fit as well.
    total_rewards = []

    # Used 'format' as it accurately describes what the contained constants do. Alternatives could be 'style' or 'font'.
    # Used a class to contain all the relevant formating strings to make adding colours or styles to string outputs easier without having to remeber the string values and repeating code.
    class format:

    # Used constants as these should not change throught the code and used the colour/format names as easiest to use. 'END' could alternatively be called 'CLEAR'.
        DARKCYAN = "\033[36m"
        PURPLE = "\033[95m"
        BLUE = "\033[94m"
        RED = "\033[91m"
        YELLOW = "\033[93m"
        GREEN = "\033[92m"
        BOLD = "\033[1m"
        UNDERLINE = "\033[4m"
        END = "\033[0m"


    # Used 'ascii_art' instead of 'message' as it hold strings specifically relating to the ascii art required in the project, rather than general string text. 
    ascii_art = format.BOLD
    ascii_art += format.RED
    ascii_art += "\n********************************************************************************\n"
    ascii_art += " █████╗ ██████╗ ██╗   ██╗███████╗███╗   ██╗████████╗██╗   ██╗██████╗ ███████╗\n"
    ascii_art += "██╔══██╗██╔══██╗██║   ██║██╔════╝████╗  ██║╚══██╔══╝██║   ██║██╔══██╗██╔════╝\n"
    ascii_art += "███████║██║  ██║██║   ██║█████╗  ██╔██╗ ██║   ██║   ██║   ██║██████╔╝█████╗\n"
    ascii_art += "██╔══██║██║  ██║╚██╗ ██╔╝██╔══╝  ██║╚██╗██║   ██║   ██║   ██║██╔══██╗██╔══╝\n"
    ascii_art += "██║  ██║██████╔╝ ╚████╔╝ ███████╗██║ ╚████║   ██║   ╚██████╔╝██║  ██║███████╗\n\n"
    ascii_art += "              █████╗ ██╗    ██╗ █████╗ ██╗████████╗███████╗██╗\n"
    ascii_art += "             ██╔══██╗██║    ██║██╔══██╗██║╚══██╔══╝██╔════╝██║\n"
    ascii_art += "             ███████║██║ █╗ ██║███████║██║   ██║   ███████╗██║\n"
    ascii_art += "             ██╔══██║██║███╗██║██╔══██║██║   ██║   ╚════██║╚═╝\n"
    ascii_art += "             ██║  ██║╚███╔███╔╝██║  ██║██║   ██║   ███████║██╗\n"
    ascii_art += "             ╚═╝  ╚═╝ ╚══╝╚══╝ ╚═╝  ╚═╝╚═╝   ╚═╝   ╚══════╝╚═╝\n"
    ascii_art += "********************************************************************************\n\n"
    ascii_art += format.END

    # Used imported method sys.stdout.write() instead of print() function as it is more efficient to use the imported method than to use the funtion plus have control over whether a new line is added or not.
    sys.stdout.write(ascii_art)

    # Used imported method sys.stdout.write() instead of print() function as it is more efficient to use the imported method than to use the funtion plus have control over whether a new line is added or not.
    sys.stdout.write("Welcome to Adventure Awaits! Please begin by entering your name: ") 

    # Used 'name' as it is the most straightforward descriptor, though an alternative could be 'username'.
    name = sys.stdin.readline().strip()

    # Used 'message' rather than 'output' to make it a bit more descriptive of what the output is, which is a message to the user
    message = "\nNice to meet you "
    message += name 
    message += "! Let's begin your adventure.\n" 

    # Used imported method sys.stdout.write() instead of print() function as it is more efficient to use the imported method than to use the funtion plus have control over whether a new line is added or not
    sys.stdout.write(message) 

    # Used 'response' rather than 'reply' as the variable is containing the users response to the question asked, though 'reply' could also work.
    response = "yes"

    # Used a 'while' loop as 'for' loop would both be not as fitting for the needed purpose and is also outside the scope for this project. An 'if-else' statement would work for the choice side of things but would only run once unless a set of repeated 'if-else' statements were put in, which would both be bad coding and still leave a set number of iterations, instead of an unlimited number llike the 'while' loop allows for.
    # Used 'while (response == "yes")' as makes more sense to run the adventure code while the user says 'yes' than to run it while they aren't saying 'no', but the alternative of 'while (response != "no") would still technically work.
    while (response == "yes"):

        # Used 'ascii_art' instead of 'message' as it hold strings specifically relating to the ascii art required in the project, rather than general string text.
        ascii_art = format.BLUE
        ascii_art += format.BOLD
        ascii_art += "\n          /\ \n"
        ascii_art += "         /**\ \n"
        ascii_art += "        /****\   /\ \n"
        ascii_art += "       /      \ /**\ \n"
        ascii_art += "      /  /\    /    \        /\    /\  /\      /\            /\/\/\  /\ \n"
        ascii_art += "     /  /  \  /      \      /  \/\/  \/  \  /\/  \/\  /\  /\/ / /  \/  \ \n"
        ascii_art += "    /  /    \/ /\     \    /    \ \  /    \/ /   /  \/  \/  \  /    \   \ \n"
        ascii_art += "   /  /      \/  \/\   \  /      \    /   /    \ \n"
        ascii_art += "__/__/_______/___/__\___\__________________________________________________\n"
        ascii_art += format.END

        # Used imported method sys.stdout.write() instead of print() function as it is more efficient to use the imported method than to use the funtion plus have control over whether a new line is added or not
        sys.stdout.write(ascii_art)

        # Used 'message' rather than 'output' to make it a bit more descriptive of what the output is, which is a message to the user
        message = "\nYou're walking through the mountains when you come to a fork in the road.\n"
        message += "Which direction do you go? (Enter left or right): "

        # Used imported method sys.stdout.write() instead of print() function as it is more efficient to use the imported method than to use the funtion plus have control over whether a new line is added or not
        sys.stdout.write(message)

        # Used 'direction' instead of a more generic name like 'choice' or a more wordy name lke 'left_or_right' as it is both concise but also descriptive.
        direction = sys.stdin.readline().strip()

        # Used an 'if-elif-else' statement as it is the easiest way to determine which of the two direction choices the user wishes to make. The other alternative of a 'while' loop doesn't really work as this funtion already exists within a 'while' loop and we don't need it to repeat at least once.
        # Used 'if  (direction == "left" or direction == "Left" or direction == "l" or direction == "L")' as it allows for a few combinations of respones a user may input to signify 'left'. 
        if (direction == "left" or direction == "Left" or direction == "l" or direction == "L"):

            # Used 'ascii_art' instead of 'message' as it hold strings specifically relating to the ascii art required in the project, rather than general string text. 
            ascii_art = format.YELLOW
            ascii_art += format.BOLD
            ascii_art += "                            _.--.\n"
            ascii_art += "                        _.-'_:-'||\n"
            ascii_art += "                    _.-'_.-::::'||\n"
            ascii_art += "               _.-:'_.-::::::'  ||\n"
            ascii_art += "            /.'`;|:::::::'      ||_\n"
            ascii_art += "           ||   ||::::::'     _.;._'-._\n"
            ascii_art += "           ||   ||:::::'  _.-!oo @.!-._'-.\n"
            ascii_art += "           \ .  ||:::::.-!()oo @!()@.-'_.|\n"
            ascii_art += "            '.'-;|:.-'.&$@.& ()$%-'o.'|U||\n"
            ascii_art += "              `>'-.!@%()@'@_%-'_.-o _.|'||\n"
            ascii_art += "               ||-._'-.@.-'_.-' _.-o  |'||\n"
            ascii_art += "               ||=[ '-._.-\ /.-'    o |'||\n"
            ascii_art += "               || '-.]=|| |'|      o  |'||\n"
            ascii_art += "               ||      || |'|        _| ';\n"
            ascii_art += "               ||      || |'|    _.-'_.-'\n"
            ascii_art += "               |'-._   || |'|_.-'_.-'\n"
            ascii_art += "                '-._'-.|| |' `_.-'\n"
            ascii_art += "                    '-.||_/.-'\n"
            ascii_art += format.END

            # Used imported method sys.stdout.write() instead of print() function as it is more efficient to use the imported method than to use the funtion plus have control over whether a new line is added or not
            sys.stdout.write(ascii_art)

            # Used 'message' rather than 'output' to make it a bit more descriptive of what the output is, which is a message to the user
            message = "\nYou selected "
            message += direction
            message += "\n\nThere is a cave in the side of the mountain with two chests marked 1 and 2.\n"
            message += "Which chest do you open? (Enter 1 or 2): "
            
            # Used imported method sys.stdout.write() instead of print() function as it is more efficient to use the imported method than to use the funtion plus have control over whether a new line is added or not
            sys.stdout.write(message)

            # Used 'selection' rather than than 'input' as it more accurately describes the users selction from the choices rather than a general input
            selection = int(sys.stdin.readline())

            # Used an 'if-elif-else' statement as it is the easiest way to determine which selection choice the user whiches to make. The other alternative of a 'while' loop doesn't really work as this funtion already exists within a 'while' loop and we don't need it to repeat at least once.
            # Used 'if  (selection == 1)' as it makes more sense to start with that then using 2 first, though that would still work as an alternative.
            if (selection == 1):
                
                # Used 'ascii_art' instead of 'message' as it hold strings specifically relating to the ascii art required in the project, rather than general string text.
                ascii_art = format.DARKCYAN
                ascii_art += format.BOLD
                ascii_art += "\n                      .\n"
                ascii_art += "                     / \ \n"
                ascii_art += "                     | |\n"
                ascii_art += "                     | |\n"
                ascii_art += "                     |.|\n"
                ascii_art += "                     |.|\n"
                ascii_art += "                     |:|\n"
                ascii_art += "                     |:|\n"
                ascii_art += "                   `--8--'\n"
                ascii_art += "                      8\n"
                ascii_art += "                      O\n"
                ascii_art += format.END

                # Used imported method sys.stdout.write() instead of print() function as it is more efficient to use the imported method than to use the funtion plus have control over whether a new line is added or not
                sys.stdout.write(ascii_art)

                # Used 'message' rather than 'output' to make it a bit more descriptive of what the output is, which is a message to the user
                message = "\nYou selected "
                message += str(selection)
                message += "\n\nThe chest contained a "

                # Used 'select_reward' as the user gets to pick what type of reward they are getting e.g. Sword of Fire or Curse of Slow. An alternative name could be 'get_item_name', but that doesn't work as well for the Curses/Blessings.
                select_reward(message, "Sword", rewards, total_rewards) 

            # Used an 'if-elif-else' statement as it is the easiest way to determine which selection choice the user whiches to make. The other alternative of a 'while' loop doesn't really work as this funtion already exists within a 'while' loop and we don't need it to repeat at least once.
            # Used 'if  (selection == 2)' as it makes more sense to have 2 be the second condition option rather than using 2 first, though that would still work as an alternative.
            elif (selection == 2):

                # Used 'ascii_art' instead of 'message' as it hold strings specifically relating to the ascii art required in the project, rather than general string text.
                ascii_art = format.GREEN
                ascii_art += format.BOLD
                ascii_art += "\n                 |`-._/\_.-`|\n"
                ascii_art += "                 |    ||    |\n"
                ascii_art += "                 |___o()o___|\n"
                ascii_art += "                 |__((<>))__|\n"
                ascii_art += "                 \   o\/o   /\n"
                ascii_art += "                  \   ||   /\n"
                ascii_art += "                   \  ||  /\n"
                ascii_art += "                    '.||.'\n"
                ascii_art += "                      ``\n"
                ascii_art += format.END

                # Used imported method sys.stdout.write() instead of print() function as it is more efficient to use the imported method than to use the funtion plus have control over whether a new line is added or not
                sys.stdout.write(ascii_art)

                # Used 'message' rather than 'output' to make it a bit more descriptive of what the output is, which is a message to the user
                message = "\nYou selected "
                message += str(selection)
                message += "\n\nThe chest contained a "

                # Used 'select_reward' as the user gets to pick what type of reward they are getting e.g. Sword of Fire or Curse of Slow. An alternative name could be 'get_item_name', but that doesn't work as well for the Curses/Blessings.
                select_reward(message, "Shield", rewards, total_rewards)

            # Used this to call error_message() for any input other than the ones used in the 'if-elif' statements, as it is a basic way to control the flow in cases where the user inputs an invalid string.
            else:

                # Used 'error_message' as it accurately describes the meaning of the function. 'display_error' would be a possible alternative.
                error_message("chest", name)

        # Used an 'if-elif-else' statement as it is the easiest way to determine wof the two direction choices the user wishes to make. The other alternative of a 'while' loop doesn't really work as this funtion already exists within a 'while' loop and we don't need it to repeat at least once.
        # Used 'if  (direction == "right" or direction == "Right" or direction == "r" or direction == "R")' as it allows for a few combinations of respones a user may input to signify 'right'. 
        elif (direction == "right" or direction == "Right" or direction == "r" or direction == "R"):

            # Used 'ascii_art' instead of 'message' as it hold strings specifically relating to the ascii art required in the project, rather than general string text.
            ascii_art = format.DARKCYAN
            ascii_art += format.BOLD
            ascii_art += "\n                                  |>>>\n"
            ascii_art += "                                  |\n"
            ascii_art += "                    |>>>      _  _|_  _         |>>>\n"
            ascii_art += "                    |        |;| |;| |;|        |\n"
            ascii_art += "                _  _|_  _    \\\\.    .  /    _  _|_\n"
            ascii_art += "               |;|_|;|_|;|    \\\\:. ,  /    |;|_|;|_|;|\n"
            ascii_art += "               \\\\..      /    ||;   . |    \\\\.    .  /\n"
            ascii_art += "                \\\\.  ,  /     ||:  .  |     \\\\:  .  /\n"
            ascii_art += "                 ||:   |_   _ ||_ . _ | _   _||:   |\n"
            ascii_art += "                 ||:  .|||_|;|_|;|_|;|_|;|_|;||:.  |\n"
            ascii_art += "                 ||:   ||.    .     .      . ||:  .|\n"
            ascii_art += "                 ||: . || .     . .   .  ,   ||:   |       \,/\n"
            ascii_art += "                 ||:   ||:  ,  _______   .   ||: , |            /`\ \n"
            ascii_art += "                 ||:   || .   /+++++++\    . ||:   |\n"
            ascii_art += "                 ||:   ||.    |+++++++| .    ||: . |\n"
            ascii_art += "              __ ||: . ||: ,  |+++++++|.  . _||_   |\n"
            ascii_art += "     ____--`~    '--~~__|.    |+++++__|----~    ~`---,   \n"
            ascii_art += "-~--~                   ~---__|,--~'                  ~~----_____-~'   `~----~~\n"
            ascii_art += format.END
            
            # Used imported method sys.stdout.write() instead of print() function as it is more efficient to use the imported method than to use the funtion plus have control over whether a new line is added or not
            sys.stdout.write(ascii_art)

            # Used 'message' rather than 'output' to make it a bit more descriptive of what the output is, which is a message to the user
            message = "You selected "
            message += direction
            message += "\n\nHidden amongst the mountains is a castle containing two doors marked 1 and 2.\n" 
            message += "Which door do you open? (Enter 1 or 2):"

            # Used imported method sys.stdout.write() instead of print() function as it is more efficient to use the imported method than to use the funtion plus have control over whether a new line is added or not
            sys.stdout.write(message) 

            # Used 'selection' rather than than 'input' as it more accurately describes the users selction from the choices rather than a general input
            selection = int(sys.stdin.readline())

            # Used an 'if-elif-else' statement as it is the easiest way to determine which selection choice the user whiches to make. The other alternative of a 'while' loop doesn't really work as this funtion already exists within a 'while' loop and we don't need it to repeat at least once.
            # Used 'if  (selection == 1)' as it makes more sense to start with that then using 2 first, though that would still work as an alternative.
            if (selection == 1):
                
                # Used 'ascii_art' instead of 'message' as it hold strings specifically relating to the ascii art required in the project, rather than general string text.
                ascii_art = format.GREEN
                ascii_art += format.BOLD
                ascii_art += "\n                      {} \n"
                ascii_art += "                     .--.\n"
                ascii_art += "                    /.--.\ \n"
                ascii_art += "                    |====|\n"
                ascii_art += "                    |`::`|\n"
                ascii_art += "                .-;`\..../`;-.\n"
                ascii_art += "               /  |...::...|  \ \n"
                ascii_art += "              |   /'''::'''\   |\n"
                ascii_art += "              ;--'\   ::   /\--;\n"
                ascii_art += "              <__>,>._::_.<,<__>\n"
                ascii_art += "              |  |/   ^^   \|  |\n"
                ascii_art += "              \::/|        |\::/\n"
                ascii_art += "              |||\|        |/|||\n"
                ascii_art += "              ''' |___/\___| '''\n"
                ascii_art += "                   \_ || _/\n"
                ascii_art += "                   <_ >< _>\n"
                ascii_art += "                   |  ||  |\n"
                ascii_art += "                   |  ||  |\n"
                ascii_art += "                  _\.:||:./_\n"
                ascii_art += "                 /____/\____\ \n"
                ascii_art += format.END

                # Used imported method sys.stdout.write() instead of print() function as it is more efficient to use the imported method than to use the funtion plus have control over whether a new line is added or not
                sys.stdout.write(ascii_art)

                # Used 'message' rather than 'output' to make it a bit more descriptive of what the output is, which is a message to the user
                message = "\nYou selected "
                message += str(selection)
                message += "\n\nThe door opens to a blacksmith containing an "

                # Used 'select_reward' as the user gets to pick what type of reward they are getting e.g. Sword of Fire or Curse of Slow. An alternative name could be 'get_item_name', but that doesn't work as well for the Curses/Blessings.
                select_reward(message, "Armour", rewards, total_rewards) 

            # Used an 'if-elif-else' statement as it is the easiest way to determine which selection choice the user whiches to make. The other alternative of a 'while' loop doesn't really work as this funtion already exists within a 'while' loop and we don't need it to repeat at least once.
            # Used 'if  (selection == 2)' as it makes more sense to have 2 be the second condition option rather than using 2 first, though that would still work as an alternative.
            elif (selection == 2):

                # Used 'ascii_art' instead of 'message' as it hold strings specifically relating to the ascii art required in the project, rather than general string text. 
                ascii_art = format.YELLOW
                ascii_art += format.BOLD
                ascii_art += "\n                     ,-==-,\n"
                ascii_art += "                     \/\/\/\n"
                ascii_art += "                      \\\\//\n"
                ascii_art += "                    .--''--.\n"
                ascii_art += "                  .'.--::--.'.\n"
                ascii_art += "                 / /        \ \ \n"
                ascii_art += "                | |          | |\n"
                ascii_art += "                 \ \        / / \n"
                ascii_art += "                  '.'--::--'.'\n"
                ascii_art += "                    '--__--'\n"
                ascii_art += format.END

                # Used imported method sys.stdout.write() instead of print() function as it is more efficient to use the imported method than to use the funtion plus have control over whether a new line is added or not
                sys.stdout.write(ascii_art)

                # Used 'message' rather than 'output' to make it a bit more descriptive of what the output is, which is a message to the user
                message = "\nYou selected "
                message += str(selection)
                message += "\n\nThe door opens to a jewelers containing an "

                # Used 'select_reward' as the user gets to pick what type of reward they are getting e.g. Sword of Fire or Curse of Slow. An alternative name could be 'get_item_name', but that doesn't work as well for the Curses/Blessings.
                select_reward(message, "Ring", rewards, total_rewards)

            # Used this to call error_message() for any input other than the ones used in the 'if-elif' statements, as it is a basic way to control the flow in cases where the user inputs an invalid string.
            else:

                # Used 'error_message' as it accurately describes the meaning of the function. 'display_error' would be a possible alternative.
                error_message("door", name)

        # Used this to call error_message() for any input other than the ones used in the 'if-elif' statements, as it is a basic way to control the flow in cases where the user inputs an invalid string.
        else:

            # Used 'error_message' as it accurately describes the meaning of the function. 'display_error' would be a possible alternative.
            error_message("direction", name)

        # Used 'message' rather than 'output' to make it a bit more descriptive of what the output is, which is a message to the user
        message = "\nAs you continue on your adventure you come across a weary fellow adventurer.\n"
        message += "They ask you if you can share some of your water with them. How much of your water \n"
        message += "do you decide to share? (Enter a percentage as a fraction e.g. 0.5 = 50%): "

        # Used imported method sys.stdout.write() instead of print() function as it is more efficient to use the imported method than to use the funtion plus have control over whether a new line is added or not
        sys.stdout.write(message) 

        # Used 'water_shared' instead of 'shared_water' as it works better with the follow up variable 'water_percentage'
        water_shared = float(sys.stdin.readline())

        # Used 'water_percentage' rather than 'percentage_shared' as it works better with the previous variable 'water_shared'
        water_percentage = int(water_shared * 100)

        # Used an 'if-elif-else' statement as it is the easiest way to determine which selection choice the user whiches to make. The other alternative of a 'while' loop doesn't really work as this funtion already exists within a 'while' loop and we don't need it to repeat at least once.
        # Used 'if  (water_shared >= 0 and water_shared < 0.5)' as it makes sense to have the first condition check if 'water_shared' is more than or equal to "0%" (0) but less than "50%" (0.5). This could have been done the other way around and still worked, but made sense to start by checking the lower condition first.
        if (water_shared >= 0 and water_shared < 0.5):

            # Used the name 'ascii_wizard' rather than just 'wizard' to more accurately describe what the function is about
            ascii_wizard()

            # Used 'message' rather than 'output' to make it a bit more descriptive of what the output is, which is a message to the user
            message = "\nYou chose to share "
            message += str(water_percentage)
            message += "% of your water.\n"
            message += "The adventurer turns out to be a powerful wizard!\n"
            message += "As a punishment for you're greedy ways he casts upon you \n" 
            message += "the "

            # Used 'select_reward' as the user gets to pick what type of reward they are getting e.g. Sword of Fire or Curse of Slow. An alternative name could be 'get_item_name', but that doesn't work as well for the Curses/Blessings.
            select_reward(message, "Curse", rewards, total_rewards)


        # Used an 'if-elif-else' statement as it is the easiest way to determine which selection choice the user whiches to make. The other alternative of a 'while' loop doesn't really work as this funtion already exists within a 'while' loop and we don't need it to repeat at least once.
        # Used 'if  (water_shared >= 0.5 and water_shared <= 1)' as it makes sense to have the second condition check if 'water_shared' is more than or equal to "50%" (0.5) but less than or equal to "100%" (1). This could have been done the other way around and still worked, but made sense to start by checking the lower condition first.
        elif (water_shared >= 0.5 and water_shared <= 1):

            # Used the name 'ascii_wizard' rather than just 'wizard' to more accurately describe what the function is about
            ascii_wizard()

            # Used 'message' rather than 'output' to make it a bit more descriptive of what the output is, which is a message to the user
            message = "\nYou chose to share "
            message += str(water_percentage)
            message += "% of your water.\n"
            message += "The adventurer turns out to be a powerful wizard!\n"
            message += "As a reward for you're generous ways he casts upon you \n" 
            message += "the "

            # Used 'select_reward' as the user gets to pick what type of reward they are getting e.g. Sword of Fire or Curse of Slow. An alternative name could be 'get_item_name', but that doesn't work as well for the Curses/Blessings.
            select_reward(message, "Blessing", rewards, total_rewards)

        # Used this to call error_message() for any input other than the ones used in the 'if-elif' statements, as it is a basic way to control the flow in cases where the user inputs an invalid string.
        else:

            # Used 'error_message' as it accurately describes the meaning of the function. 'display_error' would be a possible alternative.
            error_message("water amount", name)

        # Used 'message' rather than 'output' to make it a bit more descriptive of what the output is, which is a message to the user
        message = format.RED
        message += format.BOLD
        message += format.UNDERLINE
        message += "\nThe adventurer "
        message += name
        message += " returns home, having completed their adventure.\n"
        message += "The rewards gained on this adventure were:\n"
        message += format.END

        # Used imported method sys.stdout.write() instead of print() function as it is more efficient to use the imported method than to use the funtion plus have control over whether a new line is added or not
        sys.stdout.write(message)

        # Used 'display _list' as it most accurately describes the functions purpose. Alternative could be 'show_list'.
        display_list(rewards)

        # Used del rewards[ : ] instead of rewards.clear() as del rewards[ : ]was the only method of emptying a lost that had been demonstrated in the modules/live lectorials, and as such was the only method within the scope of the project.
        del rewards[ : ]

        # Used 'response' rather than 'reply' as the variable is containing the users response to the question asked, though 'reply' could also work.
        response = end_game(name)

    # Used 'message' rather than 'output' to make it a bit more descriptive of what the output is, which is a message to the user
    message = format.RED
    message += format.BOLD
    message += format.UNDERLINE
    message += "\nThank you for playing "
    message += name
    message += ". Your total rewards were:\n"
    message += format.END

    # Used imported method sys.stdout.write() instead of print() function as it is more efficient to use the imported method than to use the funtion plus have control over whether a new line is added or not
    sys.stdout.write(message)

    # Used 'display _list' as it most accurately describes the functions purpose. Alternative could be 'show_list'.
    display_list(total_rewards)

    # Used imported method sys.stdout.write() instead of print() function as it is more efficient to use the imported method than to use the funtion plus have control over whether a new line is added or not
    sys.stdout.write("\n\n")

# Used only a call to main() outside of any of the functions written both for simplicity as well as it being a functional requirement for the project
main()
