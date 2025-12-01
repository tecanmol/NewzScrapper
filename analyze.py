import os
from google.genai import types 
from google import genai
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("GEMINI_API_KEY")

client = genai.Client(api_key=API_KEY)

def analyzeContent(data):
    if not data or len(data.strip()) < 100:
        print("⚠️  Content too short or empty. Skipping analysis.")
        return

    prompt = f"""
        You are an expert new summarizer who job is to analyze the content of the following scraped webpage and output a structured summary.

        Please provide:
        1. **TL;DR**: A one-sentence summary of the main point.
        2. **Key Takeaways**: 3 distinct bullet points highlighting technical details, specific arguments, or interesting facts.
        3. **Category**: (e.g., AI, DevOps, Politics, Programming, etc.)

        for all individual webpages(title) keep the response in json format so that the summary of individual webpages can be accesed easily
        Also return the link for each article exactly as provided.
        ---
        Webpage Content:
        {data}
        """ 
    try:
        response = client.models.generate_content(
            model="gemini-2.5-flash", 
            contents=prompt,
            config=types.GenerateContentConfig(
                temperature=0.3, # Lower temperature = more factual/concise
                max_output_tokens=8000
            )
        )
        
        if response.text:
            # print("\n" + "="*40)
            # print(response.text)
            # print("="*40 + "\n")
            return response
        else:
            # Fallback: Try to grab partial text if it exists
            print("\n⚠️ The model returned no clean text. Checking candidates...")
            print(f"Reason: {response.candidates[0].finish_reason}")
            return
    except Exception as e:
        print(f"❌ Error during analysis: {e}")
