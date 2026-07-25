import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(
    api_key=os.getenv("OPENROUTER_API_KEY"),
    base_url="https://openrouter.ai/api/v1",
)


def generate_report(prediction, confidence):
    prompt = f"""
You are an AI medical assistant.

An AI model analyzed a chest X-ray image.

Prediction: {prediction}
Confidence: {confidence:.2f}%

Generate a professional medical report with the following sections:

1. Summary
2. Interpretation
3. Possible Clinical Significance
4. Recommendations
5. Disclaimer

Keep the report concise and do not claim a definitive diagnosis.
"""

    try:
        response = client.chat.completions.create(
            model="nvidia/nemotron-3-ultra-550b-a55b:free",
            messages=[
                {
                    "role": "system",
                    "content": "You are a professional medical AI assistant.",
                },
                {
                    "role": "user",
                    "content": prompt,
                },
            ],
            temperature=0.4,
            max_tokens=500,
        )

        return response.choices[0].message.content

    except Exception as e:
        print(f"OpenRouter Error: {e}")

        return f"""
Medical AI Report

Prediction: {prediction}
Confidence: {confidence:.2f}%

The AI model successfully analyzed the uploaded chest X-ray.

⚠ AI-generated report is currently unavailable.

Recommendation:
Please consult a qualified healthcare professional for diagnosis.
"""