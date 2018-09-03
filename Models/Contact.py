class Contact:

    def __init__(self, contact_id, name, phone_number, created, is_deleted):
        self._contact_id = contact_id
        self._name = name
        self._phone_number = phone_number
        self._created = created
        self._is_deleted = is_deleted

    @property
    def contact_id(self):
        return self._contact_id

    @contact_id.setter
    def contact_id(self, contact_id):
        self._contact_id = contact_id

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name

    @property
    def phone_number(self):
        return self._phone_number

    @phone_number.setter
    def phone_number(self, phone_number):
        self._phone_number = phone_number

    @property
    def created(self):
        return self._created

    @created.setter
    def created(self, created):
        self._created = created

    @property
    def is_deleted(self):
        return self._is_deleted

    @is_deleted.setter
    def is_deleted(self, is_deleted):
        self.is_deleted = is_deleted
