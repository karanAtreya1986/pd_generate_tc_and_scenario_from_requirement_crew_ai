[Task] #1 - Assignment 1 — Test Case Generator Crew (Level: Beginner)

You are given a feature requirement as plain text input (e.g., "User Registration with Email Verification"). 

Build a CrewAI crew with two agents working in a sequential process. 


Agent 1 is a "Requirements Analyst" who reads the feature requirement and breaks it down into testable scenarios covering positive, negative, and edge cases. 

Agent 2 is a "Test Case Writer" who takes those scenarios and writes detailed test cases with test ID, title, pre-conditions, steps, expected result, and priority (P0–P4). 

The crew should accept any feature requirement string as input via crew.kickoff(inputs={"feature": "..."}) and produce the final test cases. 

Use Groq or OpenAI as your LLM. 

Write at least 3 pytest tests that validate your agent roles are configured correctly and your crew has exactly 2 agents running sequentially. 

Save the final output to a file using the output_file parameter on the last task.