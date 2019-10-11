from room import Room
from player import Player
from world import World
from roomgraphs import roomGraph0, roomGraph1, roomGraph2, roomGraph3, roomGraph4
from util import Stack, Queue  # These may come in handy
import random

                    
# Load world
world = World()

world.loadGraph(roomGraph2)
#world.printRooms()
#print(world.rooms[1].getExits())
#print(world.roomGrid)
# start at room 0, pick a random direction, go to that room, add step taken to list, 
player = Player("Name", world.startingRoom)
player2 = Player("Doug", world.startingRoom)
player3 = Player("NotDoug", world.startingRoom)
player4 = Player("TheRealDeal", world.startingRoom)
# FILL THIS IN
graphlist = {}
visited = set()
traversalPath = []
exitPath = []

def theRealDeal():
    print(player4.currentRoom)


theRealDeal()
    
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
#bft(0)
'''
# TRAVERSAL TEST
visited_rooms = set()
player.currentRoom = world.startingRoom
print(world.startingRoom)
visited_rooms.add(player.currentRoom)
for move in traversalPath:
    player.travel(move)
    visited_rooms.add(player.currentRoom)

if len(visited_rooms) == len(roomGraph3):
    print(f"TESTS PASSED: {len(traversalPath)} moves, {len(visited_rooms)} rooms visited")
else:
    print("TESTS FAILED: INCOMPLETE TRAVERSAL")
    print(f"{len(roomGraph3) - len(visited_rooms)} unvisited rooms")
print(len(traversalPath))
'''

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
