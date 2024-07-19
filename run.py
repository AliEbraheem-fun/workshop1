# начальный результат, создаваемый участником 1
# через веб-интерфейс github.com
def print_my_info(name: str) -> None:
    print(f'Меня зовут {name}')


print_my_info('Alexander')

# фича, котрую необходимо добавить участнику 2
def print_my_info(name: str, patronymic: str) -> None:
    print(f'Меня зовут {name} {patronymic}')


print_my_info('Alexander', 'Aleksandrovich')
