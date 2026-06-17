
from src.rank_candidates import run_pipeline

def main():

    print("=" * 60)
    print(" Intelligent Candidate Discovery System ")
    print("=" * 60)

    ranked_df = run_pipeline()

    print("\nPipeline Completed Successfully.")
    print("Submission file generated.")

    return ranked_df


if __name__ == "__main__":
    main()