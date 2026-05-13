class Solution:
    def minWindow(self, s: str, t: str) -> str:
        need = Counter(t)
        required = len(need)
        window = defaultdict(int)
        formed = 0
        min_len = float('inf')
        left = 0 
        ans_left = 0

        for right, ch in enumerate(s):
            window[ch] += 1
            if window[ch] == need[ch]:
                formed += 1

            while formed == required:
                if right - left +1 < min_len:
                    min_len = right  - left + 1 
                    ans_left = left 

                left_ch = s[left]
                window[left_ch] -=1

                if left_ch in need and window[left_ch] < need[left_ch]:
                    formed -= 1
                
                left += 1

        if min_len == float('inf'):
            return ''
        else:
            return s[ans_left : ans_left + min_len]
        