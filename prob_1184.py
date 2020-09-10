class Solution:
    def distanceBetweenBusStops(self, distance, start, stop):
        if start == stop:
            return 0
        start, stop = min(start, stop), max(start, stop)
        ans1 = sum(distance[start: stop])
        i = 0
        while i != start:
            distance.append(distance[i])
            i += 1
        ans2 = sum(distance[stop:])
        # print(distance)
        return min(ans1, ans2)
