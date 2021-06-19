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
    BandwidthPackageIds: Optional[str]
    Description: Optional[str]
    DryRun: Optional[bool]
    Force: Optional[bool]
    ForwardTableIds: Optional[str]
    Id: Optional[str]
    InstanceChargeType: Optional[str]
    InternetChargeType: Optional[str]
    Name: Optional[str]
    NatGatewayName: Optional[str]
    NatType: Optional[str]
    PaymentType: Optional[str]
    Period: Optional[float]
    SnatTableIds: Optional[str]
    Spec: Optional[str]
    Specification: Optional[str]
    Status: Optional[str]
    Tags: Optional[Sequence["_TagsDefinition"]]
    VpcId: Optional[str]
    VswitchId: Optional[str]
    BandwidthPackages: Optional[Sequence["_BandwidthPackagesDefinition"]]
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
            BandwidthPackageIds=json_data.get("BandwidthPackageIds"),
            Description=json_data.get("Description"),
            DryRun=json_data.get("DryRun"),
            Force=json_data.get("Force"),
            ForwardTableIds=json_data.get("ForwardTableIds"),
            Id=json_data.get("Id"),
            InstanceChargeType=json_data.get("InstanceChargeType"),
            InternetChargeType=json_data.get("InternetChargeType"),
            Name=json_data.get("Name"),
            NatGatewayName=json_data.get("NatGatewayName"),
            NatType=json_data.get("NatType"),
            PaymentType=json_data.get("PaymentType"),
            Period=json_data.get("Period"),
            SnatTableIds=json_data.get("SnatTableIds"),
            Spec=json_data.get("Spec"),
            Specification=json_data.get("Specification"),
            Status=json_data.get("Status"),
            Tags=deserialize_list(json_data.get("Tags"), TagsDefinition),
            VpcId=json_data.get("VpcId"),
            VswitchId=json_data.get("VswitchId"),
            BandwidthPackages=deserialize_list(json_data.get("BandwidthPackages"), BandwidthPackagesDefinition),
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
class BandwidthPackagesDefinition(BaseModel):
    Bandwidth: Optional[float]
    IpCount: Optional[float]
    Zone: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_BandwidthPackagesDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_BandwidthPackagesDefinition"]:
        if not json_data:
            return None
        return cls(
            Bandwidth=json_data.get("Bandwidth"),
            IpCount=json_data.get("IpCount"),
            Zone=json_data.get("Zone"),
        )


# work around possible type aliasing issues when variable has same name as a model
_BandwidthPackagesDefinition = BandwidthPackagesDefinition


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


