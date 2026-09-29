class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charset = set()
        l = 0
        res = 0

        for r in range(len(s)):
            # 重複が消えるまで左から削除していき、ウィンドウ幅を狭くする
            while s[r] in charset:
                charset.remove(s[l])
                l += 1
            
            charset.add(s[r])
            # 過去最大と現在のウィンドウ幅を比べて更新
            res = max(res, r-l+1)
        
        return res
