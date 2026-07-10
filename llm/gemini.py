from transformers import pipeline

# Load the model once when the application starts
generator = pipeline(
    "text-generation",
    model="TinyLlama/TinyLlama-1.1B-Chat-v1.0"
)

def analyze_resume(resume_text, category):
    prompt = f"""
You are an expert HR recruiter.

Resume Category: {category}

Resume:
{resume_text}

Provide:
1. Resume Summary
2. Top Skills
3. Candidate Strengths
4. Candidate Weaknesses
5. 5 Interview Questions
6. Career Recommendation
"""

    result = generator(
        prompt,
        max_new_tokens=300,
        do_sample=False
    )

    # Return only the generated part
    return result[0]["generated_text"]