from room import Room
from player import Player
from world import World
from roomgraphs import roomGraph0, roomGraph1, roomGraph2, roomGraph3, roomGraph4
from util import Stack, Queue
import random

# Load world
world = World()

# You may uncomment the smaller graphs for development and testing purposes.
 
world.loadGraph(roomGraph0)
world.printRooms()
player = Player("Name", world.startingRoom)

vertices = {}
visited2 = set()
graphList1 = {}
traversalList1 = []
verticesList = []

def big_traverse(starting_vertex):
    pass

# FILL THIS IN
traversalPath = ['n', 's']


# TRAVERSAL TEST
visited_rooms = set()
player.currentRoom = world.startingRoom
visited_rooms.add(player.currentRoom)
for move in traversalPath:
    player.travel(move)
    visited_rooms.add(player.currentRoom)

if len(visited_rooms) == len(roomGraph):
    print(f"TESTS PASSED: {len(traversalPath)} moves, {len(visited_rooms)} rooms visited")
else:
    print("TESTS FAILED: INCOMPLETE TRAVERSAL")
    print(f"{len(roomGraph) - len(visited_rooms)} unvisited rooms")



#######
# UNCOMMENT TO WALK AROUND
#######
# player.currentRoom.printRoomDescription(player)
# while True:
#     cmds = input("-> ").lower().split(" ")
#     if cmds[0] in ["n", "s", "e", "w"]:
#         player.travel(cmds[0], True)
#     else:
#         print("I did not understand that command.")
