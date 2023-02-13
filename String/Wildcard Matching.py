# Finite State machine
# Time: O(s*p) (?); Space O(s+p)
# https://leetcode.com/problems/wildcard-matching/discuss/138878/Finite-state-machine-with-Python-and-dictionary.-13-lines-O(p%2Bs)-time
# Represent the pattern as a finite state machine

# * and ? are slightly different: ? can match only 1 character, which means after you transfer through a ? link,
# you can't traverse it again, but after you transfer through a * link, you still have access to it, infinitely. This
# is why a ? link takes you to a new state, while a * link takes you back to where it starts, thus this link can be
# traversed infinitely.
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        transfer = {}  # state transfer map <(current_state_id, char), next_state_id>
        state_id = 0  # state id.

        # 1) Construct state transfer map
        for char in p:
            if char == '*':
                # Not going to the next state since * is reusable. So it means we can stay
                # at this state
                transfer[(state_id, char)] = state_id
            else:
                transfer[(state_id, char)] = state_id + 1  # else, takes us to the next state
                state_id += 1

        # One state is pointed from an earlier state. So if you can reach the final state, you can reach every single
        # earlier state
        accept = state_id  # final state
        states = {0}  # Reachable states at this round

        # for char in s:
        #     states = {transfer.get((at, token)) for at in states if at is not None for token in (char, '*', '?')}
        for char in s:
            next_states = set()  # reachable states of the next round
            for token in [char, '*', '?']: # 3 possibilities for having a match in p for the given char
                for state_id in states:
                    next_state = transfer.get((state_id, token))  # check if (state, token) can get us to the next state
                    if next_state is not None:  # if this next state exists. NOTE: "if next_state" fails!
                        next_states.add(next_state)

            if not next_states:
                return False
            states = next_states

        return accept in states  # see if we can reach the final state of the given pattern from input s

# DP
#     /*
#      * Both s and p can contain '*' and/or '?'
#      *
#      * DP: http://blog.csdn.net/linhuanmars/article/details/21198049
#      * http://m4tiku.duapp.com/report?pid=123
#      */
#     public class Solution_DP {
# 	public boolean isMatch(String s, String p) {
# 	    boolean[] preFlag = new boolean[s.length() + 1];
# 	    boolean[] curFlag = new boolean[s.length() + 1];

# 	    int minCount = 0;
# 	    for (int i = 0; i < p.length(); i++) {
# 		if (p.charAt(i) != '*') {
# 		    minCount++;
# 		}
# 	    }
# 	    if (minCount > s.length()) {
# 		return false;
# 	    }

# 	    preFlag[0] = true;
# 	    for (int i = 0; i < p.length(); i++) {
# 		for (int j = 0; j <= s.length(); j++) {
# 		    if (p.charAt(i) == '?') {
# 			curFlag[j] = j == 0 ? false : preFlag[j - 1];
# 		    } else if (p.charAt(i) == '*') {
# 			curFlag[j] = j == 0 ? preFlag[j]
# 				: (preFlag[j] || curFlag[j - 1]);
# 		    } else {
# 			curFlag[j] = (j == 0 || p.charAt(i) != s.charAt(j - 1)) ? false
# 				: preFlag[j - 1];
# 		    }
# 		}
# 		boolean[] temp = preFlag;
# 		preFlag = curFlag;
# 		curFlag = temp;
# 	    }
# 	    return preFlag[s.length()];
# 	}
#     }
