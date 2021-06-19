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
    Id: Optional[str]
    ServiceId: Optional[str]
    IncidentRule: Optional[Sequence["_IncidentRuleDefinition"]]

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
            Id=json_data.get("Id"),
            ServiceId=json_data.get("ServiceId"),
            IncidentRule=deserialize_list(json_data.get("IncidentRule"), IncidentRuleDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class IncidentRuleDefinition(BaseModel):
    ConditionMatchType: Optional[str]
    Conditions: Optional[Sequence["_ConditionsDefinition"]]
    IncidentProperties: Optional[Sequence["_IncidentPropertiesDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_IncidentRuleDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_IncidentRuleDefinition"]:
        if not json_data:
            return None
        return cls(
            ConditionMatchType=json_data.get("ConditionMatchType"),
            Conditions=deserialize_list(json_data.get("Conditions"), ConditionsDefinition),
            IncidentProperties=deserialize_list(json_data.get("IncidentProperties"), IncidentPropertiesDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_IncidentRuleDefinition = IncidentRuleDefinition


@dataclass
class ConditionsDefinition(BaseModel):
    ExpectedValue: Optional[str]
    Field: Optional[str]
    Key: Optional[str]
    Not: Optional[bool]
    Operation: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ConditionsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ConditionsDefinition"]:
        if not json_data:
            return None
        return cls(
            ExpectedValue=json_data.get("ExpectedValue"),
            Field=json_data.get("Field"),
            Key=json_data.get("Key"),
            Not=json_data.get("Not"),
            Operation=json_data.get("Operation"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ConditionsDefinition = ConditionsDefinition


@dataclass
class IncidentPropertiesDefinition(BaseModel):
    Description: Optional[str]
    Details: Optional[Sequence["_DetailsDefinition"]]
    Message: Optional[str]
    Priority: Optional[str]
    Tags: Optional[Sequence[str]]
    StakeholderProperties: Optional[Sequence["_StakeholderPropertiesDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_IncidentPropertiesDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_IncidentPropertiesDefinition"]:
        if not json_data:
            return None
        return cls(
            Description=json_data.get("Description"),
            Details=deserialize_list(json_data.get("Details"), DetailsDefinition),
            Message=json_data.get("Message"),
            Priority=json_data.get("Priority"),
            Tags=json_data.get("Tags"),
            StakeholderProperties=deserialize_list(json_data.get("StakeholderProperties"), StakeholderPropertiesDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_IncidentPropertiesDefinition = IncidentPropertiesDefinition


@dataclass
class DetailsDefinition(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_DetailsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DetailsDefinition"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_DetailsDefinition = DetailsDefinition


@dataclass
class StakeholderPropertiesDefinition(BaseModel):
    Description: Optional[str]
    Enable: Optional[bool]
    Message: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_StakeholderPropertiesDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_StakeholderPropertiesDefinition"]:
        if not json_data:
            return None
        return cls(
            Description=json_data.get("Description"),
            Enable=json_data.get("Enable"),
            Message=json_data.get("Message"),
        )


# work around possible type aliasing issues when variable has same name as a model
_StakeholderPropertiesDefinition = StakeholderPropertiesDefinition


