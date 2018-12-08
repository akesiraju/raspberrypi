import json
# from flask_cors import CORS, cross_origin
import logging
# Import SDK packages
from AWSIoTPythonSDK.MQTTLib import AWSIoTMQTTClient
import os


class IotConnection:
    def __init__(self):
        self.config = self._load_config('.vscode/config.json')

        self.logger = logging.getLogger('IotConnection')
        self.logger.setLevel(logging.DEBUG)
        self.myMQTTClient = AWSIoTMQTTClient(self.config['thingName'])
        self.myMQTTClient.configureEndpoint(self.config['hostUrl'], 8883)
        self.myMQTTClient.configureCredentials(
            self.config['caFilePath'], self.config['privateKeyFilePath'], self.config['certFilePath'])
        self.myMQTTClient.configureOfflinePublishQueueing(-1)
        self.myMQTTClient.configureDrainingFrequency(2)  # Draining: 2 Hz
        self.myMQTTClient.configureConnectDisconnectTimeout(10)  # 10 sec
        self.myMQTTClient.configureMQTTOperationTimeout(5)  # 5 sec
        self.myMQTTClient.connect()
        self.logger.debug('connection success')
        
    def publish(self, message):
        self.myMQTTClient.publish('iotCarTopic', json.dumps(message), 0)
        self.logger.debug('publish complete')
    
    def _load_config(self, config_file_path):
        with open(config_file_path) as f:
            config = json.load(f)

        return config

    def clean(self):
        self.logger.debug('clean START')
        self.myMQTTClient.disconnect()
        self.logger.debug('clean END')