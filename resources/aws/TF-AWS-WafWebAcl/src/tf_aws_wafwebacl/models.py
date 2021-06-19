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
    Arn: Optional[str]
    Id: Optional[str]
    MetricName: Optional[str]
    Name: Optional[str]
    Tags: Optional[Sequence["_TagsDefinition"]]
    TagsAll: Optional[Sequence["_TagsAllDefinition"]]
    DefaultAction: Optional[Sequence["_DefaultActionDefinition"]]
    LoggingConfiguration: Optional[Sequence["_LoggingConfigurationDefinition"]]
    Rules: Optional[Sequence["_RulesDefinition"]]

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
            Arn=json_data.get("Arn"),
            Id=json_data.get("Id"),
            MetricName=json_data.get("MetricName"),
            Name=json_data.get("Name"),
            Tags=deserialize_list(json_data.get("Tags"), TagsDefinition),
            TagsAll=deserialize_list(json_data.get("TagsAll"), TagsAllDefinition),
            DefaultAction=deserialize_list(json_data.get("DefaultAction"), DefaultActionDefinition),
            LoggingConfiguration=deserialize_list(json_data.get("LoggingConfiguration"), LoggingConfigurationDefinition),
            Rules=deserialize_list(json_data.get("Rules"), RulesDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class TagsDefinition(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_TagsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TagsDefinition"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TagsDefinition = TagsDefinition


@dataclass
class TagsAllDefinition(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_TagsAllDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TagsAllDefinition"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TagsAllDefinition = TagsAllDefinition


@dataclass
class DefaultActionDefinition(BaseModel):
    Type: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_DefaultActionDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DefaultActionDefinition"]:
        if not json_data:
            return None
        return cls(
            Type=json_data.get("Type"),
        )


# work around possible type aliasing issues when variable has same name as a model
_DefaultActionDefinition = DefaultActionDefinition


@dataclass
class LoggingConfigurationDefinition(BaseModel):
    LogDestination: Optional[str]
    RedactedFields: Optional[Sequence["_RedactedFieldsDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_LoggingConfigurationDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_LoggingConfigurationDefinition"]:
        if not json_data:
            return None
        return cls(
            LogDestination=json_data.get("LogDestination"),
            RedactedFields=deserialize_list(json_data.get("RedactedFields"), RedactedFieldsDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_LoggingConfigurationDefinition = LoggingConfigurationDefinition


@dataclass
class RedactedFieldsDefinition(BaseModel):
    FieldToMatch: Optional[Sequence["_FieldToMatchDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_RedactedFieldsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_RedactedFieldsDefinition"]:
        if not json_data:
            return None
        return cls(
            FieldToMatch=deserialize_list(json_data.get("FieldToMatch"), FieldToMatchDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_RedactedFieldsDefinition = RedactedFieldsDefinition


@dataclass
class FieldToMatchDefinition(BaseModel):
    Data: Optional[str]
    Type: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_FieldToMatchDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_FieldToMatchDefinition"]:
        if not json_data:
            return None
        return cls(
            Data=json_data.get("Data"),
            Type=json_data.get("Type"),
        )


# work around possible type aliasing issues when variable has same name as a model
_FieldToMatchDefinition = FieldToMatchDefinition


@dataclass
class RulesDefinition(BaseModel):
    Priority: Optional[float]
    RuleId: Optional[str]
    Type: Optional[str]
    Action: Optional[Sequence["_ActionDefinition"]]
    OverrideAction: Optional[Sequence["_OverrideActionDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_RulesDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_RulesDefinition"]:
        if not json_data:
            return None
        return cls(
            Priority=json_data.get("Priority"),
            RuleId=json_data.get("RuleId"),
            Type=json_data.get("Type"),
            Action=deserialize_list(json_data.get("Action"), ActionDefinition),
            OverrideAction=deserialize_list(json_data.get("OverrideAction"), OverrideActionDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_RulesDefinition = RulesDefinition


@dataclass
class ActionDefinition(BaseModel):
    Type: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ActionDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ActionDefinition"]:
        if not json_data:
            return None
        return cls(
            Type=json_data.get("Type"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ActionDefinition = ActionDefinition


@dataclass
class OverrideActionDefinition(BaseModel):
    Type: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_OverrideActionDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_OverrideActionDefinition"]:
        if not json_data:
            return None
        return cls(
            Type=json_data.get("Type"),
        )


# work around possible type aliasing issues when variable has same name as a model
_OverrideActionDefinition = OverrideActionDefinition


