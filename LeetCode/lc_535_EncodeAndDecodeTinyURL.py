class Codec:
    import string
    tiny_base = "http://tinyurl.com"
    _alpha_beta = string.ascii_letters + string.digits
    _base = len(_alpha_beta)

    def __init__(self):
        self.urls = ['placeholder']

    def encode(self, longUrl):
        """Encodes a URL to a shortened URL.

        :type longUrl: str
        :rtype: str
        """
        self.urls.append(longUrl)
        idx = len(self.urls) - 1
        my_str = ''
        while idx:
            my_str = self._alpha_beta[idx % self._base] + my_str
            idx //= self._base
        return '/'.join((self.tiny_base, my_str))

    def decode(self, shortUrl):
        """Decodes a shortened URL to its original URL.

        :type shortUrl: str
        :rtype: str
        """
        assert '/'.join(shortUrl.split('/')[:-1]) == self.tiny_base
        my_str = shortUrl.split('/')[-1]
        idx = 0
        for c in my_str:
            idx = idx * self._base + self._alpha_beta.index(c)
        return self.urls[idx]


if __name__ == "__main__":
    # Your Codec object will be instantiated and called as such:
    codec = Codec()

    # simulation that already has some tiny url created
    from itertools import repeat

    map(codec.encode, repeat('placeholder', 1000))

    url1 = "https://leetcode.com/problems/design-tinyurl"

    tiny1 = codec.encode(url1)
    assert codec.decode(tiny1) == url1

    url2 = "https://leetcode.com/problems/design-tinyurl_second"

    tiny2 = codec.encode(url2)
    assert codec.decode(tiny2) == url2
