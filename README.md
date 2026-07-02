# 🤖 LLM Chatbot — Aditya Kumar Singh's AI Resume Chatbot

A terminal-based AI chatbot powered by **Google Gemini 2.5 Flash** that answers questions about Aditya Kumar Singh's resume, skills, projects, and experience.

---

## ✨ Features

- 🔑 **Auto-prompts for API Key**: Prompts for your Gemini API key on the first run and automatically saves it to a `.env` file for future runs.
- 💬 **Interactive Terminal Loop**: Chat directly with the assistant through a command-line interface.
- 🧠 **Engineered Prompt & System Rules**:
  - *Context Priority*: Answers questions regarding Aditya's education, skills, projects, internships, certifications, achievements, or experience using the resume database.
  - *General Knowledge Fallback*: If the question is outside the scope of the resume, the chatbot answers using its general knowledge.
  - *Tone Constraint*: Programmed to be concise and helpful.
- ⚡ **Gemini 2.5 Flash**: Powered by the latest, fast `gemini-2.5-flash` model.

---

## 🚀 Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/adityakumarsingh2/LLMChatbot.git
cd LLMChatbot
```

### 2. Install Dependencies

Install the requirements (we use the `--user` flag to prevent permission and file-locking errors on Windows):
```bash
pip install -r requirements.txt --user
```

### 3. Set Up Your API Key

Get a **free** Gemini API key from [Google AI Studio](https://aistudio.google.com/).

You can either:
- Create a `.env` file manually:
  ```
  GEMINI_API_KEY=your_api_key_here
  ```
- Or just **run the chatbot** — it will prompt you to enter the key and save it automatically.

### 4. Run the Chatbot

You can run either the terminal-based chatbot or the modern Streamlit web application:

#### Terminal-based Chatbot
```bash
python chatbot.py
```

#### Streamlit Web Application (Premium Interface)
```bash
# Run the Streamlit app
streamlit run app.py
```

---

## 💬 Example Usage

```
You: What are Aditya's skills?
Bot: Aditya is proficient in C/C++, Java, JavaScript, PHP...

You: Tell me about his projects.
Bot: Aditya has worked on Confess It, a full-stack anonymous social media platform...

You: exit
Bot: Goodbye!
```

---

## 📁 Project Structure

```
LLMChatbot/
├── app.py              # Streamlit Web App (Premium Interface)
├── chatbot.py          # Terminal-based chatbot script
├── requirements.txt    # Python dependencies
├── .gitignore          # Git ignore rules
├── .env                # Your API key (NOT committed to git)
└── README.md           # This file
```

---

## 🛠️ Tech Stack

| Tool | Purpose |
|------|---------|
| Python | Core language |
| Google Gemini 2.5 Flash | LLM backend |
| `google-genai` | Google GenAI SDK |
| `python-dotenv` | Environment variable management |

---

## ⚠️ Important Notes

- **Never commit your `.env` file** — it's in `.gitignore` for this reason.
- The chatbot is constrained via prompt engineering to only answer resume-related questions.

---

## 👤 Author

**Aditya Kumar Singh**  
📧 adityakumarsingh909@outlook.com  
🔗 [LinkedIn](https://linkedin.com/in/adityakumarsingh2) | [GitHub](https://github.com/adityakumarsingh2) | [Portfolio](https://adityakumaronline.netlify.app)
