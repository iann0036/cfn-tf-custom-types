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
    ApiManagementName: Optional[str]
    Description: Optional[str]
    Id: Optional[str]
    Name: Optional[str]
    Protocol: Optional[str]
    ResourceGroupName: Optional[str]
    ResourceId: Optional[str]
    Title: Optional[str]
    Url: Optional[str]
    Credentials: Optional[Sequence["_Credentials"]]
    Proxy: Optional[Sequence["_Proxy"]]
    ServiceFabricCluster: Optional[Sequence["_ServiceFabricCluster"]]
    Timeouts: Optional["_Timeouts"]
    Tls: Optional[Sequence["_Tls"]]
    Authorization: Optional[Sequence["_Authorization"]]
    ServerX509Name: Optional[Sequence["_ServerX509Name"]]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceModel"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceModel"]:
        if not json_data:
            return None
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
            Credentials=json_data.get("Credentials"),
            Proxy=json_data.get("Proxy"),
            ServiceFabricCluster=json_data.get("ServiceFabricCluster"),
            Timeouts=Timeouts._deserialize(json_data.get("Timeouts")),
            Tls=json_data.get("Tls"),
            Authorization=json_data.get("Authorization"),
            ServerX509Name=json_data.get("ServerX509Name"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class Credentials:
    Certificate: Optional[Sequence[str]]
    Header: Optional[Sequence["_Header"]]
    Query: Optional[Sequence["_Query"]]
    Authorization: Optional[Sequence["_Authorization"]]

    @classmethod
    def _deserialize(
        cls: Type["_Credentials"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Credentials"]:
        if not json_data:
            return None
        return cls(
            Certificate=json_data.get("Certificate"),
            Header=json_data.get("Header"),
            Query=json_data.get("Query"),
            Authorization=json_data.get("Authorization"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Credentials = Credentials


@dataclass
class Header:
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Header"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Header"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Header = Header


@dataclass
class Query:
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Query"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Query"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Query = Query


@dataclass
class Authorization:
    Parameter: Optional[str]
    Scheme: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Authorization"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Authorization"]:
        if not json_data:
            return None
        return cls(
            Parameter=json_data.get("Parameter"),
            Scheme=json_data.get("Scheme"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Authorization = Authorization


@dataclass
class Proxy:
    Password: Optional[str]
    Url: Optional[str]
    Username: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Proxy"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Proxy"]:
        if not json_data:
            return None
        return cls(
            Password=json_data.get("Password"),
            Url=json_data.get("Url"),
            Username=json_data.get("Username"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Proxy = Proxy


@dataclass
class ServiceFabricCluster:
    ClientCertificateThumbprint: Optional[str]
    ManagementEndpoints: Optional[Sequence[str]]
    MaxPartitionResolutionRetries: Optional[float]
    ServerCertificateThumbprints: Optional[Sequence[str]]
    ServerX509Name: Optional[Sequence["_ServerX509Name"]]

    @classmethod
    def _deserialize(
        cls: Type["_ServiceFabricCluster"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ServiceFabricCluster"]:
        if not json_data:
            return None
        return cls(
            ClientCertificateThumbprint=json_data.get("ClientCertificateThumbprint"),
            ManagementEndpoints=json_data.get("ManagementEndpoints"),
            MaxPartitionResolutionRetries=json_data.get("MaxPartitionResolutionRetries"),
            ServerCertificateThumbprints=json_data.get("ServerCertificateThumbprints"),
            ServerX509Name=json_data.get("ServerX509Name"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ServiceFabricCluster = ServiceFabricCluster


@dataclass
class ServerX509Name:
    IssuerCertificateThumbprint: Optional[str]
    Name: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ServerX509Name"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ServerX509Name"]:
        if not json_data:
            return None
        return cls(
            IssuerCertificateThumbprint=json_data.get("IssuerCertificateThumbprint"),
            Name=json_data.get("Name"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ServerX509Name = ServerX509Name


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
class Tls:
    ValidateCertificateChain: Optional[bool]
    ValidateCertificateName: Optional[bool]

    @classmethod
    def _deserialize(
        cls: Type["_Tls"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Tls"]:
        if not json_data:
            return None
        return cls(
            ValidateCertificateChain=json_data.get("ValidateCertificateChain"),
            ValidateCertificateName=json_data.get("ValidateCertificateName"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Tls = Tls


