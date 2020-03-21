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
    Name: Optional[str]
    Tags: Optional[Sequence[str]]
    Condition: Optional[Sequence["_Condition"]]
    Formula: Optional[Sequence["_Formula"]]
    Notify: Optional[Sequence["_Notify"]]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceModel"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceModel"]:
        if not json_data:
            return None
        return cls(
            tfcfnid=json_data.get("tfcfnid"),
            Name=json_data.get("Name"),
            Tags=json_data.get("Tags"),
            Condition=json_data.get("Condition"),
            Formula=json_data.get("Formula"),
            Notify=json_data.get("Notify"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class Condition:
    Index: Optional[float]
    MatchingSeverities: Optional[Sequence[str]]
    RuleSet: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Condition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Condition"]:
        if not json_data:
            return None
        return cls(
            Index=json_data.get("Index"),
            MatchingSeverities=json_data.get("MatchingSeverities"),
            RuleSet=json_data.get("RuleSet"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Condition = Condition


@dataclass
class Formula:
    Expression: Optional[str]
    RaiseSeverity: Optional[float]
    Wait: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_Formula"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Formula"]:
        if not json_data:
            return None
        return cls(
            Expression=json_data.get("Expression"),
            RaiseSeverity=json_data.get("RaiseSeverity"),
            Wait=json_data.get("Wait"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Formula = Formula


@dataclass
class Notify:
    Sev1: Optional[Sequence[str]]
    Sev2: Optional[Sequence[str]]
    Sev3: Optional[Sequence[str]]
    Sev4: Optional[Sequence[str]]
    Sev5: Optional[Sequence[str]]

    @classmethod
    def _deserialize(
        cls: Type["_Notify"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Notify"]:
        if not json_data:
            return None
        return cls(
            Sev1=json_data.get("Sev1"),
            Sev2=json_data.get("Sev2"),
            Sev3=json_data.get("Sev3"),
            Sev4=json_data.get("Sev4"),
            Sev5=json_data.get("Sev5"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Notify = Notify


