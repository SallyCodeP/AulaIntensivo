class DatabaseController:
    def execute(self, query: str) -> list[str]:
        raise NotImplementedError()