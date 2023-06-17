def solution(players, callings):
    idx_pos_dict = {i : player for i, player in enumerate(players)}
    pos_idx_dict = {player : i for i, player in enumerate(players)}
    

    for call in callings:
        cur_idx = pos_idx_dict[call]
        front_idx = cur_idx-1
        
        cur_player = call
        front_player = idx_pos_dict[front_idx]
        
        idx_pos_dict[cur_idx] = front_player
        idx_pos_dict[front_idx] = cur_player
        
        pos_idx_dict[cur_player] = front_idx
        pos_idx_dict[front_player] = cur_idx
        
        
        
    return list(idx_pos_dict.values())


