# ==========================================
# Redrob Intelligent Candidate Discovery
# explainability.py
# ==========================================

from src.scorer import (
    score_breakdown,
    recommendation_label
)

from src.utils import build_reason


# ------------------------------------------
# Positive Reasons
# ------------------------------------------

def generate_strengths(candidate):

    details = score_breakdown(
        candidate
    )

    strengths = []

    if details[
        "semantic_score"
    ] >= 0.80:

        strengths.append(
            "Strong semantic alignment with Senior AI Engineer role"
        )

    if details[
        "retrieval_score"
    ] >= 0.50:

        strengths.append(
            "Demonstrated retrieval and search system experience"
        )

    if details[
        "ranking_score"
    ] >= 0.50:

        strengths.append(
            "Experience with ranking and relevance systems"
        )

    if details[
        "recommendation_score"
    ] >= 0.50:

        strengths.append(
            "Background in recommendation systems"
        )

    if details[
        "product_company_score"
    ] >= 0.50:

        strengths.append(
            "Experience working in product-driven environments"
        )

    if details[
        "behavioral_score"
    ] >= 0.75:

        strengths.append(
            "Excellent recruiter engagement and platform activity"
        )

    if details[
        "experience_score"
    ] >= 0.80:

        strengths.append(
            "Relevant years of professional experience"
        )

    if details[
        "title_score"
    ] >= 0.80:

        strengths.append(
            "Current role aligns closely with AI engineering responsibilities"
        )

    return strengths


# ------------------------------------------
# Candidate Gaps
# ------------------------------------------

def generate_gaps(candidate):

    details = score_breakdown(
        candidate
    )

    gaps = []

    if details[
        "retrieval_score"
    ] < 0.30:

        gaps.append(
            "Limited evidence of retrieval systems experience"
        )

    if details[
        "ranking_score"
    ] < 0.30:

        gaps.append(
            "Limited ranking system exposure"
        )

    if details[
        "recommendation_score"
    ] < 0.30:

        gaps.append(
            "Recommendation system experience not clearly demonstrated"
        )

    if details[
        "behavioral_score"
    ] < 0.50:

        gaps.append(
            "Lower recruiter engagement signals"
        )

    if details[
        "experience_score"
    ] < 0.60:

        gaps.append(
            "Experience range differs from target role"
        )

    return gaps


# ------------------------------------------
# Single Reasoning String
# ------------------------------------------

def generate_reasoning(candidate):

    strengths = generate_strengths(
        candidate
    )

    if len(strengths) == 0:

        return (
            "Moderate profile relevance based on available evidence"
        )

    return build_reason(
        strengths[:5]
    )


# ------------------------------------------
# Recruiter Summary
# ------------------------------------------

def recruiter_summary(candidate):

    details = score_breakdown(
        candidate
    )

    recommendation = recommendation_label(
        details["final_score"]
    )

    strengths = generate_strengths(
        candidate
    )

    gaps = generate_gaps(
        candidate
    )

    return {

        "final_score":
        details["final_score"],

        "recommendation":
        recommendation,

        "top_strengths":
        strengths,

        "potential_gaps":
        gaps,

        "reasoning":
        generate_reasoning(
            candidate
        )
    }


# ------------------------------------------
# Submission Explanation
# ------------------------------------------

def submission_reason(
    candidate
):

    summary = recruiter_summary(
        candidate
    )

    return summary[
        "reasoning"
    ]


# ------------------------------------------
# Detailed Report
# ------------------------------------------

def detailed_report(candidate):

    summary = recruiter_summary(
        candidate
    )

    report = f"""
Candidate Score:
{summary['final_score']}

Recommendation:
{summary['recommendation']}

Strengths:
"""

    for item in summary[
        "top_strengths"
    ]:

        report += f"\n✓ {item}"

    report += "\n\nPotential Gaps:"

    for item in summary[
        "potential_gaps"
    ]:

        report += f"\n• {item}"

    return report


# ------------------------------------------
# Testing
# ------------------------------------------

if __name__ == "__main__":

    print(
        "Explainability Module Loaded"
    )