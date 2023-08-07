from typing import Union
import json

# from .channel import Message

class Message:
    id = 123456789


class Sticker:
    pass


class Component:
    pass


class Button(Component):
    pass

class Provider:
    def __init__(
        self,
        name: str = None,
        url: str = None
    ) -> None:
        self.name = name
        self.url = url

    def __iter__(self) -> dict:
        return iter(dict(
            name = self.name,
            url = self.url
        ).items())
        
class Footer:
    def __init__(
            self,
            text: str,
            icon_url: str = None,
            proxy_icon_url: str = None
        ) -> None:
        
        self.text = text
        self.icon_url = icon_url
        self.proxy_icon_url = proxy_icon_url

    def __iter__(self) -> dict:
        return iter(dict(
            text = self.text,
            icon_url = self.icon_url,
            proxy_icon_url = self.proxy_icon_url
        ).items())

class Author:
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

    def __iter__(self) -> dict:
        return iter(dict(
            name = self.name,
            url = self.url,
            icon_url = self.icon_url,
            proxy_icon_url = self.proxy_icon_url
        ).items())

class Field:
    def __init__(
        self,
        name: str = None,
        value: str = None,
        inline: bool = False
    ) -> None:

        self.name = name
        self.value = value
        self.inline = inline

    def __iter__(self) -> dict:
        return iter(dict(
            name = self.name,
            value = self.value,
            inline = self.inline
        ).items())

class Image:
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

    def __iter__(self) -> dict:
        return iter(dict(
            url = self.url,
            proxy_url = self.proxy_url,
            height = self.height,
            width = self.width
        ).items())
    
Video = Image

class Embed:

    def __init__(
        self,
        title: str = None,
        description: str = None,
        type: str = "rich",
        url: str = None,
        timestamp: str = "2069-04-20T00:00:00+0000",
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

    def __iter__(self) -> dict:
        return iter(dict(
            title = self.title,
            type = self.type,
            description = self.description,
            url = self.url,
            timestamp = self.timestamp,
            color = self.color,
            
            provider = None if self.provider is None else dict(self.provider),
            image = None if self.image is None else dict(self.image),
            video = None if self.video is None else dict(self.video),
            footer = None if self.footer is None else dict(self.footer),
            author = None if self.author is None else dict(self.author),
            
            fields = [] if not self.fields else [ dict(field) for field in self.fields ]

        ).items())


class Text:

    def __init__(
        self,
        content: str,
        embeds: list[Embed] = [],
        components: list[Component] = [],
        nonce: str = "undefined",
        tts: bool = False,
        # allowed_mentions
        message_reference: Union[Message, int] = None,
        sticker_ids: list[Union[Sticker, int]] = [],
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
        self.components = components
        self.sticker_ids = sticker_ids
        self.flags = flags

    def __iter__(self) -> dict:
        
        return iter(dict(
            content = self.content,
            nonce = self.nonce,
            tts = self.tts,
            flags = self.flags,
            sticker_ids = self.sticker_ids,

            embeds = ( [] if not self.embeds else [ dict(embed) for embed in self.embeds ] ),
            components = ( [] if not self.components else [ dict(component) for component in self.components ] ),
            
            message_reference = ( 
                None
                    if self.message_reference is None 
                    else ( self.message_reference
                        if type(self.message_reference) is int 
                        else self.message_reference.id
                    )
            )
        ).items())




print(json.dumps(dict(Text(
    "Hallo Welt, das ist meine allererste Nachricht :)",
    embeds=[
        Embed(
            "Titel",
            "Wie es sich für eine erste Nachricht gehört, ist hier etwas Text.",
            fields=[
                Field("Fußballfeld","Was ist das überhaupt??")
            ]
        ),
        Embed("Kein Titel?", "Doch!")
    ]
)), indent=4))
