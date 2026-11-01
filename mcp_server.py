# -*- coding: utf-8 -*-
"""FastMCP Server for Personal Agent Decision Fatigue Entropy Allocator Skill."""

from mcp.server.fastmcp import FastMCP
from client import PersonalAgentDecisionFatigueEntropyAllocator

mcp = FastMCP("PersonalAgentDecisionFatigueEntropyAllocator")
client = PersonalAgentDecisionFatigueEntropyAllocator()

@mcp.tool()
def audit_daily_decision_budget(
    decisions_logged: list[dict]
) -> str:
    """Audits cumulative decision load, prefrontal executive remaining, and default bias risk."""
    import json
    return json.dumps(client.audit_daily_decision_budget(decisions_logged), indent=2)

@mcp.tool()
def optimize_high_stakes_decision_timing(
    upcoming_decisions: list[dict],
    current_hour: float = 14.5
) -> str:
    """Prioritizes upcoming choices into morning peak or batch windows based on irreversibility."""
    import json
    return json.dumps(client.optimize_high_stakes_decision_timing(upcoming_decisions, current_hour), indent=2)

if __name__ == "__main__":
    mcp.run()
