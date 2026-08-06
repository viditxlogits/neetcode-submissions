class Solution:

    def encode(self, strs: List[str]) -> str:
        msg = ""
        for s in strs:
            msg += s + ";$@"

        return msg

    def decode(self, s: str) -> List[str]:

        output = s.split(";$@")

        output.pop()

        return output