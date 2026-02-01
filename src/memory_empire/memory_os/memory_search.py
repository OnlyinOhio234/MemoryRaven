"""
Memory search configuration inspired by Clawdbot architecture
"""

from dataclasses import dataclass
from typing import List, Literal, Optional


@dataclass
class MemorySearchConfig:
    """Configuration for memory search functionality."""
    
    enabled: bool = True
    sources: List[str] = None
    provider: Literal["local", "remote"] = "local"
    
    def __post_init__(self):
        if self.sources is None:
            self.sources = ["memory"]