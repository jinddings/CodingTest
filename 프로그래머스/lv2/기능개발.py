from collections import deque

def solution(progresses, speeds):
    answer = []
    process_q = deque(progresses)
    speeds_q = deque(speeds)

    while process_q:
        if process_q[0] < 100:
            for i in range(len(process_q)):
                process_q[i] += speeds_q[i]
        else:
            count = 0
            while process_q and process_q[0] >= 100:
                process_q.popleft()
                speeds_q.popleft()
                count += 1
            answer.append(count)

    return answer