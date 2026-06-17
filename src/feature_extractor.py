from src.config import (
    TARGET_SKILLS,
    RETRIEVAL_KEYWORDS,
    PRODUCT_COMPANIES,
    GOOD_TITLES,
    PREFERRED_LOCATIONS
)

from src.utils import (
    normalize_text,
    get_all_skills,
    get_candidate_text,
    keyword_count,
    clamp
)


def skill_match_score(candidate):

    candidate_skills = get_all_skills(
        candidate
    )

    matched = 0

    for skill in TARGET_SKILLS:

        if normalize_text(skill) in candidate_skills:
            matched += 1

    return clamp(
        matched / len(TARGET_SKILLS)
    )

def experience_score(candidate):

    years = candidate["profile"].get(
        "years_of_experience",
        0
    )

    if 5 <= years <= 9:
        return 1.0

    if 3 <= years <= 12:
        return 0.8

    if years > 12:
        return 0.7

    return 0.4

def title_score(candidate):

    title = normalize_text(
        candidate["profile"].get(
            "current_title",
            ""
        )
    )

    for good_title in GOOD_TITLES:

        if normalize_text(good_title) in title:
            return 1.0

    return 0.4

def product_company_score(candidate):

    score = 0

    history = candidate.get(
        "career_history",
        []
    )

    for job in history:

        company = normalize_text(
            job.get(
                "company",
                ""
            )
        )

        for pc in PRODUCT_COMPANIES:

            if normalize_text(pc) in company:
                score += 0.3

    return clamp(score)
def retrieval_score(candidate):

    text = get_candidate_text(
        candidate
    )

    matches = keyword_count(
        text,
        RETRIEVAL_KEYWORDS
    )

    return clamp(
        matches / len(RETRIEVAL_KEYWORDS)
    )


def ranking_score(candidate):

    text = get_candidate_text(
        candidate
    )

    keywords = [
        "ranking",
        "relevance",
        "search ranking",
        "learning to rank",
        "xgboost ranker",
        "ndcg",
        "mrr",
        "map"
    ]

    matches = keyword_count(
        text,
        keywords
    )

    return clamp(
        matches / len(keywords)
    )


def recommendation_score(candidate):

    text = get_candidate_text(
        candidate
    )

    keywords = [
        "recommendation",
        "recommendation system",
        "personalization",
        "user recommendation",
        "content recommendation"
    ]

    matches = keyword_count(
        text,
        keywords
    )

    return clamp(
        matches / len(keywords)
    )


def location_score(candidate):

    location = normalize_text(
        candidate["profile"].get(
            "location",
            ""
        )
    )

    for loc in PREFERRED_LOCATIONS:

        if normalize_text(loc) in location:
            return 1.0

    return 0.5


def education_score(candidate):

    education = candidate.get(
        "education",
        []
    )

    if len(education) == 0:
        return 0.3

    score = 0

    for edu in education:

        tier = edu.get(
            "tier",
            "unknown"
        )

        if tier == "tier_1":
            score += 0.5

        elif tier == "tier_2":
            score += 0.3

        elif tier == "tier_3":
            score += 0.2

    return clamp(score)


def behavioral_score(candidate):

    sig = candidate[
        "redrob_signals"
    ]

    score = 0

    score += (
        sig[
            "recruiter_response_rate"
        ] * 0.20
    )

    score += (
        sig[
            "interview_completion_rate"
        ] * 0.15
    )

    score += (
        max(
            sig[
                "offer_acceptance_rate"
            ],
            0
        ) * 0.10
    )

    score += (
        sig[
            "profile_completeness_score"
        ] / 100
    ) * 0.10

    score += (
        min(
            sig[
                "saved_by_recruiters_30d"
            ] / 50,
            1
        )
    ) * 0.10

    score += (
        min(
            sig[
                "search_appearance_30d"
            ] / 100,
            1
        )
    ) * 0.10

    github_score = max(
        sig[
            "github_activity_score"
        ],
        0
    )

    score += (
        github_score / 100
    ) * 0.10

    if sig[
        "open_to_work_flag"
    ]:
        score += 0.05

    if sig[
        "willing_to_relocate"
    ]:
        score += 0.05

    if sig[
        "notice_period_days"
    ] <= 30:
        score += 0.05

    return clamp(score)

def extract_features(candidate):

    return {

        "skill_score":
        skill_match_score(candidate),

        "experience_score":
        experience_score(candidate),

        "title_score":
        title_score(candidate),

        "product_company_score":
        product_company_score(candidate),

        "retrieval_score":
        retrieval_score(candidate),

        "ranking_score":
        ranking_score(candidate),

        "recommendation_score":
        recommendation_score(candidate),

        "location_score":
        location_score(candidate),

        "education_score":
        education_score(candidate),

        "behavioral_score":
        behavioral_score(candidate)
    }