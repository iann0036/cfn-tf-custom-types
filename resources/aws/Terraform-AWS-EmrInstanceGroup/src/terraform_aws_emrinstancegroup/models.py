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
    AutoscalingPolicy: Optional[str]
    BidPrice: Optional[str]
    ClusterId: Optional[str]
    ConfigurationsJson: Optional[str]
    EbsOptimized: Optional[bool]
    InstanceCount: Optional[float]
    InstanceType: Optional[str]
    Name: Optional[str]
    RunningInstanceCount: Optional[float]
    Status: Optional[str]
    EbsConfig: Optional[Sequence["_EbsConfig"]]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceModel"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceModel"]:
        if not json_data:
            return None
        return cls(
            tfcfnid=json_data.get("tfcfnid"),
            AutoscalingPolicy=json_data.get("AutoscalingPolicy"),
            BidPrice=json_data.get("BidPrice"),
            ClusterId=json_data.get("ClusterId"),
            ConfigurationsJson=json_data.get("ConfigurationsJson"),
            EbsOptimized=json_data.get("EbsOptimized"),
            InstanceCount=json_data.get("InstanceCount"),
            InstanceType=json_data.get("InstanceType"),
            Name=json_data.get("Name"),
            RunningInstanceCount=json_data.get("RunningInstanceCount"),
            Status=json_data.get("Status"),
            EbsConfig=json_data.get("EbsConfig"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class EbsConfig:
    Iops: Optional[float]
    Size: Optional[float]
    Type: Optional[str]
    VolumesPerInstance: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_EbsConfig"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_EbsConfig"]:
        if not json_data:
            return None
        return cls(
            Iops=json_data.get("Iops"),
            Size=json_data.get("Size"),
            Type=json_data.get("Type"),
            VolumesPerInstance=json_data.get("VolumesPerInstance"),
        )


# work around possible type aliasing issues when variable has same name as a model
_EbsConfig = EbsConfig


