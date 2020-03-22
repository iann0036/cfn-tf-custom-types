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
    Id: Optional[str]
    Location: Optional[str]
    Name: Optional[str]
    ResourceGroupName: Optional[str]
    Tags: Optional[Sequence["_Tags"]]
    CustomRules: Optional[Sequence["_CustomRules"]]
    PolicySettings: Optional[Sequence["_PolicySettings"]]
    Timeouts: Optional["_Timeouts"]
    MatchConditions: Optional[Sequence["_MatchConditions"]]
    MatchVariables: Optional[Sequence["_MatchVariables"]]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceModel"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceModel"]:
        if not json_data:
            return None
        return cls(
            tfcfnid=json_data.get("tfcfnid"),
            Id=json_data.get("Id"),
            Location=json_data.get("Location"),
            Name=json_data.get("Name"),
            ResourceGroupName=json_data.get("ResourceGroupName"),
            Tags=json_data.get("Tags"),
            CustomRules=json_data.get("CustomRules"),
            PolicySettings=json_data.get("PolicySettings"),
            Timeouts=Timeouts._deserialize(json_data.get("Timeouts")),
            MatchConditions=json_data.get("MatchConditions"),
            MatchVariables=json_data.get("MatchVariables"),
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
class CustomRules:
    Action: Optional[str]
    Name: Optional[str]
    Priority: Optional[float]
    RuleType: Optional[str]
    MatchConditions: Optional[Sequence["_MatchConditions"]]

    @classmethod
    def _deserialize(
        cls: Type["_CustomRules"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_CustomRules"]:
        if not json_data:
            return None
        return cls(
            Action=json_data.get("Action"),
            Name=json_data.get("Name"),
            Priority=json_data.get("Priority"),
            RuleType=json_data.get("RuleType"),
            MatchConditions=json_data.get("MatchConditions"),
        )


# work around possible type aliasing issues when variable has same name as a model
_CustomRules = CustomRules


@dataclass
class MatchConditions:
    MatchValues: Optional[Sequence[str]]
    NegationCondition: Optional[bool]
    Operator: Optional[str]
    MatchVariables: Optional[Sequence["_MatchVariables"]]

    @classmethod
    def _deserialize(
        cls: Type["_MatchConditions"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_MatchConditions"]:
        if not json_data:
            return None
        return cls(
            MatchValues=json_data.get("MatchValues"),
            NegationCondition=json_data.get("NegationCondition"),
            Operator=json_data.get("Operator"),
            MatchVariables=json_data.get("MatchVariables"),
        )


# work around possible type aliasing issues when variable has same name as a model
_MatchConditions = MatchConditions


@dataclass
class MatchVariables:
    Selector: Optional[str]
    VariableName: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_MatchVariables"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_MatchVariables"]:
        if not json_data:
            return None
        return cls(
            Selector=json_data.get("Selector"),
            VariableName=json_data.get("VariableName"),
        )


# work around possible type aliasing issues when variable has same name as a model
_MatchVariables = MatchVariables


@dataclass
class PolicySettings:
    Enabled: Optional[bool]
    Mode: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_PolicySettings"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_PolicySettings"]:
        if not json_data:
            return None
        return cls(
            Enabled=json_data.get("Enabled"),
            Mode=json_data.get("Mode"),
        )


# work around possible type aliasing issues when variable has same name as a model
_PolicySettings = PolicySettings


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


