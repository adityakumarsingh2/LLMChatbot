# 🤖 LLM Chatbot — Aditya Kumar Singh's AI Resume Chatbot

A terminal-based AI chatbot powered by **Google Gemini 2.5 Flash** that answers questions about Aditya Kumar Singh's resume, skills, projects, and experience.

---

## ✨ Features

- 🔑 Auto-prompts for your Gemini API key on first run and saves it to `.env`
- 💬 Interactive conversational loop via the terminal
- 🧠 Uses prompt engineering to constrain answers to resume-related queries only
- ⚡ Powered by `gemini-2.5-flash` — fast and free via Google AI Studio

---

## 🚀 Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/adityakumarsingh2/LLMChatbot.git
cd LLMChatbot
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
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

```bash
python chatbot.py
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
├── chatbot.py          # Main chatbot script
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
