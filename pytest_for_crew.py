import pytest
from crew import crew, requirements_analyst, test_case_writer
from crewai import Process


# =========================
# TEST 1: Agent Roles
# =========================
def test_agent_roles():
    assert requirements_analyst.role == "Requirements Analyst"
    assert test_case_writer.role == "Test Case Writer"


# =========================
# TEST 2: Crew Agent Count
# =========================
def test_crew_has_two_agents():
    assert len(crew.agents) == 2


# =========================
# TEST 3: Sequential Process
# =========================
def test_crew_process_sequential():
    assert crew.process == Process.sequential


# =========================
# TEST 4: Task Assignment
# =========================
def test_tasks_assigned_correctly():
    assert crew.tasks[0].agent == requirements_analyst
    assert crew.tasks[1].agent == test_case_writer


# =========================
# TEST 5: Output File Config
# =========================
def test_output_file_set():
    assert crew.tasks[1].output_file == "test_cases_output.txt"