from weatherApiHandler import ApiHandler
from weatherInputHandler import InputHandler


def main():
    db_handler = ApiHandler()
    input_handler = InputHandler(db_handler)

    while True:
        command = raw_input("Weather App>")
        input_handler.handle_command(command)

main()
