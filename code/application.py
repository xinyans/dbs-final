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

#TODO: UNCOMMENT THIS
# from database import Vehicles_data


def PRINT_POEM():
    '''Useless easter egg'''
    print("> Congratulations! A poem for you by Robert Frost")
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

def RUN_TEAM():
    '''Runs the team command with proper formating'''
    team = []
    team.append('Xinyan Sun (sunx15) - sunx15@rpi.edu')
    team.append('Frank Liang (liangt2) - liangt2@rpi.edu')
    team.append('Yutao Yang (yangy27) - yangy27@rpi.edu')
    team.append('Brian Gembarski (gembab) - gembab@rpi.edu')
    team.append('Abdulai Jalloh (jalloa) - jalloa@rpi.edu')
    print("> Team Members:")
    for t in team:
        print(">     {}".format(t))

def RUN_HELP(command_line):
    '''Runs the help function with proper formating'''
    if len(command_line)==1:
        print("> Here is a list of commands:")
        for c in sorted(commands.keys()):
            print(">    '{}'".format(c))
        print("> Use 'help <command>' to view that command's description")
    else:
        print(">")
        if command_line[1] in commands.keys():
            print("> {}".format(command_line[1]))
            print("> {}".format(commands[command_line[1]]))
        else:
            print("> '{}' is an unknown command".format(command_line[1]))
    print(">")

    

def RUN_GET_MUNICIPALITY(database,command_line):
    '''Runs listTrafficVolume query'''
    if len(command_line) != 2:
        print("> incorrect number of arguments.\n> Call with 'get_municipality <vol>'")
        return

    #TODO: make sure this returns correctly with proper formatting
    records = database.listVolumeCrash(command_line[1])

    # is records of the format [(municipality, year), (municipality, year), ...]?

    print("> Municipalities and years that had traffic volume greater than {}".format(command_line[1]))
    for i in records:
        print("> {} in year {}".format(i[0],i[1]))


def RUN_CRASHES(database, command_line):
    '''Runs vehicleAndCarCrash'''
    if len(command_line) != 2:
        print("> incorrect number of arguments.\n> Call with 'crashes <num>'")
        return

    #TODO: make sure this returns correctly with proper formatting
    records = database.vehicleAndCarCrash(command_line[1])

    # Assuming records = [ (municipality, year, description), ... ]

    print("> All crashes with more than {} vehicle's involved".format(command_line[1]))
    for i in records:
        print("> {}, {}\n>     Crash descriptor = {}".format(i[0],i[1],i[2]))

def RUN_GET_VOLUME(database, command_line):
    '''Runs the listVolumeCrash query'''
    if len(command_line) != 1:
        print("> incorrect number of arguments.\n> Call with 'get_volume' only")

    #TODO: make sure this returns correctly with proper formatting
    records = database.listVolumeCrash()

    # Assuming structure [ (Municipality,yeah,total_creashes,traffic_vol), ... ]

    print("> Crashes and traffic of a municipality")
    for i in records:
        print("> {} crashes and {} total traffic for {} in {}".format(i[2],i[3],i[0],i[1]))
    


def RUN_STRUCTURE(database, command_line):
    '''Runs structureCrashRelation'''
    if len(command_line) < 2 or len(command_line)> 3:
        print("> incorrect number of arguments.\n> Call with 'structure <arg>'\n"\
                "> Note: arg = ramp, bridge, railroad crossing, or one-way")
        return

    #TODO: make sure this returns correctly with proper formatting

    if len(command_line) == 3:
        s = command_line[1] + ' ' + command_line[2]
    else:
        s = command_line[1]
    
    records = database.structureCrashRelation(s)

    # records = []
    # records.append( (319865,10391742,3.01298749320,'Y') )
    # records.append( (967865,74965742,12.01298749320,None) )

    if records == None:
        print("> Invalid structure was supplied")
    # here is assuming that the call has succeeded


    if len(records) != 2:
        print("> IMPROPER RETURN VALUE!!!")
        return

    percent_with = records[0][2]
    percent_wout = records[1][2]
    
    print("> Percentage of crashes involving '{}' was {:.2f}".format(s, percent_with))

    #this stat is not clear and will cause confusion
    # print("> Percentage of crashes not involving '{}' was {:.2f}".format(s, percent_wout))



def RUN_CRASH_RATE(database, command_line):
    '''Runs the crashRateMunicipality query with proper output formating'''

    # how do we make sure that a county is 1 word? same for rmunicipality

    if len(command_line) != 3:
        print("> incorrect number of arguments.\n"
                "> Call with 'crash_rate <municipality> <county>'")
        return

    #TODO: make sure records is in the proper structure and can be retrieved
    records = database.crashRateMunicipality(command_line[1], command_line[2])





    print("> Statistics for ")



def MAKE_COMMANDS():
    '''makes the dict of commands, and their description'''
    commands = {}
    commands['team'] = "Displays the team members"
    commands['crash_rate'] = "Return Crashes, Volume and crash rate of every year.\n" \
                            "> Call with 'crash_rate <municipality> <county>'"
    commands['get_volume'] = "Lists the number of crashes and total traffic in a specific year and municipality."
    commands['get_municipality'] = "Returns municipalities and year whose traffic volume is greater than vol.\n"\
                                    "> Call with 'get_municipality <vol>'"
    commands['crashes'] = "Lists the municipality,year and crash_descriptor of the car crashes\n"\
        		    "> that have the number_of_vehicles involved >= num.\n"\
                    "> Call with 'crashes <num>'"
    commands['structure'] = "Returns the crash statistics involving accidents with a specific structure.\n"\
                            "> Call with 'structure <arg>' where arg = ramp, bridge, railroad crossing, or one-way."
    
    return commands

if __name__ == "__main__":



    print("> Database Systems Final Project\n> Instructor: Samuel Johnson")
    RUN_TEAM()

    print(">\n> Welcome, traveller, to the Command Line Interface of a Database Systems final project")
    print("> If you should find yourself lost, simply type 'help'. Also, feel free to visit")
    print("> our team's GitHub repo, at 'https://github.com/xinyans/dbs-final'\n>")

    commands = MAKE_COMMANDS()

    database=2

    #TODO: UNCOMMENT THIS
    # connection_string = "host='localhost' dbname='dbs-final' user='dbs-final_user' password='dbs_password'"
    # database = Vehicles_data(connection_string)

    while(True):
        print(">", end =" ")

        # accept input from user
        command = input()

        # tokenize input
        command_line = command.split()

        if len(command_line)==0: # no command given
            continue

        elif command_line[0] == 'exit':
            print("> Farewell! May the the road rise to meet you!")
            break

        elif command_line[0] == 'egg':
            PRINT_POEM()
        
        elif command_line[0] == 'help':
            RUN_HELP(command_line)

        elif command_line[0] == 'team':
            RUN_TEAM()

        elif command_line[0] == 'crash_rate':
            #TODO: finalize RUN_CRASH_RATE
            print("> This feature is not implemented yet...")
            # RUN_CRASH_RATE(database, command_line)

        elif command_line[0] == 'get_volume':
            #TODO finalize RUN_GET_VOLME
            print("> This feature is not implemented yet...")
            # RUN_GET_VOLUME(database, command_line)

        elif command_line[0] == 'get_municipality':
            #TODO finalize RUN_GET_MUNICIPALITY
            print("> This feature is not implemented yet...")
            # RUN_GET_MUNICIPALITY(database, command_line)

        elif command_line[0] == 'crashes':
            #TODO finalize RUN_CRASHES
            print("> This feature is not implemented yet...")
            # RUN_CRASHES(database, command_line)
        
        elif command_line[0] == 'structure':
            RUN_STRUCTURE(database, command_line)



        else:
            print("> '{}' is an unknown command".format(command_line[0]))



    