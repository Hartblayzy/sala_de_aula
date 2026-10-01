class Livro:
    titulo: str
    autor: str
    numero_paginas: int

    def __init__(self, titulo: str, autor: str, numero_paginas: int):
        self.titulo = titulo
        self.autor = autor
        self.numero_paginas = numero_paginas

    def exibir_resumo(self):
        print (f'O Livro {self.titulo} foi escrito por {self.autor} e possui {self.numero_paginas} páginas.')


livro = Livro(autor='Sir Arthur Conan Doyle', numero_paginas= 180, titulo='"Um Estudo em Vermelho"')


livro.exibir_resumo()
        