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
    AdditionalVolumeIds: Optional[Sequence[str]]
    BootType: Optional[str]
    BootscriptId: Optional[str]
    CloudInit: Optional[str]
    EnableDynamicIp: Optional[bool]
    EnableIpv6: Optional[bool]
    Id: Optional[str]
    Image: Optional[str]
    IpId: Optional[str]
    Ipv6Address: Optional[str]
    Ipv6Gateway: Optional[str]
    Ipv6PrefixLength: Optional[float]
    Name: Optional[str]
    OrganizationId: Optional[str]
    PlacementGroupId: Optional[str]
    PlacementGroupPolicyRespected: Optional[bool]
    PrivateIp: Optional[str]
    ProjectId: Optional[str]
    PublicIp: Optional[str]
    SecurityGroupId: Optional[str]
    State: Optional[str]
    Tags: Optional[Sequence[str]]
    Type: Optional[str]
    UserData: Optional[Sequence["_UserDataDefinition"]]
    Zone: Optional[str]
    RootVolume: Optional[Sequence["_RootVolumeDefinition"]]
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
            AdditionalVolumeIds=json_data.get("AdditionalVolumeIds"),
            BootType=json_data.get("BootType"),
            BootscriptId=json_data.get("BootscriptId"),
            CloudInit=json_data.get("CloudInit"),
            EnableDynamicIp=json_data.get("EnableDynamicIp"),
            EnableIpv6=json_data.get("EnableIpv6"),
            Id=json_data.get("Id"),
            Image=json_data.get("Image"),
            IpId=json_data.get("IpId"),
            Ipv6Address=json_data.get("Ipv6Address"),
            Ipv6Gateway=json_data.get("Ipv6Gateway"),
            Ipv6PrefixLength=json_data.get("Ipv6PrefixLength"),
            Name=json_data.get("Name"),
            OrganizationId=json_data.get("OrganizationId"),
            PlacementGroupId=json_data.get("PlacementGroupId"),
            PlacementGroupPolicyRespected=json_data.get("PlacementGroupPolicyRespected"),
            PrivateIp=json_data.get("PrivateIp"),
            ProjectId=json_data.get("ProjectId"),
            PublicIp=json_data.get("PublicIp"),
            SecurityGroupId=json_data.get("SecurityGroupId"),
            State=json_data.get("State"),
            Tags=json_data.get("Tags"),
            Type=json_data.get("Type"),
            UserData=deserialize_list(json_data.get("UserData"), UserDataDefinition),
            Zone=json_data.get("Zone"),
            RootVolume=deserialize_list(json_data.get("RootVolume"), RootVolumeDefinition),
            Timeouts=TimeoutsDefinition._deserialize(json_data.get("Timeouts")),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class UserDataDefinition(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_UserDataDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_UserDataDefinition"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_UserDataDefinition = UserDataDefinition


@dataclass
class RootVolumeDefinition(BaseModel):
    DeleteOnTermination: Optional[bool]
    SizeInGb: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_RootVolumeDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_RootVolumeDefinition"]:
        if not json_data:
            return None
        return cls(
            DeleteOnTermination=json_data.get("DeleteOnTermination"),
            SizeInGb=json_data.get("SizeInGb"),
        )


# work around possible type aliasing issues when variable has same name as a model
_RootVolumeDefinition = RootVolumeDefinition


@dataclass
class TimeoutsDefinition(BaseModel):
    Default: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_TimeoutsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TimeoutsDefinition"]:
        if not json_data:
            return None
        return cls(
            Default=json_data.get("Default"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TimeoutsDefinition = TimeoutsDefinition


