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
    CustomBlockResponseBody: Optional[str]
    CustomBlockResponseStatusCode: Optional[float]
    Enabled: Optional[bool]
    FrontendEndpointIds: Optional[Sequence[str]]
    Id: Optional[str]
    Location: Optional[str]
    Mode: Optional[str]
    Name: Optional[str]
    RedirectUrl: Optional[str]
    ResourceGroupName: Optional[str]
    Tags: Optional[Sequence["_Tags"]]
    CustomRule: Optional[Sequence["_CustomRule"]]
    ManagedRule: Optional[Sequence["_ManagedRule"]]
    Timeouts: Optional["_Timeouts"]
    MatchCondition: Optional[Sequence["_MatchCondition"]]
    Exclusion: Optional[Sequence["_Exclusion"]]
    Override: Optional[Sequence["_Override"]]
    Rule: Optional[Sequence["_Rule"]]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceModel"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceModel"]:
        if not json_data:
            return None
        return cls(
            tfcfnid=json_data.get("tfcfnid"),
            CustomBlockResponseBody=json_data.get("CustomBlockResponseBody"),
            CustomBlockResponseStatusCode=json_data.get("CustomBlockResponseStatusCode"),
            Enabled=json_data.get("Enabled"),
            FrontendEndpointIds=json_data.get("FrontendEndpointIds"),
            Id=json_data.get("Id"),
            Location=json_data.get("Location"),
            Mode=json_data.get("Mode"),
            Name=json_data.get("Name"),
            RedirectUrl=json_data.get("RedirectUrl"),
            ResourceGroupName=json_data.get("ResourceGroupName"),
            Tags=json_data.get("Tags"),
            CustomRule=json_data.get("CustomRule"),
            ManagedRule=json_data.get("ManagedRule"),
            Timeouts=Timeouts._deserialize(json_data.get("Timeouts")),
            MatchCondition=json_data.get("MatchCondition"),
            Exclusion=json_data.get("Exclusion"),
            Override=json_data.get("Override"),
            Rule=json_data.get("Rule"),
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
class CustomRule:
    Action: Optional[str]
    Enabled: Optional[bool]
    Name: Optional[str]
    Priority: Optional[float]
    RateLimitDurationInMinutes: Optional[float]
    RateLimitThreshold: Optional[float]
    Type: Optional[str]
    MatchCondition: Optional[Sequence["_MatchCondition"]]

    @classmethod
    def _deserialize(
        cls: Type["_CustomRule"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_CustomRule"]:
        if not json_data:
            return None
        return cls(
            Action=json_data.get("Action"),
            Enabled=json_data.get("Enabled"),
            Name=json_data.get("Name"),
            Priority=json_data.get("Priority"),
            RateLimitDurationInMinutes=json_data.get("RateLimitDurationInMinutes"),
            RateLimitThreshold=json_data.get("RateLimitThreshold"),
            Type=json_data.get("Type"),
            MatchCondition=json_data.get("MatchCondition"),
        )


# work around possible type aliasing issues when variable has same name as a model
_CustomRule = CustomRule


@dataclass
class MatchCondition:
    MatchValues: Optional[Sequence[str]]
    MatchVariable: Optional[str]
    NegationCondition: Optional[bool]
    Operator: Optional[str]
    Selector: Optional[str]
    Transforms: Optional[Sequence[str]]

    @classmethod
    def _deserialize(
        cls: Type["_MatchCondition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_MatchCondition"]:
        if not json_data:
            return None
        return cls(
            MatchValues=json_data.get("MatchValues"),
            MatchVariable=json_data.get("MatchVariable"),
            NegationCondition=json_data.get("NegationCondition"),
            Operator=json_data.get("Operator"),
            Selector=json_data.get("Selector"),
            Transforms=json_data.get("Transforms"),
        )


# work around possible type aliasing issues when variable has same name as a model
_MatchCondition = MatchCondition


@dataclass
class ManagedRule:
    Type: Optional[str]
    Version: Optional[str]
    Exclusion: Optional[Sequence["_Exclusion"]]
    Override: Optional[Sequence["_Override"]]

    @classmethod
    def _deserialize(
        cls: Type["_ManagedRule"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ManagedRule"]:
        if not json_data:
            return None
        return cls(
            Type=json_data.get("Type"),
            Version=json_data.get("Version"),
            Exclusion=json_data.get("Exclusion"),
            Override=json_data.get("Override"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ManagedRule = ManagedRule


@dataclass
class Exclusion:
    MatchVariable: Optional[str]
    Operator: Optional[str]
    Selector: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Exclusion"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Exclusion"]:
        if not json_data:
            return None
        return cls(
            MatchVariable=json_data.get("MatchVariable"),
            Operator=json_data.get("Operator"),
            Selector=json_data.get("Selector"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Exclusion = Exclusion


@dataclass
class Override:
    RuleGroupName: Optional[str]
    Exclusion: Optional[Sequence["_Exclusion"]]
    Rule: Optional[Sequence["_Rule"]]

    @classmethod
    def _deserialize(
        cls: Type["_Override"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Override"]:
        if not json_data:
            return None
        return cls(
            RuleGroupName=json_data.get("RuleGroupName"),
            Exclusion=json_data.get("Exclusion"),
            Rule=json_data.get("Rule"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Override = Override


@dataclass
class Rule:
    Action: Optional[str]
    Enabled: Optional[bool]
    RuleId: Optional[str]
    Exclusion: Optional[Sequence["_Exclusion"]]

    @classmethod
    def _deserialize(
        cls: Type["_Rule"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Rule"]:
        if not json_data:
            return None
        return cls(
            Action=json_data.get("Action"),
            Enabled=json_data.get("Enabled"),
            RuleId=json_data.get("RuleId"),
            Exclusion=json_data.get("Exclusion"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Rule = Rule


@dataclass
class Timeouts:
    Create: Optional[str]
    Delete: Optional[str]
    Read: Optional[str]
    Update: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Timeouts"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Timeouts"]:
        if not json_data:
            return None
        return cls(
            Create=json_data.get("Create"),
            Delete=json_data.get("Delete"),
            Read=json_data.get("Read"),
            Update=json_data.get("Update"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Timeouts = Timeouts


