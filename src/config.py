TARGET_SKILLS = [
    "python",
    "machine learning",
    "deep learning",
    "natural language processing",
    "nlp",
    "large language models",
    "llm",
    "retrieval",
    "retrieval systems",
    "information retrieval",
    "semantic search",
    "ranking",
    "ranking systems",
    "recommendation systems",
    "recommendation engine",
    "embeddings",
    "openai embeddings",
    "sentence transformers",
    "vector databases",
    "pinecone",
    "weaviate",
    "qdrant",
    "milvus",
    "faiss",
    "elasticsearch",
    "opensearch",
    "rag",
    "hybrid retrieval",
    "learning to rank",
    "xgboost ranker",
    "fine tuning",
    "lora",
    "qlora",
    "peft",
    "ab testing",
    "ndcg",
    "mrr",
    "map",
    "evaluation framework",
]

# HIGH VALUE KEYWORDS
RETRIEVAL_KEYWORDS = [
    "retrieval",
    "ranking",
    "recommendation",
    "search",
    "semantic search",
    "vector search",
    "relevance",
    "information retrieval",
    "hybrid retrieval",
    "embeddings",
    "rag",
    "retriever",
    "dense retrieval",
    "sparse retrieval",
]

# PRODUCT / STARTUP EXPERIENCE BONUS
PRODUCT_COMPANIES = [
    "google",
    "amazon",
    "microsoft",
    "meta",
    "uber",
    "airbnb",
    "netflix",
    "linkedin",
    "atlassian",
    "adobe",
    "salesforce",
    "flipkart",
    "swiggy",
    "zomato",
    "ola",
    "paytm",
    "razorpay",
    "cred",
    "freshworks",
]

# SERVICE COMPANIES PENALTY
SERVICE_COMPANIES = [
    "tcs",
    "infosys",
    "wipro",
    "cognizant",
    "capgemini",
    "hcl",
    "tech mahindra",
    "accenture",
]

# IDEAL TITLES
GOOD_TITLES = [
    "ai engineer",
    "machine learning engineer",
    "ml engineer",
    "data scientist",
    "applied scientist",
    "research engineer",
    "search engineer",
    "relevance engineer",
    "recommendation engineer",
    "nlp engineer",
]

# LOW RELEVANCE TITLES
BAD_TITLES = [
    "marketing manager",
    "sales manager",
    "business development",
    "recruiter",
    "hr manager",
    "account manager",
]

# EXPERIENCE RANGE FROM JD
MIN_EXPERIENCE = 5
MAX_EXPERIENCE = 9

# LOCATION BONUS
PREFERRED_LOCATIONS = [
    "pune",
    "noida",
    "delhi",
    "gurgaon",
    "gurugram",
    "hyderabad",
    "mumbai",
    "bangalore",
    "bengaluru",
]

# FEATURE WEIGHTS
WEIGHTS = {
    "semantic_score": 0.05,
    "skill_score": 0.15,
    "retrieval_score": 0.15,
    "career_score": 0.10,
    "title_score": 0.10,
    "experience_score": 0.10,
    "behavior_score": 0.35,
}

# BEHAVIORAL WEIGHTS
BEHAVIOR_WEIGHTS = {
    "recruiter_response_rate": 0.20,
    "interview_completion_rate": 0.15,
    "offer_acceptance_rate": 0.10,
    "profile_completeness_score": 0.10,
    "saved_by_recruiters_30d": 0.10,
    "search_appearance_30d": 0.10,
    "github_activity_score": 0.10,
    "open_to_work_flag": 0.05,
    "notice_period_days": 0.05,
    "willing_to_relocate": 0.05,
}

# EXPLAINABILITY RULES
TOP_REASON_COUNT = 5

# OUTPUT FILE
OUTPUT_FILE = "outputs/submission.csv"

# TOP N CANDIDATES
TOP_K = 100