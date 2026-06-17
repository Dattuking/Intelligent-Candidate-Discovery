# ==========================================
# Redrob Intelligent Candidate Discovery
# utils.py
# ==========================================

import re
import math
from datetime import datetime
from dateutil.parser import parse


def normalize_text(text):
    """
    Clean and normalize text.
    """

    if text is None:
        return ""

    text = str(text).lower()

    text = re.sub(
        r"[^a-z0-9\s]",
        " ",
        text
    )

    text = re.sub(
        r"\s+",
        " ",
        text
    )

    return text.strip()


def safe_divide(a, b):

    if b == 0:
        return 0.0

    return a / b


def clamp(value, min_value=0.0, max_value=1.0):

    return max(
        min_value,
        min(value, max_value)
    )


def normalize_score(
    value,
    min_val,
    max_val
):

    if max_val == min_val:
        return 0

    return (
        value - min_val
    ) / (
        max_val - min_val
    )


def contains_keyword(
    text,
    keywords
):

    text = normalize_text(text)

    for keyword in keywords:

        if normalize_text(keyword) in text:
            return True

    return False


def keyword_count(
    text,
    keywords
):

    text = normalize_text(text)

    count = 0

    for keyword in keywords:

        if normalize_text(keyword) in text:
            count += 1

    return count


def months_between(
    start_date,
    end_date=None
):

    try:

        start = parse(start_date)

        if end_date:
            end = parse(end_date)

        else:
            end = datetime.now()

        months = (
            (end.year - start.year) * 12
            +
            (end.month - start.month)
        )

        return max(months, 0)

    except Exception:

        return 0


def get_candidate_text(
    candidate
):

    """
    Create one large text blob
    for semantic matching.
    """

    sections = []

    profile = candidate.get(
        "profile",
        {}
    )

    sections.append(
        profile.get(
            "headline",
            ""
        )
    )

    sections.append(
        profile.get(
            "summary",
            ""
        )
    )

    sections.append(
        profile.get(
            "current_title",
            ""
        )
    )

    # skills

    for skill in candidate.get(
        "skills",
        []
    ):

        sections.append(
            skill.get(
                "name",
                ""
            )
        )

    # career history

    for job in candidate.get(
        "career_history",
        []
    ):

        sections.append(
            job.get(
                "title",
                ""
            )
        )

        sections.append(
            job.get(
                "description",
                ""
            )
        )

    return " ".join(sections)


def get_all_skills(
    candidate
):

    skills = []

    for skill in candidate.get(
        "skills",
        []
    ):

        skills.append(
            normalize_text(
                skill.get(
                    "name",
                    ""
                )
            )
        )

    return list(
        set(skills)
    )


def get_profile_age_days(
    signup_date
):

    try:

        signup = parse(
            signup_date
        )

        today = datetime.now()

        delta = (
            today - signup
        ).days

        return delta

    except Exception:

        return 0


def get_last_active_days(
    last_active_date
):

    try:

        last_active = parse(
            last_active_date
        )

        today = datetime.now()

        delta = (
            today - last_active
        ).days

        return delta

    except Exception:

        return 999


def log_scale(
    value
):

    if value <= 0:
        return 0

    return math.log1p(value)


def build_reason(
    reasons
):

    reasons = [
        r.strip()
        for r in reasons
        if r
    ]

    return "; ".join(reasons)


def percentile_rank(
    value,
    values
):

    if len(values) == 0:
        return 0

    count = sum(
        v <= value
        for v in values
    )

    return count / len(values)