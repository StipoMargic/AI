from vok import VOK

def generate(vokb, _set):
    if(str(vokb) in _set):
        return
    
    print(vokb)
    _set.add(str(vokb))

    if(vokb.is_terminal()):
        return
    
    for i in vokb.next_action():
        vokb.action(i)
        generate(vokb, _set)
        vokb.undo_action(i)

    return

def grab(dictionary, solution):
    while(solution != None):
        print(str(solution))
        solution = dictionary[str(solution)]
        


def solution_dfs(vok):
    queue = [vok]
    dictionary = {}
    dictionary[str(vok)] = None
    visited = set({})    
    while(len(queue) > 0):
        q_top = queue.pop(-1) 
        
        if(q_top.is_terminal()):
            visited.add(q_top.__str__())
            if(q_top.is_solved()):
                print("Visited length", len(visited))
                grab(dictionary, q_top)
                return dictionary
        elif(str(q_top) not in visited):
            visited.add(q_top.__str__())
            for i in q_top.next_states():
                if(str(i) not in dictionary):    
                    dictionary[str(i)] = str(q_top)
                queue.append(i)
    
    return dictionary


def solution_bfs(vok):
    queue = [vok]
    dictionary = {}
    dictionary[str(vok)] = None
    visited = set({})
    
    while(len(queue) > 0):
        q_top = queue.pop(0) 
        if(q_top.is_terminal()):
            visited.add(q_top.__str__())
            if(q_top.is_solved()):
                print("Visited len ", len(visited))
                grab(dictionary, q_top)
                
                return dictionary
        
        elif(str(q_top) not in visited):
            visited.add(q_top.__str__())
            for i in q_top.next_states():
                if(str(i) not in dictionary):    
                    dictionary[str(i)] = str(q_top)
                queue.append(i)
    return dictionary


def BestFS(vok):
    queue = [vok]
    dictionary = {}
    dictionary[str(vok)] = None
    visited = set({})

    while(len(queue) > 0):
        queue = sorted(queue, key=heuristic)
        q_top = queue.pop(0)
        
        if(q_top.is_terminal()):
            visited.add(q_top.__str__())
            if(q_top.is_solved()):
                print("Visited len ", len(visited))
                grab(dictionary, q_top)
                return dictionary
        elif(str(q_top) not in visited):
            visited.add(q_top.__str__())
            for i in q_top.next_states():
                if(str(i) not in dictionary):
                    dictionary[str(i)] = str(q_top)
                queue.append(i)
    return dictionary


def heuristic(state):
    counter = 0
    right = state.board[-4:]
    
    for i in right:
        if(i == "-"):
            counter += 1

    return counter


if __name__ == "__main__":
    vokb = VOK()
    print("Generate: ")
    BestFS(vokb)
