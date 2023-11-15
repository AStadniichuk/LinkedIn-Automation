import os


class ManipulationWithFile:
    @staticmethod
    def give_path_to_file(file_name: str) -> str:
        script_directory = os.path.dirname(os.path.abspath(__file__))
        script_directory = script_directory.split('\\')
        path = f'{script_directory[0]}\\{script_directory[1]}\\files_for_send_messages'

        return os.path.join(path, file_name)

    @staticmethod
    def read_file(file_name: str) -> str:
        file_path = ManipulationWithFile.give_path_to_file(file_name)

        assert os.path.exists(file_path), f"The file {file_path} doesn't exist."

        with open(file_path, 'r') as file:
            data = file.read()

        return data


if __name__ == '__main__':
    print(ManipulationWithFile.give_path_to_file('test.txt'))

