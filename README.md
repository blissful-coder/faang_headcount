# FAANG Headcount Analysis Project

## Description

This project demonstrates a simple agentic approach to analyze the combined headcount of FAANG companies (Facebook, Apple, Amazon, Netflix, Google) in 2024. It uses a supervisor agent to orchestrate the tasks of three specialized agents:

*   **Research Agent:** Searches the internet for the headcount of each FAANG company.
*   **Math Agent:** Calculates the combined headcount of all FAANG companies.
*   **Poet Agent:** Writes a poem about the combined headcount.

## Functionalities

The project performs the following steps:

1.  The supervisor agent instructs the research agent to find the headcount of each FAANG company in 2024.
2.  The supervisor agent then instructs the math agent to calculate the total headcount based on the research agent's findings.
3.  Finally, the supervisor agent instructs the poet agent to write a poem about the combined headcount.

The project uses the `graphviz` library to visualize the agent interactions.

## Development Configuration

### Dependencies

*   graphviz

### Setup

1.  Install the required dependencies:

    ```bash
    pip install graphviz
    ```

2.  Ensure that Graphviz is installed on your system. You may need to download and install it separately from the Graphviz website: [https://graphviz.org/download/](https://graphviz.org/download/)

3.  Run the `supervisor.py` script:

    ```bash
    python faang_headcount/supervisor.py
    ```

## Agentic Approach

This project demonstrates a basic agentic approach where a supervisor agent coordinates the tasks of multiple specialized agents. Each agent has a specific responsibility, and the supervisor agent orchestrates their interactions to achieve a common goal.

*   **Supervisor Agent:** The `supervisor.py` script acts as the supervisor agent. It defines the overall workflow and delegates tasks to the other agents.
*   **Research Agent:** The `research_agent.py` script defines the research agent, which is responsible for searching the internet for information. Currently, it uses a placeholder function that returns a dummy search result.
*   **Math Agent:** The `math_agent.py` script defines the math agent, which is responsible for performing mathematical calculations. It provides a simple `add` function to calculate the sum of two numbers.
*   **Poet Agent:** The `poet_agent.py` script defines the poet agent, which is responsible for writing poems. Currently, it uses a placeholder function that returns a simple poem.

This example showcases how an agentic approach can be used to break down a complex problem into smaller, more manageable tasks that can be handled by specialized agents.
