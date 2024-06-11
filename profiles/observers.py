class Subject:
    def __init__(self):
        self.observers = []

    def attach(self, observer):
        self.observers.append(observer)

    def detach(self, observer):
        self.observers.remove(observer)

    def notify(self):
        for observer in self.observers:
            observer.update()

class UserLoginNotifier(Subject):
    def login(self, user):
        print(f"Привет, {user.username}! Добро пожаловать в нашу систему!")
        self.notify()

class UserGreetingObserver:
    def __init__(self, subject):
        self.subject = subject
        self.subject.attach(self)

    def update(self):
        print("Получено уведомление о входе пользователя")