import facebook


class channel(object): #Abstract class for all channels
    def authenticate(self):
        raise NotImplementedError

    def broadcast(self):
        raise NotImplementedError


class fb(channel): #Class for facebook

    def __init__(self, token, message):
        self.access_token = token
        self.post = message
        self.status = "Success"
        self.error_code = 0
        
    def broadcast(self, graph):
        try:
            
            print "starting broadcast"
            graph.put_object("me", "feed", message = self.post)
            self.error_code = 1
            
        except facebook.GraphAPIError as err: 
            self.error_code = -1
            if 'expired' in err[0]:
                self.status = "Token expired"
            elif 'status' in err[0]:
                self.status = "Duplicate message"
            elif 'limit reached' in err[0]:
                self.status = "Feed limit reached. Please Try again after 24 hours"
