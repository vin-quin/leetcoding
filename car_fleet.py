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
        
        cars = sorted(zip(position, speed), reverse=True) # pos,step
        fleetCount = (len(cars))
        fleets = []
        print(cars)
        # [(12,4),(12,2),(6,1),(6,3),(1,1)]
        currFleetCount = fleetCount
        
        l, r = 0, len(cars)-1
        while cars and l < r: # Slide from i+1 to end, consolidating until we can't. Then +1 and consolidate next
            # cars = [(c[0]+c[1], c[1]) for c in cars] # step cars forward 1 tick
            lCar = cars[l][0]+speed[l]
            cars[l] = (cars[l][0]+speed[l], cars[l][1])
            print(l, r)

            while cars[r][0] + speed[r] >= lCar: # Car R has to slow down to match L in the fleet
                rCar = cars[r][0]+speed[r]
                fleetCar = (min(lCar, rCar), min(speed[l], speed[r]))
                print(f'Joining fleet: {fleetCar}')
                cars[r] = cars[l] = fleetCar
                r -= 1

            print(cars)
            if cars[l][0] >= target:# A fleet has gone remove em all
                fleetCount -= 1
                while cars[l][0] >= target:
                    l += 1
                    r -= 1
            else:
                l+=1
                r-=1

        return fleetCount 


def main():
    s = Solution()
    # print(s.solve(12, [10,8,0,5,3], [2,4,1,1,3]))
    # print(s.solve(10, [3], [3]))
    print(s.solve(100, [0,2,4], [4,2,1]))

if __name__ == '__main__':
    main()