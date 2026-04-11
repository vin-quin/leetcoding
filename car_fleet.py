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

        (target - pos) / speed = how many steps it will take for that car to finish
        0->2/2=1 
        1->4/4=1 
        2->12/1=12
        3->7/1=7
        4->9/3=3

        if the car @ i+1 finishes BEFORE or WITH the car @ i then a fleet must be formed of (i, i+1)
        since i+1 cannot actually overtake i, it would have to join in

        [(10,1), (8,1), (0,12), (5,7), (3,3)]
        [(10,1), (8,1), (5,7), (3,3), (0,12),]
        go in reverse from r->l
        for i 
            if stack
                if i is faster than top of stack they become a fleet because we know top of stack is in front of i
                    pop top of stack and push new speed for fleet (pos, slowest) may actually not need to do anything since top should always be sl
            push onto stack
        0,12
        5,7
        10,1
        '''

        cars = sorted([(p, (target-p)/s) for p, s in zip(position, speed)]) # (pos,time to finish)
        fleets = []
     
        for i in range(len(cars)-1, -1, -1):
            if fleets and cars[i][1] <= fleets[-1][1]:
                print(f'{cars[i]} faster than top of stack {fleets[-1]}')
                continue # We don't need to do anything let this car be absorbed by the currnet fleet  

            print(f'{cars[i]} is a new fleet')
            fleets.append(cars[i])

        return len(fleets) 


def main():
    s = Solution()
    print(s.solve(12, [10,8,0,5,3], [2,4,1,1,3]))
    print(s.solve(10, [3], [3]))
    print(s.solve(100, [0,2,4], [4,2,1]))
    print(s.solve(10, [8,3,7,4,6,5], [4,4,4,4,4,4]))

if __name__ == '__main__':
    main()