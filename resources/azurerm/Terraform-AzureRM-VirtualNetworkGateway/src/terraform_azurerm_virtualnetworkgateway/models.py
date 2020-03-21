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
    ActiveActive: Optional[bool]
    DefaultLocalNetworkGatewayId: Optional[str]
    EnableBgp: Optional[bool]
    Generation: Optional[str]
    Id: Optional[str]
    Location: Optional[str]
    Name: Optional[str]
    ResourceGroupName: Optional[str]
    Sku: Optional[str]
    Tags: Optional[Sequence["_Tags"]]
    Type: Optional[str]
    VpnType: Optional[str]
    BgpSettings: Optional[Sequence["_BgpSettings"]]
    IpConfiguration: Optional[Sequence["_IpConfiguration"]]
    Timeouts: Optional["_Timeouts"]
    VpnClientConfiguration: Optional[Sequence["_VpnClientConfiguration"]]
    RevokedCertificate: Optional[Sequence["_RevokedCertificate"]]
    RootCertificate: Optional[Sequence["_RootCertificate"]]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceModel"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceModel"]:
        if not json_data:
            return None
        return cls(
            tfcfnid=json_data.get("tfcfnid"),
            ActiveActive=json_data.get("ActiveActive"),
            DefaultLocalNetworkGatewayId=json_data.get("DefaultLocalNetworkGatewayId"),
            EnableBgp=json_data.get("EnableBgp"),
            Generation=json_data.get("Generation"),
            Id=json_data.get("Id"),
            Location=json_data.get("Location"),
            Name=json_data.get("Name"),
            ResourceGroupName=json_data.get("ResourceGroupName"),
            Sku=json_data.get("Sku"),
            Tags=json_data.get("Tags"),
            Type=json_data.get("Type"),
            VpnType=json_data.get("VpnType"),
            BgpSettings=json_data.get("BgpSettings"),
            IpConfiguration=json_data.get("IpConfiguration"),
            Timeouts=Timeouts._deserialize(json_data.get("Timeouts")),
            VpnClientConfiguration=json_data.get("VpnClientConfiguration"),
            RevokedCertificate=json_data.get("RevokedCertificate"),
            RootCertificate=json_data.get("RootCertificate"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class Tags:
    Key: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Tags"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Tags"]:
        if not json_data:
            return None
        return cls(
            Key=json_data.get("Key"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Tags = Tags


@dataclass
class BgpSettings:
    Asn: Optional[float]
    PeerWeight: Optional[float]
    PeeringAddress: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_BgpSettings"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_BgpSettings"]:
        if not json_data:
            return None
        return cls(
            Asn=json_data.get("Asn"),
            PeerWeight=json_data.get("PeerWeight"),
            PeeringAddress=json_data.get("PeeringAddress"),
        )


# work around possible type aliasing issues when variable has same name as a model
_BgpSettings = BgpSettings


@dataclass
class IpConfiguration:
    Name: Optional[str]
    PrivateIpAddressAllocation: Optional[str]
    PublicIpAddressId: Optional[str]
    SubnetId: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_IpConfiguration"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_IpConfiguration"]:
        if not json_data:
            return None
        return cls(
            Name=json_data.get("Name"),
            PrivateIpAddressAllocation=json_data.get("PrivateIpAddressAllocation"),
            PublicIpAddressId=json_data.get("PublicIpAddressId"),
            SubnetId=json_data.get("SubnetId"),
        )


# work around possible type aliasing issues when variable has same name as a model
_IpConfiguration = IpConfiguration


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


@dataclass
class VpnClientConfiguration:
    AddressSpace: Optional[Sequence[str]]
    RadiusServerAddress: Optional[str]
    RadiusServerSecret: Optional[str]
    VpnClientProtocols: Optional[Sequence[str]]
    RevokedCertificate: Optional[Sequence["_RevokedCertificate"]]
    RootCertificate: Optional[Sequence["_RootCertificate"]]

    @classmethod
    def _deserialize(
        cls: Type["_VpnClientConfiguration"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_VpnClientConfiguration"]:
        if not json_data:
            return None
        return cls(
            AddressSpace=json_data.get("AddressSpace"),
            RadiusServerAddress=json_data.get("RadiusServerAddress"),
            RadiusServerSecret=json_data.get("RadiusServerSecret"),
            VpnClientProtocols=json_data.get("VpnClientProtocols"),
            RevokedCertificate=json_data.get("RevokedCertificate"),
            RootCertificate=json_data.get("RootCertificate"),
        )


# work around possible type aliasing issues when variable has same name as a model
_VpnClientConfiguration = VpnClientConfiguration


@dataclass
class RevokedCertificate:
    Name: Optional[str]
    Thumbprint: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_RevokedCertificate"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_RevokedCertificate"]:
        if not json_data:
            return None
        return cls(
            Name=json_data.get("Name"),
            Thumbprint=json_data.get("Thumbprint"),
        )


# work around possible type aliasing issues when variable has same name as a model
_RevokedCertificate = RevokedCertificate


@dataclass
class RootCertificate:
    Name: Optional[str]
    PublicCertData: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_RootCertificate"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_RootCertificate"]:
        if not json_data:
            return None
        return cls(
            Name=json_data.get("Name"),
            PublicCertData=json_data.get("PublicCertData"),
        )


# work around possible type aliasing issues when variable has same name as a model
_RootCertificate = RootCertificate


