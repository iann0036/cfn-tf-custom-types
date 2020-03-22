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
    DefaultAction: Optional[str]
    EdgeGateway: Optional[str]
    Id: Optional[str]
    Org: Optional[str]
    Vdc: Optional[str]
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
            DefaultAction=json_data.get("DefaultAction"),
            EdgeGateway=json_data.get("EdgeGateway"),
            Id=json_data.get("Id"),
            Org=json_data.get("Org"),
            Vdc=json_data.get("Vdc"),
            Rule=json_data.get("Rule"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class Rule:
    Description: Optional[str]
    DestinationIp: Optional[str]
    DestinationPort: Optional[str]
    Id: Optional[str]
    Policy: Optional[str]
    Protocol: Optional[str]
    SourceIp: Optional[str]
    SourcePort: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Rule"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Rule"]:
        if not json_data:
            return None
        return cls(
            Description=json_data.get("Description"),
            DestinationIp=json_data.get("DestinationIp"),
            DestinationPort=json_data.get("DestinationPort"),
            Id=json_data.get("Id"),
            Policy=json_data.get("Policy"),
            Protocol=json_data.get("Protocol"),
            SourceIp=json_data.get("SourceIp"),
            SourcePort=json_data.get("SourcePort"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Rule = Rule


