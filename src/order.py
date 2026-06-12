#defines the class that stores an order

class order:
    def __init__(self, orderIdIn, traderIdIN, sideIn, typeIn, priceIn, quantityIn, timeIn):
        self.orderId = orderIdIn
        self.tradrId = traderIdIN
        self.side = sideIn
        self.type = typeIn
        self.price = priceIn
        self.quantity = quantityIn
        self.quantityRemaining = quantityIn
        self.timeStamp = timeIn

