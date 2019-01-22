
class ApiError(Exception):
    def __init__(self, error, status_code):
        self.message = error
        self.status_code = status_code

    def __str__(self):
        return self.message
