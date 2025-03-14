from BD.firebase_config import db
import random

def adicionar_livro(id,titulo, autor, paginas, ano):
    doc_ref = db.collection("livros").add({
        "id": id,
        "titulo": titulo,
        "autor": autor,
        "paginas": paginas,
        "ano": ano
    })
    print(f"Livro adicionado com sucesso! ID do livro: {doc_ref[1].id}")


def listar_livros():
    livros_ref = db.collection("livros").stream()
    livros = {}

    for doc in livros_ref:
        livros[doc.id] = doc.to_dict() 

    return livros





def atualizar_livro(id_livro, novos_dados):
    livros_ref = db.collection("livros").stream()
    for doc in livros_ref:
        if doc.id == str(id_livro):  
            livro_ref = db.collection("livros").document(doc.id)
            livro_ref.update(novos_dados)
            print(f"Livro com ID '{id_livro}' atualizado com sucesso!")
            return True 
    print(f"Erro: Nenhum livro encontrado com o ID '{id_livro}'")
    return False  

    for livro in livros_encontrados:
        livro.reference.update(novos_dados)
    





def deletar_livro(id):
    try:
        livro_ref = db.collection("livros").document(id)
        livro = livro_ref.get()

        if livro.exists:
            livro_ref.delete()
            print(f"Livro com ID '{id}' removido com sucesso!")
        else:
            print(f"Erro: Nenhum livro encontrado com o ID '{id}'")

    except Exception as e:
        print(f"Erro ao deletar livro: {e}")
        
        


ids_gerados = set()

# Função para gerar um ID único
def gerar_id_unico():
    while True:
        # Gera um ID aleatório entre 1 e 1000
        id_aleatorio = random.randint(1, 10000)
        
        # Se o ID já foi gerado, continue tentando
        if id_aleatorio not in ids_gerados:
            ids_gerados.add(id_aleatorio)  # Adiciona o ID ao conjunto
            return id_aleatorio

