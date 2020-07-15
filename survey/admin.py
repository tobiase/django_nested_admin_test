import nested_admin
from django.contrib import admin

from survey.models import (
    BlockMarkdown,
    Survey,
    Block,
    SurveyStep,
    BlockRadioGroup,
    BlockRadioButton,
)


class BlockRadioButtonInline(nested_admin.NestedTabularInline):
    model = BlockRadioButton


class BlockInline(nested_admin.NestedStackedPolymorphicInline):
    model = Block

    class BlockMarkdownInline(nested_admin.NestedStackedPolymorphicInline.Child):
        model = BlockMarkdown

    class BlockRadioGroupInline(nested_admin.NestedStackedPolymorphicInline.Child):
        model = BlockRadioGroup
        inlines = [BlockRadioButtonInline]

    child_inlines = (
        BlockMarkdownInline,
        BlockRadioGroupInline,
    )


class SurveyStepInline(nested_admin.NestedStackedInline):
    model = SurveyStep
    inlines = [BlockInline]
    extra = 1


@admin.register(Survey)
class SurveyAdmin(nested_admin.NestedPolymorphicModelAdmin):
    inlines = [SurveyStepInline]
