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
    Authorization: Optional[Sequence["_AuthorizationDefinition"]]
    ClusterEndpoint: Optional[str]
    Description: Optional[str]
    Id: Optional[str]
    ProjectId: Optional[str]
    ServiceEndpointName: Optional[str]
    AzureActiveDirectory: Optional[Sequence["_AzureActiveDirectoryDefinition"]]
    Certificate: Optional[Sequence["_CertificateDefinition"]]
    None: Optional[Sequence["_NoneDefinition"]]
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
            Authorization=deserialize_list(json_data.get("Authorization"), AuthorizationDefinition),
            ClusterEndpoint=json_data.get("ClusterEndpoint"),
            Description=json_data.get("Description"),
            Id=json_data.get("Id"),
            ProjectId=json_data.get("ProjectId"),
            ServiceEndpointName=json_data.get("ServiceEndpointName"),
            AzureActiveDirectory=deserialize_list(json_data.get("AzureActiveDirectory"), AzureActiveDirectoryDefinition),
            Certificate=deserialize_list(json_data.get("Certificate"), CertificateDefinition),
            None=deserialize_list(json_data.get("None"), NoneDefinition),
            Timeouts=TimeoutsDefinition._deserialize(json_data.get("Timeouts")),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class AuthorizationDefinition(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_AuthorizationDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AuthorizationDefinition"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AuthorizationDefinition = AuthorizationDefinition


@dataclass
class AzureActiveDirectoryDefinition(BaseModel):
    Password: Optional[str]
    ServerCertificateCommonName: Optional[str]
    ServerCertificateLookup: Optional[str]
    ServerCertificateThumbprint: Optional[str]
    Username: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_AzureActiveDirectoryDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AzureActiveDirectoryDefinition"]:
        if not json_data:
            return None
        return cls(
            Password=json_data.get("Password"),
            ServerCertificateCommonName=json_data.get("ServerCertificateCommonName"),
            ServerCertificateLookup=json_data.get("ServerCertificateLookup"),
            ServerCertificateThumbprint=json_data.get("ServerCertificateThumbprint"),
            Username=json_data.get("Username"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AzureActiveDirectoryDefinition = AzureActiveDirectoryDefinition


@dataclass
class CertificateDefinition(BaseModel):
    ClientCertificate: Optional[str]
    ClientCertificatePassword: Optional[str]
    ServerCertificateCommonName: Optional[str]
    ServerCertificateLookup: Optional[str]
    ServerCertificateThumbprint: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_CertificateDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_CertificateDefinition"]:
        if not json_data:
            return None
        return cls(
            ClientCertificate=json_data.get("ClientCertificate"),
            ClientCertificatePassword=json_data.get("ClientCertificatePassword"),
            ServerCertificateCommonName=json_data.get("ServerCertificateCommonName"),
            ServerCertificateLookup=json_data.get("ServerCertificateLookup"),
            ServerCertificateThumbprint=json_data.get("ServerCertificateThumbprint"),
        )


# work around possible type aliasing issues when variable has same name as a model
_CertificateDefinition = CertificateDefinition


@dataclass
class NoneDefinition(BaseModel):
    ClusterSpn: Optional[str]
    Unsecured: Optional[bool]

    @classmethod
    def _deserialize(
        cls: Type["_NoneDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_NoneDefinition"]:
        if not json_data:
            return None
        return cls(
            ClusterSpn=json_data.get("ClusterSpn"),
            Unsecured=json_data.get("Unsecured"),
        )


# work around possible type aliasing issues when variable has same name as a model
_NoneDefinition = NoneDefinition


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


