from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
import os
from crewai import LLM
from datetime import date

llm = LLM(
    model="xai/grok-beta",
    base_url="https://api.x.ai/v1",
    api_key=os.environ['XAI_API_KEY']
)
today = str(date.today())




@CrewBase
class StockExpertsSearchCrew():
    """Stockexperts crew"""


    @agent
    def research_analyst(self) -> Agent:
        return Agent(
            config=self.agents_config['research_analyst'],
            llm=llm,
            # tools=[MyCustomTool()], # Example of custom tool, loaded on the beginning of file
            verbose=True
        )

    @agent
    def financial_analyst(self) -> Agent:
        return Agent(
            config=self.agents_config['financial_analyst'],
            llm=llm,
            verbose=True
        )

    @task
    def stock_research_task(self) -> Task:
        return Task(
            config=self.tasks_config['stock_research_task'],
            output_file='reports/md/' + today + '_search_stock_results.md'
        )

    @task
    def financial_analysis_task(self) -> Task:
        return Task(
            config=self.tasks_config['financial_analysis_task'],
            output_file='reports/md/' + today + '_search_stock_report.md'
        )

    @crew
    def crew(self) -> Crew:
        """Creates the Stockexperts crew"""
        return Crew(
            agents=self.agents,  # Automatically created by the @agent decorator
            tasks=self.tasks,  # Automatically created by the @task decorator
            process=Process.sequential,
            verbose=True,
            manager_llm=llm,
            # process=Process.hierarchical, # In case you wanna use that instead https://docs.crewai.com/how-to/Hierarchical/
        )


@CrewBase
class StockExpertsCompareCrew():
    """Stockexperts crew"""


    @agent
    def research_analyst(self) -> Agent:
        return Agent(
            config=self.agents_config['research_analyst'],
            llm=llm,
            # tools=[MyCustomTool()], # Example of custom tool, loaded on the beginning of file
            verbose=True
        )

    @agent
    def financial_analyst(self) -> Agent:
        return Agent(
            config=self.agents_config['financial_analyst'],
            llm=llm,
            verbose=True
        )

    @task
    def stock_research_task(self) -> Task:
        return Task(
            config=self.tasks_config['stocks_information_gathering'],
            output_file='reports/md/' + today + '_compare_stock_results.md'
        )

    @task
    def financial_analysis_task(self) -> Task:
        return Task(
            config=self.tasks_config['financial_analysis_task'],
            output_file='reports/md/' + today + '_compare_stock_report.md'
        )

    @crew
    def crew(self) -> Crew:
        """Creates the Stockexperts crew"""
        return Crew(
            agents=self.agents,  # Automatically created by the @agent decorator
            tasks=self.tasks,  # Automatically created by the @task decorator
            process=Process.sequential,
            verbose=True,
            manager_llm=llm,
            # process=Process.hierarchical, # In case you wanna use that instead https://docs.crewai.com/how-to/Hierarchical/
        )

