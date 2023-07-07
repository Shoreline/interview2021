# Sort by {x[0] desc; x[1] asc}
class Solution:
    def numberOfWeakCharacters(self, properties: List[List[int]]) -> int:
        properties.sort(key=lambda x: (-x[0], x[1]))
        ans = 0
        max_d_sofar = 0

        # a <= previous attack
        for a, d in properties:
            # why d < cur_max_defense is enough to verify that we have a weak character?
            # 1) if there is any previous char has higher atk than current atk
            #   Since cur_max_defense is also from one of the previous char
            #   -> there is at least one previous char has both atk and def higher than cur char
            # 2) if there is no previous char has higher atk than current atk
            #    it means that for now all pre_atk == cur_atk
            #    For chars with same atk, def is sorted in ascending order. 
            #    So d is always >= cur_max_defense -> won't increment the ans
            if d < max_d_sofar:
                ans += 1
            max_d_sofar = max(max_d_sofar, d)
        return ans        