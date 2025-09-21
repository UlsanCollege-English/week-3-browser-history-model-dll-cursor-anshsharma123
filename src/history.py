# src/history.py

class _N:
    __slots__ = ("url", "prev", "next")
    def __init__(self, url):
        self.url = url
        self.prev = None
        self.next = None

class BrowserHistory:
    def __init__(self):
        self.head = None
        self.tail = None
        self.cur = None

    def current(self):
        """Return the current URL or None if empty"""
        return self.cur.url if self.cur else None

    def visit(self, url):
        """
        Visit a new URL. If not at the end, truncate forward history.
        Then append url and move cursor.
        """
        new_node = _N(url)

        if self.cur is None:
            # first visit
            self.head = self.tail = self.cur = new_node
            return

        # if not at the tail, cut forward history
        if self.cur.next:
            self.cur.next.prev = None  # detach forward nodes
            self.cur.next = None
            self.tail = self.cur

        # append new node
        self.cur.next = new_node
        new_node.prev = self.cur
        self.cur = new_node
        self.tail = new_node

    def back(self, steps=1):
        """Move back up to 'steps' times and return current URL"""
        while steps > 0 and self.cur and self.cur.prev:
            self.cur = self.cur.prev
            steps -= 1
        return self.current()

    def forward(self, steps=1):
        """Move forward up to 'steps' times and return current URL"""
        while steps > 0 and self.cur and self.cur.next:
            self.cur = self.cur.next
            steps -= 1
        return self.current()
