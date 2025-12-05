from abc import ABC, abstractmethod

class MakeCall(ABC):

    @abstractmethod
    def make_call(self):
        pass

class SendSMS(ABC):
    @abstractmethod
    def send_sms(self):
        pass

class GetInternet(ABC):
    @abstractmethod
    def get_internet(self):
        pass

class IPhone(ConnectioniconDevices):
    def make_call(self):
        print("colling...")
    def send_sms(self):
        print("sending sms to abonent...")
    def get_internet(self):
        print("getting internet connection...")

class SumsungOld(ConnectioniconDevices):
    def make_call(self):


iphine = IPhone()
iphine.make_call()
iphine.send_sms()
iphine.get_internet()