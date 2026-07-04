class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        target_sum = sum(ord(c) for c in s1)
        target_count = {}

        for c in s1:
            target_count[c] = target_count.get(c, 0) + 1

        window_len = len(s1)

        for l in range(len(s2) - window_len + 1):
            sub = s2[l:l + window_len]

            if sum(ord(c) for c in sub) == target_sum:
                sub_count = {}

                for c in sub:
                    sub_count[c] = sub_count.get(c, 0) + 1

                if sub_count == target_count:
                    return True

        return False