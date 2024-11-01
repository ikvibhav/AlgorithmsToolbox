
# Time Complexity: O(n)
# Space Complexity: O(1)
def greedy_min_tank_refill(G_CityDistance, G_MinRefillDistance, G_NumberOfStops, G_StopArray):
    NumRefills = 0
    CurrentRefill = 0

    # Iterate through the stops
    while CurrentRefill <= G_NumberOfStops:
        LastRefill = CurrentRefill
        
        #import pdb; pdb.set_trace()
        # Check if the next stop is within the minimum refill distance
        # Until next stop is within the minimum refill distance, keep incrementing the CurrentRefill index
        while CurrentRefill <= G_NumberOfStops and G_StopArray[CurrentRefill+1] - G_StopArray[LastRefill] <= G_MinRefillDistance:
                CurrentRefill += 1
        
        if LastRefill == CurrentRefill:
            return -1
        
        if CurrentRefill <= G_NumberOfStops:
            NumRefills += 1        
        
    return NumRefills

if __name__ == "__main__":
    CityDistance = int(input())
    MinRefillDistance = int(input())
    NumberOfStops = int(input())
    StringStopArray = input()
    StopArray = [0]*NumberOfStops

    for index in range(NumberOfStops):
        StopArray[index] = (int(StringStopArray.split()[index]))
        
    StopArray.append(CityDistance)
    StopArray = [0] + StopArray

    print(greedy_min_tank_refill(CityDistance,MinRefillDistance,NumberOfStops,StopArray))        