class TypeCall:
    def __init__(self, id_type, type_code, description):
        self._id_type = id_type
        self._type_code = type_code
        self._description = description

    @property
    def id_type(self):
        return self._id_type

    @id_type.setter
    def id_type(self, id_type):
        self._id_type = id_type

    @property
    def type_code(self):
        return self._type_code

    @type_code.setter
    def type_code(self, type_code):
        self._type_code = type_code

    @property
    def description(self):
        return self._description

    @description.setter
    def description(self, description):
        self._description = description
