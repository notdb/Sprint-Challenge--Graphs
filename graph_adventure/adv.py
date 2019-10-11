from room import Room
from player import Player
from world import World
from roomgraphs import roomGraph0
from util import Stack, Queue  # These may come in handy
import random

                    
# Load world
world = World()

world.loadGraph(roomGraph0)
#world.printRooms()
#print(world.rooms[1].getExits())
#print(world.roomGrid)

player = Player("Name", world.startingRoom)
player2 = Player("Doug", world.startingRoom)

# FILL THIS IN
graphlist = {}
def construct_traversal():
    for i in range(len(world.rooms)):
        player2.currentRoom = world.rooms[i]
    
    #while len(graphlist) is not len(world.rooms):
        unvisited = {}
        listOfExits = player2.currentRoom.getExits()
        for exit in listOfExits:
            unvisited[exit] = '?'
            graphlist[player2.currentRoom.id] = unvisited
        print(graphlist)
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

           
    
construct_traversal()
#print(world.rooms)
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
traversalPath = ['n', 'n','s','s','e','w']
# TRAVERSAL TEST
visited_rooms = set()
player.currentRoom = world.startingRoom
visited_rooms.add(player.currentRoom)
for move in traversalPath:
    player.travel(move)
    visited_rooms.add(player.currentRoom)

if len(visited_rooms) == len(roomGraph0):
    print(f"TESTS PASSED: {len(traversalPath)} moves, {len(visited_rooms)} rooms visited")
else:
    print("TESTS FAILED: INCOMPLETE TRAVERSAL")
    print(f"{len(roomGraph0) - len(visited_rooms)} unvisited rooms")
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
