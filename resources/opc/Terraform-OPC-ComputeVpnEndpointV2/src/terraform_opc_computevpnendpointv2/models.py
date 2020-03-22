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
    CustomerVpnGateway: Optional[str]
    Description: Optional[str]
    Enabled: Optional[bool]
    Id: Optional[str]
    IkeIdentifier: Optional[str]
    IpNetwork: Optional[str]
    LocalGatewayIpAddress: Optional[str]
    LocalGatewayPrivateIpAddress: Optional[str]
    Name: Optional[str]
    PreSharedKey: Optional[str]
    ReachableRoutes: Optional[Sequence[str]]
    RequirePerfectForwardSecrecy: Optional[bool]
    Tags: Optional[Sequence[str]]
    TunnelStatus: Optional[str]
    Uri: Optional[str]
    VnicSets: Optional[Sequence[str]]
    PhaseOneSettings: Optional[Sequence["_PhaseOneSettings"]]
    PhaseTwoSettings: Optional[Sequence["_PhaseTwoSettings"]]
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
            CustomerVpnGateway=json_data.get("CustomerVpnGateway"),
            Description=json_data.get("Description"),
            Enabled=json_data.get("Enabled"),
            Id=json_data.get("Id"),
            IkeIdentifier=json_data.get("IkeIdentifier"),
            IpNetwork=json_data.get("IpNetwork"),
            LocalGatewayIpAddress=json_data.get("LocalGatewayIpAddress"),
            LocalGatewayPrivateIpAddress=json_data.get("LocalGatewayPrivateIpAddress"),
            Name=json_data.get("Name"),
            PreSharedKey=json_data.get("PreSharedKey"),
            ReachableRoutes=json_data.get("ReachableRoutes"),
            RequirePerfectForwardSecrecy=json_data.get("RequirePerfectForwardSecrecy"),
            Tags=json_data.get("Tags"),
            TunnelStatus=json_data.get("TunnelStatus"),
            Uri=json_data.get("Uri"),
            VnicSets=json_data.get("VnicSets"),
            PhaseOneSettings=json_data.get("PhaseOneSettings"),
            PhaseTwoSettings=json_data.get("PhaseTwoSettings"),
            Timeouts=Timeouts._deserialize(json_data.get("Timeouts")),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class PhaseOneSettings:
    DhGroup: Optional[str]
    Encryption: Optional[str]
    Hash: Optional[str]
    Lifetime: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_PhaseOneSettings"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_PhaseOneSettings"]:
        if not json_data:
            return None
        return cls(
            DhGroup=json_data.get("DhGroup"),
            Encryption=json_data.get("Encryption"),
            Hash=json_data.get("Hash"),
            Lifetime=json_data.get("Lifetime"),
        )


# work around possible type aliasing issues when variable has same name as a model
_PhaseOneSettings = PhaseOneSettings


@dataclass
class PhaseTwoSettings:
    Encryption: Optional[str]
    Hash: Optional[str]
    Lifetime: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_PhaseTwoSettings"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_PhaseTwoSettings"]:
        if not json_data:
            return None
        return cls(
            Encryption=json_data.get("Encryption"),
            Hash=json_data.get("Hash"),
            Lifetime=json_data.get("Lifetime"),
        )


# work around possible type aliasing issues when variable has same name as a model
_PhaseTwoSettings = PhaseTwoSettings


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


