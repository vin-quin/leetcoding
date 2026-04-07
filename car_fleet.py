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
        
        cars = sorted(zip(position, speed)) # pos,step
        fleetCount = (len(cars))
        fleets = []
        print(cars)
        [(12,4),(12,2),(6,1),(6,3),(1,1)]
        currFleetCount = fleetCount

        while cars:
            cars = [(c[0]+c[1], c[1]) for c in cars] # step cars forward 1 tick
            carsPasssed = []
            fleetsSeen = {} # pos: minspeed

            for i in range(len(cars)):
                # Remove all cars that >= target, that is 1 fleet 
                if cars[i][0] >= target:
                    carsPasssed.append(i)
                    continue

                # Consolidate remaining fleets
                if cars[i][0] not in fleetsSeen: # Min speed of this fleet is the only car
                    fleetsSeen[cars[i][0]] = cars[i][1]
                else: # Slow fleet down to slowest car
                    fleetsSeen[cars[i][0]] = min(cars[i][1], fleetsSeen[cars[i][1]])

            print(fleetsSeen)
            if carsPasssed:
                for i in reversed(carsPasssed):
                    cars.pop(i)
                fleetCount -= 1
            print(cars)

        return fleetCount 


def main():
    s = Solution()
    print(s.solve(12, [10,8,0,5,3], [2,4,1,1,3]))

if __name__ == '__main__':
    main()