# We need a room once a new meeting starts, and returns a room when a meeting finishes
# So sort all start and end times, and count the max number of rooms needed simultaneously
# To distinguish start and end times, mark all end times negative.
# But this way we need to write our own comparator
class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        times = [val if i == 0 else -val for interval in intervals for i, val in enumerate(interval)]
        # Can't just do times.sort(key=lambda x: abs(x)).
        # Need to put negative val ahead when equal: [-10, 10] ([10, -10] will be wrong)
        times.sort(key=lambda x: [abs(x), 0 if x < 0 else 1])

        max_rooms, cur_rooms = 0, 0
        for t in times:
            if t >= 0:
                cur_rooms += 1
            else:
                cur_rooms -= 1

            max_rooms = max(max_rooms, cur_rooms)
        return max_rooms

# Same logic but a bit troublesome way is to use two separated sorted lists for start and end times, and two pointers
# Note: there is at least one meeting
# class Solution:
#     def minMeetingRooms(self, intervals: List[List[int]]) -> int:
#         starts = sorted([i[0] for i in intervals])
#         ends = sorted([i[1] for i in intervals])

#         max_rooms, cur_rooms = 0, 0
#         s, e = 0, 0 # pointers of start times and end times

#         while s < len(starts): # when there is still a chance of needing more rooms
#             if starts[s] < ends[e]:
#                 cur_rooms += 1
#                 max_rooms = max(max_rooms, cur_rooms)
#                 s += 1
#             else:
#                 cur_rooms -= 1
#                 e += 1

#         return max_rooms


# 	/*
# 	 * My thought. Time: O(2Nlog2N); Sapce: O(2N) Put all start and (-1)*end
# 	 * time in an array, and sort it by absolute value:
# 	 * [[0, 30],[5, 10],[15, 20]]
# 	 * -> [0, 5, -10, 15, -20, -30]
# 	 *
# 	 * then scan this array, curNeededRooms++ if sees an >=0 number,
# 	 * otherwise --. Then record the maximal needed room number
# 	 */
# 	public int minMeetingRooms(Interval[] intervals) {
# 	    if (intervals == null || intervals.length == 0) {
# 		return 0;
# 	    }

# 	    Integer[] times = new Integer[intervals.length * 2];
# 	    int i = 0;
# 	    for (Interval interval : intervals) {
# 		times[i++] = interval.start;
# 		times[i++] = -1 * interval.end;
# 	    }

# 	    Arrays.sort(times, new Comparator<Integer>() {
# 		@Override
# 		public int compare(Integer i1, Integer i2) {
# 		    if (Math.abs(i1) != Math.abs(i2)) {
# 			return Math.abs(i1) - Math.abs(i2);
# 		    } else {
# 			return i1 - i2;
# 		    }
# 		}
# 	    });

# 	    int needed = 0;
# 	    int max = 0;
# 	    for (int k = 0; k < times.length; k++) {
# 		needed = times[k] >= 0 ? needed + 1 : needed - 1;
# 		max = Math.max(max, needed);
# 	    }

# 	    return max;
# 	}        