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
    Description: Optional[str]
    DisplayName: Optional[str]
    Id: Optional[str]
    InsertBefore: Optional[str]
    IsDefault: Optional[bool]
    Revision: Optional[float]
    SectionType: Optional[str]
    Stateful: Optional[bool]
    AppliedTo: Optional[Sequence["_AppliedTo"]]
    Rule: Optional[Sequence["_Rule"]]
    Tag: Optional[Sequence["_Tag"]]
    Destination: Optional[Sequence["_Destination"]]
    Service: Optional[Sequence["_Service"]]
    Source: Optional[Sequence["_Source"]]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceModel"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceModel"]:
        if not json_data:
            return None
        return cls(
            tfcfnid=json_data.get("tfcfnid"),
            Description=json_data.get("Description"),
            DisplayName=json_data.get("DisplayName"),
            Id=json_data.get("Id"),
            InsertBefore=json_data.get("InsertBefore"),
            IsDefault=json_data.get("IsDefault"),
            Revision=json_data.get("Revision"),
            SectionType=json_data.get("SectionType"),
            Stateful=json_data.get("Stateful"),
            AppliedTo=json_data.get("AppliedTo"),
            Rule=json_data.get("Rule"),
            Tag=json_data.get("Tag"),
            Destination=json_data.get("Destination"),
            Service=json_data.get("Service"),
            Source=json_data.get("Source"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class AppliedTo:
    TargetId: Optional[str]
    TargetType: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_AppliedTo"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AppliedTo"]:
        if not json_data:
            return None
        return cls(
            TargetId=json_data.get("TargetId"),
            TargetType=json_data.get("TargetType"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AppliedTo = AppliedTo


@dataclass
class Rule:
    Action: Optional[str]
    Description: Optional[str]
    DestinationsExcluded: Optional[bool]
    Direction: Optional[str]
    Disabled: Optional[bool]
    DisplayName: Optional[str]
    IpProtocol: Optional[str]
    Logged: Optional[bool]
    Notes: Optional[str]
    RuleTag: Optional[str]
    SourcesExcluded: Optional[bool]
    AppliedTo: Optional[Sequence["_AppliedTo"]]
    Destination: Optional[Sequence["_Destination"]]
    Service: Optional[Sequence["_Service"]]
    Source: Optional[Sequence["_Source"]]

    @classmethod
    def _deserialize(
        cls: Type["_Rule"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Rule"]:
        if not json_data:
            return None
        return cls(
            Action=json_data.get("Action"),
            Description=json_data.get("Description"),
            DestinationsExcluded=json_data.get("DestinationsExcluded"),
            Direction=json_data.get("Direction"),
            Disabled=json_data.get("Disabled"),
            DisplayName=json_data.get("DisplayName"),
            IpProtocol=json_data.get("IpProtocol"),
            Logged=json_data.get("Logged"),
            Notes=json_data.get("Notes"),
            RuleTag=json_data.get("RuleTag"),
            SourcesExcluded=json_data.get("SourcesExcluded"),
            AppliedTo=json_data.get("AppliedTo"),
            Destination=json_data.get("Destination"),
            Service=json_data.get("Service"),
            Source=json_data.get("Source"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Rule = Rule


@dataclass
class Destination:
    TargetId: Optional[str]
    TargetType: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Destination"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Destination"]:
        if not json_data:
            return None
        return cls(
            TargetId=json_data.get("TargetId"),
            TargetType=json_data.get("TargetType"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Destination = Destination


@dataclass
class Service:
    TargetId: Optional[str]
    TargetType: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Service"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Service"]:
        if not json_data:
            return None
        return cls(
            TargetId=json_data.get("TargetId"),
            TargetType=json_data.get("TargetType"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Service = Service


@dataclass
class Source:
    TargetId: Optional[str]
    TargetType: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Source"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Source"]:
        if not json_data:
            return None
        return cls(
            TargetId=json_data.get("TargetId"),
            TargetType=json_data.get("TargetType"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Source = Source


@dataclass
class Tag:
    Scope: Optional[str]
    Tag: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Tag"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Tag"]:
        if not json_data:
            return None
        return cls(
            Scope=json_data.get("Scope"),
            Tag=json_data.get("Tag"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Tag = Tag


