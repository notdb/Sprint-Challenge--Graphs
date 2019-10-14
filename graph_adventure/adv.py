from room import Room
from player import Player
from world import World
from roomgraphs import roomGraph0, roomGraph1, roomGraph2, roomGraph3, roomGraph4
from util import Stack, Queue  # These may come in handy
import random

                    
# Load world
world = World()

world.loadGraph(roomGraph1)
#world.printRooms()
#print(world.rooms[1].getExits())
#print(world.roomGrid)
# start at room 0, add room to dictionary with available exits pick a random direction, go to that room, add step taken to list, 
#player = Player("Name", world.startingRoom)
#player2 = Player("Doug", world.startingRoom)
#player3 = Player("NotDoug", world.startingRoom)
#player4 = Player("TheRealDeal", world.startingRoom)
# FILL THIS IN

visited = set()
traversalPath = []
exitPath = []
cRoom = set()
graphlist = {}
# have to find a way to find last question mark

def theRealDeal():
    for i in range(0,3):
        print(i)
        newArray = []
        newArray2 = []
        oldRoom = player4.currentRoom.id
        oldDirection = 0
        newArray = player4.currentRoom.getExits()
        unvisited = {}
        for exit in newArray:
            unvisited[exit] = '?'
        graphlist[player4.currentRoom.id] = unvisited
        # pick first '?' in list and go that direction
        print(f'{unvisited} TEST')
       # for thing in unvisited.items():
       #     if thing[1] == '?':
       #         direction = thing[0]
       #         pass
        direction = 'e'
        oldDirection = direction
        player4.travel(direction)
        # deadend detection
        # for actual deadends only
        if oldRoom == player4.currentRoom.id and len(player4.currentRoom.getExits()) == 1:
            print('you hit a dead end')
            traversalPath.append(direction)
            print(f'{graphlist} suuuuu')
            
            # room changes and reverses to previous room with a ?
            if direction == 'n':
                unvisited['s'] = oldRoom-1
                print(cRoom)
                thingy = cRoom.pop()
                while player4.currentRoom.id is not thingy:
                    direction1 = 's'
                    player4.travel(direction1)
                    traversalPath.append(direction1)
                    print(f'{graphlist} TESTTTTTTTT')
               
            if direction == 's':
                unvisited['n'] = oldRoom-1
                thingy = cRoom.pop()
                while player4.currentRoom.id is not thingy:
                    direction1 = 'n'
                    player4.travel(direction1)
                    traversalPath.append(direction1)
            
            if direction == 'e':
                unvisited['w'] = oldRoom-1
                print(cRoom)
                thingy = cRoom.pop()
                while player4.currentRoom.id is not thingy:
                    direction1 = 'w'
                    player4.travel(direction1)
                    traversalPath.append(direction1)
            
            if direction == 'w':
                unvisited['e'] = oldRoom-1
                thingy = cRoom.pop()
                while player4.currentRoom.id is not thingy:
                    direction1 = 'e'
                    player4.travel(direction1)
                    traversalPath.append(direction1)
            
            #print(f'{graphlist} 44435345345345')
        else:
            traversalPath.append(direction)
        # add opposite directions to rooms
        # fix this part for going backwards
        if oldRoom is not player4.currentRoom.id and oldRoom - player4.currentRoom.id == -1:
            print(oldRoom)
            print(player4.currentRoom.id)
            print('running')
            if oldDirection == 'n':
               # print(oldRoom)
               # print(oldDirection)
                graphlist[oldRoom][oldDirection] = player4.currentRoom.id
                print(player4.currentRoom.id)
                print(f'{graphlist} XOOO')
                unvisited['s'] = oldRoom
            
            if oldDirection == 's':
                graphlist[oldRoom][oldDirection] = player4.currentRoom.id
                unvisited['n'] = oldRoom
             
            if oldDirection == 'w':
                graphlist[oldRoom][oldDirection] = player4.currentRoom.id
                unvisited['e'] = oldRoom
                
            if oldDirection == 'e':
                graphlist[oldRoom][oldDirection] = player4.currentRoom.id
                print(player4.currentRoom.id)
                print(f'{graphlist} XOOO')
                unvisited['w'] = oldRoom
                 
            # check if previous room still has unexplored rooms
            for pair in graphlist[oldRoom]:
               if graphlist[oldRoom][pair] == '?':
                   cRoom.add(oldRoom)
            
            

    
    
#theRealDeal()
#print(graphlist)
#print(traversalPath)
#print(world.printRooms())

# makes the initial {0: {n/s/e/w}} rooms with ?'s for directions
def construct_traversal():
    for i in range(len(world.rooms)):
        player2.currentRoom = world.rooms[i]
    
    #while len(graphlist) is not len(world.rooms):
        unvisited = {}
        listOfExits = player2.currentRoom.getExits()
        for exit in listOfExits:
            unvisited[exit] = '?'
            graphlist[player2.currentRoom.id] = unvisited
  
    '''
    for rooms in graphlist:
        listOfExits2 = []
        print(graphlist[rooms])
        print('?' in graphlist[rooms].values())
        if '?' in graphlist[rooms].values():
            for room in graphlist[rooms]:
                print(room)
                player2.travel(room)
                listOfExits2 = player2.currentRoom.getExits()
                for exit in listOfExits2:
                    unvisited = {}
                    unvisited[exit] = '?'
                    graphlist[player2.currentRoom.id] = unvisited
                    
    '''
## need to split up the traversal because you can't change a dictionaries size during something apparently
## add keys and then traverse them
def recursive_dft(starting_vertex):
    #print(f'{starting_vertex} aaa')
    if len(visited) == len(graphlist):
        return 0
    if starting_vertex not in visited:
        visited.add(starting_vertex)
        #traversalPath.append(starting_vertex)
        #print(visited)
        if starting_vertex is None:
            pass
        else:
            # fill out the '?'s with room numbers
           # print(f'{starting_vertex} bbb')
            # accessing {'direction':?}
            # all we have to do is peek into the next room, get the id, set the id as the value for the ? and dip back out
            for stub in graphlist[starting_vertex].items():
               # print(stub[1])
                if stub[1] == '?':
                    player3.currentRoom = world.rooms[starting_vertex]
                    #print(f'{player3.currentRoom} ZZZZZZZZZZ')
                    player3.travel(stub[0])
                    #print(stub[0])
                    traversalPath.append(stub[0])
                   # traversalPath.append(stub[0])
                   # traversalPath.append(stub[0])
                   # traversalPath.append(stub[0])
                   # traversalPath.append(stub[0])
                   # print(f'{player3.currentRoom.id} cccc')
                   # print(f'{graphlist[starting_vertex]} ddddd')
                    graphlist[starting_vertex][stub[0]] = player3.currentRoom.id
        for next_vert in graphlist:
            recursive_dft(next_vert)
    else:
        pass

def bfs(starting_vertex, destination_vertex):
    
    finalList = []
    newList = []
    que = Queue()
    que2 = Queue()
    visited = set()
    que.enqueue(graphlist[starting_vertex])
    #print(f'{graphlist[starting_vertex]} arstrastarstarst')
    while que.size() > 0:
        vertex = que.dequeue()
       # print(vertex)
       # print(f'{vertex.items()} aaa')
       # print(visited)
        '''
        if vertex is destination_vertex:
            dVert = destination_vertex
            newList.reverse()
            for listItem in newList:
                if dVert in graphlist[listItem]:
                    dVert = listItem
                    finalList.append(listItem)
                else:
                        dVert
            finalList.reverse()
            finalList.append(destination_vertex)
            return finalList
        '''
        if starting_vertex not in visited:
            visited.add(starting_vertex)
            
            
            for next_vert in graphlist:
                que.enqueue(graphlist[next_vert])
                visited.add(next_vert)
                newList.append(next_vert)
                #print(f'{visited} FFFF')
                #print(f'{newList} YYYY')
                #print(f'{next_vert} bbb')
        print(f'{vertex} ffff')
        
        for stub in vertex.items():
            if stub[1] == '?':
                player3.currentRoom = world.rooms[newList[0]]
                traversalPath.append(stub[0])
                player3.travel(stub[0])
                traversalPath.append(stub[0])
                listOfExits2 = player3.currentRoom.getExits()
                for exit in listOfExits2:
                   # traversalPath.append(exit)
                    pass
                   # exitPath.append(exit)
                graphlist[starting_vertex][stub[0]] = player3.currentRoom.id
                

def bft(starting_vertex):
        que = Queue()
        visited = set()
        que.enqueue(starting_vertex)
        while que.size() > 0:
            vertex = que.dequeue()
            if vertex not in visited:
                visited.add(vertex)
                print(vertex)
                for next_vert in graphlist:
                    que.enqueue(next_vert)



    
#print(f'{len(world.rooms)} aaaaaaa')
#construct_traversal()
#print('?' in graphlist[0])
#print(len(graphlist))
#print(graphlist)
#recursive_dft(0)
#print(bfs(0, '?'))
#print(graphlist)
#bft(0)
#print(traversalPath)
#print(random.shuffle(traversalPath))
#print(traversalPath)
#print(exitPath)
#print(len(traversalPath))
#print(world.printRooms())

player = Player("Doug", world.startingRoom)
print(world.printRooms())                    
# depth first search until we hit a deadend
# also add movement to traversalPath1 and qMarkRooms1 as we go
# pick a random room
vertices = {}
visited2 = set()
graphList1 = {}
traversalList1 = []
verticesList = []
#and len(vertices) != 0 len(player.currentRoom.getExits()) == 1 and
def rsdfs(starting_vertex):
    # exit condition
    #print(starting_vertex)
    if len(player.currentRoom.getExits()) == 1 and player.currentRoom.id != 0:
        print(player.currentRoom.id)
        print(player.currentRoom.getExits())
        #vertices[player.currentRoom.id-1]['s'] = 1
        print(verticesList)
        print(len(verticesList))
        print(verticesList[len(verticesList)-1])
        print(traversalList1)
        
        print(visited2)
        # abandon all hope all code below this line
        return 0
    
    print(f'{starting_vertex} ASRTARST')
    #print(player.currentRoom)
    print(len(player.currentRoom.getExits()))
    # two situations: one where we have never been to a room before and another where we've been to a partially filled out room
    
    
    # fresh room (never been visited before)
    if player.currentRoom.id not in visited2:
    # add current room id and exits to vertices
    # example {0: {'n': '?', 's': '?', 'w': '?', 'e': '?'}}
        #print('hello')
        # used for picking random direction
        tempDictOfExits = {} 
        tempArrayOfExits = player.currentRoom.getExits()
        for exit in player.currentRoom.getExits():
            tempDictOfExits[exit] = '?'
        vertices[player.currentRoom.id] = tempDictOfExits
        graphList1[player.currentRoom.id] = tempDictOfExits
        #print(vertices)
    
    
        # pick random direction
        # print(random.choice(tempArrayOfExits))
    
        direction = random.choice(tempArrayOfExits)
        #print(direction)
    #partially filled out room    
    else:
        freshList = []
        for test in vertices[player.currentRoom.id]:
            if vertices[player.currentRoom.id][test] == '?':
                freshList.append(test)
        direction = random.choice(freshList)
        # rewrite to say if room has a question mark than pick a direction
    if vertices[player.currentRoom.id][direction] == '?':
       # print(vertices[player.currentRoom.id][direction])
       # print('rue')
    # replace the question mark in the previous room with your new room id
    # in order to do this we have to:
        # create temp storage for the current room id
        # travel to the next room
        # get that room's id
        # go back to the previous room, change the question mark in the direction we traveled to the current rooms id
        # in the current room, change the opposite direction from the one we travel'd '?' to the previous rooms id
        tempStorageForPreviousRoom = player.currentRoom.id
        #if len(player.currentRoom.getExits()) == 1 and player.currentRoom.id != 0:
        #    print('TTTT')
        #    return 0
        #print(direction)
        # print(tempStorageForPreviousRoom)
        player.travel(direction)
        traversalList1.append(direction)
        verticesList.append(player.currentRoom.id)
        # print(player.currentRoom.id)
        # set previous rooms direction key to current room id
        vertices[tempStorageForPreviousRoom][direction] = player.currentRoom.id
        graphList1[tempStorageForPreviousRoom][direction] = player.currentRoom.id
        #print(vertices)
        # add current room id and exits to vertices
        # example {0: {'n': '?', 's': '?', 'w': '?', 'e': '?'}}
        tempDictOfExits = {}
        # used for picking random direction
        tempArrayOfExits = player.currentRoom.getExits()
        for exit in player.currentRoom.getExits():
            tempDictOfExits[exit] = '?'
        vertices[player.currentRoom.id] = tempDictOfExits
        graphList1[player.currentRoom.id] = tempDictOfExits
        print(vertices)
        # grab opposite direction of one travelled and put previous rooms id there
        if direction == 'n':
            vertices[player.currentRoom.id]['s'] = tempStorageForPreviousRoom
            graphList1[player.currentRoom.id]['s'] = tempStorageForPreviousRoom
            print('hoot hoot')
        if direction == 's':
            vertices[player.currentRoom.id]['n'] = tempStorageForPreviousRoom
            graphList1[player.currentRoom.id]['n'] = tempStorageForPreviousRoom
        if direction == 'e':
            vertices[player.currentRoom.id]['w'] = tempStorageForPreviousRoom
            graphList1[player.currentRoom.id]['w'] = tempStorageForPreviousRoom
        if direction == 'w':
            vertices[player.currentRoom.id]['e'] = tempStorageForPreviousRoom
            graphList1[player.currentRoom.id]['e'] = tempStorageForPreviousRoom
        print(vertices)
        print(f'{traversalList1} FFFFFF')
    # travel that direction
    # add it to traversalList
        # after moving, check previous room to see if any of it's exits contains a '?', if true, add that room to the set
        # else, remove it from the set
        # the deadend is the exit condition for the recursion
        # we shouldn't need to check for '?'s because the bfs will do that, and if the list is empty we know we're done
        if 0 in vertices:
            visited2.add(tempStorageForPreviousRoom)
        if '?' in vertices[tempStorageForPreviousRoom].values():
            visited2.add(tempStorageForPreviousRoom)
        else:
            visited2.remove(tempStorageForPreviousRoom)
        print(f'{tempStorageForPreviousRoom} zzzzZZ')
        print(f'{player.currentRoom.id} YYYYYY')
        print(graphList1)
        for next_vert in verticesList:
            rsdfs(next_vert)
    else:
        pass
    '''
    if len(visited2) == len(vertices):
        return 0
    if starting_vertex not in visited2:
        visited2.add(starting_vertex)
        if starting_vertex is None:
            pass
        else:
            print(starting_vertex)
        for next_vert in vertices[starting_vertex]:
            rsdfs(next_vert)
'''
                    

def bfs_path(starting_vertex, destination_vertex):
    print('BOO')
    print(player.currentRoom.id)
    print(destination_vertex)
    #print(visited2.pop())
    print(vertices)
    finalList = []
    newList = []
    que = Queue()
    visited = set()
    que.enqueue(starting_vertex)
    while que.size() > 0:
        vertex = que.dequeue
        if vertex is destination_vertex:
            dVert = destination_vertex
            newList.reverse()
            for listItem in newList:
                if dVert in vertices[listItem]:
                    dVert = listItem
                    finalList.append(listItem)
                else:
                    dVert
            finalList.reverse()
            finalList.append(destination_vertex)
            print(f'{finalList} this is the final list')
            return finalList
        if vertex not in visited:
            
            # check if destination_vertex is in current room
            # assuming yes
            # move to new room
            # append direction to traversalList1
            # add current room to que
            if destination_vertex in vertices[player.currentRoom.id].values():
                somethingList = []
                for test in vertices[player.currentRoom.id]:
                    if vertices[player.currentRoom.id][test] == destination_vertex:
                        somethingList.append(test)
                player.travel(somethingList[0])
                traversalList1.append(somethingList[0])
                print('DEST IS EXIT')
                # check the exits in current room
                # if 1    
            elif len(player.currentRoom.getExits()) == 1:    
                # add vertex to visited (maybe but probably not)
                exitsArray = player.currentRoom.getExits()
                # move in only available direction
                print(exitsArray)
                player.travel(exitsArray[0])
                # add vertex to visited
                visited.add(vertex)
                print(visited)
                # add direction moved to traversalList1
                traversalList1.append(exitsArray[0])
                print(player.currentRoom.id)
                print('EXIT IS ONE')
            #else:
                # else (don't write keyword)
                # pick any direction with ?
            freshList2 = []
            for test in vertices[player.currentRoom.id]:
                if vertices[player.currentRoom.id][test] == '?':
                    freshList2.append(test)
            print(f'{freshList2} FRESHLIST BRBY')
            direction = random.choice(freshList2[0])
            print(direction)
                # add vertex to visited maybe but probably not)
                # add vertex to holding variable (tempStorage)
            tempStorageDirection = direction
            tempStoragePreviousRoom = player.currentRoom.id
                # travel to new direction
            player.travel(direction)
                # append direction to traversalList1
            traversalList1.append(direction)
                # append current room id to verticesList
            verticesList.append(player.currentRoom.id)
                # if this doesn't work, make a new verticesList and put it outside the function
                # set previous rooms direction key to current room id
            vertices[tempStoragePreviousRoom][direction] = player.currentRoom.id
            graphList1[tempStoragePreviousRoom][direction] = player.currentRoom.id
                # grab opposite direction of one travelled and put previous rooms id there
            print(visited2)
            print(verticesList)
            print('PENERIC PRINT STATEMENT')
            print(vertices)
            if direction == 'n':
                vertices[player.currentRoom.id]['s'] = tempStoragePreviousRoom
                graphList1[player.currentRoom.id]['s'] = tempStoragePreviousRoom
            if direction == 's':
                vertices[player.currentRoom.id]['n'] = tempStoragePreviousRoom
                graphList1[player.currentRoom.id]['n'] = tempStoragePreviousRoom
            if direction == 'e':
                vertices[player.currentRoom.id]['w'] = tempStoragePreviousRoom
                graphList1[player.currentRoom.id]['w'] = tempStoragePreviousRoom
            if direction == 'w':
                vertices[player.currentRoom.id]['e'] = tempStoragePreviousRoom
                graphList1[player.currentRoom.id]['e'] = tempStoragePreviousRoom
                # check if the previous room has no question marks
            print(vertices[tempStoragePreviousRoom].values())
            if '?' not in vertices[tempStoragePreviousRoom].values():
                print('YES')
                testSet = set()
                print(len(testSet))
                print(tempStoragePreviousRoom)
                print(player.currentRoom.id)
                visited2.remove(tempStoragePreviousRoom)
                print(visited2)
                    # if yes, remove from visited2
            visited.add(player.currentRoom.id)
                # add current rooom to que
            
    
    
def fourth_attempt():
    #traversalPath1 = []
    #qMarkRooms1 = set()
    #graphlist1 = {}
    
    rsdfs(0)
    print(f'{traversalList1} beginning loop')
    #while len(visited2) != 0:
    print(f'{visited2} WHEEOROR')
    print(player.currentRoom.id)
    bfs_path(8,0)
        
    return print(traversalList1)

#fourth_attempt()
print(' RRERISTNIERSTNEIRST')
rsdfs(0)
#bfs_path()
'''
def bft(starting_vertex):
        que = Queue()
        visited = set()
        que.enqueue(starting_vertex)
        while que.size() > 0:
            vertex = que.dequeue()
            if vertex not in visited:
                visited.add(vertex)
                print(vertex)
                for next_vert in world.rooms[vertex].id:
                    que.enqueue(next_vert)
'''


# TRAVERSAL TEST
visited_rooms = set()
player.currentRoom = world.startingRoom
print(world.startingRoom)
visited_rooms.add(player.currentRoom)
for move in traversalList1:
    player.travel(move)
    visited_rooms.add(player.currentRoom)

if len(visited_rooms) == len(roomGraph1):
    print(f"TESTS PASSED: {len(traversalList1)} moves, {len(visited_rooms)} rooms visited")
else:
    print("TESTS FAILED: INCOMPLETE TRAVERSAL")
    print(f"{len(roomGraph1) - len(visited_rooms)} unvisited rooms")
print(len(traversalList1))
print(traversalList1)


#######
# UNCOMMENT TO WALK AROUND
#######
'''
player.currentRoom.printRoomDescription(player)
while True:
    cmds = input("-> ").lower().split(" ")
    if cmds[0] in ["n", "s", "e", "w"]:
        player.travel(cmds[0], True)
    else:
        print("I did not understand that command.")
'''
