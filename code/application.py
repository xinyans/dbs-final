'''
Database Systems Final Project

Instructor: Samuel Johnson
Group Members:
    Xinyan Sun (sunx15) - sunx15@rpi.edu
    Frank Liang (liangt2) - liangt2@rpi.edu
    Yutao Yang (yangy27) - yangy27@rpi.edu
    Brian Gembarski (gembab) - gembab@rpi.edu
    Abdulai Jalloh (jalloa) - jalloa@rpi.edu

This python file is responsible is responsible for handling the UI.

The UI will be a basic Command Line Interface giving users the ability to 
explore the database.
'''

def PRINT_POEM():
    '''Useless easter egg'''
    print(
'''> ___________________________________________
> |   Stopping by Woods on a Snowy Evening  |
> |                                         |
> |  Whose woods these are I think I know.  |
> |  His house is in the village though;    |
> |  He will not see me stopping here       |
> |  To watch his woods fill up with snow.  |
> |                                         |
> |  My little horse must think it queer    |
> |  To stop without a farmhouse near       |
> |  Between the woods and frozen lake      |
> |  The darkest evening of the year.       |
> |                                         |
> |  He gives his harness bells a shake     |
> |  To ask if there is some mistake.       |
> |  The only other sound’s the sweep       |
> |  Of easy wind and downy flake.          |
> |                                         |
> |  The woods are lovely, dark and deep,   |
> |  But I have promises to keep,           |
> |  And miles to go before I sleep,        |
> |  And miles to go before I sleep.        |
> |_________________________________________|
>''')

def PRINT_TEAM():
    team = []
    team.append('Xinyan Sun (sunx15) - sunx15@rpi.edu')
    team.append('Frank Liang (liangt2) - liangt2@rpi.edu')
    team.append('Yutao Yang (yangy27) - yangy27@rpi.edu')
    team.append('Brian Gembarski (gembab) - gembab@rpi.edu')
    team.append('Abdulai Jalloh (jalloa) - jalloa@rpi.edu')
    print("> Team Members:")
    for t in team:
        print(">     {}".format(t))


if __name__ == "__main__":


    print("> Database Systems Final Project\n> Instructor: Samuel Johnson")
    PRINT_TEAM()
    

    print(">\n> If you are supposed to be here, please type 'enter'.")
    print("> If you type anything else, we shall deny you access.")
    print(">", end =" ")
    if input() != "":
        print("> You did not type 'enter'.\nGoodbye!")
        exit()

    print(">\n> Welcome, traveller, to the Command Line Interface of a Database Systems final project")
    print("> If you should find yourself lost, simply type 'help'. Also, feel free to visit")
    print("> our team's GitHub repo, at 'https://github.com/xinyans/dbs-final'\n>")

    commands = ['help','exit','team']


    while(True):
        print(">", end =" ")
        command = input()

        if command == 'exit':
            print("> Farewell! May the the road rise to meet you!")
            break
        elif command == 'Easter Egg':
            print("> Congratulations! A poem for you by Robert Frost")
            PRINT_POEM()
        elif command == 'help':
            print("> Here is a list of commands:")
            for c in commands:
                print(">    '{}'".format(c))
        elif command == 'team':
            PRINT_TEAM()



    