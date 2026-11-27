from django.core.validators import FileExtensionValidator
from django.db import models
from django.core.exceptions import ValidationError
from django.utils import timezone   
from AccountApp.models import Doctor, Patient


class Appointment(models.Model):
    reason = models.TextField(max_length=50, blank=True)
    prescription = models.FileField(
        blank=True,
        upload_to='prescriptions/',
        validators=[
            FileExtensionValidator(allowed_extensions=['pdf'],
            message="Le fichier doit être au format PDF.")

        ]
    )
    class Status(models.TextChoices):
        PENDING = 'PENDING', 'En attente'
        CONFIRMED = 'CONFIRMED', 'Confirmé'
        CANCELLED = 'CANCELLED', 'Annulé'
    status = models.CharField(max_length=20, choices=Status.choices, default=Status.PENDING)
    #status = models.CharField(max_length=20, choices=[('PENDING', 'En attente'), ('CONFIRMED', 'Confirmé'), ('CANCELLED', 'Annulé')], default='PENDING')
    duration_mintues=models.PositiveIntegerField(default=30)
    doctor=models.ForeignKey(Doctor, on_delete=models.CASCADE, related_name='appointments')
    patient=models.ForeignKey(Patient, on_delete=models.CASCADE, related_name='appointments')
    # created_at=models.DateField(auto_now_add=True)
    # updated_at=models.DateField(auto_now=True)

    appointment_date = models.DateField()
    def clean(self):
        modified_date=self._state.adding or(
            Appointment.objects.filter(
                pk=self.pk,
                appointment_date=self.appointment_date
            ).exists()
        )
        if modified_date and self.appointment_date <= timezone.localdate():
            raise ValidationError("La date du rendez-vous doit être dans le futur.")
    class Meta:
        ordering = ['appointment_date']    
        constraints = [
            models.UniqueConstraint(fields=['doctor','appointment_date'],       
                name='unique_appointment_date',
                violation_error_message="Un rendez-vous est déjà fixé pour ce médecin à cette date.")
            ]
            