import uuid

from django.db import models


class BaseModel(models.Model):
    """
    A base abstract model providing common fields and functionality for models.

    BaseModel serves as a foundation for other models in your Django application,
    providing commonly used fields and functionality to reduce redundancy and improve maintainability.

    Usage:
        1. Inherit from BaseModel to define your models.
        2. Add specific fields and methods to your models.

    Example:
        class MyModel(BaseModel):
            name = models.CharField(max_length=100)

            def __str__(self):
                return self.name

        my_model = MyModel(name="Example")
        my_model.save()

    Note:
        - BaseModel includes common fields like `created_at`, `updated_at` abd `uid`
          for tracking creation and modification timestamps.
        - You can add more fields and methods specific to your application needs.

    """

    uid = models.UUIDField(
        db_index=True, unique=True, default=uuid.uuid4, editable=False
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
