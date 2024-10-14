class Expense:
    def __init__(self, expense_id=None, user_id=None, amount=None, category_id=None, category_name=None, date=None, description=None):
        self.__expense_id = expense_id
        self.__user_id = user_id
        self.__amount = amount
        self.__category_id = category_id
        self.__category_name = category_name  
        self.__date = date
        self.__description = description

    # Getters
    def get_expense_id(self):
        return self.__expense_id

    def get_user_id(self):
        return self.__user_id

    def get_amount(self):
        return self.__amount

    def get_category_id(self):
        return self.__category_id

    def get_category_name(self):  
        return self.__category_name

    def get_date(self):
        return self.__date

    def get_description(self):
        return self.__description

    # Setters
    def set_expense_id(self, expense_id):
        self.__expense_id = expense_id

    def set_user_id(self, user_id):
        self.__user_id = user_id

    def set_amount(self, amount):
        self.__amount = amount

    def set_category_id(self, category_id):
        self.__category_id = category_id

    def set_category_name(self, category_name):  
        self.__category_name = category_name

    def set_date(self, date):
        self.__date = date

    def set_description(self, description):
        self.__description = description
