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
    Id: Optional[str]
    Name: Optional[str]
    NumLoops: Optional[float]
    Teams: Optional[Sequence[str]]
    Rule: Optional[Sequence["_Rule"]]
    Target: Optional[Sequence["_Target"]]

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
            Id=json_data.get("Id"),
            Name=json_data.get("Name"),
            NumLoops=json_data.get("NumLoops"),
            Teams=json_data.get("Teams"),
            Rule=json_data.get("Rule"),
            Target=json_data.get("Target"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class Rule:
    EscalationDelayInMinutes: Optional[float]
    Target: Optional[Sequence["_Target"]]

    @classmethod
    def _deserialize(
        cls: Type["_Rule"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Rule"]:
        if not json_data:
            return None
        return cls(
            EscalationDelayInMinutes=json_data.get("EscalationDelayInMinutes"),
            Target=json_data.get("Target"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Rule = Rule


@dataclass
class Target:
    Id: Optional[str]
    Type: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Target"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Target"]:
        if not json_data:
            return None
        return cls(
            Id=json_data.get("Id"),
            Type=json_data.get("Type"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Target = Target


