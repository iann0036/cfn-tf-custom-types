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
    Description: Optional[str]
    Id: Optional[str]
    Mac: Optional[str]
    Name: Optional[str]
    NetworkInterfaceName: Optional[str]
    PrimaryIpAddress: Optional[str]
    PrivateIp: Optional[str]
    PrivateIpAddresses: Optional[Sequence[str]]
    PrivateIps: Optional[Sequence[str]]
    PrivateIpsCount: Optional[float]
    QueueNumber: Optional[float]
    ResourceGroupId: Optional[str]
    SecondaryPrivateIpAddressCount: Optional[float]
    SecurityGroupIds: Optional[Sequence[str]]
    SecurityGroups: Optional[Sequence[str]]
    Status: Optional[str]
    Tags: Optional[Sequence["_TagsDefinition"]]
    VswitchId: Optional[str]
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
            Description=json_data.get("Description"),
            Id=json_data.get("Id"),
            Mac=json_data.get("Mac"),
            Name=json_data.get("Name"),
            NetworkInterfaceName=json_data.get("NetworkInterfaceName"),
            PrimaryIpAddress=json_data.get("PrimaryIpAddress"),
            PrivateIp=json_data.get("PrivateIp"),
            PrivateIpAddresses=json_data.get("PrivateIpAddresses"),
            PrivateIps=json_data.get("PrivateIps"),
            PrivateIpsCount=json_data.get("PrivateIpsCount"),
            QueueNumber=json_data.get("QueueNumber"),
            ResourceGroupId=json_data.get("ResourceGroupId"),
            SecondaryPrivateIpAddressCount=json_data.get("SecondaryPrivateIpAddressCount"),
            SecurityGroupIds=json_data.get("SecurityGroupIds"),
            SecurityGroups=json_data.get("SecurityGroups"),
            Status=json_data.get("Status"),
            Tags=deserialize_list(json_data.get("Tags"), TagsDefinition),
            VswitchId=json_data.get("VswitchId"),
            Timeouts=TimeoutsDefinition._deserialize(json_data.get("Timeouts")),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class TagsDefinition(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_TagsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TagsDefinition"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TagsDefinition = TagsDefinition


@dataclass
class TimeoutsDefinition(BaseModel):
    Create: Optional[str]
    Delete: Optional[str]
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
            Update=json_data.get("Update"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TimeoutsDefinition = TimeoutsDefinition


