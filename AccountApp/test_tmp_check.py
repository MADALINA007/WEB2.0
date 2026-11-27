from datetime import date, timedelta

from django.core.exceptions import ValidationError
from django.test import TestCase

from .models import Doctor, Patient, Speciality


class ModelSmokeTests(TestCase):
    def test_doctor_and_patient(self):
        doctor = Doctor.objects.create(
            username='doc',
            password='test-password',
            license_number='ABC123',
            phone='12345678',
        )
        patient = Patient.objects.create(
            username='pat',
            password='test-password',
            phone='87654321',
            birth_date=date(2000, 1, 1),
        )
        speciality = Speciality.objects.create(name='Cardiology')
        speciality.doctors.add(doctor)

        doctor.full_clean()
        patient.full_clean()
        self.assertEqual(speciality.doctors.count(), 1)

        with self.assertRaises(ValidationError):
            Patient(
                username='future',
                password='test-password',
                phone='11111111',
                birth_date=date.today() + timedelta(days=1),
            ).full_clean()
