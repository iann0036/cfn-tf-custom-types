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
    ClusterId: Optional[str]
    Id: Optional[str]
    Name: Optional[str]
    ProvisionedOnDemandCapacity: Optional[float]
    ProvisionedSpotCapacity: Optional[float]
    TargetOnDemandCapacity: Optional[float]
    TargetSpotCapacity: Optional[float]
    InstanceTypeConfigs: Optional[Sequence["_InstanceTypeConfigsDefinition"]]
    LaunchSpecifications: Optional[Sequence["_LaunchSpecificationsDefinition"]]

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
            ClusterId=json_data.get("ClusterId"),
            Id=json_data.get("Id"),
            Name=json_data.get("Name"),
            ProvisionedOnDemandCapacity=json_data.get("ProvisionedOnDemandCapacity"),
            ProvisionedSpotCapacity=json_data.get("ProvisionedSpotCapacity"),
            TargetOnDemandCapacity=json_data.get("TargetOnDemandCapacity"),
            TargetSpotCapacity=json_data.get("TargetSpotCapacity"),
            InstanceTypeConfigs=deserialize_list(json_data.get("InstanceTypeConfigs"), InstanceTypeConfigsDefinition),
            LaunchSpecifications=deserialize_list(json_data.get("LaunchSpecifications"), LaunchSpecificationsDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class InstanceTypeConfigsDefinition(BaseModel):
    BidPrice: Optional[str]
    BidPriceAsPercentageOfOnDemandPrice: Optional[float]
    InstanceType: Optional[str]
    WeightedCapacity: Optional[float]
    Configurations: Optional[Sequence["_ConfigurationsDefinition"]]
    EbsConfig: Optional[Sequence["_EbsConfigDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_InstanceTypeConfigsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_InstanceTypeConfigsDefinition"]:
        if not json_data:
            return None
        return cls(
            BidPrice=json_data.get("BidPrice"),
            BidPriceAsPercentageOfOnDemandPrice=json_data.get("BidPriceAsPercentageOfOnDemandPrice"),
            InstanceType=json_data.get("InstanceType"),
            WeightedCapacity=json_data.get("WeightedCapacity"),
            Configurations=deserialize_list(json_data.get("Configurations"), ConfigurationsDefinition),
            EbsConfig=deserialize_list(json_data.get("EbsConfig"), EbsConfigDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_InstanceTypeConfigsDefinition = InstanceTypeConfigsDefinition


@dataclass
class ConfigurationsDefinition(BaseModel):
    Classification: Optional[str]
    Properties: Optional[Sequence["_PropertiesDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_ConfigurationsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ConfigurationsDefinition"]:
        if not json_data:
            return None
        return cls(
            Classification=json_data.get("Classification"),
            Properties=deserialize_list(json_data.get("Properties"), PropertiesDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ConfigurationsDefinition = ConfigurationsDefinition


@dataclass
class PropertiesDefinition(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_PropertiesDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_PropertiesDefinition"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_PropertiesDefinition = PropertiesDefinition


@dataclass
class EbsConfigDefinition(BaseModel):
    Iops: Optional[float]
    Size: Optional[float]
    Type: Optional[str]
    VolumesPerInstance: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_EbsConfigDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_EbsConfigDefinition"]:
        if not json_data:
            return None
        return cls(
            Iops=json_data.get("Iops"),
            Size=json_data.get("Size"),
            Type=json_data.get("Type"),
            VolumesPerInstance=json_data.get("VolumesPerInstance"),
        )


# work around possible type aliasing issues when variable has same name as a model
_EbsConfigDefinition = EbsConfigDefinition


@dataclass
class LaunchSpecificationsDefinition(BaseModel):
    OnDemandSpecification: Optional[Sequence["_OnDemandSpecificationDefinition"]]
    SpotSpecification: Optional[Sequence["_SpotSpecificationDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_LaunchSpecificationsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_LaunchSpecificationsDefinition"]:
        if not json_data:
            return None
        return cls(
            OnDemandSpecification=deserialize_list(json_data.get("OnDemandSpecification"), OnDemandSpecificationDefinition),
            SpotSpecification=deserialize_list(json_data.get("SpotSpecification"), SpotSpecificationDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_LaunchSpecificationsDefinition = LaunchSpecificationsDefinition


@dataclass
class OnDemandSpecificationDefinition(BaseModel):
    AllocationStrategy: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_OnDemandSpecificationDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_OnDemandSpecificationDefinition"]:
        if not json_data:
            return None
        return cls(
            AllocationStrategy=json_data.get("AllocationStrategy"),
        )


# work around possible type aliasing issues when variable has same name as a model
_OnDemandSpecificationDefinition = OnDemandSpecificationDefinition


@dataclass
class SpotSpecificationDefinition(BaseModel):
    AllocationStrategy: Optional[str]
    BlockDurationMinutes: Optional[float]
    TimeoutAction: Optional[str]
    TimeoutDurationMinutes: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_SpotSpecificationDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SpotSpecificationDefinition"]:
        if not json_data:
            return None
        return cls(
            AllocationStrategy=json_data.get("AllocationStrategy"),
            BlockDurationMinutes=json_data.get("BlockDurationMinutes"),
            TimeoutAction=json_data.get("TimeoutAction"),
            TimeoutDurationMinutes=json_data.get("TimeoutDurationMinutes"),
        )


# work around possible type aliasing issues when variable has same name as a model
_SpotSpecificationDefinition = SpotSpecificationDefinition


