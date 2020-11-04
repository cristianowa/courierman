from courierman.postman_entry import PostmanEntry


class Request(PostmanEntry):
    @property
    def name(self):
        return self._json["name"]

    def request_info(self):
        return None

    def execute(self):
        pass
