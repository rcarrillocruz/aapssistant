from autogen import AssistantAgent, UserProxyAgent

config_list = [
  {
    "model": "openhermes2.5-mistral",
    "base_url": "http://192.168.1.200:11434/v1",
    "api_key": "ollama",
  }
]

assistant = AssistantAgent("assistant", llm_config={"config_list": config_list})

user_proxy = UserProxyAgent("user_proxy", code_execution_config={"work_dir": "coding", "use_docker": False})
user_proxy.initiate_chat(assistant, message="Plot a chart of NVDA and TESLA stock price change YTD.")