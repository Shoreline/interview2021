# A valid number can be split up into these components (in order):

# A decimal number or an integer.
# (Optional) An 'e' or 'E', followed by an integer.
# A decimal number can be split up into these components (in order):

# (Optional) A sign character (either '+' or '-').
# One of the following formats:
# One or more digits, followed by a dot '.'.
# One or more digits, followed by a dot '.', followed by one or more digits.
# A dot '.', followed by one or more digits.
# An integer can be split up into these components (in order):

# (Optional) A sign character (either '+' or '-').
# One or more digits.
# For example, all the following are valid numbers: ["2", "0089", "-0.1", "+3.14", "4.", "-.9", "2e10", "-90E3", "3e+7", "+6e-1", "53.5e93", "-123.456e789"],
# while the following are not valid numbers: ["abc", "1a", "1e", "e3", "99e2.5", "--6", "-+3", "95a54e53"].

# Deterministic Finite Automaton (DFA)
class Solution:
    def isNumber(self, s: str) -> bool:
        # This is the DFA we have designed above
        # array as a map of <cur_state_id, map<acceptable_next_group, next_state_id>>
        # 0 - 7, in total 8 states. 0 is the starting state.
        # 0: initial state
        # 1: digit before any dot or exponent symbol
        # 2: sign (+ or -) before any dot or exponent symbol
        # 3. dot (.)
        # 4. digit after a dot symbol
        # 5. exponent (e or E)
        # 6. sign (+ / -) after an exponent symbol
        # 7. digit after an exponent symbol
        #
        # Only valid while ending at state 1, 4, 7
        dfa = [
            {"digit": 1, "sign": 2, "dot": 3},
            {"digit": 1, "dot": 4, "exponent": 5},
            {"digit": 1, "dot": 3},
            {"digit": 4},
            {"digit": 4, "exponent": 5},
            {"sign": 6, "digit": 7},
            {"digit": 7},
            {"digit": 7}
        ]

        current_state = 0  # always start from state 0.
        for c in s:
            if c.isdigit():
                group = "digit"
            elif c in "+-":
                group = "sign"
            elif c in "eE":
                group = "exponent"
            elif c == ".":
                group = "dot"
            else:
                return False

            if group not in dfa[current_state]:  # if group is not any acceptable next group
                return False

            current_state = dfa[current_state][group]

        return current_state in [1, 4, 7]