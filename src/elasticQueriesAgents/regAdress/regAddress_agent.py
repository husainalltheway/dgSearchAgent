import os
from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task

@CrewBase
class RegAddressCrew:
    """Reg Address Search Agent Of Companies """
    
    task_config = "config/tasks.yaml"
    agent_config = "config/agents.yaml"
    
    @agent
    def regAddress_agent(self)-> Agent:
        return Agent(
            config= self.agent_config["regAddress_agent"],
            tools= [],
            verbose= True
        )
        
    @task
    def search_address_task(self) -> Task:
        return Task(
            config=self.task_config["search_address_task"],
            agent=self.regAddress_agent()
        )
