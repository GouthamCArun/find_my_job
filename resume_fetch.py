import openai
import pdfplumber
import json
import os
# Function to extract text from a PDF file
def extract_text_from_pdf(pdf_path):
    try:
        with pdfplumber.open(pdf_path) as pdf:
            text = ""
            for page in pdf.pages:
                text += page.extract_text()
        return text
    except Exception as e:
        raise ValueError(f"Error reading PDF: {e}")

# Function to extract details from resume using OpenAI
def extract_details_from_resume(resume_text):
    # Set OpenAI API key
    openai.api_key = openai.api_key = os.getenv("OPENAI_API_KEY")
    
    # Messages for OpenAI Chat API
    messages = [
        {"role": "system", "content": "You are an assistant that extracts details from resumes."},
        {"role": "user", "content": f"Analyze the following resume and extract the following details as a JSON object:\n"
                                     f"1. Key skills\n"
                                     f"2. Preferred job titles\n"
                                     f"3. Experience level (Entry, Associate, Mid, Senior)\n"
                                     f"4. Preferred industries (if mentioned)\n"
                                     f"5. Location preferences (if mentioned)\n\n"
                                     f"Resume:\n{resume_text}\n\n"
                                     f"Output JSON with keys: skills, job_titles, experience_level, industries, location."}
    ]
    
    try:
        # Call OpenAI Chat API
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",  # Use "gpt-4" for more advanced responses
            messages=messages,
            max_tokens=300,
            temperature=0.7
        )
        
        # Extract the response content
        extracted_details = response['choices'][0]['message']['content'].strip()
        
        # Clean up the response
        cleaned_str = extracted_details.lstrip("```json\n").rstrip("```")
        
        # Parse the cleaned response as JSON and return it
        return json.loads(cleaned_str)
    except json.JSONDecodeError as e:
        raise ValueError(f"Error decoding JSON from OpenAI response: {e}")
    except Exception as e:
        raise ValueError(f"Error extracting details from OpenAI API: {e}")

