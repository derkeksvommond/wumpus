class Object:

    def __iter__(self) -> dict:

        attributes = [attribut for attribut in dir(self) if not callable(getattr(self, attribut)) and not attribut.startswith("__")]
        values = self.__dict__

        payload = dict()

        for key in attributes:

            payload[key] = (
                None if values[key] is None 
                else dict(values[key]) if isinstance(values[key], Object)
                else [ (dict(_) if isinstance(_, Object) else _) for _ in values[key] ] if isinstance(values[key], list)
                else values[key]
            )
            

        return iter(payload.items())
