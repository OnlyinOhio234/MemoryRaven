#!/usr/bin/env python3
"""
MemoryRaven Quick Start Example
Learn the basics of AI memory with $RAVEN integration
"""

import asyncio
from memoryraven import MemoryRaven

async def main():
    # Initialize MemoryRaven
    raven = MemoryRaven(agent_id="quickstart-agent")
    
    # Store your first memory
    await raven.remember(
        "The user's name is Alice and she loves quantum physics",
        memory_type="semantic",
        tags=["user_info", "preferences"]
    )
    
    # Store an episodic memory
    await raven.remember(
        "Alice asked about quantum entanglement at 3:47 PM",
        memory_type="episodic",
        tags=["conversation", "physics"]
    )
    
    # Recall relevant memories
    memories = await raven.recall("quantum physics discussion with Alice")
    
    print("🧠 Retrieved memories:")
    for memory in memories:
        print(f"  - {memory.content}")
        print(f"    Type: {memory.memory_type}, Relevance: {memory.relevance:.2f}")
    
    # Learn from experience
    await raven.learn_from_mistake(
        mistake="Forgot to mention Heisenberg uncertainty principle",
        lesson="Always cover uncertainty when discussing quantum mechanics",
        tags=["physics", "teaching"]
    )
    
    print("\n✅ Memory system initialized! Your AI now remembers.")

if __name__ == "__main__":
    asyncio.run(main())