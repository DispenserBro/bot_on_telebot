from keyboards.keyboards_classes import RelatedMenuItem


menu_root = RelatedMenuItem(
    'commands',
    description='Тут собраны все команды бота с описаниями\n\nДля навигации используйте кнопки ниже:'
    )

# Commands groups

private_commands = RelatedMenuItem(
    'Команды в ЛС',
    description='__*Команды в ЛС*__\n\nКоманды, которые работают __только__ в личных сообщениях',
    parent=menu_root
)

group_commands = RelatedMenuItem(
    'Команды в группах',
    description='__*Команды в группах*__\n\nКоманды, которые работают __только__ в группах',
    parent=menu_root
)

general_commands = RelatedMenuItem(
    'Общие команды',
    description='__*Общие команды*__\n\nКоманды, которые работают во всех поддерживаемых ботом типах чатов',
    parent=menu_root
)

# Commands in private_commands group

help_command = RelatedMenuItem(
    '/help',
    description='Команда /help показывает это меню\)\)\)',
    parent=private_commands
)

# Commands in group_commands group

a_to_sticker = RelatedMenuItem(
    f'А. \u2794 стикер',
    description='__*А\. \u2794 стикер*__\n\nБот ответит на сообщение, которое заканчивается на\n`А.` или `а.` стикером \(неприличным\) в группах',
    parent= group_commands
)

# Commands in general_commands group

weather_commands = RelatedMenuItem(
    'Погода',
    description='Показывает погоду в городе\n\(*по умолчанию Йошкар\-Ола*\)\
        \n\n/w, /weather, /погода, /п \- *погода на 3 дня __в виде изображения__*\
        \n\n/w2, /weather2, /погода2, /п2 \- *погода на 7 дней __в виде текста__*\
        \n\n Примеры: /w; /w Москва; /w2; /w2 Москва',
    parent=general_commands
)
