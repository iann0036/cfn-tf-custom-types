# DO NOT modify this file by hand, changes will be overwritten
import sys
from dataclasses import dataclass
from inspect import getmembers, isclass
from typing import (
    AbstractSet,
    Any,
    Generic,
    Mapping,
    MutableMapping,
    Optional,
    Sequence,
    Type,
    TypeVar,
)

from cloudformation_cli_python_lib.interface import (
    BaseModel,
    BaseResourceHandlerRequest,
)
from cloudformation_cli_python_lib.recast import recast_object
from cloudformation_cli_python_lib.utils import deserialize_list

T = TypeVar("T")


def set_or_none(value: Optional[Sequence[T]]) -> Optional[AbstractSet[T]]:
    if value:
        return set(value)
    return None


@dataclass
class ResourceHandlerRequest(BaseResourceHandlerRequest):
    # pylint: disable=invalid-name
    desiredResourceState: Optional["ResourceModel"]
    previousResourceState: Optional["ResourceModel"]


@dataclass
class ResourceModel(BaseModel):
    tfcfnid: Optional[str]
    EnvironmentId: Optional[str]
    Id: Optional[str]
    InitOnly: Optional[bool]
    MandatoryNotes: Optional[str]
    SettingId: Optional[str]
    SettingType: Optional[str]
    Value: Optional[str]
    PercentageItems: Optional[Sequence["_PercentageItemsDefinition"]]
    RolloutRules: Optional[Sequence["_RolloutRulesDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceModel"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceModel"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            tfcfnid=json_data.get("tfcfnid"),
            EnvironmentId=json_data.get("EnvironmentId"),
            Id=json_data.get("Id"),
            InitOnly=json_data.get("InitOnly"),
            MandatoryNotes=json_data.get("MandatoryNotes"),
            SettingId=json_data.get("SettingId"),
            SettingType=json_data.get("SettingType"),
            Value=json_data.get("Value"),
            PercentageItems=deserialize_list(json_data.get("PercentageItems"), PercentageItemsDefinition),
            RolloutRules=deserialize_list(json_data.get("RolloutRules"), RolloutRulesDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class PercentageItemsDefinition(BaseModel):
    Percentage: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_PercentageItemsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_PercentageItemsDefinition"]:
        if not json_data:
            return None
        return cls(
            Percentage=json_data.get("Percentage"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_PercentageItemsDefinition = PercentageItemsDefinition


@dataclass
class RolloutRulesDefinition(BaseModel):
    Comparator: Optional[str]
    ComparisonAttribute: Optional[str]
    ComparisonValue: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_RolloutRulesDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_RolloutRulesDefinition"]:
        if not json_data:
            return None
        return cls(
            Comparator=json_data.get("Comparator"),
            ComparisonAttribute=json_data.get("ComparisonAttribute"),
            ComparisonValue=json_data.get("ComparisonValue"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_RolloutRulesDefinition = RolloutRulesDefinition


