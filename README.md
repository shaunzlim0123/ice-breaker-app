# Ice Breaker App

## Project Overview
Ice Breaker is a web application that generates personalized conversation starters. Simply enter a name, and the app will fetch the person’s LinkedIn and Twitter details, then use langchain agents to generate a brief summary, interesting facts, icebreaker questions, and topics of interest.

## Features
- **Automatic Profile Lookup:** Finds LinkedIn and Twitter profiles based on the provided name.
- **AI-Generated Insights:** Produces a concise professional summary, highlights, and fun icebreaker questions.
- **User-Friendly Interface:** Clean, single-page design with instant results.
- **Profile Display:** Shows the person’s profile picture (if available).

## Installation
1. **Clone the Repository:**
   ```bash
   git clone https://github.com/shaunzlim0123/ice_breaker-app.git
   cd ice_breaker-app
   ```
2. **Set Up a Virtual Environment (Optional but Recommended):**
   ```bash
   python3 -m venv venv
   source venv/bin/activate   # Windows: venv\Scripts\activate
   ```
3. **Install Dependencies:**
   ```bash
   pip install -r requirements.txt
   ```
4. **Configure API Keys:**  
   Create a `.env` file in the project root with the following keys:
   - `OPENAI_API_KEY`
   - `SCRAPIN_API_KEY`
   - `TAVILY_API_KEY`
   - `TWITTER_API_KEY`
   - `TWITTER_API_KEY_SECRET`
   - `TWITTER_BEARER_TOKEN`
   - `TWITTER_ACCESS_TOKEN`
   - `TWITTER_ACCESS_TOKEN_SECRET`

5. **Run the App:**
   ```bash
   python app.py
   ```
   The app will be available at `http://localhost:5000`.

## Usage
1. **Enter a Name:** Navigate to the homepage and type the full name of the person.
2. **Generate Results:** Click the **"Do Your Magic"** button. The app will fetch profile data and generate insights.
3. **View Output:** The page will display the profile picture, a summary, interesting facts, icebreaker questions, and topics of interest.

## Technologies Used
- **Python & Flask:** Backend server and routing.
- **LangChain & OpenAI:** AI for generating summaries and questions.
- **APIs:** Uses external APIs (Scrapin, Tavily, and Twitter) to retrieve profile data.

## Demo
![ice_breaker_demo_img](https://github.com/user-attachments/assets/5554b749-bba1-4242-b18c-aadbf46bb994)

## License
This project is licensed under the **Apache License 2.0**. See the [LICENSE](LICENSE) file for details.

---

Happy networking and enjoy using Ice Breaker!
