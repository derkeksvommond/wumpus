from typing import Union

from object import Object
from components import *
from message import Message

import json

class Provider(Object):
    def __init__(
        self,
        name: str = None,
        url: str = None
    ) -> None:
        self.name = name
        self.url = url
        
class Footer(Object):
    def __init__(
            self,
            text: str,
            icon_url: str = None,
            proxy_icon_url: str = None
        ) -> None:
        
        self.text = text
        self.icon_url = icon_url
        self.proxy_icon_url = proxy_icon_url

class Author(Object):
    def __init__(
        self,
        name: str,
        url: str = None,
        icon_url: str = None,
        proxy_icon_url: str = None
    ) -> None:
        
        self.name = name
        self.url = url
        self.icon_url = icon_url
        self.proxy_icon_url = proxy_icon_url

class Field(Object):
    def __init__(
        self,
        name: str = None,
        value: str = None,
        inline: bool = False
    ) -> None:

        self.name = name
        self.value = value
        self.inline = inline

class Image(Object):
    def __init__(
            self,
            url: str,
            proxy_url: str = None,
            height: int = None,
            width: int = None
        ) -> None:
        
        self.url = url
        self.proxy_url = proxy_url
        self.height = height
        self.width = width

Video = Image

class Embed(Object):

    def __init__(
        self,
        title: str = None,
        description: str = None,
        type: str = "rich",
        url: str = None,
        timestamp: str = None,
        color: int = None,
        footer: Footer = None,
        image: Image = None,
        video: Video = None,
        provider: Provider = None,
        author: Author = None,
        fields: list[Field] = []
    ) -> None:
        
        self.title = title
        self.type = type
        self.description = description
        self.url = url
        self.timestamp = timestamp
        self.color = color
        self.footer = footer
        self.image = image
        self.video = video
        self.provider = provider
        self.author = author
        self.fields = fields

class Text(Object):

    def __init__(
        self,
        content: str,
        embeds: list[Embed] = [],
        components: list[Component] = None,
        nonce: str = None,
        tts: bool = False,
        # allowed_mentions
        message_reference: Union[Message, int] = None,
        sticker_ids: list[int] = [],
        # files
        # payload_json
        # attachments
        flags: str = None
    ) -> None:
        self.content = content
        self.nonce = nonce
        self.tts = tts
        self.embeds = embeds
        self.message_reference = message_reference
        self.sticker_ids = sticker_ids
        self.flags = flags

        self.components = [dict(
            type=1,
            components=[component.json() for component in components]
        )] if components is not None else None
