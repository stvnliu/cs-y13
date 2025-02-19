class Company:
    def __init__(self, company_name: str, email: str, date_last: str):
        self.__company_name = company_name
        self.__email = email
        self.__date_last = date_last
    def set_date(self, d):
        self.__date_last = d
    def get_name(self):
        return self.__company_name
    def get_email(self):
        return self.__email
    def get_date(self):
        return self.__date_last

c = Company("XX Co. Ltd.", "example@example.com", "date")
