# ==========================================
# Redrob Intelligent Candidate Discovery
# scorer.py
# ==========================================

from src.feature_extractor import extract_features
from src.semantic_matcher import semantic_features
from src.config import WEIGHTS
from src.utils import clamp


# ------------------------------------------
# Weighted Final Score
# ------------------------------------------

def calculate_final_score(
    candidate
):

    features = extract_features(
        candidate
    )

    semantic = {
    "semantic_score": 0.5,
    "retrieval_semantic": 0.5,
    "ranking_semantic": 0.5,
    "recommendation_semantic": 0.5
    }

    score = 0

    # Semantic Relevance
    score += (
        semantic["semantic_score"]
        *
        WEIGHTS["semantic_score"]
    )

    # Skill Match
    score += (
        features["skill_score"]
        *
        WEIGHTS["skill_score"]
    )

    # Retrieval Experience
    score += (
        features["retrieval_score"]
        *
        WEIGHTS["retrieval_score"]
    )

    # Career Quality
    score += (
        features["product_company_score"]
        *
        WEIGHTS["career_score"]
    )

    # Title Match
    score += (
        features["title_score"]
        *
        WEIGHTS["title_score"]
    )

    # Experience Match
    score += (
        features["experience_score"]
        *
        WEIGHTS["experience_score"]
    )

    # Behavioral Intelligence
    score += (
        features["behavioral_score"]
        *
        WEIGHTS["behavior_score"]
    )

    return round(
        clamp(score),
        6
    )


# ------------------------------------------
# Industry Grade Score Breakdown
# ------------------------------------------

def score_breakdown(
    candidate
):

    features = extract_features(
        candidate
    )

    semantic = semantic_features(
        candidate
    )

    final_score = calculate_final_score(
        candidate
    )

    return {

        "final_score":
        final_score,

        "semantic_score":
        semantic["semantic_score"],

        "retrieval_semantic":
        semantic[
            "retrieval_semantic"
        ],

        "ranking_semantic":
        semantic[
            "ranking_semantic"
        ],

        "recommendation_semantic":
        semantic[
            "recommendation_semantic"
        ],

        "skill_score":
        features["skill_score"],

        "experience_score":
        features["experience_score"],

        "title_score":
        features["title_score"],

        "product_company_score":
        features[
            "product_company_score"
        ],

        "retrieval_score":
        features["retrieval_score"],

        "ranking_score":
        features["ranking_score"],

        "recommendation_score":
        features[
            "recommendation_score"
        ],

        "behavioral_score":
        features[
            "behavioral_score"
        ],

        "education_score":
        features[
            "education_score"
        ],

        "location_score":
        features[
            "location_score"
        ]
    }


# ------------------------------------------
# Tier Assignment
# ------------------------------------------

def assign_candidate_tier(
    score
):

    if score >= 0.90:
        return "Tier 1"

    elif score >= 0.80:
        return "Tier 2"

    elif score >= 0.70:
        return "Tier 3"

    elif score >= 0.60:
        return "Tier 4"

    return "Tier 5"


# ------------------------------------------
# Recruiter Friendly Label
# ------------------------------------------

def recommendation_label(
    score
):

    if score >= 0.90:
        return "Strong Hire"

    elif score >= 0.80:
        return "Hire"

    elif score >= 0.70:
        return "Consider"

    elif score >= 0.60:
        return "Review"

    return "Low Priority"


# ------------------------------------------
# Full Candidate Evaluation
# ------------------------------------------

def evaluate_candidate(
    candidate
):

    score = calculate_final_score(
        candidate
    )

    return {

        "candidate_id":
        candidate["candidate_id"],

        "score":
        score,

        "tier":
        assign_candidate_tier(
            score
        ),

        "recommendation":
        recommendation_label(
            score
        ),

        "details":
        score_breakdown(
            candidate
        )
    }


# ------------------------------------------
# Candidate Comparison
# ------------------------------------------

def compare_candidates(
    candidate_a,
    candidate_b
):

    score_a = calculate_final_score(
        candidate_a
    )

    score_b = calculate_final_score(
        candidate_b
    )

    if score_a > score_b:

        return {
            "winner":
            candidate_a[
                "candidate_id"
            ],
            "score":
            score_a
        }

    return {
        "winner":
        candidate_b[
            "candidate_id"
        ],
        "score":
        score_b
    }


# ------------------------------------------
# Testing
# ------------------------------------------

if __name__ == "__main__":

    print(
        "Scoring Engine Loaded"
    )