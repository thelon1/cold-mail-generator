# 🚀 Cold Email Generator

Cold Email Generator is a smart, AI-powered application that automates the creation of personalized cold emails for job applications. Built with Streamlit, LangChain, Groq, and ChromaDB, this tool streamlines the outreach process by analyzing company job listings and aligning them with your personal skills and portfolio.

Whether you're a job seeker aiming for tailored communication or a recruiter automating engagement, this tool offers a powerful way to scale personalized emails without compromising quality.

# 🔍 Features

🔗 URL-Based Job Extraction
Simply input the careers page URL of a company. The app uses LLMs to parse and extract job listings in real time.

🧠 Skill Matching with Vector Search
Your portfolio or resume is embedded and stored in ChromaDB. The app matches job requirements against your profile using vector similarity.

✉️ AI-Powered Cold Email Generation
Automatically generates high-quality, customized cold emails for each relevant job using Groq's LLMs and LangChain pipelines.

🖥️ Interactive UI with Streamlit
Simple, clean, and user-friendly interface to manage the entire process end-to-end without writing a line of code.

![Screenshot (54)](https://github.com/user-attachments/assets/9c91b887-8f07-4d07-be6d-eb44aac4c531)


![Screenshot (55)](https://github.com/user-attachments/assets/db1c637e-28f5-4731-bea1-8dac0e3da0aa)

# 🛠️ Tech Stack

### Tool	Purpose

| Technology              | Role / Description                                |
|-------------------------|---------------------------------------------------|
| **Streamlit**           | UI for interacting with the app                   |
| **Groq**                | Fast and efficient LLM inference                  |
| **LangChain**           | Orchestration of prompt workflows                 |
| **ChromaDB**            | Vector database for skill matching                |
| **BeautifulSoup / Requests** | Web scraping (optional fallback mechanism)   |

# 🧠 Example Use Case

You're applying to multiple data science roles across various companies.
Instead of writing a custom cold email for each one, just:

Upload your resume once

Paste each company’s career URL

Instantly get personalized cold emails, crafted to match each role’s requirements

# 📁 Folder Structure

## 📁 Project Structure

| Path                         | Description                                                   |
|------------------------------|---------------------------------------------------------------|
| `cold-mail-generator/`       | Root directory of the project                                 |
| ├── `app.py`                 | Main Streamlit app entry point                               |
| ├── `requirements.txt`       | Python dependencies list                                     |
| ├── `README.md`              | Project documentation                                        |
| └── `utils/`                 | Utility modules for core functionalities                     |
| &nbsp;&nbsp;&nbsp;&nbsp;├── `extract_jobs.py`     | Extracts job listings from company URLs              |
| &nbsp;&nbsp;&nbsp;&nbsp;├── `vector_search.py`    | Matches job listings with user portfolio using ChromaDB |
| &nbsp;&nbsp;&nbsp;&nbsp;└── `email_generator.py`  | Generates personalized cold emails using LLM         |


# 📬 Connect

For questions or collaboration:

Email: rohitwamane19@gmail.com

GitHub: https://github.com/thelon1

LinkedIn: https://www.linkedin.com/in/rohitwamane/




