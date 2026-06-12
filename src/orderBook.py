#stores all orders and data about them

from collections import defaultdict, deque

class orderBook:
    def __init__(self):
        self.bids = defaultdict(deque)
        self.asks = defaultdict(deque)

    def addOrder(self, order):
        if order.side == 'buy':
            self.bids[order.price].append(order)
        else:
            self.asks[order.price].append(order)
        
    def removeOrder(self, order):
        if order.side == 'buy':
            self.bids[order.price].remove(order)
            if not self.bids[order.price]: #if empty at that price remove the price level completely
                del self.bids[order.price]
        else:
            self.asks[order.price].remove(order)
            if not self.asks[order.price]:
                del self.asks[order.price]

    def bestBid(self):
        if not self.bids:
            return None
        return max(self.bids)
    
    def bestAsk(self):
        if not self.asks:
            return None
        return min(self.asks)

    def midPrice(self):
        b = self.bestBid()
        a = self.bestAsk()
        if not a or not b:
            return None
        return (self.bestBid() + self.bestAsk())/2
    
    def spread(self):
        b = self.bestBid()
        a = self.bestAsk()
        if not a or not b:
            return None
        return (a - b)