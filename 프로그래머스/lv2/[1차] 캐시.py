from collections import deque


def search_cache(cache, city):
    if city in cache:
        return True
    else:
        return False


def solution(cacheSize, cities):
    answer = 0
    queue = deque(maxlen=cacheSize)

    for city in cities:
        city = city.lower()

        if cacheSize == 0:
            answer = len(cities) * 5
            return answer
        if search_cache(queue, city):
            queue.remove(city)
            answer += 1
        else:
            answer += 5

        queue.append(city)

    return answer