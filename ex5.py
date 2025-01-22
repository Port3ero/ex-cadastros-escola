from time import sleep

# Cadastro de alunos e professores

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


# Programa principal

action = 11
while action != 0:

    print('-'*80)
    print(f'{'BEM-VINDO AO SISTEMA!':^80}')
    print('-'*80)
    sleep(0.5)

    # Menu de interações

    print(f'{'O que voce deseja?':^80}')
    sleep(0.5)
    print('-'*80)
    sleep(0.5)
    print('1. Consultar Cursos')
    print('2. Consultar Professores')
    print('3. Consultar Alunos')
    print('4. Cadastrar Curso')
    print('5. Cadastrar Professor(a)')
    print('6. Cadastrar Aluno(a)')
    print('7. Remover Curso')
    print('8. Remover Professor')
    print('9. Remover Aluno')
    print('0. Sair do Sistema')
    print('-'*80)
    sleep(0.5)
    try:
        action = int(input())
    except (ValueError, TypeError):
        sleep(0.5)
        print('-'*80)
        sleep(0.5)
        print('ERRO! Insira um valor válido.')
    else:
        sleep(0.5)
        print('-'*80)

        # Consulta de cursos

        if action == 1:

            print(f'{'Buscando cursos...':^80}')
            print('-'*80)
            sleep(1)
            if len(Cursos.lista_cursos) > 0:
                Cursos.show_curso()
            else:
                print('Não há cursos cadastrados!')
            sleep(0.5)

        # Consulta de professores

        elif action == 2:

            print(f'{'Buscando professores...':^80}')
            print('-'*80)
            sleep(1)
            if len(Professores.lista_prof) > 0:
                Professores.show_professor()
            else:
                print('Não há professores cadastrados!')
            sleep(0.5)

        # Consulta de alunos

        elif action == 3:

            print(f'{'Buscando alunos...':^80}')
            print('-'*80)
            sleep(1)
            if len(Alunos.lista_alunos) > 0:
                Alunos.show_aluno()
            else:
                print('Não há alunos cadastrados!')
            sleep(0.5)

        # Cadastro de cursos

        elif action == 4:

            print(f'{'Cadastrar Curso':^80}')
            sleep(0.5)
            print('-'*80)
            sleep(0.5)
            id = len(Cursos.lista_cursos)
            curso = input('Nome do Curso: ')
            Cursos.add_curso(id, curso)
            sleep(0.5)
            print('-'*80)
            sleep(0.5)
            print('Curso cadastrado com sucesso!')
            sleep(0.5)

        # Cadastro de professores
        
        elif action == 5:

            print(f'{'Cadastrar Professor(a)':^80}')
            sleep(0.5)
            print('-'*80)
            sleep(0.5)
            id = len(Professores.lista_prof)
            nome = input('Nome: ')
            sleep(0.5)
            matricula = int(input('Matrícula: '))
            sleep(0.5)
            idade = int(input('Idade: '))
            Professores.add_professor(id, nome, matricula, idade)
            sleep(0.5)
            print('-'*80)
            sleep(0.5)
            print('Professor(a) cadastrado com sucesso!')
            sleep(0.5)

        # Cadastro de alunos

        elif action == 6:

            print(f'{'Cadastrar Aluno(a)':^80}')
            sleep(0.5)
            print('-'*80)
            sleep(0.5)
            id = len(Alunos.lista_alunos)
            nome = input('Nome: ')
            sleep(0.5)
            matricula = int(input('Matrícula: '))
            sleep(0.5)
            idade = int(input('Idade: '))
            Alunos.add_aluno(id, nome, matricula, idade)
            sleep(0.5)
            print('-'*80)
            sleep(0.5)
            print('Aluno(a) cadastrado com sucesso!')
            sleep(0.5)

        # Remover Curso

        elif action == 7:
            remover = int(input('Digite o Id do curso que deseja remover: '))
            Cursos.del_curso(remover)
            sleep(0.5)
            print('-'*80)
            sleep(0.5)
            print(f'{'Removendo Curso...'}')
            sleep(1)
            print('-'*80)
            sleep(0.5)
            print('Curso removido com sucesso!')
            sleep(0.5)
        
        # Remover Professor

        elif action == 8:
            remover = int(input('Digite o Id do Professor(a) que deseja remover: '))
            Professores.del_professor(remover)
            sleep(0.5)
            print('-'*80)
            sleep(0.5)
            print(f'{'Removendo Professor(a)...'}')
            sleep(1)
            print('-'*80)
            sleep(0.5)
            print('Professor(a) removido com sucesso!')
            sleep(0.5)

        # Remover Aluno

        elif action == 9:
            remover = int(input('Digite o Id do Aluno(a) que deseja remover: '))
            Alunos.del_aluno(remover)
            sleep(0.5)
            print('-'*80)
            sleep(0.5)
            print(f'{'Removendo Aluno(a)...'}')
            sleep(1)
            print('-'*80)
            sleep(0.5)
            print('Aluno(a) removido com sucesso!')
            sleep(0.5)

        # Sair do sistema

        elif action == 0:
            sleep(0.5)
            print('Encerrando...')
            sleep(1)
            print('-'*80)
            sleep(0.5)
            exit()

        # Ação inválida

        else:
            print('ERRO! Digite um valor válido.')
