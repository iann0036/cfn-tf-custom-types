# DO NOT modify this file by hand, changes will be overwritten
from dataclasses import dataclass
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
    BaseResourceHandlerRequest,
    BaseResourceModel,
)

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
class ResourceModel(BaseResourceModel):
    tfcfnid: Optional[str]
    Arn: Optional[str]
    Id: Optional[str]
    MetricName: Optional[str]
    Name: Optional[str]
    Tags: Optional[Sequence["_Tags"]]
    DefaultAction: Optional[Sequence["_DefaultAction"]]
    LoggingConfiguration: Optional[Sequence["_LoggingConfiguration"]]
    Rule: Optional[Sequence["_Rule"]]
    RedactedFields: Optional[Sequence["_RedactedFields"]]
    Action: Optional[Sequence["_Action"]]
    OverrideAction: Optional[Sequence["_OverrideAction"]]
    FieldToMatch: Optional[Sequence["_FieldToMatch"]]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceModel"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceModel"]:
        if not json_data:
            return None
        return cls(
            tfcfnid=json_data.get("tfcfnid"),
            Arn=json_data.get("Arn"),
            Id=json_data.get("Id"),
            MetricName=json_data.get("MetricName"),
            Name=json_data.get("Name"),
            Tags=json_data.get("Tags"),
            DefaultAction=json_data.get("DefaultAction"),
            LoggingConfiguration=json_data.get("LoggingConfiguration"),
            Rule=json_data.get("Rule"),
            RedactedFields=json_data.get("RedactedFields"),
            Action=json_data.get("Action"),
            OverrideAction=json_data.get("OverrideAction"),
            FieldToMatch=json_data.get("FieldToMatch"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class Tags:
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Tags"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Tags"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Tags = Tags


@dataclass
class DefaultAction:
    Type: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_DefaultAction"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DefaultAction"]:
        if not json_data:
            return None
        return cls(
            Type=json_data.get("Type"),
        )


# work around possible type aliasing issues when variable has same name as a model
_DefaultAction = DefaultAction


@dataclass
class LoggingConfiguration:
    LogDestination: Optional[str]
    RedactedFields: Optional[Sequence["_RedactedFields"]]

    @classmethod
    def _deserialize(
        cls: Type["_LoggingConfiguration"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_LoggingConfiguration"]:
        if not json_data:
            return None
        return cls(
            LogDestination=json_data.get("LogDestination"),
            RedactedFields=json_data.get("RedactedFields"),
        )


# work around possible type aliasing issues when variable has same name as a model
_LoggingConfiguration = LoggingConfiguration


@dataclass
class RedactedFields:
    FieldToMatch: Optional[Sequence["_FieldToMatch"]]

    @classmethod
    def _deserialize(
        cls: Type["_RedactedFields"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_RedactedFields"]:
        if not json_data:
            return None
        return cls(
            FieldToMatch=json_data.get("FieldToMatch"),
        )


# work around possible type aliasing issues when variable has same name as a model
_RedactedFields = RedactedFields


@dataclass
class FieldToMatch:
    Data: Optional[str]
    Type: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_FieldToMatch"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_FieldToMatch"]:
        if not json_data:
            return None
        return cls(
            Data=json_data.get("Data"),
            Type=json_data.get("Type"),
        )


# work around possible type aliasing issues when variable has same name as a model
_FieldToMatch = FieldToMatch


@dataclass
class Rule:
    Priority: Optional[float]
    RuleId: Optional[str]
    Type: Optional[str]
    Action: Optional[Sequence["_Action"]]
    OverrideAction: Optional[Sequence["_OverrideAction"]]

    @classmethod
    def _deserialize(
        cls: Type["_Rule"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Rule"]:
        if not json_data:
            return None
        return cls(
            Priority=json_data.get("Priority"),
            RuleId=json_data.get("RuleId"),
            Type=json_data.get("Type"),
            Action=json_data.get("Action"),
            OverrideAction=json_data.get("OverrideAction"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Rule = Rule


@dataclass
class Action:
    Type: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Action"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Action"]:
        if not json_data:
            return None
        return cls(
            Type=json_data.get("Type"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Action = Action


@dataclass
class OverrideAction:
    Type: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_OverrideAction"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_OverrideAction"]:
        if not json_data:
            return None
        return cls(
            Type=json_data.get("Type"),
        )


# work around possible type aliasing issues when variable has same name as a model
_OverrideAction = OverrideAction


