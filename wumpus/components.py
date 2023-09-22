from typing import Union, Callable, List, Set
import random

from object import Object

PRIMARY, SECONDARY, SUCCESS, DANGER, LINK = 1, 2, 3, 4, 5
TEXT, USER, ROLE, MENTIONABLE, CHANNEL = 3, 5, 6, 7, 8

GUILD_TEXT, DM, GUILD_VOICE, GROUP_DM, GUILD_CATEGORY, GUILD_ANNOUNCEMENT = 0, 1, 2, 3, 4, 5
ANNOUNCEMENT_THREAD, PUBLIC_THREAD, PRIVATE_THREAD, GUILD_STAGE_VOICE = 10, 11, 12, 13
GUILD_DIRECTORY, GUILD_FORUM, GUILD_MEDIA = 14, 15, 16

"""
emojiparameter isn't implemented yet

3, 6, 8, 2, 4, 5, 7
"""

class Component(Object):
    def __init__(
            self, type: int,
            custom_id: Union[Callable, str]
        ) -> None:
        
        self.type = type

        self.custom_id = (
            custom_id if isinstance(custom_id, str) 
            else f"wumpus_{random.random() * 1000}" if custom_id is None
            else custom_id.__name__
        )

class Option(Object):
    def __init__(
            self,
            label: str,
            value: str,
            description: str = None,
            emoji: dict = None,
            default: bool = False
    ) -> None:
        
        self.label = label
        self.value = value
        self.description = description
        self.default = default
        self.emoji = emoji
    

class Button(Component):

    __allowed_styles: Set[int] = (PRIMARY, SECONDARY, SUCCESS, DANGER, LINK)

    def __init__(
            self,
            style: __allowed_styles = 1,
            label: str = "N/A",
            emoji: dict = None,
            custom_id: Union[Callable, str] = None,
            url: str = "https://example.org/",
            disabled: bool = False
        ) -> None:
        
        super().__init__(2, custom_id)
        
        self.style = style
        self.label = label
        self.disabled = disabled

        if self.style == 5: self.url = url


class Select(Component):

    __allowed_types: Set[int] = (TEXT, USER, ROLE, MENTIONABLE, CHANNEL)
    __allowed_channel_types: Set[int] = (
        GUILD_TEXT, DM, GUILD_VOICE, GROUP_DM, GUILD_CATEGORY, GUILD_ANNOUNCEMENT,
        ANNOUNCEMENT_THREAD, PUBLIC_THREAD, PRIVATE_THREAD, GUILD_STAGE_VOICE,
        GUILD_DIRECTORY, GUILD_FORUM, GUILD_MEDIA
    )

    def __init__(
            self,
            type: __allowed_types = 3,
            placeholder: str = None,
            custom_id: Union[Callable, str] = None,
            options: List[Option] = None,
            min_values: int = None,
            max_values: int = None,
            disabled: bool = False,
            channel_types: __allowed_channel_types = None
    ) -> None:
        
        super().__init__(type, custom_id)
        self.placeholder = placeholder
        self.options = options
        self.min_values = min_values
        self.max_values = max_values
        self.disabled = disabled
        
        if type == 8: self.channel_types = channel_types
