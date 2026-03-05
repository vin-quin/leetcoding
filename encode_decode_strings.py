# https://neetcode.io/problems/string-encode-and-decode/question?list=neetcode150
import base64

HTML_PREFIX='&#'
HTML_SUFFIX=';'
STR_BREAK = f'{HTML_PREFIX}\\LB{HTML_SUFFIX}'
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
        return STR_BREAK.join(strs).format_map(RESERVED_MAP) 

    def decode(self, s: str) -> list[str]:
        return s.format_map(RESERVED_MAP).split(STR_BREAK)

def main():
    s = Solution()
    r = s.encode(["Hello", "World"])
    print(r)
    r = s.decode(r)
    print(r)

if __name__ == '__main__':
    main()