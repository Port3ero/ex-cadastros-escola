from time import sleep
from classes import Professores
from classes import Alunos
from classes import Cursos


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
