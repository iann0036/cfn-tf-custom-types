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
    AccessLogEnabled: Optional[bool]
    ApplicationProfilePath: Optional[str]
    DefaultPoolMemberPorts: Optional[Sequence[str]]
    Description: Optional[str]
    DisplayName: Optional[str]
    Enabled: Optional[bool]
    Id: Optional[str]
    IpAddress: Optional[str]
    LogSignificantEventOnly: Optional[bool]
    MaxConcurrentConnections: Optional[float]
    MaxNewConnectionRate: Optional[float]
    NsxId: Optional[str]
    Path: Optional[str]
    PersistenceProfilePath: Optional[str]
    PoolPath: Optional[str]
    Ports: Optional[Sequence[str]]
    Revision: Optional[float]
    ServicePath: Optional[str]
    SorryPoolPath: Optional[str]
    AccessListControl: Optional[Sequence["_AccessListControlDefinition"]]
    ClientSsl: Optional[Sequence["_ClientSslDefinition"]]
    ServerSsl: Optional[Sequence["_ServerSslDefinition"]]
    Tag: Optional[Sequence["_TagDefinition"]]

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
            AccessLogEnabled=json_data.get("AccessLogEnabled"),
            ApplicationProfilePath=json_data.get("ApplicationProfilePath"),
            DefaultPoolMemberPorts=json_data.get("DefaultPoolMemberPorts"),
            Description=json_data.get("Description"),
            DisplayName=json_data.get("DisplayName"),
            Enabled=json_data.get("Enabled"),
            Id=json_data.get("Id"),
            IpAddress=json_data.get("IpAddress"),
            LogSignificantEventOnly=json_data.get("LogSignificantEventOnly"),
            MaxConcurrentConnections=json_data.get("MaxConcurrentConnections"),
            MaxNewConnectionRate=json_data.get("MaxNewConnectionRate"),
            NsxId=json_data.get("NsxId"),
            Path=json_data.get("Path"),
            PersistenceProfilePath=json_data.get("PersistenceProfilePath"),
            PoolPath=json_data.get("PoolPath"),
            Ports=json_data.get("Ports"),
            Revision=json_data.get("Revision"),
            ServicePath=json_data.get("ServicePath"),
            SorryPoolPath=json_data.get("SorryPoolPath"),
            AccessListControl=deserialize_list(json_data.get("AccessListControl"), AccessListControlDefinition),
            ClientSsl=deserialize_list(json_data.get("ClientSsl"), ClientSslDefinition),
            ServerSsl=deserialize_list(json_data.get("ServerSsl"), ServerSslDefinition),
            Tag=deserialize_list(json_data.get("Tag"), TagDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class AccessListControlDefinition(BaseModel):
    Action: Optional[str]
    Enabled: Optional[bool]
    GroupPath: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_AccessListControlDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AccessListControlDefinition"]:
        if not json_data:
            return None
        return cls(
            Action=json_data.get("Action"),
            Enabled=json_data.get("Enabled"),
            GroupPath=json_data.get("GroupPath"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AccessListControlDefinition = AccessListControlDefinition


@dataclass
class ClientSslDefinition(BaseModel):
    CaPaths: Optional[Sequence[str]]
    CertificateChainDepth: Optional[float]
    ClientAuth: Optional[str]
    CrlPaths: Optional[Sequence[str]]
    DefaultCertificatePath: Optional[str]
    SniPaths: Optional[Sequence[str]]
    SslProfilePath: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ClientSslDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ClientSslDefinition"]:
        if not json_data:
            return None
        return cls(
            CaPaths=json_data.get("CaPaths"),
            CertificateChainDepth=json_data.get("CertificateChainDepth"),
            ClientAuth=json_data.get("ClientAuth"),
            CrlPaths=json_data.get("CrlPaths"),
            DefaultCertificatePath=json_data.get("DefaultCertificatePath"),
            SniPaths=json_data.get("SniPaths"),
            SslProfilePath=json_data.get("SslProfilePath"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ClientSslDefinition = ClientSslDefinition


@dataclass
class ServerSslDefinition(BaseModel):
    CaPaths: Optional[Sequence[str]]
    CertificateChainDepth: Optional[float]
    ClientCertificatePath: Optional[str]
    CrlPaths: Optional[Sequence[str]]
    ServerAuth: Optional[str]
    SslProfilePath: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ServerSslDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ServerSslDefinition"]:
        if not json_data:
            return None
        return cls(
            CaPaths=json_data.get("CaPaths"),
            CertificateChainDepth=json_data.get("CertificateChainDepth"),
            ClientCertificatePath=json_data.get("ClientCertificatePath"),
            CrlPaths=json_data.get("CrlPaths"),
            ServerAuth=json_data.get("ServerAuth"),
            SslProfilePath=json_data.get("SslProfilePath"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ServerSslDefinition = ServerSslDefinition


@dataclass
class TagDefinition(BaseModel):
    Scope: Optional[str]
    Tag: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_TagDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TagDefinition"]:
        if not json_data:
            return None
        return cls(
            Scope=json_data.get("Scope"),
            Tag=json_data.get("Tag"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TagDefinition = TagDefinition


