def stirling_subsets(length: int):
    num_of_block = []
    direction_to_move = []
    next = [0] * length

    for _ in range(length):
        num_of_block.append(0)
        direction_to_move.append(True)

    print(num_of_block)
    print(direction_to_move)
    print(next)

    active_element = length - 1
    k = num_of_block[active_element]

    if direction_to_move[active_element]:
        # move element forward
        pass


if __name__ == '__main__':
    SEQUENCE_LENGTH = 3
    stirling_subsets(SEQUENCE_LENGTH)
