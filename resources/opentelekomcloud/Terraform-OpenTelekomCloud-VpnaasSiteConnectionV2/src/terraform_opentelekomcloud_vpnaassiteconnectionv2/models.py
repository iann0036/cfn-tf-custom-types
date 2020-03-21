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
    AdminStateUp: Optional[bool]
    Description: Optional[str]
    Id: Optional[str]
    IkepolicyId: Optional[str]
    Initiator: Optional[str]
    IpsecpolicyId: Optional[str]
    LocalEpGroupId: Optional[str]
    LocalId: Optional[str]
    Mtu: Optional[float]
    Name: Optional[str]
    PeerAddress: Optional[str]
    PeerCidrs: Optional[Sequence[str]]
    PeerEpGroupId: Optional[str]
    PeerId: Optional[str]
    Psk: Optional[str]
    Region: Optional[str]
    TenantId: Optional[str]
    ValueSpecs: Optional[Sequence["_ValueSpecs"]]
    VpnserviceId: Optional[str]
    Dpd: Optional[Sequence["_Dpd"]]
    Timeouts: Optional["_Timeouts"]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceModel"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceModel"]:
        if not json_data:
            return None
        return cls(
            tfcfnid=json_data.get("tfcfnid"),
            AdminStateUp=json_data.get("AdminStateUp"),
            Description=json_data.get("Description"),
            Id=json_data.get("Id"),
            IkepolicyId=json_data.get("IkepolicyId"),
            Initiator=json_data.get("Initiator"),
            IpsecpolicyId=json_data.get("IpsecpolicyId"),
            LocalEpGroupId=json_data.get("LocalEpGroupId"),
            LocalId=json_data.get("LocalId"),
            Mtu=json_data.get("Mtu"),
            Name=json_data.get("Name"),
            PeerAddress=json_data.get("PeerAddress"),
            PeerCidrs=json_data.get("PeerCidrs"),
            PeerEpGroupId=json_data.get("PeerEpGroupId"),
            PeerId=json_data.get("PeerId"),
            Psk=json_data.get("Psk"),
            Region=json_data.get("Region"),
            TenantId=json_data.get("TenantId"),
            ValueSpecs=json_data.get("ValueSpecs"),
            VpnserviceId=json_data.get("VpnserviceId"),
            Dpd=json_data.get("Dpd"),
            Timeouts=Timeouts._deserialize(json_data.get("Timeouts")),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class ValueSpecs:
    Key: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ValueSpecs"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ValueSpecs"]:
        if not json_data:
            return None
        return cls(
            Key=json_data.get("Key"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ValueSpecs = ValueSpecs


@dataclass
class Dpd:
    Action: Optional[str]
    Interval: Optional[float]
    Timeout: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_Dpd"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Dpd"]:
        if not json_data:
            return None
        return cls(
            Action=json_data.get("Action"),
            Interval=json_data.get("Interval"),
            Timeout=json_data.get("Timeout"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Dpd = Dpd


@dataclass
class Timeouts:
    Create: Optional[str]
    Delete: Optional[str]
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
            Update=json_data.get("Update"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Timeouts = Timeouts


