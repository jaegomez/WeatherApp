#!/usr/bin/python
#

import sys


class InputHandler:

    def __init__(self, db):
        self.database_handler = db

    def handle_command(self, command):
        """
        this will handle the commands
        :param command: a command given
        :return:
        """

        dictionary_commands = {'help': "Shows a list of options",
                               'temperature': "Shows current temperature for designated address",
                               'humidity': 'Shows current humidity for designated address',
                               'exit': 'Exits you out from the program'}

        if command.lower() == "temperature":
            self.handle_temperature_command()
        elif command.lower() == 'humidity':
            self.handle_humidity_command()
        elif command.lower() == 'exit':
            sys.exit(0)
        elif command.lower() == 'help':
            for key, value in dictionary_commands.iteritems():
                print key + ": " + value
        else:
            print "Unknown command: " + command

    def handle_temperature_command(self):
        """
        this will handle the temperature command
        :return:
        """

        get_temperature = raw_input("Enter an address you would like to know the TEMPERATURE for: ")

        self.database_handler.temperature(get_temperature)

    def handle_humidity_command(self):
        """
        this will handle the humidity command
        :return:
        """

        get_humidity = raw_input("Enter an address you would like to know the HUMIDITY for: ")

        self.database_handler.humidity(get_humidity)
