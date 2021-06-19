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
    ApiManagementName: Optional[str]
    Description: Optional[str]
    Id: Optional[str]
    Name: Optional[str]
    Protocol: Optional[str]
    ResourceGroupName: Optional[str]
    ResourceId: Optional[str]
    Title: Optional[str]
    Url: Optional[str]
    Credentials: Optional[Sequence["_CredentialsDefinition"]]
    Proxy: Optional[Sequence["_ProxyDefinition"]]
    ServiceFabricCluster: Optional[Sequence["_ServiceFabricClusterDefinition"]]
    Timeouts: Optional["_TimeoutsDefinition"]
    Tls: Optional[Sequence["_TlsDefinition"]]

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
            ApiManagementName=json_data.get("ApiManagementName"),
            Description=json_data.get("Description"),
            Id=json_data.get("Id"),
            Name=json_data.get("Name"),
            Protocol=json_data.get("Protocol"),
            ResourceGroupName=json_data.get("ResourceGroupName"),
            ResourceId=json_data.get("ResourceId"),
            Title=json_data.get("Title"),
            Url=json_data.get("Url"),
            Credentials=deserialize_list(json_data.get("Credentials"), CredentialsDefinition),
            Proxy=deserialize_list(json_data.get("Proxy"), ProxyDefinition),
            ServiceFabricCluster=deserialize_list(json_data.get("ServiceFabricCluster"), ServiceFabricClusterDefinition),
            Timeouts=TimeoutsDefinition._deserialize(json_data.get("Timeouts")),
            Tls=deserialize_list(json_data.get("Tls"), TlsDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class CredentialsDefinition(BaseModel):
    Certificate: Optional[Sequence[str]]
    Header: Optional[Sequence["_HeaderDefinition"]]
    Query: Optional[Sequence["_QueryDefinition"]]
    Authorization: Optional[Sequence["_AuthorizationDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_CredentialsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_CredentialsDefinition"]:
        if not json_data:
            return None
        return cls(
            Certificate=json_data.get("Certificate"),
            Header=deserialize_list(json_data.get("Header"), HeaderDefinition),
            Query=deserialize_list(json_data.get("Query"), QueryDefinition),
            Authorization=deserialize_list(json_data.get("Authorization"), AuthorizationDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_CredentialsDefinition = CredentialsDefinition


@dataclass
class HeaderDefinition(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_HeaderDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_HeaderDefinition"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_HeaderDefinition = HeaderDefinition


@dataclass
class QueryDefinition(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_QueryDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_QueryDefinition"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_QueryDefinition = QueryDefinition


@dataclass
class AuthorizationDefinition(BaseModel):
    Parameter: Optional[str]
    Scheme: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_AuthorizationDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AuthorizationDefinition"]:
        if not json_data:
            return None
        return cls(
            Parameter=json_data.get("Parameter"),
            Scheme=json_data.get("Scheme"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AuthorizationDefinition = AuthorizationDefinition


@dataclass
class ProxyDefinition(BaseModel):
    Password: Optional[str]
    Url: Optional[str]
    Username: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ProxyDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ProxyDefinition"]:
        if not json_data:
            return None
        return cls(
            Password=json_data.get("Password"),
            Url=json_data.get("Url"),
            Username=json_data.get("Username"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ProxyDefinition = ProxyDefinition


@dataclass
class ServiceFabricClusterDefinition(BaseModel):
    ClientCertificateThumbprint: Optional[str]
    ManagementEndpoints: Optional[Sequence[str]]
    MaxPartitionResolutionRetries: Optional[float]
    ServerCertificateThumbprints: Optional[Sequence[str]]
    ServerX509Name: Optional[Sequence["_ServerX509NameDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_ServiceFabricClusterDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ServiceFabricClusterDefinition"]:
        if not json_data:
            return None
        return cls(
            ClientCertificateThumbprint=json_data.get("ClientCertificateThumbprint"),
            ManagementEndpoints=json_data.get("ManagementEndpoints"),
            MaxPartitionResolutionRetries=json_data.get("MaxPartitionResolutionRetries"),
            ServerCertificateThumbprints=json_data.get("ServerCertificateThumbprints"),
            ServerX509Name=deserialize_list(json_data.get("ServerX509Name"), ServerX509NameDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ServiceFabricClusterDefinition = ServiceFabricClusterDefinition


@dataclass
class ServerX509NameDefinition(BaseModel):
    IssuerCertificateThumbprint: Optional[str]
    Name: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ServerX509NameDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ServerX509NameDefinition"]:
        if not json_data:
            return None
        return cls(
            IssuerCertificateThumbprint=json_data.get("IssuerCertificateThumbprint"),
            Name=json_data.get("Name"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ServerX509NameDefinition = ServerX509NameDefinition


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


@dataclass
class TlsDefinition(BaseModel):
    ValidateCertificateChain: Optional[bool]
    ValidateCertificateName: Optional[bool]

    @classmethod
    def _deserialize(
        cls: Type["_TlsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TlsDefinition"]:
        if not json_data:
            return None
        return cls(
            ValidateCertificateChain=json_data.get("ValidateCertificateChain"),
            ValidateCertificateName=json_data.get("ValidateCertificateName"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TlsDefinition = TlsDefinition


