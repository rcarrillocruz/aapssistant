import autogen
from autogen import AssistantAgent, UserProxyAgent

filter_dict = {"model": "openhermes2.5-mistral"}
config_list = autogen.config_list_from_json(env_or_file="OAI_CONFIG_LIST.json", filter_dict=filter_dict)

assistant = AssistantAgent("assistant", llm_config={"config_list": config_list})

user_proxy = UserProxyAgent("user_proxy", code_execution_config={"work_dir": "coding", "use_docker": False})
user_proxy.initiate_chat(assistant, message="Plot a chart of NVDA and TESLA stock price change YTD.")