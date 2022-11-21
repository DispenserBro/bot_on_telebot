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
    'А. \u2794 стикер',
    description='__*А\. \u2794 стикер*__\n\nБот ответит на сообщение, которое заканчивается на\n`А.` или `а.` стикером в группах',
    parent=group_commands
)

admin_commands = RelatedMenuItem(
    'Команды администраторов',
    description='__*Команды администраторов*__\n\nКоманды, которые могут вызваны только администраторами групп',
    parent=group_commands
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

# Commands in admin_commands group

ro_admin_command = RelatedMenuItem(
    '!ro',
    description='__*Команда \!ro*__\n\nЗапрещает пользователю писать в группу\
        \n\n`!ro` на протяжении 1 минуты без причины\
        \n`!ro <причина>` на протяжении 1 минуты с определённой причиной \(1 слово\)\
        \n`!ro <время>` на протяжении указанного времени без причины\
        \n`!ro <время> \<причина\>` на протяжении указанного времени с определённой причиной \(несколько слов\)\
        \n\nФормат *времени*:\
        \n  `<x>d` \- x дней\
        \n  `<x>h` \- x часов\
        \n  `<x>m` \- x минут\
        \nГде x \> 0',
    parent=admin_commands
)

ban_admin_commands = RelatedMenuItem(
    '!ban и !pardon',
    description='__*Команды \!ban и \!pardon*__\
        \n\n`!ban` банит пользователя в группе\
        \n\(должна быть ответом на сообщение пользователя, которого надо забанить\)\
        \n\n`!pardon \<id\>` разбанить пользователя с указанным id в группе\
        \n\(id можно взять из сообщения о бане\)',
    parent=admin_commands
)