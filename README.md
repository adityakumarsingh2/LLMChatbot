# 🤖 LLM Chatbot — Aditya Kumar Singh's AI Resume Assistant

A modern AI chatbot application featuring both a terminal interface and a stunning Streamlit web application. Powered by **Google Gemini 2.5 Flash**, it is designed to interactively answer questions about Aditya Kumar Singh's resume, skills, projects, and professional experience.

---

## ✨ Features

### 🌐 Web Application Interface (Streamlit Upgrade)
- 🎨 **Premium Aesthetics**: Styled with a custom font (`Outfit`), linear purple-pink headers, and interactive elements.
- 🧊 **Glassmorphism Sidebar**: Premium glassmorphic panel detailing a quick biography, active developer profile, and social links.
- 🔑 **Dynamic Configuration**: Seamlessly loads your `GEMINI_API_KEY` from the environment/`.env` file, with a clean interactive password input fallback in the sidebar if not set.
- 💬 **Interactive Chat Interface**: Styled chat bubbles with subtle hover animations, handling chat history natively in `st.session_state`.

### 💻 Terminal Command Line Interface (CLI)
- 🔑 **Auto-prompts for API Key**: Prompts for your Gemini API key on the first run and saves it to a local `.env` file automatically.
- 💬 **Interactive Terminal Loop**: Direct connection and messaging loop via standard console output.

### 🧠 Under the Hood
- 🚀 **Gemini 2.5 Flash**: Leverages Google's latest fast, cost-efficient `gemini-2.5-flash` model.
- 🛡️ **Engineered Prompt Constraints**: Custom rules ensuring context priority, fallback responses for general questions, and a helpful, concise tone.

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
| Python | Core backend programming language |
| Streamlit | Modern responsive web application framework |
| Google Gemini 2.5 Flash | Large Language Model (LLM) backend |
| `google-genai` | Official Google GenAI SDK |
| `python-dotenv` | Automatic environment variable loading |

---

## ⚠️ Important Notes

- **Never commit your `.env` file** — it's in `.gitignore` for this reason.
- The chatbot is constrained via prompt engineering to only answer resume-related questions.

---

## 👤 Author

**Aditya Kumar Singh**  
📧 adityakumarsingh909@outlook.com  
🔗 [LinkedIn](https://linkedin.com/in/adityakumarsingh2) | [GitHub](https://github.com/adityakumarsingh2) | [Portfolio](https://adityakumaronline.netlify.app)
