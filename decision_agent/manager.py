class DecisionAgent:
    def __init__(self, results):
        self.results = results

    def generate_summary(self):
        return {
            "recommendations": [r.get("recommendation") for r in self.results.values()],
            "raw_data": self.results
        }
