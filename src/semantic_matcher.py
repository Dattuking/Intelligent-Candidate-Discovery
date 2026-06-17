# ==========================================
# Redrob Intelligent Candidate Discovery
# semantic_matcher.py
# FAST VERSION - NO TRANSFORMERS
# ==========================================

from src.utils import (
    normalize_text,
    get_candidate_text
)

JD_KEYWORDS = {
    "python",
    "machine learning",
    "deep learning",
    "llm",
    "retrieval",
    "ranking",
    "recommendation",
    "embeddings",
    "vector database",
    "semantic search",
    "rag",
    "faiss",
    "pinecone",
    "weaviate",
    "qdrant",
    "ndcg",
    "mrr",
    "map"
}

RETRIEVAL_KEYWORDS = {
    "retrieval",
    "semantic search",
    "vector search",
    "rag",
    "embeddings",
    "faiss",
    "pinecone",
    "weaviate",
    "qdrant"
}

RANKING_KEYWORDS = {
    "ranking",
    "relevance",
    "learning to rank",
    "ndcg",
    "mrr",
    "map"
}

RECOMMENDATION_KEYWORDS = {
    "recommendation",
    "personalization",
    "recommendation engine",
    "content recommendation"
}


def keyword_similarity(text, keywords):

    text = normalize_text(text)

    matches = 0

    for keyword in keywords:

        if normalize_text(keyword) in text:
            matches += 1

    return matches / max(len(keywords), 1)


def semantic_similarity(candidate):

    text = get_candidate_text(candidate)

    return round(
        keyword_similarity(
            text,
            JD_KEYWORDS
        ),
        4
    )


def retrieval_semantic_score(candidate):

    text = get_candidate_text(candidate)

    return round(
        keyword_similarity(
            text,
            RETRIEVAL_KEYWORDS
        ),
        4
    )


def ranking_semantic_score(candidate):

    text = get_candidate_text(candidate)

    return round(
        keyword_similarity(
            text,
            RANKING_KEYWORDS
        ),
        4
    )


def recommendation_semantic_score(candidate):

    text = get_candidate_text(candidate)

    return round(
        keyword_similarity(
            text,
            RECOMMENDATION_KEYWORDS
        ),
        4
    )


def semantic_features(candidate):

    return {

        "semantic_score":
        semantic_similarity(candidate),

        "retrieval_semantic":
        retrieval_semantic_score(candidate),

        "ranking_semantic":
        ranking_semantic_score(candidate),

        "recommendation_semantic":
        recommendation_semantic_score(candidate)
    }


if __name__ == "__main__":

    print(
        "Fast Semantic Matcher Loaded"
    )