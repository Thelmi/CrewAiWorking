----- VMS (Virtual Market Simulator) -----
  Problem:
Understanding and predicting market response, sales, growth, and vision when introducing a business, product, or policy is complex and uncertain. 
Companies, governments, and entrepreneurs often face challenges in making informed decisions about entering a market, expanding to new regions, or launching new initiatives. 
These challenges arise due to the lack of tools to simulate market dynamics, assess public response, and visualize potential outcomes.

  Solution:
The Market Simulator addresses this challenge by providing an interactive tool to simulate market scenarios. It takes two key inputs:
- A description of the business/product/policy/etc.
- A description of the market (e.g., a global market, specific country, or city).
Using this information, the system simulates the market's response, including potential sales, public sentiment, growth trajectory, and alignment with the market's vision. 
By leveraging historical data, market analysis algorithms, and sentiment intelligence, the simulator offers actionable insights, helping users anticipate market outcomes 
and make data-driven decisions. This tool benefits businesses, policymakers, and investors by reducing risk, enhancing strategic planning, and improving the success rate of new 
market entries or initiatives.

  Technical Choices:
- SambaNova Models (real-time inference for running high-speed simulations with large datasets)
- CrewAi (to create Multiple Agents)
- Serper tools (To fetch the data)

Instruction on How to use Our Project:
- git clone https://github.com/<your-username>/<your-repo-name>.git
- cd <your-repo-name>
- python --version (should be more that 3.10 versions)
- pip3 install crewai
