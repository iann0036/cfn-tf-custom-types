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
    BackupWindow: Optional[str]
    Backups: Optional[bool]
    Datacenter: Optional[str]
    Id: Optional[str]
    Image: Optional[str]
    Ipv4Address: Optional[str]
    Ipv6Address: Optional[str]
    Ipv6Network: Optional[str]
    Iso: Optional[str]
    KeepDisk: Optional[bool]
    Labels: Optional[Sequence["_Labels"]]
    Location: Optional[str]
    Name: Optional[str]
    Rescue: Optional[str]
    ServerType: Optional[str]
    SshKeys: Optional[Sequence[str]]
    Status: Optional[str]
    UserData: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceModel"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceModel"]:
        if not json_data:
            return None
        return cls(
            tfcfnid=json_data.get("tfcfnid"),
            BackupWindow=json_data.get("BackupWindow"),
            Backups=json_data.get("Backups"),
            Datacenter=json_data.get("Datacenter"),
            Id=json_data.get("Id"),
            Image=json_data.get("Image"),
            Ipv4Address=json_data.get("Ipv4Address"),
            Ipv6Address=json_data.get("Ipv6Address"),
            Ipv6Network=json_data.get("Ipv6Network"),
            Iso=json_data.get("Iso"),
            KeepDisk=json_data.get("KeepDisk"),
            Labels=json_data.get("Labels"),
            Location=json_data.get("Location"),
            Name=json_data.get("Name"),
            Rescue=json_data.get("Rescue"),
            ServerType=json_data.get("ServerType"),
            SshKeys=json_data.get("SshKeys"),
            Status=json_data.get("Status"),
            UserData=json_data.get("UserData"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class Labels:
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Labels"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Labels"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Labels = Labels


