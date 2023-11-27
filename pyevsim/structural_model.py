# structural_model.py
from .definition import CoreModel, ModelType

class StructuralModel(CoreModel):
    def __init__(self, _name=""):
        super(StructuralModel, self).__init__(_name, ModelType.STRUCTURAL)
        self._models = []

    def insert_model(self, model):
        self._models.append(model)

    def retrieve_models(self):
        return self._models
