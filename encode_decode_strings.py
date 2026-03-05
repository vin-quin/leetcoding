# https://neetcode.io/problems/string-encode-and-decode/question?list=neetcode150
HTML_PREFIX='&#'
HTML_SUFFIX=';'
STR_BREAK = f'&!#\\LB{HTML_SUFFIX}'
EMPTY = "&#NULL;"
RESERVED_MAP = {
    ':': HTML_PREFIX + ':' + HTML_SUFFIX,    
    HTML_PREFIX + ':' + HTML_SUFFIX: ':',
    '/': HTML_PREFIX + '/' + HTML_SUFFIX,    
    HTML_PREFIX + '/' + HTML_SUFFIX: '/',
    '?': HTML_PREFIX + '?' + HTML_SUFFIX,   
    HTML_PREFIX + '?' + HTML_SUFFIX: '?',
    '#': HTML_PREFIX + '#' + HTML_SUFFIX,    
    HTML_PREFIX + '#' + HTML_SUFFIX: '#',
    '[': HTML_PREFIX + '[' + HTML_SUFFIX,    
    HTML_PREFIX + '[' + HTML_SUFFIX: '[',
    ']': HTML_PREFIX + ']' + HTML_SUFFIX,    
    HTML_PREFIX + ']' + HTML_SUFFIX: ']',
    '@': HTML_PREFIX + '@' + HTML_SUFFIX,    
    HTML_PREFIX + '@' + HTML_SUFFIX: '@',
}
class Solution:
    def encode(self, strs: list[str]) -> str:
        if len(strs) == 0:
            return EMPTY
        
        for i in range(len(strs)):
            s = strs[i]
            offset = 0
            for j in range(len(strs[i])):
                if not strs[i][j].isalnum() and strs[i][j] != '-' and strs[i][j] != '_' and strs[i][j] != '.' and strs[i][j] != '~':
                    enc =  f"{HTML_PREFIX}{ord(strs[i][j])}{HTML_SUFFIX}"
                    s = s[:j+offset] + enc + s[j+offset+1:]
                    offset += len(enc)-1
                    
            strs[i] = s

        return STR_BREAK.join(strs)   
               

    def decode(self, s: str) -> list[str]:
        if s is EMPTY:
            return []
        
        idx = s.find(HTML_PREFIX)
        while idx != -1:
            stop = s.find(HTML_SUFFIX, idx)
            print(f'{s=}\n{idx=}\n{stop=}\n{s[idx+len(HTML_PREFIX):stop]=}')
            s = s[:idx] + chr(int(s[idx+len(HTML_PREFIX):stop])) + s[stop+len(HTML_SUFFIX):]

            idx = s.find(HTML_PREFIX)

        print(s)

        return s.split(STR_BREAK)
    
def main():
    s = Solution()
    r = s.encode([""])
    print(r)
    r = s.decode(r)
    print(r)
    r = s.encode([])
    print(r)
    r = s.decode(r)
    print(r)

if __name__ == '__main__':
    main()