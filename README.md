🧊Cold Email Generator
Generate high-conversion cold emails using OpenAI's GPT models, with a clean and responsive Streamlit UI.


🚀 Live Demo
👉 Launch App

📌 Features
Generate cold emails for any product or service

Select tone, target audience, and language

Built using Streamlit, OpenAI GPT, and Python

Mobile-friendly & deployable

🛠️ Tech Stack
Python 3.10+

Streamlit

OpenAI API

dotenv for environment config

streamlit.components for responsive design

📦 Installation

# Clone the repository
git clone https://github.com/your-username/cold-email-generator.git
cd cold-email-generator

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Set your OpenAI key
 "OPENAI_API_KEY=your-api-key-here" > .env

# Run the app
streamlit run app.py
🔐 Environment Variables
Create a .env file in the root directory:


OPENAI_API_KEY=your-openai-api-key
❗ Do not push .env to GitHub – it's ignored via .gitignore.

📁 Project Structure

cold-email-generator/
│
├── app.py                  # Streamlit UI logic
├── utils.py                # GPT email generation logic
├── .env                    # 🔐 Your API key (excluded from GitHub)
├── .gitignore              # Excludes .env, venv, etc.
├── requirements.txt        # Python dependencies
└── README.md               # You are here
💡 Example Use Cases
Startups reaching out to potential users

Freelancers contacting new clients

B2B sales and SaaS outreach

Product launch announcements

📄 License
MIT License
