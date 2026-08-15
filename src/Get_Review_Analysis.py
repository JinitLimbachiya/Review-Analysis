from langchain_google_genai import ChatGoogleGenerativeAI
from Result_Schema import ResultSchema
from dotenv import load_dotenv

load_dotenv()


# ==================================================
# GETTING PYDANTIC OBJECT AS A RESULT OF THE REVIEW 
# ==================================================    


def get_review_result(result_option_btn, review_prompt):
    model = ChatGoogleGenerativeAI(model = "gemini-3.6-flash")
    structured_output = model.with_structured_output(ResultSchema)

    response = structured_output.invoke(review_prompt)

    if result_option_btn.lower() == "summary":
        return response.summary
    
    elif result_option_btn.lower() == "sentiment":
        return response.sentiment
    
    elif result_option_btn.lower() == "pros":
        return response.pros
    
    elif result_option_btn.lower() == "cons":
        return response.cons
    
    else:
        print("Click any of the given button")