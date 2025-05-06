from fastapi import FastAPI
from pydantic import BaseModel
from agents.sales_agent import SalesAgent
from agents.price_agent import PriceAgent
from agents.ads_agent import AdsAgent
from agents.card_agent import CardAgent
from agents.reviews_agent import ReviewsAgent
from agents.profit_agent import ProfitAgent
from agents.audience_agent import AudienceAgent
from decision_agent.manager import DecisionAgent

app = FastAPI()

class AnalyzeRequest(BaseModel):
    marketplace: str
    period_days: int
    sku_list: list[str] | str

@app.post("/analyze")
def analyze(request: AnalyzeRequest):
    sku = request.sku_list[0] if isinstance(request.sku_list, list) else "test-sku"

    agent_results = {
        "sales": SalesAgent(sku, request.marketplace, request.period_days).run(),
        "price": PriceAgent(sku, request.marketplace, request.period_days).run(),
        "ads": AdsAgent(sku, request.marketplace, request.period_days).run(),
        "card": CardAgent(sku, request.marketplace, request.period_days).run(),
        "reviews": ReviewsAgent(sku, request.marketplace, request.period_days).run(),
        "profit": ProfitAgent(sku, request.marketplace, request.period_days).run(),
        "audience": AudienceAgent(sku, request.marketplace, request.period_days).run()
    }

    summary = DecisionAgent(agent_results).generate_summary()
    return summary
    
if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=5000)
