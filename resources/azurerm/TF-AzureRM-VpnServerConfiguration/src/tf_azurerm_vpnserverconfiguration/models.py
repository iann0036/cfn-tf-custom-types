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
    Id: Optional[str]
    Location: Optional[str]
    Name: Optional[str]
    ResourceGroupName: Optional[str]
    Tags: Optional[Sequence["_TagsDefinition"]]
    VpnAuthenticationTypes: Optional[Sequence[str]]
    VpnProtocols: Optional[Sequence[str]]
    AzureActiveDirectoryAuthentication: Optional[Sequence["_AzureActiveDirectoryAuthenticationDefinition"]]
    ClientRevokedCertificate: Optional[Sequence["_ClientRevokedCertificateDefinition"]]
    ClientRootCertificate: Optional[Sequence["_ClientRootCertificateDefinition"]]
    IpsecPolicy: Optional[Sequence["_IpsecPolicyDefinition"]]
    Radius: Optional[Sequence["_RadiusDefinition"]]
    RadiusServer: Optional[Sequence["_RadiusServerDefinition"]]
    Timeouts: Optional["_TimeoutsDefinition"]

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
            Id=json_data.get("Id"),
            Location=json_data.get("Location"),
            Name=json_data.get("Name"),
            ResourceGroupName=json_data.get("ResourceGroupName"),
            Tags=deserialize_list(json_data.get("Tags"), TagsDefinition),
            VpnAuthenticationTypes=json_data.get("VpnAuthenticationTypes"),
            VpnProtocols=json_data.get("VpnProtocols"),
            AzureActiveDirectoryAuthentication=deserialize_list(json_data.get("AzureActiveDirectoryAuthentication"), AzureActiveDirectoryAuthenticationDefinition),
            ClientRevokedCertificate=deserialize_list(json_data.get("ClientRevokedCertificate"), ClientRevokedCertificateDefinition),
            ClientRootCertificate=deserialize_list(json_data.get("ClientRootCertificate"), ClientRootCertificateDefinition),
            IpsecPolicy=deserialize_list(json_data.get("IpsecPolicy"), IpsecPolicyDefinition),
            Radius=deserialize_list(json_data.get("Radius"), RadiusDefinition),
            RadiusServer=deserialize_list(json_data.get("RadiusServer"), RadiusServerDefinition),
            Timeouts=TimeoutsDefinition._deserialize(json_data.get("Timeouts")),
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
class AzureActiveDirectoryAuthenticationDefinition(BaseModel):
    Audience: Optional[str]
    Issuer: Optional[str]
    Tenant: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_AzureActiveDirectoryAuthenticationDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AzureActiveDirectoryAuthenticationDefinition"]:
        if not json_data:
            return None
        return cls(
            Audience=json_data.get("Audience"),
            Issuer=json_data.get("Issuer"),
            Tenant=json_data.get("Tenant"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AzureActiveDirectoryAuthenticationDefinition = AzureActiveDirectoryAuthenticationDefinition


@dataclass
class ClientRevokedCertificateDefinition(BaseModel):
    Name: Optional[str]
    Thumbprint: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ClientRevokedCertificateDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ClientRevokedCertificateDefinition"]:
        if not json_data:
            return None
        return cls(
            Name=json_data.get("Name"),
            Thumbprint=json_data.get("Thumbprint"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ClientRevokedCertificateDefinition = ClientRevokedCertificateDefinition


@dataclass
class ClientRootCertificateDefinition(BaseModel):
    Name: Optional[str]
    Thumbprint: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ClientRootCertificateDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ClientRootCertificateDefinition"]:
        if not json_data:
            return None
        return cls(
            Name=json_data.get("Name"),
            Thumbprint=json_data.get("Thumbprint"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ClientRootCertificateDefinition = ClientRootCertificateDefinition


@dataclass
class IpsecPolicyDefinition(BaseModel):
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
        cls: Type["_IpsecPolicyDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_IpsecPolicyDefinition"]:
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
_IpsecPolicyDefinition = IpsecPolicyDefinition


@dataclass
class RadiusDefinition(BaseModel):
    ClientRootCertificate: Optional[Sequence["_ClientRootCertificateDefinition"]]
    Server: Optional[Sequence["_ServerDefinition"]]
    ServerRootCertificate: Optional[Sequence["_ServerRootCertificateDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_RadiusDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_RadiusDefinition"]:
        if not json_data:
            return None
        return cls(
            ClientRootCertificate=deserialize_list(json_data.get("ClientRootCertificate"), ClientRootCertificateDefinition),
            Server=deserialize_list(json_data.get("Server"), ServerDefinition),
            ServerRootCertificate=deserialize_list(json_data.get("ServerRootCertificate"), ServerRootCertificateDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_RadiusDefinition = RadiusDefinition


@dataclass
class ServerDefinition(BaseModel):
    Address: Optional[str]
    Score: Optional[float]
    Secret: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ServerDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ServerDefinition"]:
        if not json_data:
            return None
        return cls(
            Address=json_data.get("Address"),
            Score=json_data.get("Score"),
            Secret=json_data.get("Secret"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ServerDefinition = ServerDefinition


@dataclass
class ServerRootCertificateDefinition(BaseModel):
    Name: Optional[str]
    PublicCertData: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ServerRootCertificateDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ServerRootCertificateDefinition"]:
        if not json_data:
            return None
        return cls(
            Name=json_data.get("Name"),
            PublicCertData=json_data.get("PublicCertData"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ServerRootCertificateDefinition = ServerRootCertificateDefinition


@dataclass
class RadiusServerDefinition(BaseModel):
    Address: Optional[str]
    Secret: Optional[str]
    ClientRootCertificate: Optional[Sequence["_ClientRootCertificateDefinition"]]
    ServerRootCertificate: Optional[Sequence["_ServerRootCertificateDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_RadiusServerDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_RadiusServerDefinition"]:
        if not json_data:
            return None
        return cls(
            Address=json_data.get("Address"),
            Secret=json_data.get("Secret"),
            ClientRootCertificate=deserialize_list(json_data.get("ClientRootCertificate"), ClientRootCertificateDefinition),
            ServerRootCertificate=deserialize_list(json_data.get("ServerRootCertificate"), ServerRootCertificateDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_RadiusServerDefinition = RadiusServerDefinition


@dataclass
class TimeoutsDefinition(BaseModel):
    Create: Optional[str]
    Delete: Optional[str]
    Read: Optional[str]
    Update: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_TimeoutsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TimeoutsDefinition"]:
        if not json_data:
            return None
        return cls(
            Create=json_data.get("Create"),
            Delete=json_data.get("Delete"),
            Read=json_data.get("Read"),
            Update=json_data.get("Update"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TimeoutsDefinition = TimeoutsDefinition


