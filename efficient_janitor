def getMinTrips(weight, n):
    weight.sort()
    left = 0
    right = n - 1
    trips = 0

    while left <= right:
        if weight[right] > 1.99 or (weight[left] + weight[right] > 3):
            trips += 1
            right -= 1
        else:
            trips += 1
            left += 1
            right -= 1

        if left > right:
            break

    return trips

n = int(input())
weight = list(map(float, input().strip().split()))
trips = getMinTrips(weight, n)
print(trips)
