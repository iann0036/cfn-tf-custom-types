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
    AvailabilityZoneId: Optional[str]
    AvailabilityZoneName: Optional[str]
    DnsName: Optional[str]
    FileSystemArn: Optional[str]
    FileSystemId: Optional[str]
    Id: Optional[str]
    IpAddress: Optional[str]
    MountTargetDnsName: Optional[str]
    NetworkInterfaceId: Optional[str]
    OwnerId: Optional[str]
    SecurityGroups: Optional[Sequence[str]]
    SubnetId: Optional[str]

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
            AvailabilityZoneId=json_data.get("AvailabilityZoneId"),
            AvailabilityZoneName=json_data.get("AvailabilityZoneName"),
            DnsName=json_data.get("DnsName"),
            FileSystemArn=json_data.get("FileSystemArn"),
            FileSystemId=json_data.get("FileSystemId"),
            Id=json_data.get("Id"),
            IpAddress=json_data.get("IpAddress"),
            MountTargetDnsName=json_data.get("MountTargetDnsName"),
            NetworkInterfaceId=json_data.get("NetworkInterfaceId"),
            OwnerId=json_data.get("OwnerId"),
            SecurityGroups=json_data.get("SecurityGroups"),
            SubnetId=json_data.get("SubnetId"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


