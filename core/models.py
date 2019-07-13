from django.db import models


class FibNumber(models.Model):
    original_number = models.DecimalField(
        "Número", max_digits=99, decimal_places=0
    )
    fib_number = models.DecimalField(
        "Fibonacci Número", max_digits=99, decimal_places=0, null=True
    )

    def __str__(self):
        return f"{self.original_number}: fibonacci {self.fib_number}"
