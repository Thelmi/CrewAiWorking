from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai_tools import SerperDevTool


# If you want to run a snippet of code before or after the crew starts, 
# you can use the @before_kickoff and @after_kickoff decorators
# https://docs.crewai.com/concepts/crews#example-crew-class-with-decorators

@CrewBase
class Builder():
	"""Builder crew"""

	# Learn more about YAML configuration files here:
	# Agents: https://docs.crewai.com/concepts/agents#yaml-configuration-recommended
	# Tasks: https://docs.crewai.com/concepts/tasks#yaml-configuration-recommended
	agents_config = 'config/agents.yaml'
	tasks_config = 'config/tasks.yaml'

	# If you would like to add tools to your agents, you can learn more about it here:
	# https://docs.crewai.com/concepts/agents#agent-tools
	@agent
	def researcher(self) -> Agent:
		return Agent(
			config=self.agents_config['researcher'],
			verbose=True,
  			allow_delegation=False,
  			tools=[SerperDevTool()],
 		 	max_iter=15
		)

	@agent
	def social_media_monitor(self) -> Agent:
		return Agent(
			config=self.agents_config['social_media_monitor'],
			verbose=True,
  			allow_delegation=False,
			tools=[SerperDevTool()],
  			max_iter=15
		)
	
	@agent
	def sentiment_analyzer(self) -> Agent:
		return Agent(
			config=self.agents_config['sentiment_analyzer'],
			verbose=True,
  			allow_delegation=False,
  			max_iter=15
		)
	
	@agent
	def report_generator(self) -> Agent:
		return Agent(
			config=self.agents_config['report_generator'],
			verbose=True,
  			allow_delegation=False,
  			max_iter=15
		)
	

	@task
	def research_task(self) -> Task:
		return Task(
			config=self.tasks_config['research_task'],
		)

	@task
	def monitoring_task(self) -> Task:
		return Task(
			config=self.tasks_config['monitoring_task'],
		)
	
	@task
	def sentiment_analysis_task(self) -> Task:
		return Task(
			config=self.tasks_config['sentiment_analysis_task'],
		)
	
	@task
	def report_generation_task(self) -> Task:
		return Task(
			config=self.tasks_config['report_generation_task'],
		)
	


	@crew
	def crew(self) -> Crew:
		"""Creates the Builder crew"""
		# To learn how to add knowledge sources to your crew, check out the documentation:
		# https://docs.crewai.com/concepts/knowledge#what-is-knowledge

		return Crew(
			agents=self.agents, # Automatically created by the @agent decorator
			tasks=self.tasks, # Automatically created by the @task decorator
			process=Process.sequential,
			verbose=True,
			# process=Process.hierarchical, # In case you wanna use that instead https://docs.crewai.com/how-to/Hierarchical/
		)
