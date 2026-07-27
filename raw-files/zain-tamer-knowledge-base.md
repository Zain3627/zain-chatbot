# Zain Tamer Zain Elabdin — Complete Personal Knowledge Base
---
## Personal Identity & Contact
| Field | Detail |
|---|---|
| Full Name | Zain Tamer Zain Elabdin |
| Location | Alexandria, Egypt |
| Email | zaintamer10@gmail.com |
| Phone | +20 1094332424 |
| LinkedIn | linkedin.com/in/zaintamer |
| GitHub | github.com/Zain3627 |
| Codeforces | codeforces.com/profile/Zain3627 |
| Kaggle | kaggle.com/zaintamer |
| Portfolio | zaintamer.vercel.app |

**Professional identity:** Zain identifies as an AI/ML Engineer and MLOps practitioner. He is a final-year Computer Engineering student who builds and deploys production-grade ML systems, competes in programming contests, and coaches others.

---

## Education

### University — Arab Academy for Science, Technology & Maritime Transport (AAST)
- **Degree:** Bachelor of Science in Computer Engineering
- **Location:** Alexandria, Egypt
- **Duration:** September 2022 – February 2027 (expected graduation ~July 2027)
- **CGPA:** 3.98 / 4.0 (near-perfect GPA)
- **Academic focus:** Artificial Intelligence, Machine Learning, Computer Vision, and MLOps.

#### Academic Performance
- Maintained an **Excellent** GPA throughout all academic years.
- Consistently ranked among the top-performing students in the department.
- Completed coursework spanning software engineering, artificial intelligence, computer vision, embedded systems, networking, cybersecurity, distributed systems, and human-computer interaction.

#### Areas of Study
Core subjects include:
- Artificial Intelligence
- Image Processing & Pattern Recognition
- Data Analytics & Optimization using Python
- Distributed and Parallel Systems
- Operating Systems
- Computer Graphics
- Cyber Security
- Embedded Systems Design
- Intelligent Human Computer Interaction
- Data Structures & Algorithms
- Computing Algorithms
- Computer Networks
- Advanced Networks
- Database Systems
- Systems Programming
- Computer Architecture
- Numerical Methods
- Probability & Statistical Analysis
- Object-Oriented Programming
- Java Programming


#### Coursework

##### Artificial Intelligence
- Artificial Intelligence
- Image Processing & Pattern Recognition

##### Machine Learning & Data
- Data Analytics & Optimization using Python
- Probability & Statistical Analysis

##### Software Engineering
- Object-Oriented Programming
- Java Programming
- Systems Programming
- Operating Systems

##### Algorithms
- Data Structures & Algorithms
- Computing Algorithms
- Numerical Methods

##### Systems
- Computer Architecture
- Embedded Systems Design
- Microprocessor Systems
- Distributed & Parallel Systems

##### Networking
- Computer Networks
- Advanced Networks

##### Security
- Cyber Security

##### Databases
- Database Systems

### Gharbiya STEM High School

**Degree:** STEM High School Diploma
**Location:** Tanta, Egypt
**Duration:** Sep 2019 – Jul 2022

A highly competitive boarding STEM school focused on project-based learning, scientific research, and interdisciplinary education. Living away from home for three years developed independence, discipline, adaptability, and teamwork.

**Achievements**
- Graduated **2nd in school**
- Ranked **34th nationally** in senior year
- Completed **three year-long interdisciplinary capstone projects**
- Developed strong teamwork through project-based education
- Built excellent time management and communication skills while living in a boarding environment
- Learned to collaborate with students from diverse backgrounds
---

## Work Experience

### Machine Learning Engineer Intern — Digital Egypt Pioneers Initiative (DEPI)
- **Duration:** June 2025 – December 2025
- **Type:** Structured government-backed applied ML programme
- **Hours:** 180 hours of applied content
- **Domains covered:** Data engineering, Computer Vision, NLP, Cloud deployment
- **Key work:**
  - Designed, trained, and deployed end-to-end ML pipelines for computer vision and predictive analytics
  - Covered the full ML lifecycle: data preprocessing → feature engineering → model training → evaluation → deployment
  - Deployed models on **Azure Machine Learning** and **Azure App Service**
  - Developed NLP pipelines for text classification and sentiment analysis using **Transformer-based models**
  - Managed model artifacts on **Azure Blob Storage**

---

## Projects

### Project 1: Premier League Predictor — End-to-End MLOps System
This is one of Zain's projects. This project is called Premier League Predictor.
- **GitHub:** github.com/Zain3627/pl_predictor
- **Goal:** Predict Premier League match outcomes and project final league standings
- **Tech Stack:** Python 3.10, ZenML, MLflow, XGBoost, RandomForest, LogisticRegression, pandas, NumPy, Supabase (PostgreSQL via psycopg2), Pydantic, Streamlit
- **Pipelines:**
  - *Data pipeline:* fetch → clean → upload
  - *Prediction pipeline:* ingest → train → evaluate → predict
- **MLflow:** Tracks experiments and model registry; automatically promotes the highest-accuracy model to a champion alias
- **Storage:** Supabase PostgreSQL for processed datasets; AWS S3 for MLflow artifacts
- **Deployment:** Containerized with Docker, pushed to AWS ECR, deployed to AWS EC2
- **Automation:** Cron-based scheduling — triggers full retraining when live prediction accuracy drops below threshold
- **Dashboard:** Streamlit frontend for match predictions and league table projections

---

### Project 2: FPL Vision — AI-Powered Fantasy Premier League Assistant
This is one of Zain's projects. This project is called FPL Vision.
- **GitHub:** https://github.com/Zain3627/Fantasy_Premier_League_Predictor
- **Goal:** Help Fantasy Premier League managers make data-driven decisions
- **What it does:** Generates player recommendations and expected points projections
- **Model:** Fine-tuned XGBoost classifier
- **Data:** Aggregated from the FPL REST API across 700+ players and 20 teams
- **Deployment:** Streamlit app on Azure App Service; artifacts on Azure Blob Storage
- **CI/CD:** GitHub Actions — auto-deploys on data change or code update
- **Frontend:** Live dashboards for player and team statistics

---

### Project 3: Facial Recognition System
This is one of Zain's projects. This project is called Facial Recognition System.
- **GitHub:** https://github.com/Zain3627/Facial-Recognition-System
- **Goal:** Real-time facial recognition for multiple identities
- **Model:** Pre-trained FaceNet backbone with fine-tuned transfer learning classification head
- **Dataset:** LFW dataset — 303 identities, 640 embeddings
- **Accuracy:** 98%
- **Pipeline:** Multi-face detection via MediaPipe → 128-dimensional L2-normalized embeddings → cosine similarity matching
- **Feature:** User registration flow supporting new identity enrollment
- **Deployment:** Dockerized Streamlit app deployed on Hugging Face Spaces

---

### Project 4: Vision Transformer — Blood Cell Classification
This is one of Zain's projects. This is an academic project called Vision Transformer Blood Cell Classification.
- **Task:** 8-class blood cell classification on the BloodMNIST dataset (MedMNIST benchmark)
- **Models compared:** ViT-B/16 (fine-tuned) vs. Swin Transformer-B vs. ResNet-50 (baseline)
- **Accuracy achieved:** 98.54% with ViT-B/16
- **Hardware constraint:** 4 GB VRAM (RTX 3050 Ti); explored Kaggle free-tier GPU for training

---

### Project 5: Pose-Based Sports Action Recognition
This is one of Zain's projects. This is an academic HCI project called Pose-Based Sports Action Recognition.
- **Dataset:** Penn Action dataset
- **Task:** Recognize 15 sport classes from pose keypoints
- **Models:** LSTM (Model A) vs. GRU (Model B) — identical hyperparameters, comparative evaluation
- **Output:** SVG architecture diagrams; HCI content mapped to Nielsen's heuristics

---

### Project 6: Kubernetes/Kafka Distributed Weather Station Pipeline
This is one of Zain's projects. This is an academic distributed systems project called Weather Station Pipeline.
- **Goal:** IoT-style weather data pipeline using distributed systems
- **Stack:** Java microservices, PostgreSQL, Minikube, Kafka
- **Kubernetes objects used:** ConfigMaps, Secrets, PVCs, Services, StatefulSets
- **Environment:** Arch Linux

---

### Project 7: WHO COVID-19 Global Daily Data Analysis
This is one of Zain's projects. This project is a data analysis project called WHO COVID-19 Global Daily Data Analysis.
- **GitHub:** https://github.com/Zain3627/WHO-COVID-19-global-daily-data-analysis-project
- **Dataset:** WHO global COVID-19 dataset — 250,000+ daily records across 200+ countries/regions
- **Work:** In-depth EDA — data cleaning, feature engineering, statistical visualization
- **Goal:** Uncover insights about global case trends and country-level patterns

---

### Project 8: Chat Room
This is one of Zain's projects. This project is a networking project called Chat Room.
- **GitHub:** https://github.com/Zain3627/Chatroom
- **Goal:** LAN-based real-time chatroom supporting text, voice, and video
- **Stack:** Python, socket programming
- **Capacity:** Up to 10 concurrent users with seamless media switching
- **Concepts:** Socket programming, client–server architecture, multithreading, low-latency network communication

---

### Project 9: Autonomous Point-to-Point Smart Car
This is one of Zain's projects. This project is an embedded systems project called Autonomous Smart Car.
- **Goal:** Autonomous ground vehicle that navigates to user-specified 2D coordinates
- **Hardware:** Arduino with onboard IMU-based localization and motion control
- **Communication:** MQTT protocol for wireless commands; voice recognition for voice-based positioning
- **Concepts:** Embedded control, sensor fusion, IoT communication
## Research

### Research Interests
- Large Language Models
- Retrieval-Augmented Generation (RAG)
- Computer Vision
- MLOps
- Representation Learning
- Deep Learning Optimization
- AI Agents
- Sports Analytics

### AI Research Notes & Paper Reproductions

GitHub: https://github.com/Zain3627/ai-research-summary

An ongoing collection of structured analyses and reproductions of influential AI papers spanning ML, DL, Computer Vision, NLP, LLMs, MLOps, and related fields.

**Highlights**
- Summarizes methodologies, experiments, strengths, weaknesses, and future work.
- Reproduces selected papers to verify published results.
- Maintains a long-term AI research knowledge base.

### Data Augmentation & Hyperparameter Tuning for Image Classification
- **GitHub:** https://github.com/Zain3627/An-Experimental-Analysis-of-Data-Augmentation-and-Hyperparameter-Tuning-for-Image-Classification
- **Duration:** October 2025 – December 2025
- **Co-author:** Adham Mahmoud Waheeb
- **Dataset:** Caltech-101
- **Models compared:** Handcrafted CNN vs. EfficientNet-B0
- **Novel contributions:**
  - Proposed and evaluated new augmentation methods: **Pairwise Channel Transfer**, **Object Occlusion**, **Novel Masking**
  - Studied the contribution of each augmentation technique to model performance

### Comparison of Quicksort and BFPRT for the K-th Element Selection Problem
- **GitHub:** https://github.com/Zain3627/quicksort-bfprt-kth-selection-analysis
- **Date:** February 2025
- **Focus:** Algorithmic analysis of selection problem solutions
- **Content:** Performance comparison of Quicksort vs. BFPRT (Median of Medians) with respect to problem size

---

## Technical Skills

### Programming Languages
- Python (primary), C, C++, C#, Java, SQL, Bash

### Machine Learning & Data Science
- **Data:** Pandas, NumPy, Matplotlib, Seaborn, Plotly
- **ML:** scikit-learn, XGBoost
- **Deep Learning:** TensorFlow, Keras, PyTorch
- **NLP:** HuggingFace Transformers
- **Vision:** OpenCV, MediaPipe, FaceNet

### Cloud & Infrastructure
- **Azure:** Azure Machine Learning, Azure App Service, Azure Blob Storage
- **AWS:** EC2, ECR, S3, SageMaker, Bedrock, Lambda, CloudWatch, IAM
- **Databases:** PostgreSQL (Supabase), general SQL
- **Containers & Orchestration:** Docker, Kubernetes (Minikube), Kafka

### MLOps & Deployment
- ZenML (pipeline orchestration)
- MLflow (experiment tracking, model registry)
- GitHub Actions (CI/CD)
- Streamlit (frontend/dashboards)
- Hugging Face Spaces

### Algorithms & Problem Solving
- Data structures, graph algorithms, dynamic programming
- Binary search on answer + greedy feasibility
- Monotonic deques, number theory (linear sieve, Euler's totient, modular combinatorics)
- Game theory, constructive problems
- C++ STL containers

### Additional Tools
- Hadoop, Arduino, MQTT, LaTeX
- Obsidian (notes), Git/GitHub

---

## Soft Skills
- **Leadership** — coaches a CP club, led cloud workshops, mentored 30+ students
- **Communication** — explains complex ML and algorithm topics to beginners
- **Teamwork** — co-authored research, collaborated on group academic projects
- **Problem-Solving** — competitive programming Specialist, debugging complex infra issues
- **Flexibility & Resilience** — manages CGPA near 4.0 while juggling internships, coaching, and research
- **Multitasking** — simultaneously runs coursework projects, personal ML projects, CP sessions, and internship work

---

## Languages
| Language | Level |
|---|---|
| Arabic | Native |
| English | Advanced |
| German | Beginner |

---

## Competitions & Achievements & Honors

| Competition / Achievement | Date | Result |
|---|---|---|
| Second Place — HackerRank × CPClub AAST Event | April 2026 | 🥈 2nd place |
| Codeforces Specialist | November 2025 | Max rating 1448, top ~2% |
| ECPC (Egyptian Collegiate Programming Contest) | July 2025 | Qualified |
| Zindi Financial Inclusion in Africa | June 2025 | **Ranked 15th / 2000+ participants** |
| IEEEXtreme Programming Competition | October 2024 | Top 2% Egypt, top 20% worldwide (8000+ teams) |

---

## Certificates & Courses 

| Certificate | Issuer | Date |
|---|---|---|
| Artificial Intelligence Engineer 1 | Coursera – IBM | October 2025 |
| Sprints × Microsoft Summer Camp — AI & ML | Microsoft / Sprints | October 2025 |
| IBM Software Developer Roadmap | Coursera – IBM | October 2024 |
| IEEEXtreme participation + top ranking | IEEE | October 2024 |

---

## Volunteering & Leadership

### AWS Student Builder Group at AAST — Team Member
- **Duration:** March 2026 – Present
- **Activities:**
  - Organized multiple cloud practitioner training sessions
  - Led a 2-hour hands-on workshop on AWS services (EC2, S3, IAM, CloudWatch, billing) for 20+ students
  - Deployed a GitHub-hosted static site to EC2 via User Data scripts as a live demo

### AAST Competitive Programming Club — Coach
- **Duration:** September 2025 – Present
- **Activities:**
  - Led 15+ tutoring sessions covering competitive programming fundamentals and algorithms
  - Monitored and coached a group of 30+ students
  - Contributed to preparing materials and contest problems for trainees
  - Topics covered: STL containers, binary search, greedy, number theory, game theory, constructive problems

---

## Development Environment & Setup

- **OS:** Arch Linux by the way 
---

## Interests & Hobbies

### Football / Soccer
- Passionate football fan and analyst who supports Al-Ahly in Egypt.
- Interest extends into football analytics and data-driven match prediction (see PL Predictor project)

### Films
- Enjoys stylish ensemble films with clever plots
- Favorites: **Pulb Fiction**, **The Social Network**, **Intouchables**, **Klaus**, **Oppenheimer**, **spiderman across the spider verse**

### Anime
- Favorites: **Attack on titan**, **Boku no hero academia**, **Full metal** 

### Competitive Programming
- Active specialist Codeforces solver (C++)
- Practices on CSES and Codeforces problem sets
- Enjoys algorithmic puzzle-solving as both a personal hobby and professional skill


---

## Personality & Character

- **Methodical builder:** Prefers shipping complete systems over toy demos — projects have proper pipelines, CI/CD, and cloud deployment.
- **Lifelong learner:** Simultaneously studies ML deployment, distributed systems, cybersecurity, and algorithms — not just surface-level.
- **Teacher instinct:** Voluntarily coaches 30+ students in CP and ran AWS workshops; explains clearly at varying levels.
- **High standards:** 3.98/4.0 GPA while running multiple projects and internships demonstrates exceptional discipline.
- **Systems thinker:** Thinks in pipelines, architectures, and lifecycle — from data ingestion to production retraining.
- **Pragmatic tinkerer:** Runs Arch Linux + Hyprland, uses local LLMs, customizes Modelfiles — enjoys owning his own tools.
- **Competitive spirit:** Ranked top 2% in Egypt on IEEEXtreme, top 15 out of 2000+ on Zindi — performs under pressure.
- Curious
- Detail-oriented
- Analytical
- Self-motivated
- Organized
- Fast learner
- Enjoys building production-ready systems

---

## Current Focus Areas (as of mid-2026)

- Completing Computer Engineering degree at AAST (graduating ~early 2027)
- Deepening expertise in ML deployment: AWS Bedrock, SageMaker, vLLM, RAG systems
- Expanding PL Predictor to Azure and adding computer vision components (SoccerNet)
- Coaching competitive programming club at AAST
- Volunteering with AWS Student Builder Group
- Building personal RAG bot (this knowledge base is part of that project)
- Exploring startup ideas in AI automation, computer vision, sports analytics, and coding education

---

## Goals & Aspirations

- Become a production-grade ML/MLOps Engineer working on real-world AI systems at scale
- Bridge the gap between research and deployment — build things that actually run in production
- Grow as a technical leader and mentor within the Egyptian AI/tech community
- Eventually explore applied research at the intersection of computer vision and sports analytics

---

*Last updated: July 2026. Sources: CV, personal portfolio (zaintamer.vercel.app), and conversation history.*


---

## Additional Sections

### Learning Philosophy

- Learn from original research papers.
- Build implementations.
- Reproduce published work.
- Deploy complete end-to-end systems.
- Teach others to reinforce understanding if applicable or someone needs help.

### Current Learning

- GPT architecture
- Decoder-only Transformers
- Vision Transformers
- RAG systems
- Agentic AI
- Kubernetes
- AWS Cloud Practitioner certificate
