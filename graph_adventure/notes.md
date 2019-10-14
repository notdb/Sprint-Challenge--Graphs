Work on solutions for three different room types, modifying as needed before
working ono the final solution.

So we have to fill in the traversal path somehow, we have a graph, need a way to
test movement

we also have the graph of rooms, a dictionary of rooms
that looks like

roomGraph0={0: [(3, 5), {'n': 1}], 1: [(3, 6), {'s': 0, 'n': 2}], 2: [(3, 7),
{'s': 1}]}

It's a dictionary whose key is an array, with a tuple, and another dictionary
containing valid directions

It looks like what we're going to end up doing is looping through the room
graph, and adding n, s, e ,w to the traversal path

Two more questions, how do we know we've visited every room, and whats moving to
a new room look like

going to make a bft to traverse all the rooms to build up the traversalPath and
try that. It's not going to work for every situation but it's a start


Third attempt
We need to write a dft until we hit a dead end, and then a bfs to go back to the
nearest room with unexplored rooms. Then start the dft again

We need to keep track of two things, unexplored rooms (rooms with question
marks) and the traversal path (rooms we've traveled to)

dft (do this recursively until we get a deadend)
a stack or a set that contains only rooms that have at least one questionmark
a traversal list that contains every room we've visited
and a bfs that is used whenever we need to go from the current room to the
nearest room with a question mark (this should be the last room we've added
thats in the set or stack)

add rs dfs
add bft

when we get back from break

finish checking to make sure the graphlist for the current room is set up

pick random room direction
move in that direction
add that direction to traversal list
set up exit condition for deadend

need to find out what to do when a room has no question marks
attempting recursion until we hit a deadend

figure out how to solve origin

use vertices list to go back to the room before the deadend and fix everything

now i think we can work on our bfs_path to send us back to a room from visited2
on our current path

so our current vertex is the players current room id, the destination vertex
should be the last vertex we added to the set (to minimize distance traveled

we'll be able to get back to our vertex it might take a little while but we
should be able to write it as planned

finish writing bfs
finish writing notes in bfs
checking to see if we'll ever have to travel to a completely filled path while
doing this
check to see what happens when a completed roomid is enterd to rsdft
