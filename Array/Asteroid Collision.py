# asteroids = [5,10,-5]
#    the absolute value represents its size, and the sign represents its direction. Speeds are all the same.

# Two stacks
class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        plus = []
        minus = []
        for a in asteroids:
            if a > 0:
                plus.append(a)
            else:
                while plus and plus[-1] < abs(a):
                    plus.pop()
                if not plus:
                    minus.append(a)
                elif plus[-1] == abs(a):
                    plus.pop()

        return minus + plus

    # One stack


class Solution2:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        res = []
        for asteroid in asteroids:
            # We only need to resolve collisions under the following conditions:
            # - stack is non-empty
            # - current asteroid is -ve
            # - top of the stack is +ve
            while res and asteroid < 0 and res[-1] > 0:
                # Both asteroids are equal, destroy both.
                if res[-1] == -asteroid:
                    res.pop()
                    break
                # Stack top is smaller, remove the +ve asteroid
                # from the stack and continue the comparison.
                elif res[-1] < -asteroid:
                    res.pop()
                    continue
                # Stack top is larger, -ve asteroid is destroyed.
                elif res[-1] > -asteroid:
                    break
            else:
                # -ve asteroid made it all the way to the
                # bottom of the stack and destroyed all asteroids.
                res.append(asteroid)
        return res        