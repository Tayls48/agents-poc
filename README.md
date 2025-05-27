## Welcome ##

This notebook is a sandbox to play around with if/how OpenAI's Agents SDK could be a viable option for Kliro's current MVP development. 

My aim with this poc is:
1. Create 5 dummy users based on different regions (US, Canada, UK) that start with a basic json object from the onboarding flow.
2. An "education" agent that starts to work with users and help them understand how their inheritance is going to work. 
3. Create a "triage agent" that can handle basic Q&A but will often handoff to more specialized agents for specific tasks
4. Create 3 other specialized agents:
    4.1 An Inheritance Risk Agent: That starts to calculate the potential inheritance or estate taxes that a user may pay
    4.2 An Estate Risk Agent: That starts to calculate how the estate is going to be wound up and everything that the user should be doing ahead of time to minimize a smooth transition
    4.3 A "Coach" Agent: That takes the conversation, starts to act as a "estate planner" and builds a roadmap for a user and personalized tasks that a user can start to action and follow up with. 
5. Each of these agents should have access to specialized tools which we will also create. 