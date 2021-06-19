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
    AddressIpVersion: Optional[str]
    ClbName: Optional[str]
    ClbVips: Optional[Sequence[str]]
    Id: Optional[str]
    InternetBandwidthMaxOut: Optional[float]
    InternetChargeType: Optional[str]
    LoadBalancerPassToTarget: Optional[bool]
    MasterZoneId: Optional[str]
    NetworkType: Optional[str]
    ProjectId: Optional[float]
    SecurityGroups: Optional[Sequence[str]]
    SlaveZoneId: Optional[str]
    SubnetId: Optional[str]
    Tags: Optional[Sequence["_TagsDefinition"]]
    TargetRegionInfoRegion: Optional[str]
    TargetRegionInfoVpcId: Optional[str]
    VipIsp: Optional[str]
    VpcId: Optional[str]
    ZoneId: Optional[str]

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
            AddressIpVersion=json_data.get("AddressIpVersion"),
            ClbName=json_data.get("ClbName"),
            ClbVips=json_data.get("ClbVips"),
            Id=json_data.get("Id"),
            InternetBandwidthMaxOut=json_data.get("InternetBandwidthMaxOut"),
            InternetChargeType=json_data.get("InternetChargeType"),
            LoadBalancerPassToTarget=json_data.get("LoadBalancerPassToTarget"),
            MasterZoneId=json_data.get("MasterZoneId"),
            NetworkType=json_data.get("NetworkType"),
            ProjectId=json_data.get("ProjectId"),
            SecurityGroups=json_data.get("SecurityGroups"),
            SlaveZoneId=json_data.get("SlaveZoneId"),
            SubnetId=json_data.get("SubnetId"),
            Tags=deserialize_list(json_data.get("Tags"), TagsDefinition),
            TargetRegionInfoRegion=json_data.get("TargetRegionInfoRegion"),
            TargetRegionInfoVpcId=json_data.get("TargetRegionInfoVpcId"),
            VipIsp=json_data.get("VipIsp"),
            VpcId=json_data.get("VpcId"),
            ZoneId=json_data.get("ZoneId"),
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


