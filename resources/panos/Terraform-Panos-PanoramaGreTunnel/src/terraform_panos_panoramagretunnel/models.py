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
    CopyTos: Optional[bool]
    Disabled: Optional[bool]
    EnableKeepAlive: Optional[bool]
    Interface: Optional[str]
    KeepAliveHoldTimer: Optional[float]
    KeepAliveInterval: Optional[float]
    KeepAliveRetry: Optional[float]
    LocalAddressType: Optional[str]
    LocalAddressValue: Optional[str]
    Name: Optional[str]
    PeerAddress: Optional[str]
    Template: Optional[str]
    Ttl: Optional[float]
    TunnelInterface: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceModel"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceModel"]:
        if not json_data:
            return None
        return cls(
            tfcfnid=json_data.get("tfcfnid"),
            CopyTos=json_data.get("CopyTos"),
            Disabled=json_data.get("Disabled"),
            EnableKeepAlive=json_data.get("EnableKeepAlive"),
            Interface=json_data.get("Interface"),
            KeepAliveHoldTimer=json_data.get("KeepAliveHoldTimer"),
            KeepAliveInterval=json_data.get("KeepAliveInterval"),
            KeepAliveRetry=json_data.get("KeepAliveRetry"),
            LocalAddressType=json_data.get("LocalAddressType"),
            LocalAddressValue=json_data.get("LocalAddressValue"),
            Name=json_data.get("Name"),
            PeerAddress=json_data.get("PeerAddress"),
            Template=json_data.get("Template"),
            Ttl=json_data.get("Ttl"),
            TunnelInterface=json_data.get("TunnelInterface"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


