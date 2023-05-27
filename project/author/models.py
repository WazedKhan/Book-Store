from django.db import models

from common.models import BaseModel


class Author(BaseModel):
    """
    Model representing an author.

    Inherits from the BaseModel providing common fields and functionality for models.

    Fields:
        - name (CharField): The name of the author.
        - age (IntegerField): The age of the author.

    Methods:
        - __str__: Returns a string representation of the author object.

    Example:
        author = Author(name="John Doe", age=30)
        author.save()

    """

    name = models.CharField(max_length=100)
    age = models.IntegerField()

    def __str__(self):
        return f"{self.id}: Name: {self.name} - Age: {self.age}"
