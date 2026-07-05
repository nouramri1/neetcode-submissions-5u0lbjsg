class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        position_to_speed = {}
        for i in range(len(position)):
            position_to_speed[position[i]] = speed[i]
        position.sort(reverse = True)
        fleet_count = 0
        current_finish_time = (target - position[0])/position_to_speed[position[0]]
        for i in range(1, len(position)):
            
            finish_time = (target - position[i])/position_to_speed[position[i]]
            if finish_time > current_finish_time:
                fleet_count += 1
                current_finish_time = finish_time
        fleet_count +=1 
        return fleet_count

        
        