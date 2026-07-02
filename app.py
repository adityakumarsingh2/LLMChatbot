import os
import streamlit as st
from google import genai
from dotenv import load_dotenv

# Load environment variables from .env if present
load_dotenv()

# ----------------------------
# 1. Page Configuration
# ----------------------------
st.set_page_config(
    page_title="Resume AI Assistant",
    page_icon="🤖",
    layout="wide"
)

# ----------------------------
# Premium Custom Styling (Aesthetics)
# ----------------------------
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Outfit:wght@300;400;600;700&display=swap');
    
    /* Global Typography & Font Styling */
    html, body, [class*="css"] {
        font-family: 'Outfit', sans-serif;
    }
    
    /* Header styling with modern gradient text */
    .title-container {
        padding: 1.5rem 0rem;
        text-align: left;
    }
    .main-title {
        background: linear-gradient(135deg, #4f46e5 0%, #7c3aed 50%, #db2777 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        font-size: 3rem;
        font-weight: 700;
        margin: 0;
        padding-bottom: 0.5rem;
    }
    .subtitle {
        color: #64748b;
        font-size: 1.2rem;
        font-weight: 400;
    }
    
    /* Sidebar premium glassmorphism styling */
    [data-testid="stSidebar"] {
        background: linear-gradient(180deg, rgba(15, 23, 42, 0.95) 0%, rgba(30, 41, 59, 0.95) 100%) !important;
        backdrop-filter: blur(12px);
        border-right: 1px solid rgba(255, 255, 255, 0.05);
    }
    
    /* Custom chat bubbles styling */
    .stChatMessage {
        border-radius: 16px;
        padding: 15px 20px;
        margin-bottom: 12px;
        border: 1px solid rgba(255, 255, 255, 0.05);
        box-shadow: 0 4px 15px rgba(0, 0, 0, 0.05);
        transition: transform 0.2s ease, box-shadow 0.2s ease;
    }
    .stChatMessage:hover {
        transform: translateY(-1px);
        box-shadow: 0 6px 20px rgba(0, 0, 0, 0.1);
    }
    
    /* Styling for different roles */
    div[data-testid="stChatMessage"] {
        background-color: rgba(248, 250, 252, 0.6);
    }
    
    .sidebar-card {
        background: rgba(255, 255, 255, 0.03);
        border: 1px solid rgba(255, 255, 255, 0.08);
        border-radius: 12px;
        padding: 15px;
        margin-bottom: 15px;
    }
    
    /* Animated links */
    .contact-link {
        color: #818cf8;
        text-decoration: none;
        transition: color 0.2s ease;
        display: inline-block;
        margin-right: 15px;
    }
    .contact-link:hover {
        color: #a5b4fc;
        text-decoration: underline;
    }
</style>
""", unsafe_allow_html=True)

# ----------------------------
# Sidebar Configuration & Resume Options
# ----------------------------
with st.sidebar:
    st.markdown('<div class="sidebar-card">', unsafe_allow_html=True)
    st.image("https://img.icons8.com/color/96/artificial-intelligence.png", width=70)
    st.subheader("Configuration Panel")
    st.markdown('</div>', unsafe_allow_html=True)

    # Allow toggling between Aditya and Mukund Kumar
    profile = st.selectbox(
        "Choose Resume Assistant Profile",
        ["Aditya Kumar Singh (Default)", "Mukund Kumar (Tutorial Profile)"]
    )
    
    st.markdown("---")

    # API Key check and input fallback
    # Look for API key in env or .env file first
    env_api_key = os.getenv("GEMINI_API_KEY")
    
    if env_api_key:
        st.success("🔑 Gemini API Key loaded from `.env` file.")
        API_KEY = env_api_key
    else:
        st.warning("⚠️ No API Key found in `.env` environment.")
        # User input box for API Key
        API_KEY = st.text_input("Enter your Gemini API Key:", type="password", help="Get a free key from Google AI Studio")
        if not API_KEY:
            st.info("Please enter your API Key to enable chat functions.")

    st.markdown("---")
    st.markdown("### Profile Summary")

# ----------------------------
# 2. Resume Data Configuration
# ----------------------------
# Resume Data for Aditya Kumar Singh
aditya_data = """
==================================================================
RESUME OF ADITYA KUMAR SINGH
==================================================================

CONTACT DETAILS:
- Name: Aditya Kumar Singh
- Email: adityakumarsingh909@outlook.com
- Mobile: +91 7654944940
- LinkedIn: linkedin.com/in/adityakumarsingh2
- GitHub: github.com/adityakumarsingh2
- Portfolio/Website: adityakumaronline.netlify.app

SKILLS:
- Languages: C/C++, Java, JavaScript, PHP
- Frameworks & Libraries: HTML and CSS, Tailwind CSS, React.js, Node.js, Express.js
- Tools & Platforms: MySQL, Git, GitHub, MongoDB Compass, Postman, VS Code, XAMPP, Netlify, Supabase
- Core CS Fundamentals: Data Structures and Algorithms (DSA), Operating Systems, Computer Networks, OOPs, DBMS
- Soft Skills: Problem-Solving, Teamwork, Leadership, Discipline, Resilience, Adaptability

FREELANCE EXPERIENCE:
1. Freelancer | Fit Kart, Begusarai (Nov 2025 - Dec 2025)
   - Project: Fit Kart (Full-stack e-commerce platform with AI try-on)
   - Key Responsibilities & Achievements:
     * Delivered full-stack platform enabling 1,000+ users to explore products, receive size recommendations, and complete purchases.
     * Handled secure authentication, real-time order tracking, wish list management, and Stripe payments, reducing checkout drop-offs by 35% and improving user engagement by 45%.
     * Followed modular architecture and reusable component design to improve scalability and maintainability.
   - Technologies: React.js, JavaScript, Supabase (Auth & Database), Stripe API, Netlify, Git, Express.js

2. Freelancer | Shanti Brick Field, Kannauj (Mar 2025 - Apr 2025)
   - Project: Company Website for Shanti Brick Field
   - Key Responsibilities & Achievements:
     * Designed a responsive company website featuring product listings, gallery slideshow, contact and purchase request forms.
     * Integrated secure backend functionality using PHP and MySQL, including form handling, file/image uploads, and database-driven product management.
     * Published the website on a custom subdomain via shared cPanel hosting (InfinityFree) with PHPMailer-based email notifications.
   - Technologies: HTML and CSS, JavaScript, jQuery, PHP, MySQL, PHPMailer

PROJECTS:
1. Confess It (Jan 2026 - Apr 2026)
   - Description: A full-stack anonymous social media platform using the MERN stack, enabling users to share confessions and interact securely without revealing their identity.
   - Key Responsibilities & Achievements:
     * Implemented Google OAuth 2.0 authentication with Passport.js and protected REST APIs, reducing unauthorized access risks by 100% through secure session-based authorization.
     * Streamlined backend services and MongoDB Atlas queries, improving API response time by 35% and handling 1,000+ API requests with scalable architecture.
     * Deployed the frontend on Vercel, backend on Render, and cloud database on MongoDB Atlas, ensuring reliable and scalable production hosting.
   - Technologies: MERN Stack, Google OAuth, MongoDB Atlas, Passport.js, Vercel, Render

2. Personal Portfolio (Dec 2025 - Jan 2026)
   - Description: A modern, responsive portfolio website to showcase full-stack skills and projects, featuring dark/light mode, smooth animations, a custom magnetic cursor, and real-time LeetCode statistics integration.
   - Key Responsibilities & Achievements:
     * Optimized the website for SEO using structured metadata and sitemaps, achieving Google indexing and tracking 1,000+ visits via Google Analytics.
     * Hosted the portfolio on a custom domain using Netlify with Cloudflare as the DNS provider.
   - Technologies: React.js, Tailwind CSS, SEO, Netlify, Cloudflare, Google Analytics

CERTIFICATIONS:
- Cloud Computing | NPTEL (Nov 2025)
- Demystifying Networking | NPTEL (Sep 2025)
- Oracle Cloud Infrastructure 2025 Certified Foundation Associate | Oracle (Aug 2025)

ACHIEVEMENTS:
- Obtained a rank of 1543 among 30.7k+ participants in LeetCode Weekly Contest 470 (Oct 2025).
- Attained a top 10 rank among 3.5k+ participants in CODE-A-HUNT hackathon, LPU (Mar 2024).
- Secured 1st position at KVS Regional Boxing Championship, West Bengal, showcasing discipline, resilience, and strong decision-making under pressure (Oct 2019).

EDUCATION:
1. Lovely Professional University (Phagwara, Punjab)
   - Degree: Bachelor of Technology - Computer Science and Engineering
   - CGPA: 7.43
   - Duration: Apr 2023 - Present
2. Kendriya Vidyalaya (Island Grounds, Chennai)
   - Intermediate (Class 12)
   - Percentage: 71.2%
   - Duration: Apr 2022 - Mar 2023
3. Kendriya Vidyalaya No. 1 (Nausenabaugh, Visakhapatnam)
   - Matriculation (Class 10)
   - Percentage: 86%
   - Duration: Apr 2020 - Mar 2021
"""

# Resume Data for Mukund Kumar
mukund_data = """
==================================================================
RESUME OF MUKUND KUMAR
==================================================================

CONTACT DETAILS:
- Name: Mukund Kumar
- Email: mukund.kumar@example.com
- Mobile: +91 9876543210
- LinkedIn: linkedin.com/in/mukundkumar
- GitHub: github.com/mukundkumar

SKILLS:
- Languages: Python, JavaScript, HTML/CSS, SQL
- Frameworks & Libraries: Streamlit, FastAPI, React
- Tools & Platforms: Git, Docker, Google Cloud Platform (GCP)
- Areas of Interest: Artificial Intelligence, Web Development, Data Science

EXPERIENCE & PROJECTS:
1. AI Research Intern | TechCorp (2025 - Present)
   - Built several NLP-based chatbot assistants and document analysis tools.
   - Deployed LLM pipelines using FastAPI and Streamlit.
2. Web Developer | Freelance
   - Designed responsive portfolio websites and simple dashboards.
"""

# Determine selected profile details
if profile.startswith("Aditya"):
    my_data = aditya_data
    profile_name = "Aditya Kumar Singh"
    page_title_heading = "Aditya AI Resume Assistant"
    st.sidebar.markdown(f"""
    **Name**: Aditya Kumar Singh  
    **Role**: Full-Stack Developer  
    **Skills**: React.js, Node.js, C++, Java  
    
    [LinkedIn](https://linkedin.com/in/adityakumarsingh2) | [GitHub](https://github.com/adityakumarsingh2)
    """)
else:
    my_data = mukund_data
    profile_name = "Mukund Kumar"
    page_title_heading = "Mukund AI Resume Assistant"
    st.sidebar.markdown(f"""
    **Name**: Mukund Kumar  
    **Role**: AI & Web Developer  
    **Skills**: Python, Streamlit, FastAPI  
    
    [LinkedIn](https://linkedin.com/in/mukundkumar) | [GitHub](https://github.com/mukundkumar)
    """)

# ----------------------------
# 3. Page Header
# ----------------------------
st.markdown(f"""
<div class="title-container">
    <h1 class="main-title">✨ {page_title_heading}</h1>
    <p class="subtitle">Ask me anything about {profile_name} or ask any general question.</p>
</div>
""", unsafe_allow_html=True)

# ----------------------------
# 4. Check Chat History & Create Empty Chat List
# ----------------------------
if "messages" not in st.session_state:
    st.session_state.messages = []

# Show previous messages stored in history
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# ----------------------------
# 5. User Input
# ----------------------------
question = st.chat_input("Type your question here...")

if question:
    # Save & display user message
    st.session_state.messages.append({"role": "user", "content": question})
    with st.chat_message("user"):
        st.markdown(question)
        
    # Build prompt instructions
    prompt = f"""
You are {profile_name}'s AI Assistant.
Rules:
1. Answer using the resume if possible.
2. Otherwise answer using general knowledge.
3. Keep answers simple.

Resume Data:
{my_data}

Question:
{question}
"""
    
    # ----------------------------
    # 6. API Client & Inference
    # ----------------------------
    if not API_KEY:
        answer = "Error: API Key is required. Please check your `.env` file or provide the key in the sidebar."
        st.session_state.messages.append({"role": "assistant", "content": answer})
        with st.chat_message("assistant"):
            st.markdown(answer)
    else:
        try:
            # Create Gemini Client and call models API
            client = genai.Client(api_key=API_KEY)
            response = client.models.generate_content(
                model="gemini-2.5-flash",
                contents=prompt
            )
            answer = response.text
        except Exception as e:
            answer = f"Error communicating with Gemini API: {e}"
            
        # Save and display bot response
        st.session_state.messages.append({"role": "assistant", "content": answer})
        with st.chat_message("assistant"):
            st.markdown(answer)
