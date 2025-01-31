class UpdateMixin:
    def update_fields_fro_entity(self, source_object, fields: list[str]):
        """
        Копирует перечисленные поля из source_object в self (ORM-модель).
        """
        for field in fields:
            if hasattr(source_object, field):
                setattr(self, field, getattr(source_object, field))
