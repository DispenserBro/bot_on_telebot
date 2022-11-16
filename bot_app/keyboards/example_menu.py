from keyboards.keyboards_classes import RelatedMenuItem

root = RelatedMenuItem('menu', description='Главная страница меню\nВыберите один пункт:')
category_1 = RelatedMenuItem('Первая категория', description='Первая категория\n*Транспорт*\n\nВыберите один из видов транспорта ниже:', parent=root)
item_1_1 = RelatedMenuItem('Машина', description='Машина\n\nАБОБА', parent=category_1)
item_1_2 = RelatedMenuItem('Ноги', description='Ноги\n\nСАС', parent=category_1)
item_1_3 = RelatedMenuItem('Самолёт', description='Самолёт\n\nАМОГУС', parent=category_1)
category_2 = RelatedMenuItem('Вторая категория', description='Вторая категория\n*Телефоны*\n\nВыберите один из телефонов ниже:', parent=root)
item_2_1 = RelatedMenuItem('Самсунг', description='Самсунг\n\nАЬОЬА', parent=category_2)
item_2_2 = RelatedMenuItem('АйФон', description='АйФон\n\nАМОГУС', parent=category_2)
item_2_3 = RelatedMenuItem('Хуавей', description='Хуавей\n\nСАС', parent=category_2)
item_2_4 = RelatedMenuItem('Хонор', description='Хонор\n\nСАС', parent=category_2)

menu_root = root
