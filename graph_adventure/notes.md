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
