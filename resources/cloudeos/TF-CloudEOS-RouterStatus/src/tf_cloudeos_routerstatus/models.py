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
    AvailabilitySetId: Optional[str]
    AvailabilityZone: Optional[str]
    CloudProvider: Optional[str]
    Cnps: Optional[str]
    CvContainer: Optional[str]
    DeploymentStatus: Optional[str]
    HaName: Optional[str]
    Id: Optional[str]
    InstanceId: Optional[str]
    InstanceType: Optional[str]
    InternalRtTableIds: Optional[Sequence[str]]
    IntfId: Optional[Sequence[str]]
    IntfName: Optional[Sequence[str]]
    IntfPrivateIp: Optional[Sequence[str]]
    IntfSubnetId: Optional[Sequence[str]]
    IntfType: Optional[Sequence[str]]
    IsRr: Optional[bool]
    PrimaryNetworkInterfaceId: Optional[str]
    PrivateRtTableIds: Optional[Sequence[str]]
    PublicIp: Optional[str]
    PublicRtTableIds: Optional[Sequence[str]]
    Region: Optional[str]
    RgLocation: Optional[str]
    RgName: Optional[str]
    RouterBgpAsn: Optional[str]
    RoutingResourceInfo: Optional[Sequence[str]]
    Tags: Optional[Sequence["_TagsDefinition"]]
    TfId: Optional[str]
    VpcId: Optional[str]
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
            AvailabilitySetId=json_data.get("AvailabilitySetId"),
            AvailabilityZone=json_data.get("AvailabilityZone"),
            CloudProvider=json_data.get("CloudProvider"),
            Cnps=json_data.get("Cnps"),
            CvContainer=json_data.get("CvContainer"),
            DeploymentStatus=json_data.get("DeploymentStatus"),
            HaName=json_data.get("HaName"),
            Id=json_data.get("Id"),
            InstanceId=json_data.get("InstanceId"),
            InstanceType=json_data.get("InstanceType"),
            InternalRtTableIds=json_data.get("InternalRtTableIds"),
            IntfId=json_data.get("IntfId"),
            IntfName=json_data.get("IntfName"),
            IntfPrivateIp=json_data.get("IntfPrivateIp"),
            IntfSubnetId=json_data.get("IntfSubnetId"),
            IntfType=json_data.get("IntfType"),
            IsRr=json_data.get("IsRr"),
            PrimaryNetworkInterfaceId=json_data.get("PrimaryNetworkInterfaceId"),
            PrivateRtTableIds=json_data.get("PrivateRtTableIds"),
            PublicIp=json_data.get("PublicIp"),
            PublicRtTableIds=json_data.get("PublicRtTableIds"),
            Region=json_data.get("Region"),
            RgLocation=json_data.get("RgLocation"),
            RgName=json_data.get("RgName"),
            RouterBgpAsn=json_data.get("RouterBgpAsn"),
            RoutingResourceInfo=json_data.get("RoutingResourceInfo"),
            Tags=deserialize_list(json_data.get("Tags"), TagsDefinition),
            TfId=json_data.get("TfId"),
            VpcId=json_data.get("VpcId"),
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
    Delete: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_TimeoutsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TimeoutsDefinition"]:
        if not json_data:
            return None
        return cls(
            Delete=json_data.get("Delete"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TimeoutsDefinition = TimeoutsDefinition


