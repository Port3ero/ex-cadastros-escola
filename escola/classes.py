class Professores():

    lista_prof = []

    # Adiciona um professor novo

    def add_professor(id, nome, matricula, idade):
        prof = [id, nome, matricula, idade]
        Professores.lista_prof.append(prof)

    # Exclui um professor pelo Id

    def del_professor(id):
        del Professores.lista_prof[id]

        # Refaz os Id's dos professores

        re_id = 0
        for p in range(len(Professores.lista_prof)):
            Professores.lista_prof[p][0] = re_id
            re_id += 1
        re_id = 0

    # Exibe os professores cadastrados

    def show_professor():
        print(f'{'Id':<5}{'Nome':<30}{'Matrícula':<15}{'Idade':<5}')
        for c in range(len(Professores.lista_prof)):
            print(f'{Professores.lista_prof[c][0]:<5}', end='')
            print(f'{Professores.lista_prof[c][1]:<30}', end='')
            print(f'{Professores.lista_prof[c][2]:<15}', end='')
            print(f'{Professores.lista_prof[c][3]:<5}')


class Alunos():

    lista_alunos = []

    # Adiciona um aluno novo

    def add_aluno(id, nome, matricula, idade):
        aluno = [id, nome, matricula, idade]
        Alunos.lista_alunos.append(aluno)

    # Exclui um aluno pelo Id

    def del_aluno(id):
        del Alunos.lista_alunos[id]

        # Refaz os Id's dos alunos

        re_id = 0
        for q in range(len(Alunos.lista_alunos)):
            Alunos.lista_alunos[q][0] = re_id
            re_id += 1
        re_id = 0

    # Exibe os alunos cadastrados

    def show_aluno():
        print(f'{'Id':<5}{'Nome':<30}{'Matrícula':<15}{'Idade':<5}')
        for a in range(len(Alunos.lista_alunos)):
            print(f'{Alunos.lista_alunos[a][0]:<5}', end='')
            print(f'{Alunos.lista_alunos[a][1]:<30}', end='')
            print(f'{Alunos.lista_alunos[a][2]:<15}', end='')
            print(f'{Alunos.lista_alunos[a][3]:<5}')

    
class Cursos():
     
    lista_cursos = []

     # Adiciona um novo curso

    def add_curso(id, curso):
        curso = [id, curso]
        Cursos.lista_cursos.append(curso)

    # Exclui um curso pelo Id

    def del_curso(id):
        del Cursos.lista_cursos[id]

        # Refaz os Id's dos cursos

        re_id = 0
        for r in range(len(Cursos.lista_cursos)):
            Cursos.lista_cursos[r][0] = re_id
            re_id += 1
        re_id = 0

    # Exibe os cursos cadastrados

    def show_curso():
        print(f'{'Id':<5}{'Curso':<30}')
        for b in range(len(Cursos.lista_cursos)):
            print(f'{Cursos.lista_cursos[b][0]:<5}', end='')
            print(f'{Cursos.lista_cursos[b][1]:<30}')
