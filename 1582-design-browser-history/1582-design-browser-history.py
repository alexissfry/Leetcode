class BrowserHistory:

    def __init__(self, homepage: str):
        self.urls = []
        self.urls.append(homepage)
        self.index = 0

    def visit(self, url: str) -> None:
        while len(self.urls)-1 > self.index:
            self.urls.pop()

        self.urls.append(url)
        self.index += 1 

    def back(self, steps: int) -> str:
        if steps > self.index:
            steps = self.index
        self.index -= steps

        return self.urls[self.index]

    def forward(self, steps: int) -> str:
        stepsLeft = len(self.urls)-1-self.index
        if steps > stepsLeft:
            steps = stepsLeft
        self.index += steps

        return self.urls[self.index]

"""
["a","b","c"]
index = 2

back(1)

["a","b","c"]
index = 1

visit("d")

["a","b","d"]
index = 2

forward(1)

["a","b","d"]
index = 2

back(2)

["a","b","d"]
index = 0

visit("e")

["a","e"]
index = 1
"""



# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)