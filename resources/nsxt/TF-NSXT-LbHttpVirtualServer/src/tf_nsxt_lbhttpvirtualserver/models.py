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
    ApplicationProfileId: Optional[str]
    DefaultPoolMemberPort: Optional[str]
    Description: Optional[str]
    DisplayName: Optional[str]
    Enabled: Optional[bool]
    Id: Optional[str]
    IpAddress: Optional[str]
    MaxConcurrentConnections: Optional[float]
    MaxNewConnectionRate: Optional[float]
    PersistenceProfileId: Optional[str]
    PoolId: Optional[str]
    Port: Optional[str]
    Revision: Optional[float]
    RuleIds: Optional[Sequence[str]]
    SorryPoolId: Optional[str]
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
            ApplicationProfileId=json_data.get("ApplicationProfileId"),
            DefaultPoolMemberPort=json_data.get("DefaultPoolMemberPort"),
            Description=json_data.get("Description"),
            DisplayName=json_data.get("DisplayName"),
            Enabled=json_data.get("Enabled"),
            Id=json_data.get("Id"),
            IpAddress=json_data.get("IpAddress"),
            MaxConcurrentConnections=json_data.get("MaxConcurrentConnections"),
            MaxNewConnectionRate=json_data.get("MaxNewConnectionRate"),
            PersistenceProfileId=json_data.get("PersistenceProfileId"),
            PoolId=json_data.get("PoolId"),
            Port=json_data.get("Port"),
            Revision=json_data.get("Revision"),
            RuleIds=json_data.get("RuleIds"),
            SorryPoolId=json_data.get("SorryPoolId"),
            ClientSsl=deserialize_list(json_data.get("ClientSsl"), ClientSslDefinition),
            ServerSsl=deserialize_list(json_data.get("ServerSsl"), ServerSslDefinition),
            Tag=deserialize_list(json_data.get("Tag"), TagDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class ClientSslDefinition(BaseModel):
    CaIds: Optional[Sequence[str]]
    CertificateChainDepth: Optional[float]
    ClientAuth: Optional[bool]
    ClientSslProfileId: Optional[str]
    CrlIds: Optional[Sequence[str]]
    DefaultCertificateId: Optional[str]
    SniCertificateIds: Optional[Sequence[str]]

    @classmethod
    def _deserialize(
        cls: Type["_ClientSslDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ClientSslDefinition"]:
        if not json_data:
            return None
        return cls(
            CaIds=json_data.get("CaIds"),
            CertificateChainDepth=json_data.get("CertificateChainDepth"),
            ClientAuth=json_data.get("ClientAuth"),
            ClientSslProfileId=json_data.get("ClientSslProfileId"),
            CrlIds=json_data.get("CrlIds"),
            DefaultCertificateId=json_data.get("DefaultCertificateId"),
            SniCertificateIds=json_data.get("SniCertificateIds"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ClientSslDefinition = ClientSslDefinition


@dataclass
class ServerSslDefinition(BaseModel):
    CaIds: Optional[Sequence[str]]
    CertificateChainDepth: Optional[float]
    ClientCertificateId: Optional[str]
    CrlIds: Optional[Sequence[str]]
    ServerAuth: Optional[bool]
    ServerSslProfileId: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ServerSslDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ServerSslDefinition"]:
        if not json_data:
            return None
        return cls(
            CaIds=json_data.get("CaIds"),
            CertificateChainDepth=json_data.get("CertificateChainDepth"),
            ClientCertificateId=json_data.get("ClientCertificateId"),
            CrlIds=json_data.get("CrlIds"),
            ServerAuth=json_data.get("ServerAuth"),
            ServerSslProfileId=json_data.get("ServerSslProfileId"),
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


