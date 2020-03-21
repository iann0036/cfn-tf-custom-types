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
    SecurityGroupId: Optional[str]
    InboundRule: Optional[Sequence["_InboundRule"]]
    OutboundRule: Optional[Sequence["_OutboundRule"]]

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
            SecurityGroupId=json_data.get("SecurityGroupId"),
            InboundRule=json_data.get("InboundRule"),
            OutboundRule=json_data.get("OutboundRule"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class InboundRule:
    Action: Optional[str]
    Ip: Optional[str]
    IpRange: Optional[str]
    Port: Optional[float]
    PortRange: Optional[str]
    Protocol: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_InboundRule"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_InboundRule"]:
        if not json_data:
            return None
        return cls(
            Action=json_data.get("Action"),
            Ip=json_data.get("Ip"),
            IpRange=json_data.get("IpRange"),
            Port=json_data.get("Port"),
            PortRange=json_data.get("PortRange"),
            Protocol=json_data.get("Protocol"),
        )


# work around possible type aliasing issues when variable has same name as a model
_InboundRule = InboundRule


@dataclass
class OutboundRule:
    Action: Optional[str]
    Ip: Optional[str]
    IpRange: Optional[str]
    Port: Optional[float]
    PortRange: Optional[str]
    Protocol: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_OutboundRule"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_OutboundRule"]:
        if not json_data:
            return None
        return cls(
            Action=json_data.get("Action"),
            Ip=json_data.get("Ip"),
            IpRange=json_data.get("IpRange"),
            Port=json_data.get("Port"),
            PortRange=json_data.get("PortRange"),
            Protocol=json_data.get("Protocol"),
        )


# work around possible type aliasing issues when variable has same name as a model
_OutboundRule = OutboundRule


