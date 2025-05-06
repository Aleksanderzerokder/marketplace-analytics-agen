class PriceAgent:
    def __init__(self, sku, marketplace, period):
        self.sku = sku
        self.marketplace = marketplace
        self.period = period

    def run(self):
        return {"recommendation": "Снизьте цену на 5%."}
