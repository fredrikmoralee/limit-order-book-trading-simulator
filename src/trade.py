##defines the class that stores a match of two orders

class trade:
    def __init__(self, tradeIdIn, buyIdIn, sellIdIN, priceIn, quantityIn, timeIn, causeSideIn):
        self.tradeId = tradeIdIn
        self.buyId = buyIdIn
        self.sellId = sellIdIN
        self.price = priceIn
        self.quantity = quantityIn
        self.quantityTraded = quantityIn
        self.timeStamp = timeIn
        self.side = causeSideIn
