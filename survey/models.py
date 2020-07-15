from django.db import models
from django.utils.translation import ugettext_lazy as _

from polymorphic.models import PolymorphicModel


class SurveyStep(models.Model):
    survey = models.ForeignKey("survey.Survey", models.CASCADE)
    title = models.CharField(max_length=255, verbose_name=_("title"))


class Block(PolymorphicModel):
    survey_step = models.ForeignKey("survey.SurveyStep", models.CASCADE)


class BlockMarkdown(Block):
    value = models.TextField(verbose_name=_("Value"))


class BlockRadioGroup(Block):
    label = models.CharField(verbose_name=_("Label"), max_length=255)


class BlockRadioButton(models.Model):
    radio_group = models.ForeignKey(Block, models.CASCADE)
    label = models.CharField(verbose_name=_("Label"), max_length=255)


class Survey(models.Model):
    title = models.CharField(max_length=255, verbose_name=_("Title"))

    def __str__(self):
        return self.title
