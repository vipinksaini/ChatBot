from rasa_core.channels import HttpInputChannel
from rasa_core.agent import Agent
from rasa_core.interpreter import RasaNLUInterpreter
from rasa_slack_connector import SlackInput
import ruamel.yaml as yaml
import warnings


warnings.simplefilter('ignore', yaml.error.UnsafeLoaderWarning)

nlu_interpreter = RasaNLUInterpreter('./models/nlu/default/restaurantnlu')
agent = Agent.load('./models/dialogue', interpreter = nlu_interpreter)

input_channel = SlackInput('xoxp-515306069779-515410677122-515619949060-fccc2be4cd32409c69c4c60f9d258115', #app verification token
							'xoxb-515306069779-515183929761-SwvBrSozQody6EB8fn88jeQZ', # bot verification token
							'6ahChzuqYFpHR1p0LzAEbqIb', # slack verification token
							True)

agent.handle_channel(HttpInputChannel(5004, '/', input_channel))