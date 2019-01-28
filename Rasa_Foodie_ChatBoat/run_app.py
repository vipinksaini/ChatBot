from rasa_core.channels import HttpInputChannel
from rasa_core.agent import Agent
from rasa_core.interpreter import RasaNLUInterpreter
from rasa_slack_connector import SlackInput
import ruamel.yaml as yaml
import warnings


warnings.simplefilter('ignore', yaml.error.UnsafeLoaderWarning)

nlu_interpreter = RasaNLUInterpreter('./models/nlu/default/restaurantnlu')
agent = Agent.load('./models/dialogue', interpreter = nlu_interpreter)

input_channel = SlackInput('xoxp-Verf.Key', #app verification token
							'xoxb-bot.key', # bot verification token
							'slack.key', # slack verification token
							True)

agent.handle_channel(HttpInputChannel(5004, '/', input_channel))