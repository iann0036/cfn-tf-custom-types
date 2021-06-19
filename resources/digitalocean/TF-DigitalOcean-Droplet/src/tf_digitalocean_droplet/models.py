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
    Backups: Optional[bool]
    CreatedAt: Optional[str]
    Disk: Optional[float]
    Id: Optional[str]
    Image: Optional[str]
    Ipv4Address: Optional[str]
    Ipv4AddressPrivate: Optional[str]
    Ipv6: Optional[bool]
    Ipv6Address: Optional[str]
    Locked: Optional[bool]
    Memory: Optional[float]
    Monitoring: Optional[bool]
    Name: Optional[str]
    PriceHourly: Optional[float]
    PriceMonthly: Optional[float]
    PrivateNetworking: Optional[bool]
    Region: Optional[str]
    ResizeDisk: Optional[bool]
    Size: Optional[str]
    SshKeys: Optional[Sequence[str]]
    Status: Optional[str]
    Tags: Optional[Sequence[str]]
    Urn: Optional[str]
    UserData: Optional[str]
    Vcpus: Optional[float]
    VolumeIds: Optional[Sequence[str]]
    VpcUuid: Optional[str]

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
            Backups=json_data.get("Backups"),
            CreatedAt=json_data.get("CreatedAt"),
            Disk=json_data.get("Disk"),
            Id=json_data.get("Id"),
            Image=json_data.get("Image"),
            Ipv4Address=json_data.get("Ipv4Address"),
            Ipv4AddressPrivate=json_data.get("Ipv4AddressPrivate"),
            Ipv6=json_data.get("Ipv6"),
            Ipv6Address=json_data.get("Ipv6Address"),
            Locked=json_data.get("Locked"),
            Memory=json_data.get("Memory"),
            Monitoring=json_data.get("Monitoring"),
            Name=json_data.get("Name"),
            PriceHourly=json_data.get("PriceHourly"),
            PriceMonthly=json_data.get("PriceMonthly"),
            PrivateNetworking=json_data.get("PrivateNetworking"),
            Region=json_data.get("Region"),
            ResizeDisk=json_data.get("ResizeDisk"),
            Size=json_data.get("Size"),
            SshKeys=json_data.get("SshKeys"),
            Status=json_data.get("Status"),
            Tags=json_data.get("Tags"),
            Urn=json_data.get("Urn"),
            UserData=json_data.get("UserData"),
            Vcpus=json_data.get("Vcpus"),
            VolumeIds=json_data.get("VolumeIds"),
            VpcUuid=json_data.get("VpcUuid"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


