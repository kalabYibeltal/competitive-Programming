class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        houses.sort()
        heaters.sort()

        heater_ptr = 0
        answer = 0 

        for house in houses:
            dist = abs(house - heaters[heater_ptr])

            for index in range(heater_ptr + 1, len(heaters)):
                dist2 = abs(house - heaters[index])

                if dist2 > dist:
                    break

                else:
                    dist = dist2
                    heater_ptr = index
                     
            answer = max (answer, dist)

        return answer