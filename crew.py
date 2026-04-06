from crewai import Agent, LLM ,Task ,Crew,Process
import os
from dotenv import load_dotenv

load_dotenv()
# Step 0 - set the llm. brain
llm = LLM(
    model="groq/llama-3.3-70b-versatile",
    api_key=os.getenv("GROQ_API_KEY")
)

# Store the feature required here 
result =""



# =========================
# ENTRY FUNCTION
# =========================
def run(feature: str):
    return crew.kickoff(inputs={"feature": feature})



# =========================
# AGENT 1: Requirements Analyst
# =========================
requirements_analyst = Agent(
    role="Requirements Analyst",
    goal="Break feature requirements into structured, testable scenarios",
    backstory=(
        "You are an expert QA analyst skilled at interpreting product requirements "
        "and converting them into clear, structured test scenarios including positive, "
        "negative, and edge cases."
    ),
    llm=llm,
    verbose=True
)

# =========================
# AGENT 2: Test Case Writer
# =========================
test_case_writer = Agent(
    role="Test Case Writer",
    goal="Convert scenarios into detailed, structured test cases",
    backstory=(
        "You are a QA engineer who writes highly detailed and structured test cases "
        "with IDs, steps, expected results, and priorities."
    ),
    llm=llm,
    verbose=True
)

# =========================
# TASK 1: Generate Scenarios
# =========================
scenario_task = Task(
    description=(
        "Given the following feature requirement:\n\n"
        "{feature}\n\n"
        "Break it into structured test scenarios covering:\n"
        "- Positive cases\n"
        "- Negative cases\n"
        "- Edge cases\n\n"
        "Return scenarios in a clean bullet list grouped by category."
    ),
    expected_output="Structured test scenarios categorized as positive, negative, and edge cases.",
    agent=requirements_analyst,
    output_file="test_scenarios_output.txt"
)

# =========================
# TASK 2: Generate Test Cases
# =========================
testcase_task = Task(
    description=(
        "Using the provided scenarios, create detailed test cases.\n\n"
        "Each test case must include:\n"
        "- Test ID\n"
        "- Title\n"
        "- Preconditions\n"
        "- Steps\n"
        "- Expected Result\n"
        "- Priority (P0–P4)\n\n"
        "Ensure clarity and completeness."
    ),
    expected_output="A complete list of structured test cases.",
    agent=test_case_writer,
    output_file="test_cases_output.txt"
)

# =========================
# CREW DEFINITION
# =========================
crew = Crew(
    agents=[requirements_analyst, test_case_writer],
    tasks=[scenario_task, testcase_task],
    process=Process.sequential,
    verbose=True
)


if __name__ == "__main__":
    # Call the function 
    result = run("User Registration with Email Verification")
    print(result)