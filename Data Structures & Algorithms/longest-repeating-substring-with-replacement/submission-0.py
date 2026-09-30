class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        res = 0
        l = 0
        maxf = 0

        for r in range(len(s)):
            count[s[r]] = count.get(s[r],0) + 1
            maxf = max(maxf, count[s[r]])

            # ウィンドウのサイズから最も登場頻度の高い文字の文字数を引いた値がk（置換可能回数）より大きい場合は、置換可能回数に収まるようにウィンドウを縮小する
            while (r-l+1) - maxf > k:
                count[s[l]] -= 1
                l += 1
            
            res = max(res, r-l+1)
        
        return res