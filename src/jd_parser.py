# ==========================================
# Redrob Intelligent Candidate Discovery
# jd_parser.py
# ==========================================

from src.config import (
    TARGET_SKILLS,
    RETRIEVAL_KEYWORDS,
    PREFERRED_LOCATIONS,
    MIN_EXPERIENCE,
    MAX_EXPERIENCE
)

class JDParser:

    def __init__(self):

        self.jd_requirements = {
            "role": "Senior AI Engineer",

            "experience_min":
            MIN_EXPERIENCE,

            "experience_max":
            MAX_EXPERIENCE,

            "skills":
            TARGET_SKILLS,

            "retrieval_keywords":
            RETRIEVAL_KEYWORDS,

            "preferred_locations":
            PREFERRED_LOCATIONS,

            "must_have": [
                "retrieval",
                "ranking",
                "embeddings",
                "vector database",
                "python"
            ],

            "good_to_have": [
                "recommendation systems",
                "fine tuning",
                "rag",
                "learning to rank",
                "ab testing"
            ]
        }

    def get_requirements(self):

        return self.jd_requirements

    def get_required_skills(self):

        return self.jd_requirements["skills"]

    def get_required_experience(self):

        return (
            self.jd_requirements["experience_min"],
            self.jd_requirements["experience_max"]
        )

    def get_locations(self):

        return self.jd_requirements[
            "preferred_locations"
        ]

    def get_role_name(self):

        return self.jd_requirements[
            "role"
        ]

    def get_must_have_skills(self):

        return self.jd_requirements[
            "must_have"
        ]

    def get_good_to_have_skills(self):

        return self.jd_requirements[
            "good_to_have"
        ]

    def print_summary(self):

        print("\n========== JD SUMMARY ==========\n")

        print(
            f"Role: {self.get_role_name()}"
        )

        print(
            f"Experience: "
            f"{MIN_EXPERIENCE}-{MAX_EXPERIENCE} years"
        )

        print(
            "\nMust Have Skills:"
        )

        for skill in self.get_must_have_skills():

            print(
                f" - {skill}"
            )

        print(
            "\nGood To Have Skills:"
        )

        for skill in self.get_good_to_have_skills():

            print(
                f" - {skill}"
            )

        print(
            "\nPreferred Locations:"
        )

        for loc in self.get_locations():

            print(
                f" - {loc}"
            )

        print(
            "\n================================"
        )


# ----------------------------------
# Singleton instance
# ----------------------------------

jd_parser = JDParser()


def get_jd_requirements():

    return jd_parser.get_requirements()


def get_required_skills():

    return jd_parser.get_required_skills()


def get_required_experience():

    return jd_parser.get_required_experience()


def get_preferred_locations():

    return jd_parser.get_locations()


if __name__ == "__main__":

    jd_parser.print_summary()