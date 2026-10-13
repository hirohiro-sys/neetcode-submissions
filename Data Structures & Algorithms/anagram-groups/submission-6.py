class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # 存在しないkeyにアクセスした場合は配列を作る
        ans = defaultdict(list)
        for s in strs:
            sorted_s = "".join(sorted(s))
            ans[sorted_s].append(s)
        
        # keyを除いたvalueのみを配列として返す
        return list(ans.values())