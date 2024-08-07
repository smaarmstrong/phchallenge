from django.db import models

class EnclosureModel(models.Model):

    LOCATION_CHOICES = [
        ('adjacent_vehicular_highway', 'Adjacent to a highway used by vehicular traffic'),
        ('facing_listed_building', 'Gate, fence, wall or other means of enclosure face onto a property with a listed building'),
        ('not_applicable', 'Not applicable'),
    ]

    HEIGHT_CHOICES = [
        ('up_to_1m', 'Up to 1 meter'),
        ('above_1m', 'Above 1 meter'),
        ('up_to_2m', 'Up to 2 meters'),
        ('above_2m', 'Above 2 meters'),
        ('not_applicable', 'Not applicable'),
    ]

    PLANNING_CONSTRAINTS = [
        ('listed_building', 'Listed building'),
        ('article_2_3', 'Article 2(3) Land removing permitted development rights for the project'),
        ('article_2_4', 'Article 2(4) Land'),
        ('article_4', 'Article 4 Directive removing the PD rights for the project'),
        ('AONB', 'AONB'),
        ('works_affecting_TPO', 'Works affecting TPO'),
        ('not_applicable', 'Not applicable'),
    ]

    location = models.CharField(max_length=255, choices=LOCATION_CHOICES, default='not_applicable')
    height = models.CharField(max_length=255, choices=HEIGHT_CHOICES, default='not_applicable')
    constraint = models.CharField(max_length=255, choices=PLANNING_CONSTRAINTS, default='not_applicable')
    permission_status = models.CharField(max_length=255, blank=True)