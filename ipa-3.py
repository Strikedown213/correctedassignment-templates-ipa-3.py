'''Individual Programming Assignment 3

70 points

This assignment will develop your ability to manipulate data.
'''

def relationship_status(from_member, to_member,social_graph):
    '''Relationship Status.
    20 points.

    Let us pretend that you are building a new app.
    Your app supports social media functionality, which means that users can have
    relationships with other users.

    There are two guidelines for describing relationships on this social media app:
    1. Any user can follow any other user.
    2. If two users follow each other, they are considered friends.

    This function describes the relationship that two users have with each other.

    Please see "assignment-4-sample-data.py" for sample data. The social graph
    will adhere to the same pattern.

    Parameters
    ----------
    from_member: str
        the subject member
    to_member: str
        the object member
    social_graph: dict
        the relationship data
 
    Returns
    -------
    str
        "follower" if fromMember follows toMember,
        "followed by" if fromMember is followed by toMember,
        "friends" if fromMember and toMember follow each other,
        "no relationship" if neither fromMember nor toMember follow each other.
    '''
    # Replace `pass` with your code.
    # Stay within the function. Only use the parameters as input. The function should return your answer.
    
    

    following1 = social_graph[from_member]["following"]
    following2 = social_graph[to_member]["following"]
    if to_member in following1:
        if from_member in following2:
            return "friends"
        if from_member not in following2:
            return "follower"
    elif from_member in following2:
        if to_member not in following1:
            return "followed by"
    else:
            return "no relationship"

graph = {
    "@bongolpoc":{"first_name":"Joselito",
                  "last_name":"Olpoc",
                  "following":[
                  ]
    },
    "@joaquin":  {"first_name":"Joaquin",
                  "last_name":"Gonzales",
                  "following":[
                      "@chums","@jobenilagan"
                  ]
    },
    "@chums" : {"first_name":"Matthew",
                "last_name":"Uy",
                "following":[
                    "@bongolpoc","@miketan","@rudyang","@joeilagan"
                ]
    },
    "@jobenilagan":{"first_name":"Joben",
                   "last_name":"Ilagan",
                   "following":[
                    "@eeebeee","@joeilagan","@chums","@joaquin"
                   ]
    },
    "@joeilagan":{"first_name":"Joe",
                  "last_name":"Ilagan",
                  "following":[
                    "@eeebeee","@jobenilagan","@chums"
                  ]
    },
    "@eeebeee":  {"first_name":"Elizabeth",
                  "last_name":"Ilagan",
                  "following":[
                    "@jobenilagan","@joeilagan"
                  ]
    },
    }   

relationship_status('@joaquin','@chums', graph)


def tic_tac_toe(board):
    '''Tic Tac Toe.
    25 points.

    Tic Tac Toe is a common paper-and-pencil game.
    Players must attempt to successfully draw a straight line of their symbol across a grid.
    The player that does this first is considered the winner.

    This function evaluates a tic tac toe board and returns the winner.

    Please see "assignment-4-sample-data.py" for sample data. The board will adhere
    to the same pattern. The board may by 3x3, 4x4, 5x5, or 6x6. The board will never
    have more than one winner. The board will only ever have 2 unique symbols at the same time.

    Parameters
    ----------
    board: list
        the representation of the tic-tac-toe board as a square list of lists

    Returns
    -------
    str
        the symbol of the winner or "NO WINNER" if there is no winner
    '''
    # Replace `pass` with your code.
    # Stay within the function. Only use the parameters as input. The function should return your answer.
   
    for row in range(len(board)):
        Item = True
        previous = board[row][0]
        for column in board[row]:
            #Check if all the values are the same with one another
            if column != previous:
                Item = False
                break
        if Item == True:
            return previous
    
    for column in range(len(board)):
        Item2 = True
        previous = board[0][column]
        for row in range(len(board)):
            if board[row][column] != previous:
                Item2 = False
                break
        if Item2 == True:
            return previous

    previous = board[0][0]
    Item3 = True
    for i in range(len(board)):
        if board[i][i] != previous:
            Item3 = False
            break
    if Item3 == True:
        return previous
    
    previous = board[0][len(board)-1]
    Item4 = True
    for r in range(len(board)):
        if board[r][len(board)-1-r] != previous:
            Item4 = False
            break
    if Item4 == True:
        return previous

    return "No winner"



board_1 = [
['O','X','O'],
['X','X','X'],
['X','',''],
]

board_2 = [
['O','O','X'],
['X','O','x'],
['X','O',''],
]

board_3 = [
['X','O','O'],
['O','X','O'],
['X','O','X'],
]

board_4 = [
['','O','X'],
['O','X','O'],
['X','O',''],
]

board_5 = [
['','O',''],
['O','X','O'],
['X','O',''],
]

tic_tac_toe(board_1)


def eta(first_stop, second_stop, route_map):
    '''ETA.
    25 points.

    A shuttle van service is tasked to travel along a predefined circlar route.
    This route is divided into several legs between stops.
    The route is one-way only, and it is fully connected to itself.

    This function returns how long it will take the shuttle to arrive at a stop
    after leaving another stop.

    Please see "mod-4-ipa-1-sample-data.py" for sample data. The route map will
    adhere to the same pattern. The route map may contain more legs and more stops,
    but it will always be one-way and fully enclosed.

    Parameters
    ----------
    first_stop: str
        the stop that the shuttle will leave
    second_stop: str
        the stop that the shuttle will arrive at
    route_map: dict
        the data describing the routes

    Returns
    -------
    int
        the time it will take the shuttle to travel from first_stop to second_stop
    '''
    # Replace `pass` with your code.
    # Stay within the function. Only use the parameters as input. The function should return your answer.
    currplace = first_stop
    overalltime = 0
    while currplace != second_stop:
        for places, time in route_map.items():
            if places[0] == currplace:
                #places[0]
                #time['travel_time_mins']
                currplace = places[1]
                overalltime += time['travel_time_mins']
                break
    return overalltime
                

legs1 = {
     ("upd","admu"):{
         "travel_time_mins":10
     },
     ("admu","dlsu"):{
         "travel_time_mins":35
     },
     ("dlsu","upd"):{
         "travel_time_mins":55
     }
}

legs2 = {
    ('a1', 'a2'): {
        'travel_time_mins': 10
    },
    ('a2', 'b1'): {
        'travel_time_mins': 10230
    },
    ('b1', 'a1'): {
        'travel_time_mins': 1
    }
}
legs3 = {
     ("upd","admu"):{
         "travel_time_mins":1
     },
     ("admu","ust"):{
         "travel_time_mins":2
     },
     ("ust","dlsu"):{
         "travel_time_mins":10
     },
     ("dlsu","upd"):{
         "travel_time_mins":90
     }
}

eta('dlsu', 'admu', legs1)
