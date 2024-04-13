class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:

        counts = defaultdict(int)

        for match in matches:
            winner = match[0]
            loser = match[1]
            counts[winner] += 0
            counts[loser] += 1

        ans = [[],[]]
        for key, val in counts.items():
            if val == 0:
                ans[0].append(key)

            if val == 1:
                ans[1].append(key)

        res1 = sorted(ans[0])
        res2 = sorted(ans[1])

        return [res1, res2]‌
