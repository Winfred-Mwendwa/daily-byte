def vacuum_robot_returns_to_org_pstn(moves) -> bool:
    left_move_count = 0
    right_move_count = 0
    up_move_count = 0
    down_move_count = 0

    for move in moves:
        if 'L' in move:
            left_move_count += 1
        if 'R' in move:
            right_move_count +=1
        if 'U' in move:
            up_move_count += 1
        if 'D' in move:
            down_move_count +=1

    # note that '&' is the bitwise AND operation and 'and' is the logical AND operation in Python
    return left_move_count == right_move_count and up_move_count == down_move_count

print(vacuum_robot_returns_to_org_pstn('UD'))



