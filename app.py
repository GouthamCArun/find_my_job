import resume_fetch
import find_jobs

# Main function to extract and display job search details
if __name__ == "__main__":
    # Path to the resume PDF file
    resume_pdf_path = "Hari Narayan Resume N.pdf"  # Replace with your actual PDF file path

    try:
        # Extract text from the resume PDF
        resume_text = resume_fetch.extract_text_from_pdf(resume_pdf_path)
    except ValueError as e:
        print(f"Failed to read the resume PDF: {e}")
        exit()

    try:
        # Extract job search details and print the JSON result
        job_search_details = resume_fetch.extract_details_from_resume(resume_text)
        print("Skill details : ",job_search_details)
        result=find_jobs.find_jobs(job_search_details['skills'])
        # print(result)
        print("\n=== Job Listings ===\n")
        for i, job in enumerate(result, start=1):
            print(f"Job {i}:")
            print(f"  Title   : {job.get('title', 'N/A')}")
            print(f"  Company : {job.get('company', 'N/A')}")
            print(f"  URL     : {job.get('url', 'N/A')}")
            print("-" * 40)
         # This will print the final extracted JSON details
    except ValueError as e:
        print(f"Failed to extract details from resume: {e}")
