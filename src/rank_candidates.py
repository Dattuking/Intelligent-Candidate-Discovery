
import json
import heapq
import pandas as pd

TOP_K = 100


def fast_score(candidate):

    profile = candidate.get("profile", {})
    signals = candidate.get("redrob_signals", {})

    score = 0.0

    # Experience
    exp = profile.get(
        "years_of_experience",
        0
    )

    if 5 <= exp <= 9:
        score += 0.30
    elif exp >= 3:
        score += 0.20

    # Open To Work
    if signals.get(
        "open_to_work_flag",
        False
    ):
        score += 0.15

    # Recruiter Response
    score += (
        signals.get(
            "recruiter_response_rate",
            0
        ) * 0.20
    )

    # Interview Completion
    score += (
        signals.get(
            "interview_completion_rate",
            0
        ) * 0.15
    )

    # Profile Completeness
    score += (
        signals.get(
            "profile_completeness_score",
            0
        ) / 100
    ) * 0.10

    # GitHub Activity
    score += (
        signals.get(
            "github_activity_score",
            0
        ) / 100
    ) * 0.10

    return round(score, 6)


def run_pipeline():

    heap = []

    count = 0

    print("Processing candidates...")

    with open(
        "data/candidates.jsonl",
        "r",
        encoding="utf-8"
    ) as f:

        for line in f:

            count += 1

            if count % 5000 == 0:

                print(
                    f"Processed {count}"
                )

            candidate = json.loads(
                line
            )

            candidate_id = candidate.get(
                "candidate_id",
                ""
            )

            score = fast_score(
                candidate
            )

            item = (
                score,
                candidate_id
            )

            if len(heap) < TOP_K:

                heapq.heappush(
                    heap,
                    item
                )

            else:

                heapq.heappushpop(
                    heap,
                    item
                )

    # IMPORTANT:
    # score DESC
    # candidate_id ASC

    heap = sorted(
        heap,
        key=lambda x: (
            -x[0],
            x[1]
        )
    )

    rows = []

    for rank, (score, cid) in enumerate(
        heap,
        start=1
    ):

        rows.append(
            {
                "candidate_id": cid,
                "rank": rank,
                "score": score,
                "reasoning":
                "Strong experience and recruiter signals"
            }
        )

    df = pd.DataFrame(
        rows
    )

    # Extra safety sort

    df = df.sort_values(
        by=[
            "score",
            "candidate_id"
        ],
        ascending=[
            False,
            True
        ]
    )

    df = df.reset_index(
        drop=True
    )

    df["rank"] = range(
        1,
        len(df) + 1
    )

    df.to_csv(
        "outputs/submission.csv",
        index=False
    )

    print(
        "\nGenerated outputs/submission.csv"
    )

    print(
        f"Total selected candidates: {len(df)}"
    )


if __name__ == "__main__":

    run_pipeline()

