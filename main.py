from random import randint

DEFAULT_ATTACK = 5
DEFAULT_DEFENCE = 10
DEFAULT_STAMINA = 80


class Character:

    RANGE_VALUE_ATTACK = (1, 3)
    RANGE_VALUE_DEFENCE = (1, 5)
    SPECIAL_SKILL = ('Удача')
    SPECIAL_BUFF = 15
    BRIEF_DESC_CHAR_CLASS = 'отважный любитель приключений'

    def __init__(self, name):
        self.name = name

    def attack(self):
        value_attack = DEFAULT_ATTACK + randint(*self.RANGE_VALUE_ATTACK)
        return (f'{self.name} нанес противнику урон, равный {value_attack}.')
    
    def defence(self):
        value_defence = DEFAULT_DEFENCE + randint(*self.RANGE_VALUE_DEFENCE)
        return (f'{self.name} заблокировал {value_defence} урона.')
    
    def special(self):
        return (f'{self.name} применил специальное умение '
                f'"{self.SPECIAL_SKILL} {self.SPECIAL_BUFF}"')
    
    def __str__(self):
        return f'{self.__class__.__name__} - {self.BRIEF_DESC_CHAR_CLASS}'


class Warrior(Character):
    BRIEF_DESC_CHAR_CLASS = (' дерзкий воин ближнего боя. '
                             'Сильный, выносливый и отважный')
    RANGE_VALUE_ATTACK = (3, 5)
    RANGE_VALUE_DEFENCE = (5, 10)
    SPECIAL_SKILL = 'Выносливость'
    SPECIAL_BUFF = DEFAULT_STAMINA + 25



class Mage(Character):
    BRIEF_DESC_CHAR_CLASS = (' находчивый воин дальнего боя. '
                             'Обладает высоким интеллектом')
    RANGE_VALUE_ATTACK = (5, 10)
    RANGE_VALUE_DEFENCE = (-2, 2)
    SPECIAL_SKILL = 'Атака'
    SPECIAL_BUFF = DEFAULT_ATTACK + 40


class Healer(Character):
    BRIEF_DESC_CHAR_CLASS = (' могущественный заклинатель. '
                             'Черпает силы из природы, веры и духов')
    RANGE_VALUE_ATTACK = (-3, -1)
    RANGE_VALUE_DEFENCE = (2, 5)
    SPECIAL_SKILL = 'Защита'
    SPECIAL_BUFF = DEFAULT_DEFENCE + 30


def choice_char_class(char_name: str) -> Character:
    """
    Возвращает строку с выбранным
    классом персонажа.
    """
    game_classes = {'warrior': Warrior, 'mage': Mage, 'healer': Healer}
    approve_choice: str = None
    while approve_choice != 'y':
        selected_class = input('Введи название персонажа, '
                           'за которого хочешь играть: Воитель — warrior, '
                           'Маг — mage, Лекарь — healer: ')
        char_class: Character = game_classes[selected_class](char_name)
        print(char_class)
        approve_choice = input('Нажми (Y), чтобы подтвердить свой выбор.').lower

    return char_class


def start_training(character):
    cmd = None
    commands = {'attack': Character.attack, 'defence': Character.defence, 'special': Character.special}
    if cmd != 'skip':
        cmd = input('Введи команду: ')
        cmd_action: Character = commands[cmd](char_class)
        print(cmd_action)

    return cmd_action
