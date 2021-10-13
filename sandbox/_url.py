


class Url:
    def __init__(
        self,
        base_url: str,
        endpoint: str,
        **kwargs
    ) -> None:
        self.base_url = base_url
        self.endpoint = endpoint
        self.kwargs = kwargs

    def get_url(self) -> str:
        url = f"{self.base_url}/{self.endpoint}"
        added_args = False
        operator='?'

        for key, value in self.kwargs.items():
            url += f"{operator}{key}={value}"

            if not added_args:
                operator = "&"
                added_args = True

        print(f"URL: {url}")
        return url
        

    def set_endpoint(self, endpoint: str) -> None:
        self.endpoint = endpoint