from django.db import models
from django.contrib.auth.models import User


class Url(models.Model):
    GET = 'get'
    POST = 'post'
    PUT = 'put'
    DELETE = 'delete'
    PATCH = 'patch'

    REQUEST_TYPES = (
        (POST, "POST"),
        (PUT, "PUT"),
        (GET, "GET"),
        (DELETE, "DELETE"),
        (PATCH, "PATCH"),
    )

    request_type = models.CharField(
        max_length=20, choices=REQUEST_TYPES, default=GET)
    url = models.URLField()

    def __str__(self):
        return f"{self.request_type} {self.url}"


class UrlSet(models.Model):
    url_set = models.ManyToManyField(Url)

    user = models.OneToOneField(User, on_delete=models.CASCADE)
