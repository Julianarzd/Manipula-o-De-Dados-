#criando arquivos
class Archive
    def __init__(self, pain_file):
        self.pain_file =  pain_file

    def create_archive(self):
        with open(self.pain_file, "w", enconding="utf-8") as file:
            csv.writer(file, delimiter=";")