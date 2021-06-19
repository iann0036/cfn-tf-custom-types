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
    BackupWindow: Optional[str]
    Backups: Optional[bool]
    Datacenter: Optional[str]
    FirewallIds: Optional[Sequence[float]]
    Id: Optional[str]
    Image: Optional[str]
    Ipv4Address: Optional[str]
    Ipv6Address: Optional[str]
    Ipv6Network: Optional[str]
    Iso: Optional[str]
    KeepDisk: Optional[bool]
    Labels: Optional[Sequence["_LabelsDefinition"]]
    Location: Optional[str]
    Name: Optional[str]
    Rescue: Optional[str]
    ServerType: Optional[str]
    SshKeys: Optional[Sequence[str]]
    Status: Optional[str]
    UserData: Optional[str]
    Network: Optional[Sequence["_NetworkDefinition"]]

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
            BackupWindow=json_data.get("BackupWindow"),
            Backups=json_data.get("Backups"),
            Datacenter=json_data.get("Datacenter"),
            FirewallIds=json_data.get("FirewallIds"),
            Id=json_data.get("Id"),
            Image=json_data.get("Image"),
            Ipv4Address=json_data.get("Ipv4Address"),
            Ipv6Address=json_data.get("Ipv6Address"),
            Ipv6Network=json_data.get("Ipv6Network"),
            Iso=json_data.get("Iso"),
            KeepDisk=json_data.get("KeepDisk"),
            Labels=deserialize_list(json_data.get("Labels"), LabelsDefinition),
            Location=json_data.get("Location"),
            Name=json_data.get("Name"),
            Rescue=json_data.get("Rescue"),
            ServerType=json_data.get("ServerType"),
            SshKeys=json_data.get("SshKeys"),
            Status=json_data.get("Status"),
            UserData=json_data.get("UserData"),
            Network=deserialize_list(json_data.get("Network"), NetworkDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class LabelsDefinition(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_LabelsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_LabelsDefinition"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_LabelsDefinition = LabelsDefinition


@dataclass
class NetworkDefinition(BaseModel):
    AliasIps: Optional[Sequence[str]]
    Ip: Optional[str]
    NetworkId: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_NetworkDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_NetworkDefinition"]:
        if not json_data:
            return None
        return cls(
            AliasIps=json_data.get("AliasIps"),
            Ip=json_data.get("Ip"),
            NetworkId=json_data.get("NetworkId"),
        )


# work around possible type aliasing issues when variable has same name as a model
_NetworkDefinition = NetworkDefinition


