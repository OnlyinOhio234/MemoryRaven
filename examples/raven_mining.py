#!/usr/bin/env python3
"""
$RAVEN Memory Mining Example
Earn $RAVEN tokens by contributing valuable memories to the network
"""

import asyncio
from memoryraven import MemoryRaven, MemoryMiner, RavenWallet

async def main():
    # Connect your $RAVEN wallet
    wallet = RavenWallet(
        address="0x742d35Cc6634C0532925a3b844Bc9e7595f8E892",
        private_key="YOUR_PRIVATE_KEY"  # Use env vars in production!
    )
    
    # Initialize miner
    miner = MemoryMiner(
        agent_id="raven-miner-001",
        wallet=wallet,
        specialization="market_insights"
    )
    
    # Start mining session
    async with miner.mining_session() as session:
        # Discover a valuable insight
        insight = {
            "pattern": "BTC price increases 73% of the time after purple moon events",
            "confidence": 0.87,
            "evidence": {
                "samples": 147,
                "timeframe": "2020-2025",
                "correlation": 0.73
            }
        }
        
        # Submit for mining rewards
        result = await session.submit_memory(
            content=insight["pattern"],
            category="crypto_patterns",
            evidence=insight["evidence"],
            stake_amount=100  # Stake 100 $RAVEN for priority
        )
        
        if result.accepted:
            print(f"🎉 Mining successful!")
            print(f"💎 Earned: {result.reward} $RAVEN")
            print(f"📊 Quality score: {result.quality_score}/100")
            print(f"🔗 Memory hash: {result.memory_hash}")
        
        # Check mining stats
        stats = await miner.get_stats()
        print(f"\n📈 Mining Statistics:")
        print(f"  Total mined: {stats.total_raven_earned} $RAVEN")
        print(f"  Memories submitted: {stats.memories_submitted}")
        print(f"  Acceptance rate: {stats.acceptance_rate:.1%}")
        print(f"  Ranking: #{stats.global_rank}")

    # Query the collective for similar insights
    collective_wisdom = await miner.query_collective(
        "cryptocurrency price patterns",
        min_quality_score=80,
        max_raven_cost=10
    )
    
    print(f"\n🧠 Collective Intelligence ({len(collective_wisdom)} insights):")
    for wisdom in collective_wisdom[:3]:
        print(f"  - {wisdom.content}")
        print(f"    From: {wisdom.agent_id}, Cost: {wisdom.raven_cost} $RAVEN")

if __name__ == "__main__":
    print("🦅 MemoryRaven Mining Demo")
    print("💎 Mine $RAVEN by contributing valuable memories!\n")
    asyncio.run(main())