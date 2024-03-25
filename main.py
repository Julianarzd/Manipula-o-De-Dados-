import os

from domain.archive import Archive
from model.transparencia import Transparencia

if __name__ =='__main__':
    file_name = "transparencia.csv"
    arquivo = Archive(file_name)
    if os.path.exists(file_name):
        dados = arquivo.file_read()
    else:
        arquivo.create_archive()

    if dados:
        novo_registro = Transparencia(
                "123456",
                "Novo nome órgão superior",
                "1234",
                "Novo nome órgão",
                "5678",
                "Novo nome unidade gestora",
                "Nova categoria econômica",
                "Receita Nova Origem",
                "Nova espécie receita",
                "Novo detalhamento",
                "1000,00",
                "900,00",
                "800,00",
                "80,00",
                "2023-03-10",
                "2023",

        )

        arquivo.edit_file(dados, 1200, novo_registro)


