import os
import sys
from dotenv import load_dotenv

# Try to load environment variables from a .env file
load_dotenv()

# Check for Gemini API key
api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    print("=" * 60)
    print("Welcome to Aditya's AI Resume Chatbot!")
    print("=" * 60)
    print("To get started, you need a Gemini API Key.")
    print("You can get one for free at: https://aistudio.google.com/")
    print("-" * 60)
    user_key = input("Enter your GEMINI_API_KEY: ").strip()
    if not user_key:
        print("Error: API Key is required to run the chatbot. Exiting.")
        sys.exit(1)
    
    # Save the key to a .env file for convenience
    try:
        with open(".env", "w") as f:
            f.write(f"GEMINI_API_KEY={user_key}\n")
        print("\n[+] API Key saved to .env file for future runs.")
        api_key = user_key
    except Exception as e:
        print(f"\n[!] Warning: Could not save API key to .env file: {e}")
        api_key = user_key

# Now import genai and initialize the client
try:
    from google import genai
except ImportError:
    print("\n[!] Error: 'google-genai' library not found.")
    print("Please install the dependencies first using:")
    print("  pip install -r requirements.txt")
    sys.exit(1)

try:
    client = genai.Client(api_key=api_key)
except Exception as e:
    print(f"\n[!] Error initializing Gemini client: {e}")
    sys.exit(1)

# Aditya Kumar Singh's Resume Data (from Resume PDF)
my_data = """
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

print("\n" + "=" * 60)
print("Aditya Kumar Singh's AI Resume Chatbot Started...")
print("Type 'exit' to quit.")
print("=" * 60 + "\n")

while True:
    try:
        question = input("You: ")
    except (KeyboardInterrupt, EOFError):
        print("\nBot: Goodbye!")
        break
        
    if question.lower().strip() == "exit":
        print("Bot: Goodbye!")
        break
        
    if not question.strip():
        continue
        
    # Constructing prompt according to Slide 12 instructions (Prompt Engineering)
    prompt = f"""
You are Aditya Kumar Singh's personal AI assistant.
Use ONLY the information below to answer questions. If the question cannot be
answered using the provided information, politely state that you can only answer 
questions about Aditya's resume, projects, skills, education, and experience.

Information:
{my_data}

Question:
{question}
"""

    try:
        # Generate content using Gemini 2.5 Flash as instructed in Slide 14
        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt
        )
        print(f"\nBot: {response.text}\n")
        #save chat history
        with open("chat_history.txt", "a",encoding="utf-8") as file:
            file.write(f"User: {question}\n")
            file.write(f"Bot: {response.text}\n")
            file.write("-"*50+"\n")
    except Exception as e:
        print(f"\nBot: Error generating response: {e}\n")


