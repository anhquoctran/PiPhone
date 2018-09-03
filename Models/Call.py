class CallsLog:

    def __init__(self, id_call, from_number, to_number, duration, time, type_call, is_deleted):
        self._id_call = id_call
        self._from_number = from_number
        self._to_number = to_number
        self._duration = duration
        self._time = time
        self._type_call = type_call
        self._is_deleted = is_deleted

    @property
    def id_call(self):
        return self._id_call

    @id_call.setter
    def id_call(self, id_call):
        self._id_call = id_call

    @property
    def from_number(self):
        return self._from_number

    @from_number.setter
    def from_number(self, from_number):
        self._from_number = from_number

    @property
    def to_number(self):
        return self._to_number

    @to_number.setter
    def to_number(self, to_number):
        self.to_number = to_number
