class NotRequest(ValueError):
    def __init__(self):
        msg ="it is not http request!"
        super(ValueError,self).__init__(msg)
        self.message = msg
    def __str__(self):
        return self.message
