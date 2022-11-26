from keyboards.keyboards_classes import RelatedMenuItem, set_menu_children
from starters.get_commands_dict import commands_descriptions


menu_root = RelatedMenuItem(
    'commands',
    description='Тут собраны все команды бота с описаниями\n\nДля навигации используйте кнопки ниже:'
)

set_menu_children(commands_descriptions, menu_root)
