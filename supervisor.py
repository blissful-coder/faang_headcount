import graphviz
from math_agent import add
from research_agent import search_internet
from poet_agent import write_poem

def solve_problem(problem):
    # Create a Digraph object
    dot = graphviz.Digraph(comment='FAANG Headcount Analysis')

    # Add nodes for each agent
    dot.node('math', 'Math Agent')
    dot.node('research', 'Research Agent')
    dot.node('poet', 'Poet Agent')
    dot.node('supervisor', 'Supervisor')

    # 1. Research the headcount of each FAANG company in 2024
    dot.edge('supervisor', 'research', label='Search Headcount')
    faang_companies = ["Facebook", "Apple", "Amazon", "Netflix", "Google"]
    headcounts = {}
    for company in faang_companies:
        query = f"{company} headcount 2024"
        search_results = search_internet(query)
        # Extract headcount from search results (this is a placeholder)
        headcount = 100000  # Placeholder value
        headcounts[company] = headcount

    # 2. Calculate the combined headcount
    dot.edge('supervisor', 'math', label='Add Headcount')
    total_headcount = 0
    for company, headcount in headcounts.items():
        total_headcount = add(total_headcount, headcount)

    # 3. Write a poem about the combined headcount
    dot.edge('supervisor', 'poet', label='Write Poem')
    poem = write_poem(f"The combined headcount of FAANG companies in 2024: {total_headcount}")

    # Render the graph to a file
    dot.render('faang_headcount_graph.gv', view=False)

    return f"The combined headcount of FAANG companies in 2024 is {total_headcount}.\n\n{poem}"

if __name__ == "__main__":
    problem = "what's the combined headcount of the FAANG companies in 2024?"
    solution = solve_problem(problem)
    print(solution)
