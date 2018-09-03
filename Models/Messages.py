class Message:
    def __init__(self, message_id, message, phonenumber, belongs_to_contact, created, box_id, is_deleted, updated):
        self._message_id = message_id
        self._message = message
        self._phonenumber = phonenumber
        self._belongs_to_contact = belongs_to_contact
        self._created = created
        self._box_id = box_id
        self._is_deleted = is_deleted
        self._updated = updated

    @property
    def message_id(self):
        return self._message_id

    @message_id.setter
    def message_id(self, message_id):
        self._message_id = message_id

    @property
    def message(self):
        return self._message

    @message.setter
    def message(self, message):
        self._message = message

    @property
    def phonenumber(self):
        return self._phonenumber

    @phonenumber.setter
    def phonenumber(self, phonenumber):
        self._phonenumber = phonenumber

    @property
    def belongs_to_contact(self):
        return self._belongs_to_contact

    @belongs_to_contact.setter
    def belongs_to_contact(self, belongs_to_contact):
        self._belongs_to_contact = belongs_to_contact

    @property
    def created(self):
        return self._created

    @created.setter
    def created(self, created):
        self._created = created

    @property
    def box_id(self):
        return self._box_id

    @box_id.setter
    def box_id(self, box_id):
        self._box_id = box_id

    @property
    def is_deleted(self):
        return self._is_deleted

    @is_deleted.setter
    def is_deleted(self, is_deleted):
        self._is_deleted = is_deleted

    @property
    def updated(self):
        return self._updated

    @updated.setter
    def updated(self, updated):
        self._updated = updated
