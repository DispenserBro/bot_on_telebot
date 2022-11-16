# NYI - TODO: implement RelatedMenuItem class in main modules!!!
import typing


class RelatedMenuItem:
    def __init__(
        self: typing.Self,
        btn_name: str,
        description: str = '',
        parent: typing.Self | None = None
    ) -> None:
        """_summary_

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
