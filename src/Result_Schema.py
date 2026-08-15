from pydantic import BaseModel, Field


# ==============================================
# CREATING A CLASS CONTAINING PYDANTIC FEATURES
# ==============================================   


class ResultSchema(BaseModel):
    summary: str = Field(description = "You are an expert product analyst. Summarize the following customer review in 1-2 concise sentences. Focus on the main takeaway and overall satisfaction.")

    sentiment: str = Field(description = "Analyze the sentiment of the following review with one line of the explanation of why.")

    pros: list[str] = Field(description = "Extract only the positive aspects (Pros) from the following review. If there are no pros, reply with 'No positive aspects mentioned.' Do not add any introductory text.")

    cons: list[str] = Field(description = "Extract only the negative complaints or weaknesses (Cons) from the following review. If there are no cons, reply with 'No negative aspects mentioned.' Do not add any introductory text.")