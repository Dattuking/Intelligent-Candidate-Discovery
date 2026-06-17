# Intelligent Candidate Discovery

## Problem Statement

Build an intelligent candidate ranking system that identifies the most suitable candidates for a Senior AI Engineer role.

Traditional Applicant Tracking Systems (ATS) rely heavily on keyword matching, which often misses highly relevant candidates whose experience is described differently.

This solution combines:

* Semantic Understanding
* Retrieval Intelligence
* Ranking Intelligence
* Recommendation System Experience
* Product Company Experience
* Behavioral Hiring Signals
* Explainable AI

to generate high-quality candidate rankings.

---

## Dataset

The challenge dataset contains:

* 100,000 Candidate Profiles
* Career History
* Skills
* Education
* Certifications
* Languages
* Behavioral Signals

Examples of behavioral signals:

* Open To Work
* Recruiter Response Rate
* Interview Completion Rate
* Offer Acceptance Rate
* GitHub Activity
* Search Appearances
* Saved By Recruiters

---

## Solution Architecture

Job Description
↓
Requirement Extraction
↓
Feature Engineering
↓
Semantic Matching
↓
Behavioral Intelligence
↓
Scoring Engine
↓
Explainability Layer
↓
Top 100 Candidate Selection
↓
submission.csv

---

## Features Used

### Technical Features

* Skill Match Score
* Retrieval Experience Score
* Ranking Experience Score
* Recommendation Experience Score
* Product Company Experience
* Education Score
* Location Score

### Semantic Features

* Candidate ↔ JD Similarity
* Retrieval Semantic Similarity
* Ranking Semantic Similarity
* Recommendation Semantic Similarity

### Behavioral Features

* Recruiter Response Rate
* Open To Work
* Offer Acceptance Rate
* Interview Completion Rate
* GitHub Activity Score
* Saved By Recruiters
* Search Appearance Score
* Profile Completeness

---

## Scoring Formula

Final Score =

0.20 × Semantic Similarity

0.15 × Skill Match

0.15 × Retrieval Experience

0.10 × Product Experience

0.10 × Title Relevance

0.10 × Experience Match

0.20 × Behavioral Signals

---

## Repository Structure

Intelligent-Candidate-Discovery/

├── data/

│ └── candidates.jsonl

├── src/

│ ├── config.py

│ ├── jd_parser.py

│ ├── feature_extractor.py

│ ├── semantic_matcher.py

│ ├── scorer.py

│ ├── explainability.py

│ ├── rank_candidates.py

│ └── utils.py

├── outputs/

│ └── submission.csv

├── docs/

│ ├── architecture.png

│ ├── workflow.png

│ └── methodology.png

├── main.py

├── requirements.txt

└── README.md

---

## Installation

Clone repository:

git clone https://github.com/your-team/intelligent-candidate-discovery

cd intelligent-candidate-discovery

Install dependencies:

pip install -r requirements.txt

---

## Run

python main.py

---

## Output

The system generates:

outputs/submission.csv

Format:

candidate_id,rank,score,reasoning

---

## Explainability

Every ranked candidate includes:

* Match Score
* Key Strengths
* Potential Gaps
* Recruiter-Friendly Explanation

Example:

Strong semantic alignment with Senior AI Engineer role; Demonstrated retrieval and search system experience; Experience with ranking systems; Excellent recruiter engagement signals.

---

## Innovation

Our solution goes beyond keyword matching by combining:

* Semantic Retrieval
* Behavioral Intelligence
* Explainable AI
* Career Trajectory Analysis
* Product Company Experience
* Retrieval & Ranking Expertise

This approach aligns more closely with real-world recruiter decision-making.

---

## Future Improvements

* Learning-to-Rank (XGBoost Ranker)
* LLM-Based Re-ranking
* Hybrid Retrieval
* Graph-Based Candidate Similarity
* Agentic Candidate Discovery
* Real-Time Recruiter Feedback Loop

---

## Team

PromptStorm

Data & AI Challenge 2026

Intelligent Candidate Discovery
