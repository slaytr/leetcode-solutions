class Solution:
    def findPoisonedDuration(self, timeSeries: List[int], duration: int) -> int:
#         if timeSeries:
#             if len(timeSeries) == 1:
#                 return duration
#             damage = 0
#             remaining_duration = 0

#             for time in range(max(timeSeries)+1):
#                 if time in timeSeries:
#                     remaining_duration = duration
#                 if remaining_duration > 0:
#                     remaining_duration -= 1
#                     damage +=1
#                 #print(damage, remaining_duration)
#             damage += remaining_duration

#             return damage
#         return 0
        print(len(timeSeries))
        if timeSeries:
            damage = 0
            ptime = None
            for time in timeSeries:
                if not ptime:
                    ptime = time+1
                
                if time+1-ptime >= duration:
                    damage += duration
                else:
                    damage += time-ptime+1
                
                ptime = time+1
                
            return damage + duration
        return 0