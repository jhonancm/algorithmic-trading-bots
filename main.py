import asyncio
import random
from typing import Dict, Any, List

class TradingPipeline:
    def __init__(self, asset_symbol: str):
        self.symbol = asset_symbol
        # O(1) Data structure tracking lookup mapping 
        self.order_book: Dict[str, List[float]] = {"bids": [], "asks": []}

    async def fetch_market_depth(self) -> Dict[str, Any]:
        """Simulates an asynchronous high-throughput API data ingestion loop."""
        await asyncio.sleep(0.2)  # Non-blocking I/O operation
        return {
            "symbol": self.symbol,
            "bid": round(random.uniform(100.0, 105.0), 2),
            "ask": round(random.uniform(105.1, 110.0), 2)
        }

    def compute_spread(self, market_data: Dict[str, Any]) -> float:
        """Calculates arithmetic logic difference with O(1) temporal execution."""
        spread = market_data["ask"] - market_data["bid"]
        return round(spread, 2)

async def main():
    bot = TradingPipeline(asset_symbol="OLYMP_BTC")
    print(f"[*] Initializing real-time analytics loop for {bot.symbol}...")
    
    for iteration in range(3):
        raw_data = await bot.fetch_market_depth()
        spread = bot.compute_spread(raw_data)
        print(f"[Iteration {iteration + 1}] Data Ingested. Current Market Spread: ${spread}")

if __name__ == "__main__":
    asyncio.run(main())
  
