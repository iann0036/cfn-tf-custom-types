# DO NOT modify this file by hand, changes will be overwritten
import sys
from dataclasses import dataclass
from inspect import getmembers, isclass
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
    BaseModel,
    BaseResourceHandlerRequest,
)
from cloudformation_cli_python_lib.recast import recast_object
from cloudformation_cli_python_lib.utils import deserialize_list

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
class ResourceModel(BaseModel):
    tfcfnid: Optional[str]
    DefaultLocalNetworkGatewayId: Optional[str]
    EnableBgp: Optional[bool]
    Id: Optional[str]
    Location: Optional[str]
    Name: Optional[str]
    ResourceGroupName: Optional[str]
    Sku: Optional[str]
    Tags: Optional[Sequence["_TagsDefinition"]]
    Type: Optional[str]
    VpnType: Optional[str]
    BgpSettings: Optional[Sequence["_BgpSettingsDefinition"]]
    IpConfiguration: Optional[Sequence["_IpConfigurationDefinition"]]
    VpnClientConfiguration: Optional[Sequence["_VpnClientConfigurationDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceModel"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceModel"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            tfcfnid=json_data.get("tfcfnid"),
            DefaultLocalNetworkGatewayId=json_data.get("DefaultLocalNetworkGatewayId"),
            EnableBgp=json_data.get("EnableBgp"),
            Id=json_data.get("Id"),
            Location=json_data.get("Location"),
            Name=json_data.get("Name"),
            ResourceGroupName=json_data.get("ResourceGroupName"),
            Sku=json_data.get("Sku"),
            Tags=deserialize_list(json_data.get("Tags"), TagsDefinition),
            Type=json_data.get("Type"),
            VpnType=json_data.get("VpnType"),
            BgpSettings=deserialize_list(json_data.get("BgpSettings"), BgpSettingsDefinition),
            IpConfiguration=deserialize_list(json_data.get("IpConfiguration"), IpConfigurationDefinition),
            VpnClientConfiguration=deserialize_list(json_data.get("VpnClientConfiguration"), VpnClientConfigurationDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class TagsDefinition(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_TagsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TagsDefinition"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TagsDefinition = TagsDefinition


@dataclass
class BgpSettingsDefinition(BaseModel):
    Asn: Optional[float]
    PeerWeight: Optional[float]
    PeeringAddress: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_BgpSettingsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_BgpSettingsDefinition"]:
        if not json_data:
            return None
        return cls(
            Asn=json_data.get("Asn"),
            PeerWeight=json_data.get("PeerWeight"),
            PeeringAddress=json_data.get("PeeringAddress"),
        )


# work around possible type aliasing issues when variable has same name as a model
_BgpSettingsDefinition = BgpSettingsDefinition


@dataclass
class IpConfigurationDefinition(BaseModel):
    Name: Optional[str]
    PrivateIpAddressAllocation: Optional[str]
    PublicIpAddressId: Optional[str]
    SubnetId: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_IpConfigurationDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_IpConfigurationDefinition"]:
        if not json_data:
            return None
        return cls(
            Name=json_data.get("Name"),
            PrivateIpAddressAllocation=json_data.get("PrivateIpAddressAllocation"),
            PublicIpAddressId=json_data.get("PublicIpAddressId"),
            SubnetId=json_data.get("SubnetId"),
        )


# work around possible type aliasing issues when variable has same name as a model
_IpConfigurationDefinition = IpConfigurationDefinition


@dataclass
class VpnClientConfigurationDefinition(BaseModel):
    AddressSpace: Optional[Sequence[str]]
    VpnClientProtocols: Optional[Sequence[str]]
    RevokedCertificate: Optional[Sequence["_RevokedCertificateDefinition"]]
    RootCertificate: Optional[Sequence["_RootCertificateDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_VpnClientConfigurationDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_VpnClientConfigurationDefinition"]:
        if not json_data:
            return None
        return cls(
            AddressSpace=json_data.get("AddressSpace"),
            VpnClientProtocols=json_data.get("VpnClientProtocols"),
            RevokedCertificate=deserialize_list(json_data.get("RevokedCertificate"), RevokedCertificateDefinition),
            RootCertificate=deserialize_list(json_data.get("RootCertificate"), RootCertificateDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_VpnClientConfigurationDefinition = VpnClientConfigurationDefinition


@dataclass
class RevokedCertificateDefinition(BaseModel):
    Name: Optional[str]
    Thumbprint: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_RevokedCertificateDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_RevokedCertificateDefinition"]:
        if not json_data:
            return None
        return cls(
            Name=json_data.get("Name"),
            Thumbprint=json_data.get("Thumbprint"),
        )


# work around possible type aliasing issues when variable has same name as a model
_RevokedCertificateDefinition = RevokedCertificateDefinition


@dataclass
class RootCertificateDefinition(BaseModel):
    Name: Optional[str]
    PublicCertData: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_RootCertificateDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_RootCertificateDefinition"]:
        if not json_data:
            return None
        return cls(
            Name=json_data.get("Name"),
            PublicCertData=json_data.get("PublicCertData"),
        )


# work around possible type aliasing issues when variable has same name as a model
_RootCertificateDefinition = RootCertificateDefinition


