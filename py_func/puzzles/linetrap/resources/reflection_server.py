from twisted.internet.protocol import ServerFactory
from twisted.protocols.basic import NetstringReceiver
import re

class TrapformService:

    
    def kayla(self, data):
        return data + "~~"

    def thelength(self, data):
        return str(len(data))

    def upper(self, data):
        return data.upper()

    def lower(self, data):
        return data.lower()

    def reverse(self, data):
        return data[::-1]
    
    def wollsmoth(self, data):
        woll = data.replace("a", "o")
        woll = woll.replace("e", "o")
        woll = woll.replace("i", "o")
        woll = woll.replace("u", "o")
        return woll
    
    def swapcase(self, data):
        return data.swapcase()
    
    def admin(self, data):
        
        data = data.strip().lower()
        
        fields = {
                  "author": "amon",
                  "language": "python",
                  "etc": "lazy",
                  "montypython": "slap that fish",
                  "goodmusic": "best coast",
                  "creepy": "xudong",
                  "free": "as in freedom",
                  "clerks": "better than clerks II",
                  "jay": "and silent bob!",
                  "team": "hiromi, amon, chonnu, fats, pedo",
                  "ctf": "win it",
                  "newt": "I got better",
                  "ni": "We no longer say that",
                  "flag": "420chan.org/cd/isseedy",
                  "voting": "http://xkcd.com/463/",
                  "python": "http://xkcd.com/353/",
                  "montypython": "http://xkcd.com/16/",
                  "hamster": "http://xkcd.com/413/",
                  "java": "http://xkcd.com/801/",
                  "yaymalefeminism": "http://xkcd.com/322/",
                  "lisp": "do it.",
                  "windowscopy": "http://xkcd.com/612/",
                  "sudo": "http://xkcd.com/149/",
                  "overused": "http://www.xkcd.com/303/",
                  "dotheyevenexist?": "http://xkcd.com/202/",
                  "lookingfordndplayers": "http://xkcd.com/244/",
                  "crypto": "http://www.xkcd.com/153/",
                  "science": "http://xkcd.com/683/",
                  "meneither": "http://www.xkcd.com/245/"
                  }
        
        if data in fields.keys():
            return fields.get(data)
        elif data == "validkeys":
            return "Valid keys: " + ", ".join(fields.keys())
        else:
            return "That is not a valid properties key (Issue validkeys to get a valid key list)."

class TrapformProtocol(NetstringReceiver):

    def stringReceived(self, request):
        pattern = re.compile(r"^\<(\w+)\>(.+)")
        matches = pattern.match(request)
        
        if matches:
            f_name, data = matches.groups()
        else:
            self.transport.loseConnection()
            return

        self.trapformRequestReceived(f_name, data)

    def trapformRequestReceived(self, f_name, data):
        trapformed_data = self.factory.trapform(f_name, data)
        
        if trapformed_data:
            self.sendString(trapformed_data)
        else:
            self.sendString("No such function")
            
        self.transport.loseConnection()

class TrapformFactory(ServerFactory):
    protocol = TrapformProtocol

    def __init__(self, service):
        self.service = service

    def trapform(self, f_name, data):
        vfunc = getattr(self.service, f_name, None)

        if vfunc is None:
            return None
        else:
            return vfunc(data)

            
            
def main():
    service = TrapformService()
    factory = TrapformFactory(service)

    from twisted.internet import reactor
    reactor.listenTCP(10000, factory)
    reactor.run()

if __name__ == "__main__":
    main()
    
