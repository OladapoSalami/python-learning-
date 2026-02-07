def hanoi_solver(n):
    # Requirement: Initialize the rods
    # Rod A starts with all disks, B and C are empty
    rods = {
        'A': list(range(n, 0, -1)),
        'B': [],
        'C': []
    }
    
    output_states = []

    def format_state():
        # Requirement: Format like "[3, 2, 1] [] []"
        return f"{rods['A']} {rods['B']} {rods['C']}"

    # Record the initial state
    output_states.append(format_state())

    def move(n, source, target, auxiliary):
        if n > 0:
            # Move n-1 disks from source to auxiliary
            move(n - 1, source, auxiliary, target)
            
            # Move the actual disk
            disk = rods[source].pop()
            rods[target].append(disk)
            
            # Record the state after the move
            output_states.append(format_state())
            
            # Move n-1 disks from auxiliary to target
            move(n - 1, auxiliary, target, source)

    # Solve from Rod A to Rod C using Rod B as auxiliary
    move(n, 'A', 'C', 'B')
    
    # Requirement: Return as a string separated by newlines
    return "\n".join(output_states)
