# https://leetcode.com/problems/car-fleet/description/
class Solution:
    def solve(self, target: int, position: list[int], speed: list[int]) -> int:
        '''
        cars cannot overtake, only follow behind slightly slower than the lead 
        a fleet's speed is the lowest speed car in the fleet

        car can join a fleet when it reaches/would pass the fleet car's position
        fleet always slows down to match the lowest speed car in the fleet

        fleets <= N
        Cars NEVER start in a fleet, so we ALWAYS start with N fleets and can only ever reduce the number
        fleets = 0

        t=0
        [10,8,0,5,3]
        t=1
        [12,12,1,6,6] 2 cars have combined into fleets, 1 fleet reached target and can be removed
        Another fleet had to match speed, so they reduce to speed of 1 to match min
        t=2
        [2,7,7] 
        ...
        t=?
        [7] The 2 car fleet has hit 12 and been removed from the road, only one fleet remains

        go thru every n in position and + speed
            remove every car that has hit the target inc fleets by 1. If no cars hit target do nothing
            set the speed of each new fleet to the min speed in its range
        '''
        from math import ceil
        cars = sorted(zip(position, speed), reverse=True) # pos,step
        fleetCount = (len(cars))
        # [(12,4),(12,2),(6,1),(6,3),(1,1)]
        
        times = [ceil((target-t[0])/t[1]) for t in cars]
        print(times)

        fleets = [times[-1]]
        for i in range(len(times)-2, -1, -1):
            if times[i] >= fleets[-1]: # car in back is faster than car in front, so they become a fleet at some point
                fleets[-1] = max(times[i], fleets[-1]) # Update the slowest car for this fleet
            else: # This car is tis own fleet
                fleets.append(times[i])

        print(fleets)

        return len(fleets) 


def main():
    s = Solution()
    print(s.solve(12, [10,8,0,5,3], [2,4,1,1,3]))
    print(s.solve(10, [3], [3]))
    print(s.solve(100, [0,2,4], [4,2,1]))

if __name__ == '__main__':
    main()