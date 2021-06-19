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
    AutoscalingPolicy: Optional[str]
    BidPrice: Optional[str]
    ClusterId: Optional[str]
    ConfigurationsJson: Optional[str]
    EbsOptimized: Optional[bool]
    Id: Optional[str]
    InstanceCount: Optional[float]
    InstanceType: Optional[str]
    Name: Optional[str]
    RunningInstanceCount: Optional[float]
    Status: Optional[str]
    EbsConfig: Optional[Sequence["_EbsConfigDefinition"]]

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
            AutoscalingPolicy=json_data.get("AutoscalingPolicy"),
            BidPrice=json_data.get("BidPrice"),
            ClusterId=json_data.get("ClusterId"),
            ConfigurationsJson=json_data.get("ConfigurationsJson"),
            EbsOptimized=json_data.get("EbsOptimized"),
            Id=json_data.get("Id"),
            InstanceCount=json_data.get("InstanceCount"),
            InstanceType=json_data.get("InstanceType"),
            Name=json_data.get("Name"),
            RunningInstanceCount=json_data.get("RunningInstanceCount"),
            Status=json_data.get("Status"),
            EbsConfig=deserialize_list(json_data.get("EbsConfig"), EbsConfigDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


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


