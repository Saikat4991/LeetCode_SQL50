class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        position_speed_pair = zip(position,speed)
        sorted_pair = sorted(position_speed_pair, reverse = True) #Decending order
        stack = []
        for p, s in sorted_pair:
            stack.append((target - p)/s)
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()

            
        return len(stack)
            