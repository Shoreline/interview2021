class Solution:
    def numberOfWeakCharacters(self, properties: List[List[int]]) -> int:
        properties.sort(key=lambda x: (-x[0], x[1]))
        res = 0
        cur_max_defense = 0

        # a <= previous attack
        for a, d in properties:
            print(a, d, cur_max_defense)
            # why d < cur_max_defense is enough to verify that we have a weak character?
            # 1) if there is any previous char has higher atk than current atk
            #   Since cur_max_defense is also from one of the previous char
            #   -> there is at least one previous char has both atk and def higher than cur char
            # 2) if if there is no previous char has higher atk than current atk
            #    it means that for now all pre_atk == cur_atk
            #    For chars with same atk, def is sorted in ascending order.
            #    So d is always >= cur_max_defense -> won't increment the res
            if d < cur_max_defense:
                res += 1
            cur_max_defense = max(cur_max_defense, d)
        return res
