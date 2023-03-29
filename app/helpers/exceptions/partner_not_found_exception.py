class PartnerNotFoundException(Exception):
    """Exception raised when a partner cannot be found"""

    def __init__(self, partner_id):
        self.message = f"Partner with ID {partner_id} not found"
        super().__init__(self.message)
