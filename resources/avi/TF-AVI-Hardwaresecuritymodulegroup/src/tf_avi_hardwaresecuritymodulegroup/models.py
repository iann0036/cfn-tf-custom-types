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
    Name: Optional[str]
    TenantRef: Optional[str]
    Uuid: Optional[str]
    Hsm: Optional[Sequence["_HsmDefinition"]]
    Markers: Optional[Sequence["_MarkersDefinition"]]

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
            Name=json_data.get("Name"),
            TenantRef=json_data.get("TenantRef"),
            Uuid=json_data.get("Uuid"),
            Hsm=deserialize_list(json_data.get("Hsm"), HsmDefinition),
            Markers=deserialize_list(json_data.get("Markers"), MarkersDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class HsmDefinition(BaseModel):
    Type: Optional[str]
    Cloudhsm: Optional[Sequence["_CloudhsmDefinition"]]
    Nethsm: Optional[Sequence["_NethsmDefinition"]]
    Rfs: Optional[Sequence["_RfsDefinition"]]
    Sluna: Optional[Sequence["_SlunaDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_HsmDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_HsmDefinition"]:
        if not json_data:
            return None
        return cls(
            Type=json_data.get("Type"),
            Cloudhsm=deserialize_list(json_data.get("Cloudhsm"), CloudhsmDefinition),
            Nethsm=deserialize_list(json_data.get("Nethsm"), NethsmDefinition),
            Rfs=deserialize_list(json_data.get("Rfs"), RfsDefinition),
            Sluna=deserialize_list(json_data.get("Sluna"), SlunaDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_HsmDefinition = HsmDefinition


@dataclass
class CloudhsmDefinition(BaseModel):
    ClusterCert: Optional[str]
    CryptoUserName: Optional[str]
    CryptoUserPassword: Optional[str]
    HsmIp: Optional[Sequence[str]]

    @classmethod
    def _deserialize(
        cls: Type["_CloudhsmDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_CloudhsmDefinition"]:
        if not json_data:
            return None
        return cls(
            ClusterCert=json_data.get("ClusterCert"),
            CryptoUserName=json_data.get("CryptoUserName"),
            CryptoUserPassword=json_data.get("CryptoUserPassword"),
            HsmIp=json_data.get("HsmIp"),
        )


# work around possible type aliasing issues when variable has same name as a model
_CloudhsmDefinition = CloudhsmDefinition


@dataclass
class NethsmDefinition(BaseModel):
    Esn: Optional[str]
    Keyhash: Optional[str]
    ModuleId: Optional[float]
    Priority: Optional[float]
    RemotePort: Optional[float]
    RemoteIp: Optional[Sequence["_RemoteIpDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_NethsmDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_NethsmDefinition"]:
        if not json_data:
            return None
        return cls(
            Esn=json_data.get("Esn"),
            Keyhash=json_data.get("Keyhash"),
            ModuleId=json_data.get("ModuleId"),
            Priority=json_data.get("Priority"),
            RemotePort=json_data.get("RemotePort"),
            RemoteIp=deserialize_list(json_data.get("RemoteIp"), RemoteIpDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_NethsmDefinition = NethsmDefinition


@dataclass
class RemoteIpDefinition(BaseModel):
    Addr: Optional[str]
    Type: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_RemoteIpDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_RemoteIpDefinition"]:
        if not json_data:
            return None
        return cls(
            Addr=json_data.get("Addr"),
            Type=json_data.get("Type"),
        )


# work around possible type aliasing issues when variable has same name as a model
_RemoteIpDefinition = RemoteIpDefinition


@dataclass
class RfsDefinition(BaseModel):
    Port: Optional[float]
    Ip: Optional[Sequence["_IpDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_RfsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_RfsDefinition"]:
        if not json_data:
            return None
        return cls(
            Port=json_data.get("Port"),
            Ip=deserialize_list(json_data.get("Ip"), IpDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_RfsDefinition = RfsDefinition


@dataclass
class IpDefinition(BaseModel):
    Addr: Optional[str]
    Type: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_IpDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_IpDefinition"]:
        if not json_data:
            return None
        return cls(
            Addr=json_data.get("Addr"),
            Type=json_data.get("Type"),
        )


# work around possible type aliasing issues when variable has same name as a model
_IpDefinition = IpDefinition


@dataclass
class SlunaDefinition(BaseModel):
    HaGroupNum: Optional[float]
    IsHa: Optional[bool]
    ServerPem: Optional[str]
    UseDedicatedNetwork: Optional[bool]
    NodeInfo: Optional[Sequence["_NodeInfoDefinition"]]
    Server: Optional[Sequence["_ServerDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_SlunaDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SlunaDefinition"]:
        if not json_data:
            return None
        return cls(
            HaGroupNum=json_data.get("HaGroupNum"),
            IsHa=json_data.get("IsHa"),
            ServerPem=json_data.get("ServerPem"),
            UseDedicatedNetwork=json_data.get("UseDedicatedNetwork"),
            NodeInfo=deserialize_list(json_data.get("NodeInfo"), NodeInfoDefinition),
            Server=deserialize_list(json_data.get("Server"), ServerDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_SlunaDefinition = SlunaDefinition


@dataclass
class NodeInfoDefinition(BaseModel):
    ChrystokiConf: Optional[str]
    ClientCert: Optional[str]
    ClientIp: Optional[str]
    ClientPrivKey: Optional[str]
    SessionMajorNumber: Optional[float]
    SessionMinorNumber: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_NodeInfoDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_NodeInfoDefinition"]:
        if not json_data:
            return None
        return cls(
            ChrystokiConf=json_data.get("ChrystokiConf"),
            ClientCert=json_data.get("ClientCert"),
            ClientIp=json_data.get("ClientIp"),
            ClientPrivKey=json_data.get("ClientPrivKey"),
            SessionMajorNumber=json_data.get("SessionMajorNumber"),
            SessionMinorNumber=json_data.get("SessionMinorNumber"),
        )


# work around possible type aliasing issues when variable has same name as a model
_NodeInfoDefinition = NodeInfoDefinition


@dataclass
class ServerDefinition(BaseModel):
    Index: Optional[float]
    PartitionPasswd: Optional[str]
    PartitionSerialNumber: Optional[str]
    RemoteIp: Optional[str]
    ServerCert: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ServerDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ServerDefinition"]:
        if not json_data:
            return None
        return cls(
            Index=json_data.get("Index"),
            PartitionPasswd=json_data.get("PartitionPasswd"),
            PartitionSerialNumber=json_data.get("PartitionSerialNumber"),
            RemoteIp=json_data.get("RemoteIp"),
            ServerCert=json_data.get("ServerCert"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ServerDefinition = ServerDefinition


@dataclass
class MarkersDefinition(BaseModel):
    Key: Optional[str]
    Values: Optional[Sequence[str]]

    @classmethod
    def _deserialize(
        cls: Type["_MarkersDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_MarkersDefinition"]:
        if not json_data:
            return None
        return cls(
            Key=json_data.get("Key"),
            Values=json_data.get("Values"),
        )


# work around possible type aliasing issues when variable has same name as a model
_MarkersDefinition = MarkersDefinition


