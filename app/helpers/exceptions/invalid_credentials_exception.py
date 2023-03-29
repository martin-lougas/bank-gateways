class InvalidCredentialsException(Exception):
    """Exception raised for invalid credentials"""

    def __init__(self, message="Invalid credentials"):
        self.message = message
        super().__init__(self.message)
