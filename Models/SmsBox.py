class SmsBox:
    def __init__(self, id_box, box_code, description):
        self._id_box = id_box
        self._box_code = box_code
        self._description = description

    @property
    def id_box(self):
        return self._id_box

    @id_box.setter
    def id_box(self, id_box):
        self._id_box = id_box

    @property
    def box_code(self):
        return self._box_code

    @box_code.setter
    def box_code(self, box_code):
        self._box_code = box_code

    @property
    def description(self):
        return self._description

    @description.setter
    def description(self, description):
        self.description = description
