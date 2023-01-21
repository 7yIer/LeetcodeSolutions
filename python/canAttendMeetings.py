# https://leetcode.com/problems/meeting-rooms/
class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        # Store every time that is reserved into a dictionary.
        # If the time is already reserved, the meetings must overlap.
        
        d = {}
        
        for interval in intervals:
            start = interval[0]
            end = interval[1]
            
            for i in range(start, end):
                if i in d:
                    return False
                d[i] = i
                
        return True
