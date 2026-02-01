"""
Question Parser - Natural Language Query Handler

This module parses natural language questions about astrology
and routes them to the appropriate analysis functions.

Enhanced with detailed reasoning that explains:
1. WHAT - The conclusion/prediction
2. HOW - Step-by-step analysis showing the calculation process
3. WHY - Textbook references and astrological principles

Examples:
- "How is my career looking?"
- "Will I get married this year?"
- "Is this a good time for travel?"
- "What about my health?"
"""
from typing import Dict, List, Optional, Tuple
from dataclasses import dataclass
from enum import Enum
import re

from .area_analysis import (
    normalize_area_query,
    analyze_area,
    get_all_area_analysis,
    AREA_HOUSE_MAPPING,
)
from .detailed_reasoning import generate_detailed_explanation


class QueryType(str, Enum):
    """Types of queries"""
    AREA_SPECIFIC = "area_specific"  # Questions about specific life area
    GENERAL_OUTLOOK = "general_outlook"  # General transit outlook
    TIMING = "timing"  # When questions
    COMPARISON = "comparison"  # Comparing areas or times
    YES_NO = "yes_no"  # Yes/no questions
    WHAT_IF = "what_if"  # Hypothetical questions


@dataclass
class ParsedQuery:
    """Result of parsing a natural language query"""
    original_query: str
    query_type: QueryType
    primary_area: Optional[str]
    secondary_areas: List[str]
    time_context: Optional[str]  # "now", "this_month", "this_year"
    intent: str  # Brief description of query intent
    confidence: float  # 0-1 confidence in parsing


# Intent patterns for area detection
AREA_PATTERNS = {
    "career": [
        r"career", r"job", r"work", r"profession", r"employment",
        r"promotion", r"office", r"boss", r"company", r"business.*go",
    ],
    "business": [
        r"business", r"startup", r"entrepreneurship", r"venture",
        r"trade", r"shop", r"enterprise",
    ],
    "finance": [
        r"money", r"wealth", r"finance", r"financial", r"income", r"earning",
        r"investment", r"savings", r"profit", r"loss",
    ],
    "health": [
        r"health", r"disease", r"illness", r"medical", r"body",
        r"sick", r"fit", r"wellness", r"recovery",
    ],
    "marriage": [
        r"marriage", r"wedding", r"spouse", r"husband", r"wife",
        r"married", r"marry", r"engagement",
    ],
    "relationships": [
        r"relationship", r"love", r"romance", r"dating",
        r"boyfriend", r"girlfriend", r"partner",
    ],
    "children": [
        r"child", r"children", r"son", r"daughter", r"baby",
        r"pregnancy", r"conceive", r"kids",
    ],
    "education": [
        r"education", r"study", r"exam", r"school", r"college",
        r"university", r"degree", r"learning", r"course",
    ],
    "travel": [
        r"travel", r"journey", r"trip", r"abroad", r"foreign",
        r"overseas", r"immigration", r"visa", r"relocat",
    ],
    "property": [
        r"property", r"house", r"home", r"land", r"real estate",
        r"apartment", r"flat", r"building",
    ],
    "legal": [
        r"legal", r"court", r"case", r"lawsuit", r"litigation",
        r"lawyer", r"justice", r"dispute",
    ],
    "spirituality": [
        r"spiritual", r"meditation", r"moksha", r"enlightenment",
        r"religion", r"temple", r"guru", r"divine",
    ],
    "family": [
        r"family", r"mother", r"father", r"parent", r"siblings",
        r"brother", r"sister", r"relative",
    ],
}

# Query type patterns
QUERY_TYPE_PATTERNS = {
    QueryType.YES_NO: [
        r"^(will|would|can|could|should|is|am|are|do|does|did)\s",
        r"\?$",
        r"is it good", r"is this", r"will i", r"should i",
    ],
    QueryType.TIMING: [
        r"when", r"what time", r"which month", r"which year",
        r"best time", r"right time", r"auspicious",
    ],
    QueryType.COMPARISON: [
        r"compare", r"better", r"worse", r"vs", r"versus",
        r"or", r"which is",
    ],
    QueryType.WHAT_IF: [
        r"what if", r"if i", r"suppose", r"in case",
    ],
}

# Time context patterns
TIME_PATTERNS = {
    "now": [r"now", r"current", r"today", r"present"],
    "this_week": [r"this week", r"coming week", r"next few days"],
    "this_month": [r"this month", r"coming month", r"next month"],
    "this_year": [r"this year", r"coming year", r"next year", r"annual"],
    "next_3_months": [r"quarter", r"next 3 months", r"few months"],
    "next_6_months": [r"next 6 months", r"half year", r"coming months"],
}


def parse_query(query: str) -> ParsedQuery:
    """
    Parse a natural language query about astrology.
    
    Args:
        query: Natural language question
    
    Returns:
        ParsedQuery with extracted information
    """
    query_lower = query.lower().strip()
    
    # Detect primary area
    primary_area = None
    secondary_areas = []
    max_confidence = 0.0
    
    for area, patterns in AREA_PATTERNS.items():
        for pattern in patterns:
            if re.search(pattern, query_lower):
                if primary_area is None:
                    primary_area = area
                    max_confidence = 0.8
                else:
                    if area not in secondary_areas:
                        secondary_areas.append(area)
    
    # If no specific area found, might be general query
    if primary_area is None:
        # Check for general keywords
        if any(word in query_lower for word in ["overall", "general", "life", "future", "outlook"]):
            primary_area = "general"
            max_confidence = 0.6
    
    # Detect query type
    query_type = QueryType.AREA_SPECIFIC  # Default
    
    for q_type, patterns in QUERY_TYPE_PATTERNS.items():
        for pattern in patterns:
            if re.search(pattern, query_lower):
                query_type = q_type
                break
    
    # If no area detected but asking general question
    if primary_area is None and query_type in [QueryType.YES_NO, QueryType.GENERAL_OUTLOOK]:
        query_type = QueryType.GENERAL_OUTLOOK
        primary_area = "general"
        max_confidence = 0.5
    
    # Detect time context
    time_context = "now"  # Default
    for time_key, patterns in TIME_PATTERNS.items():
        for pattern in patterns:
            if re.search(pattern, query_lower):
                time_context = time_key
                break
    
    # Generate intent description
    intent = _generate_intent(primary_area, query_type, time_context)
    
    return ParsedQuery(
        original_query=query,
        query_type=query_type,
        primary_area=primary_area,
        secondary_areas=secondary_areas,
        time_context=time_context,
        intent=intent,
        confidence=max_confidence,
    )


def _generate_intent(area: Optional[str], query_type: QueryType, time_context: str) -> str:
    """Generate a description of the query intent."""
    time_desc = {
        "now": "current",
        "this_week": "this week's",
        "this_month": "this month's",
        "this_year": "this year's",
        "next_3_months": "next 3 months'",
        "next_6_months": "next 6 months'",
    }.get(time_context, "current")
    
    if area == "general" or area is None:
        return f"Asking about {time_desc} overall transit outlook"
    
    area_display = area.replace("_", " ")
    
    if query_type == QueryType.YES_NO:
        return f"Yes/no question about {area_display}"
    elif query_type == QueryType.TIMING:
        return f"Timing question about {area_display}"
    elif query_type == QueryType.COMPARISON:
        return f"Comparison involving {area_display}"
    else:
        return f"Inquiry about {time_desc} {area_display} outlook"


@dataclass
class QueryResponse:
    """Response to a parsed query"""
    query: ParsedQuery
    answer: str
    detailed_analysis: Optional[Dict]
    confidence: str  # High, Medium, Low
    follow_up_suggestions: List[str]


def generate_response(
    parsed_query: ParsedQuery,
    transit_results: List[Dict],
    enhanced_report: Optional[Dict] = None,
) -> QueryResponse:
    """
    Generate a response to a parsed query with detailed reasoning.
    
    Args:
        parsed_query: The parsed query
        transit_results: List of planet transit results
        enhanced_report: Optional full enhanced transit report
    
    Returns:
        QueryResponse with answer, detailed reasoning, and analysis
    """
    area = parsed_query.primary_area
    query_type = parsed_query.query_type
    
    # Handle general outlook
    if area == "general" or area is None:
        return _handle_general_query(parsed_query, transit_results, enhanced_report)
    
    # Get area-specific analysis
    area_result = analyze_area(area, transit_results)
    
    # Generate detailed explanation with reasoning
    detailed_explanation = generate_detailed_explanation(
        area=area,
        area_result=area_result,
        transit_results=transit_results
    )
    
    # Generate answer based on query type (now includes reasoning)
    if query_type == QueryType.YES_NO:
        answer = _generate_yes_no_answer(parsed_query, area_result, detailed_explanation)
    elif query_type == QueryType.TIMING:
        answer = _generate_timing_answer(parsed_query, area_result, detailed_explanation)
    else:
        answer = _generate_detailed_answer(parsed_query, area_result, detailed_explanation)
    
    # Determine confidence
    if area_result.confidence == "High" and parsed_query.confidence >= 0.7:
        confidence = "High"
    elif area_result.confidence in ["High", "Medium"] and parsed_query.confidence >= 0.5:
        confidence = "Medium"
    else:
        confidence = "Low"
    
    # Generate follow-up suggestions
    follow_ups = _generate_follow_ups(area, area_result)
    
    return QueryResponse(
        query=parsed_query,
        answer=answer,
        detailed_analysis={
            "area": area_result.area,
            "outlook": area_result.overall_outlook,
            "score": area_result.score,
            "strengths": area_result.strengths,
            "challenges": area_result.challenges,
            "advice": area_result.advice,
            # NEW: Detailed reasoning
            "reasoning": {
                "conclusion_summary": detailed_explanation.summary,
                "analysis_steps": detailed_explanation.conclusion_steps,
                "why_explanation": detailed_explanation.why_this_conclusion,
                "supporting_factors": detailed_explanation.supporting_factors,
                "challenging_factors": detailed_explanation.challenging_factors,
                "textbook_references": detailed_explanation.textbook_references,
                "confidence_breakdown": detailed_explanation.confidence_breakdown,
            }
        },
        confidence=confidence,
        follow_up_suggestions=follow_ups,
    )


def _handle_general_query(
    parsed_query: ParsedQuery,
    transit_results: List[Dict],
    enhanced_report: Optional[Dict],
) -> QueryResponse:
    """Handle general outlook queries."""
    # Analyze all major areas
    all_areas = get_all_area_analysis(transit_results)
    
    # Find best and worst areas
    sorted_areas = sorted(all_areas.items(), key=lambda x: x[1].score, reverse=True)
    best_areas = [a[0] for a in sorted_areas[:2] if a[1].score > 0]
    challenging_areas = [a[0] for a in sorted_areas[-2:] if a[1].score < 0]
    
    # Calculate overall score
    total_score = sum(a.score for a in all_areas.values())
    avg_score = total_score / len(all_areas)
    
    if avg_score >= 10:
        overall = "favorable"
        outlook = "positive"
    elif avg_score <= -10:
        overall = "challenging"
        outlook = "cautious"
    else:
        overall = "mixed"
        outlook = "balanced"
    
    answer = f"Your overall transit period appears {overall}. "
    
    if best_areas:
        answer += f"Favorable areas include {', '.join(best_areas)}. "
    
    if challenging_areas:
        answer += f"Areas requiring attention: {', '.join(challenging_areas)}. "
    
    answer += f"A {outlook} approach is recommended."
    
    follow_ups = [
        f"Tell me more about my {best_areas[0]}" if best_areas else "What about my career?",
        f"How can I improve my {challenging_areas[0]}?" if challenging_areas else "What about my health?",
    ]
    
    return QueryResponse(
        query=parsed_query,
        answer=answer,
        detailed_analysis={
            "overall_outlook": overall,
            "average_score": round(avg_score, 2),
            "best_areas": best_areas,
            "challenging_areas": challenging_areas,
            "all_areas_summary": {k: v.overall_outlook for k, v in all_areas.items()},
        },
        confidence="Medium",
        follow_up_suggestions=follow_ups,
    )


def _generate_yes_no_answer(parsed_query: ParsedQuery, area_result, detailed_explanation=None) -> str:
    """Generate yes/no style answer with reasoning."""
    outlook = area_result.overall_outlook
    area = area_result.area_display_name
    
    # Base answer
    if outlook == "Positive":
        base = f"Yes, the transit indicators for {area} are favorable."
    elif outlook == "Challenging":
        base = f"The current transits suggest some challenges for {area}."
    else:
        base = f"The outlook for {area} is mixed."
    
    # Add detailed reasoning if available
    if detailed_explanation:
        why = f"\n\n**Why this conclusion:**\n{detailed_explanation.why_this_conclusion}"
        
        steps = "\n\n**Analysis Steps:**"
        for i, step in enumerate(detailed_explanation.conclusion_steps[:3], 1):
            steps += f"\n{i}. {step}"
        
        refs = ""
        if detailed_explanation.textbook_references:
            refs = f"\n\n**Textbook Reference:** {detailed_explanation.textbook_references[0]}"
        
        return f"{base}{why}{steps}{refs}"
    
    return f"{base} {area_result.short_term_prediction}"


def _generate_timing_answer(parsed_query: ParsedQuery, area_result, detailed_explanation=None) -> str:
    """Generate timing-focused answer with reasoning."""
    outlook = area_result.overall_outlook
    area = area_result.area_display_name
    
    # Base answer
    if outlook == "Positive":
        base = f"Current transits favor {area}. This is a good time to pursue related goals."
    elif outlook == "Challenging":
        base = f"Current transits suggest patience for {area}. Wait for more favorable planetary positions."
    else:
        base = f"Current period offers selective opportunities for {area}. Focus on well-supported initiatives."
    
    # Add detailed reasoning if available
    if detailed_explanation:
        why = f"\n\n**Timing Factors:**\n{detailed_explanation.why_this_conclusion}"
        
        factors = "\n\n**Key Influences:**"
        for factor in detailed_explanation.supporting_factors[:2]:
            if isinstance(factor, dict):
                factors += f"\n• ✓ {factor.get('planet', '')} in {factor.get('house', '')}th: {factor.get('textbook_result', '')}"
            else:
                factors += f"\n• ✓ {factor}"
        for factor in detailed_explanation.challenging_factors[:2]:
            if isinstance(factor, dict):
                factors += f"\n• ✗ {factor.get('planet', '')} in {factor.get('house', '')}th: {factor.get('textbook_result', '')}"
            else:
                factors += f"\n• ✗ {factor}"
        
        return f"{base}{why}{factors}\n\n**Advice:** {area_result.advice}"
    
    return f"{base} {area_result.advice}"


def _generate_detailed_answer(parsed_query: ParsedQuery, area_result, detailed_explanation=None) -> str:
    """Generate detailed answer for area query with full reasoning."""
    
    if detailed_explanation:
        # Build comprehensive response
        parts = []
        
        # 1. Conclusion
        parts.append(f"**{area_result.area_display_name} Outlook: {area_result.overall_outlook}**")
        parts.append(f"\n{detailed_explanation.summary}")
        
        # 2. Analysis Steps (HOW we arrived at this conclusion)
        parts.append("\n\n**📊 Analysis Process:**")
        for i, step in enumerate(detailed_explanation.conclusion_steps, 1):
            parts.append(f"\n{i}. {step}")
        
        # 3. Why Explanation (reasoning behind the conclusion)
        parts.append(f"\n\n**❓ Why This Conclusion:**\n{detailed_explanation.why_this_conclusion}")
        
        # 4. Supporting Factors
        if detailed_explanation.supporting_factors:
            parts.append("\n\n**✅ Supporting Factors:**")
            for factor in detailed_explanation.supporting_factors:
                if isinstance(factor, dict):
                    parts.append(f"\n• {factor.get('planet', '')} in {factor.get('house', '')}th house: {factor.get('textbook_result', '')}")
                else:
                    parts.append(f"\n• {factor}")
        
        # 5. Challenging Factors
        if detailed_explanation.challenging_factors:
            parts.append("\n\n**⚠️ Challenging Factors:**")
            for factor in detailed_explanation.challenging_factors:
                if isinstance(factor, dict):
                    parts.append(f"\n• {factor.get('planet', '')} in {factor.get('house', '')}th house: {factor.get('textbook_result', '')}")
                else:
                    parts.append(f"\n• {factor}")
        
        # 6. Textbook References
        if detailed_explanation.textbook_references:
            parts.append("\n\n**📚 Textbook References:**")
            for ref in detailed_explanation.textbook_references[:3]:
                parts.append(f"\n• {ref}")
        
        # 7. Advice
        parts.append(f"\n\n**💡 Advice:** {area_result.advice}")
        
        return "".join(parts)
    
    # Fallback to simple response
    parts = [area_result.short_term_prediction]
    
    if area_result.strengths:
        parts.append(f"Strengths: {'; '.join(area_result.strengths)}.")
    
    if area_result.challenges:
        parts.append(f"Challenges: {'; '.join(area_result.challenges)}.")
    
    parts.append(f"Advice: {area_result.advice}")
    
    return " ".join(parts)


def _generate_follow_ups(area: str, area_result) -> List[str]:
    """Generate follow-up question suggestions."""
    follow_ups = []
    
    # Related area suggestions
    related_areas = {
        "career": ["finance", "education"],
        "finance": ["career", "business"],
        "health": ["longevity", "family"],
        "marriage": ["relationships", "family"],
        "education": ["career", "travel"],
        "travel": ["career", "foreign"],
    }
    
    if area in related_areas:
        for related in related_areas[area][:1]:
            follow_ups.append(f"How is my {related}?")
    
    # Based on outlook
    if area_result.overall_outlook == "Challenging":
        follow_ups.append(f"What can I do to improve {area}?")
    else:
        follow_ups.append(f"When is the best time for {area} decisions?")
    
    # Generic follow-ups
    follow_ups.append("What is my overall outlook?")
    
    return follow_ups[:3]


def process_question(
    question: str,
    transit_results: List[Dict],
    enhanced_report: Optional[Dict] = None,
) -> Dict:
    """
    Main entry point for processing user questions.
    
    Args:
        question: Natural language question
        transit_results: List of transit analysis results
        enhanced_report: Optional full enhanced report
    
    Returns:
        Dict with response and metadata
    """
    # Parse the query
    parsed = parse_query(question)
    
    # Generate response
    response = generate_response(parsed, transit_results, enhanced_report)
    
    return {
        "question": question,
        "parsed_intent": parsed.intent,
        "area": parsed.primary_area,
        "answer": response.answer,
        "confidence": response.confidence,
        "detailed_analysis": response.detailed_analysis,
        "follow_up_suggestions": response.follow_up_suggestions,
    }
