# -*- coding: utf-8 -*-
"""
Personal Agent Decision Fatigue Entropy Allocator Client
Zero-dependency Baumeister ego-depletion modeler, prefrontal executive cognitive load
budgeter, default-choice bias auditor, and high-stakes decision timing optimizer.
"""

import math
from typing import Dict, List, Any, Optional

class PersonalAgentDecisionFatigueEntropyAllocator:
    """
    Quantifies daily executive decision complexity, tracks prefrontal cortex willpower depletion,
    audits default-choice bias vulnerability, and schedules high-stakes choices into peak windows.
    """

    def audit_daily_decision_budget(
        self,
        decisions_logged: List[Dict[str, Any]]
    ) -> Dict[str, Any]:
        """
        Audits cumulative cognitive decision fatigue:
        Each decision object:
        {
          'name': 'API Architecture Spec',
          'complexity': 8.0 (1-10),
          'uncertainty': 7.0 (1-10),
          'irreversibility': 9.0 (1-10)
        }
        """
        if not decisions_logged:
            return {
                "total_decisions_executed": 0,
                "cumulative_decision_load_units": 0.0,
                "prefrontal_executive_capacity_remaining": "100.0%",
                "default_choice_bias_risk": "MINIMAL: Executive function pristine.",
                "actionable_routing": "Ideal cognitive window for high-stakes strategic commitments."
            }

        total_load = 0.0
        breakdown = []

        for item in decisions_logged:
            d_name = str(item.get("name", "Unspecified Decision"))
            comp = max(1.0, min(10.0, float(item.get("complexity", 5.0))))
            unc = max(1.0, min(10.0, float(item.get("uncertainty", 5.0))))
            irrev = max(1.0, min(10.0, float(item.get("irreversibility", 5.0))))

            # Decision weight formula: comp * (unc^1.1) * (irrev^0.9) / 10.0
            load_units = round((comp * math.pow(unc, 1.1) * math.pow(irrev, 0.9)) / 10.0, 1)
            total_load += load_units

            breakdown.append({
                "decision": d_name,
                "load_units": load_units
            })

        total_load = round(total_load, 1)

        # Baseline daily capacity is roughly ~120-150 standard decision units
        daily_capacity_baseline = 140.0
        pct_depleted = min(95.0, round((total_load / daily_capacity_baseline) * 100.0, 1))
        pct_remaining = round(100.0 - pct_depleted, 1)

        # Danziger et al. judicial parole / ego-depletion default bias model
        # As capacity drops below 40%, the brain defaults to status quo, passive approvals, or avoidance
        if pct_remaining >= 65.0:
            bias_risk = "LOW (High prefrontal clarity; balanced risk appraisal)"
            routing = "Permitted to resolve major financial, hiring, or architectural decisions."
        elif pct_remaining >= 35.0:
            bias_risk = "MODERATE (Cognitive strain emerging; tendency towards conservative status quo)"
            routing = "Execute moderate decisions only. Defer irreversible commitments until post-rest or morning."
        else:
            bias_risk = "CRITICAL (Severe ego depletion; extreme vulnerability to passive default bias or reckless shortcuts)"
            routing = "STRICT DECISION BLACKOUT: Freeze all high-stakes commitments. Enforce pre-set heuristics."

        return {
            "total_decisions_executed": len(decisions_logged),
            "cumulative_decision_load_units": total_load,
            "daily_capacity_budget_units": daily_capacity_baseline,
            "prefrontal_executive_capacity_remaining": f"{pct_remaining}%",
            "default_choice_bias_risk": bias_risk,
            "actionable_routing": routing,
            "top_contributing_decisions": sorted(breakdown, key=lambda x: x["load_units"], reverse=True)[:4]
        }

    def optimize_high_stakes_decision_timing(
        self,
        upcoming_decisions: List[Dict[str, Any]],
        current_hour: float = 14.5
    ) -> Dict[str, Any]:
        """
        Schedules upcoming decisions into optimal chronological cognitive windows,
        reserving the 09:00 - 11:30 AM peak for high-stakes irreversible choices.
        """
        hour = max(0.0, min(24.0, float(current_hour)))

        scheduled = []
        for item in upcoming_decisions:
            d_name = str(item.get("name", "Task Decision"))
            impact = max(1.0, min(10.0, float(item.get("impact", 5.0))))
            irrev = max(1.0, min(10.0, float(item.get("irreversibility", 5.0))))

            stakes_score = round(impact * irrev, 1)

            if stakes_score >= 50.0:
                tier = "Tier 1: High-Stakes Irreversible"
                recommended_window = "Next Morning Peak (09:00 - 11:30 AM) with fully restored prefrontal glycogen."
                rule = "Never execute after 15:00 PM or in an agitated emotional state."
            elif stakes_score >= 25.0:
                tier = "Tier 2: Moderate Operational"
                recommended_window = "Post-Rest Midday Window (13:30 - 15:00 PM) following light protein meal."
                rule = "Cap evaluation to 25 minutes; apply 80/20 heuristic."
            else:
                tier = "Tier 3: Low-Stakes Reversible (Two-Way Door)"
                recommended_window = "Immediate / Anytime (Batch in late afternoon 16:00 - 17:00 PM)."
                rule = "Automate, delegate, or flip coin. Zero cognitive rumination permitted."

            scheduled.append({
                "decision_name": d_name,
                "stakes_score": stakes_score,
                "classification": tier,
                "optimal_execution_window": recommended_window,
                "governance_rule": rule
            })

        scheduled.sort(key=lambda x: x["stakes_score"], reverse=True)

        return {
            "current_time_hour": hour,
            "decisions_prioritized_count": len(upcoming_decisions),
            "optimized_decision_schedule": scheduled,
            "fiduciary_rule": "Treat executive decision capacity like a non-renewable daily battery. Ruthlessly automate Tier 3."
        }
