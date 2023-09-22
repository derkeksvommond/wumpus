class Object:

    def json(self) -> dict:

        attributes = [
            attribut for attribut in dir(self)
            if not callable(getattr(self, attribut))
            and not attribut.startswith("_")
        ]

        values = self.__dict__
        payload = dict()

        for key in attributes:

            payload[key] = (
                None if values[key] is None
                else values[key].json() if isinstance(values[key], Object)
                else [ (_.json() if isinstance(_, Object) else _) for _ in values[key] ] if isinstance(values[key], list)
                else values[key]
            )

        return payload
