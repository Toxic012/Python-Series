# Tower of Hanoi for n disks
def toh(n, source, auxiliary, destination, moves):
    if n == 1:
        moves.append(f"{source} -> {destination}")
        return
    # Move n-1 disks from source to auxiliary
    toh(n-1, source, destination, auxiliary, moves)
    # Move nth disk from source to destination
    moves.append(f"{source} -> {destination}")
    # Move n-1 disks from auxiliary to destination
    toh(n-1, auxiliary, source, destination, moves)

# Main
if __name__ == "__main__":
    n = 7   # number of disks
    moves = []
    toh(n, "A", "B", "C", moves)

    print(f"Total moves required: {len(moves)}")
    for i, move in enumerate(moves, 1):
        print(f"Step {i}: {move}")
