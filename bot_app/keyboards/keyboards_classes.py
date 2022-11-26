"""Module that provides layered menu feature to the bot.
::contents::
:class: RelatedMenuItem
    Class to turn data into menu items
:func: set_menu_children
    Function to generate menu from root and dict with children data"""

import typing


class RelatedMenuItem:
    """class to turn data into menu items

    Properties:
        callback: str
            returns object callback data

        parent: str
            returns object parent

        button: str
            returns a button name for the object
            sets a new button name for the object

        description: str
            returns a description for the object
            sets a new description for the object

        children: list
            returns a list of child objects
            adds a new child object to the list of child objects of the object

    Methods:
        get_buttons -> dict
            returns a callback data to generate buttons
    """
    def __init__(
        self: typing.Self,
        btn_name: str,
        description: str = '',
        parent: typing.Self | None = None
    ) -> None:
        """intializes a RelatedMenuItem class object

        Args:
            self (typing.Self)
            btn_name (str): name of button to display
            description (str, optional): text that will go in message. Defaults to ''.
            parent (typing.Self | None, optional): parent element of the menu. Defaults to None.
        """
        self.__btn_name = btn_name
        self.__desc = description
        self.__parent = self.__set_child(parent)
        self.__callback = self.__get_callback()
        self.__children = []

    def __getitem__(self: typing.Self, obj: typing.Self) -> int:
        return self.children.index(obj)

    def __set_child(self: typing.Self, parent: typing.Self | None) -> typing.Self | None:
        if not parent:
            return None
        else:
            parent.children.append(self)
            return parent

    def __get_callback(self: typing.Self) -> str:
        if not self.parent:
            return self.button

        head = self
        ids = []
        while head.parent:
            ids.append(str(head.parent[head]))
            head = head.parent

        ids.append(head.button)
        ids.reverse()
        ids = '_'.join(ids)

        return ids

    def __check_obj(self: typing.Self, obj: typing.Any, obj_type: type) -> None | Exception:
        if not isinstance(obj, obj_type):
            raise TypeError(f'Object must be a {obj_type} type!')

    @property
    def callback(self: typing.Self) -> str:
        return self.__callback

    @property
    def parent(self: typing.Self) -> typing.Self | None:
        return self.__parent

    @property
    def button(self: typing.Self) -> str:
        return self.__btn_name

    @button.setter
    def button(self: typing.Self, value: str) -> None | Exception:
        self.__check_obj(value, str)
        self.__btn_name = value

    @property
    def description(self: typing.Self) -> str:
        return self.__desc

    @description.setter
    def description(self: typing.Self, value: str) -> None | Exception:
        self.__check_obj(value, str)
        self.__desc = value

    @property
    def children(self: typing.Self) -> list:
        return self.__children

    @children.setter
    def children(self: typing.Self, obj: typing.Self) -> None | Exception:
        self.__check_obj(obj, type(self))
        self.__children.append(obj)

    def get_buttons(self: typing.Self) -> dict:
        if not self.children:
            if self.parent:
                return {'Назад': {'callback_data': self.parent.callback}}
            return {}

        buttons = {child.button: {'callback_data': child.callback} for child in self.children}
        if self.parent:
            buttons['Назад'] = {'callback_data': self.parent.callback}
        return buttons


def set_menu_children(items: dict, root: RelatedMenuItem) -> None:
    for key, value in items.items():
        current_el = RelatedMenuItem(btn_name=key, description=value[0], parent=root)
        if len(value) > 1:
            for el in value[1:]:
                set_menu_children(el, current_el)
