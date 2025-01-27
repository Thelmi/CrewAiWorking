from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai_tools import SerperDevTool

@CrewBase
class Builder():
	"""Builder crew"""

	agents_config = 'config/agents.yaml'
	tasks_config = 'config/tasks.yaml'

	@agent
	def researcher(self) -> Agent:
		return Agent(
			config=self.agents_config['researcher'],
			# verbose=True,
			verbose=False,
  			allow_delegation=False,
  			tools=[SerperDevTool()],
 		 	max_iter=1
		)

	@agent
	def market_researcher(self) -> Agent:
		return Agent(
			config=self.agents_config['market_researcher'],
			# verbose=True,
			verbose=False,
  			allow_delegation=False,
			tools=[SerperDevTool()],
  			max_iter=1
		)
	
	@agent
	def social_media_researcher(self) -> Agent:
		return Agent(
			config=self.agents_config['social_media_researcher'],
			# verbose=True,
			verbose=False,
  			allow_delegation=False,
			tools=[SerperDevTool()],
  			max_iter=1
		)
	
	@agent
	def sentiment_analyzer(self) -> Agent:
		return Agent(
			config=self.agents_config['sentiment_analyzer'],
			verbose=True,
  			allow_delegation=False,
  			max_iter=1
		)
	
	@agent
	def sales_researcher(self) -> Agent:
		return Agent(
			config=self.agents_config['sales_researcher'],
			verbose=True,
  			allow_delegation=False,
  			max_iter=1
		)
	
	@agent
	def sales_predictor(self) -> Agent:
		return Agent(
			config=self.agents_config['sales_predictor'],
			verbose=True,
  			allow_delegation=False,
  			max_iter=1
		)
	
	@agent
	def improver(self) -> Agent:
		return Agent(
			config=self.agents_config['improver'],
			verbose=True,
  			allow_delegation=False,
  			max_iter=1
		)
	

	#######TASKS########

	@task
	def research_task(self) -> Task:
		return Task(
			config=self.tasks_config['research_task'],
			async_execution=True
		)

	@task
	def market_research_task(self) -> Task:
		return Task(
			config=self.tasks_config['market_research_task'],
			async_execution=True
		)
	
	@task
	def social_media_researcher_task(self) -> Task:
		return Task(
			config=self.tasks_config['social_media_researcher_task'],
		)
	
	@task
	def sentiment_analysis_task(self) -> Task:
		return Task(
			config=self.tasks_config['sentiment_analysis_task'],
			async_execution=True,
			output_file="sentiment_analysis.md"
		)
	
	@task
	def sales_research_task(self) -> Task:
		return Task(
			config=self.tasks_config['sales_research_task'],
			async_execution=True,
			output_file="sales_research.md"
		)
	
	@task
	def sales_prediction_task(self) -> Task:
		return Task(
			config=self.tasks_config['sales_prediction_task'],
			output_file="sales_prediction.md"
		)
	@task
	def improvement_task(self) -> Task:
		return Task(
			config=self.tasks_config['improvement_task'],
			output_file="improvement.md"
		)
	

	####CREW####

	@crew
	def crew(self) -> Crew:
		"""Creates the Builder crew"""

		return Crew(
			agents=self.agents, # Automatically created by the @agent decorator
			tasks=self.tasks, # Automatically created by the @task decorator
			process=Process.sequential,
			verbose=True
		)
