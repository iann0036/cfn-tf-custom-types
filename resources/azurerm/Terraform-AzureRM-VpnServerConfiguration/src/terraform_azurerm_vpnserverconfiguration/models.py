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
    VpnAuthenticationTypes: Optional[Sequence[str]]
    VpnProtocols: Optional[Sequence[str]]
    AzureActiveDirectoryAuthentication: Optional[Sequence["_AzureActiveDirectoryAuthentication"]]
    ClientRevokedCertificate: Optional[Sequence["_ClientRevokedCertificate"]]
    ClientRootCertificate: Optional[Sequence["_ClientRootCertificate"]]
    IpsecPolicy: Optional[Sequence["_IpsecPolicy"]]
    RadiusServer: Optional[Sequence["_RadiusServer"]]
    Timeouts: Optional["_Timeouts"]
    ServerRootCertificate: Optional[Sequence["_ServerRootCertificate"]]

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
            VpnAuthenticationTypes=json_data.get("VpnAuthenticationTypes"),
            VpnProtocols=json_data.get("VpnProtocols"),
            AzureActiveDirectoryAuthentication=json_data.get("AzureActiveDirectoryAuthentication"),
            ClientRevokedCertificate=json_data.get("ClientRevokedCertificate"),
            ClientRootCertificate=json_data.get("ClientRootCertificate"),
            IpsecPolicy=json_data.get("IpsecPolicy"),
            RadiusServer=json_data.get("RadiusServer"),
            Timeouts=Timeouts._deserialize(json_data.get("Timeouts")),
            ServerRootCertificate=json_data.get("ServerRootCertificate"),
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
class AzureActiveDirectoryAuthentication:
    Audience: Optional[str]
    Issuer: Optional[str]
    Tenant: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_AzureActiveDirectoryAuthentication"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AzureActiveDirectoryAuthentication"]:
        if not json_data:
            return None
        return cls(
            Audience=json_data.get("Audience"),
            Issuer=json_data.get("Issuer"),
            Tenant=json_data.get("Tenant"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AzureActiveDirectoryAuthentication = AzureActiveDirectoryAuthentication


@dataclass
class ClientRevokedCertificate:
    Name: Optional[str]
    Thumbprint: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ClientRevokedCertificate"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ClientRevokedCertificate"]:
        if not json_data:
            return None
        return cls(
            Name=json_data.get("Name"),
            Thumbprint=json_data.get("Thumbprint"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ClientRevokedCertificate = ClientRevokedCertificate


@dataclass
class ClientRootCertificate:
    Name: Optional[str]
    Thumbprint: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ClientRootCertificate"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ClientRootCertificate"]:
        if not json_data:
            return None
        return cls(
            Name=json_data.get("Name"),
            Thumbprint=json_data.get("Thumbprint"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ClientRootCertificate = ClientRootCertificate


@dataclass
class IpsecPolicy:
    DhGroup: Optional[str]
    IkeEncryption: Optional[str]
    IkeIntegrity: Optional[str]
    IpsecEncryption: Optional[str]
    IpsecIntegrity: Optional[str]
    PfsGroup: Optional[str]
    SaDataSizeKilobytes: Optional[float]
    SaLifetimeSeconds: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_IpsecPolicy"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_IpsecPolicy"]:
        if not json_data:
            return None
        return cls(
            DhGroup=json_data.get("DhGroup"),
            IkeEncryption=json_data.get("IkeEncryption"),
            IkeIntegrity=json_data.get("IkeIntegrity"),
            IpsecEncryption=json_data.get("IpsecEncryption"),
            IpsecIntegrity=json_data.get("IpsecIntegrity"),
            PfsGroup=json_data.get("PfsGroup"),
            SaDataSizeKilobytes=json_data.get("SaDataSizeKilobytes"),
            SaLifetimeSeconds=json_data.get("SaLifetimeSeconds"),
        )


# work around possible type aliasing issues when variable has same name as a model
_IpsecPolicy = IpsecPolicy


@dataclass
class RadiusServer:
    Address: Optional[str]
    Secret: Optional[str]
    ClientRootCertificate: Optional[Sequence["_ClientRootCertificate"]]
    ServerRootCertificate: Optional[Sequence["_ServerRootCertificate"]]

    @classmethod
    def _deserialize(
        cls: Type["_RadiusServer"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_RadiusServer"]:
        if not json_data:
            return None
        return cls(
            Address=json_data.get("Address"),
            Secret=json_data.get("Secret"),
            ClientRootCertificate=json_data.get("ClientRootCertificate"),
            ServerRootCertificate=json_data.get("ServerRootCertificate"),
        )


# work around possible type aliasing issues when variable has same name as a model
_RadiusServer = RadiusServer


@dataclass
class ServerRootCertificate:
    Name: Optional[str]
    PublicCertData: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ServerRootCertificate"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ServerRootCertificate"]:
        if not json_data:
            return None
        return cls(
            Name=json_data.get("Name"),
            PublicCertData=json_data.get("PublicCertData"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ServerRootCertificate = ServerRootCertificate


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


