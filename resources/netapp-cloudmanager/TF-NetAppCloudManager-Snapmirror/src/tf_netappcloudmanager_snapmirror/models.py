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
    CapacityTier: Optional[str]
    ClientId: Optional[str]
    DestinationAggregateName: Optional[str]
    DestinationSvmName: Optional[str]
    DestinationVolumeName: Optional[str]
    DestinationWorkingEnvironmentId: Optional[str]
    DestinationWorkingEnvironmentName: Optional[str]
    Id: Optional[str]
    Iops: Optional[float]
    MaxTransferRate: Optional[float]
    Policy: Optional[str]
    ProviderVolumeType: Optional[str]
    Schedule: Optional[str]
    SourceSvmName: Optional[str]
    SourceVolumeName: Optional[str]
    SourceWorkingEnvironmentId: Optional[str]
    SourceWorkingEnvironmentName: Optional[str]
    Throughput: Optional[float]

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
            CapacityTier=json_data.get("CapacityTier"),
            ClientId=json_data.get("ClientId"),
            DestinationAggregateName=json_data.get("DestinationAggregateName"),
            DestinationSvmName=json_data.get("DestinationSvmName"),
            DestinationVolumeName=json_data.get("DestinationVolumeName"),
            DestinationWorkingEnvironmentId=json_data.get("DestinationWorkingEnvironmentId"),
            DestinationWorkingEnvironmentName=json_data.get("DestinationWorkingEnvironmentName"),
            Id=json_data.get("Id"),
            Iops=json_data.get("Iops"),
            MaxTransferRate=json_data.get("MaxTransferRate"),
            Policy=json_data.get("Policy"),
            ProviderVolumeType=json_data.get("ProviderVolumeType"),
            Schedule=json_data.get("Schedule"),
            SourceSvmName=json_data.get("SourceSvmName"),
            SourceVolumeName=json_data.get("SourceVolumeName"),
            SourceWorkingEnvironmentId=json_data.get("SourceWorkingEnvironmentId"),
            SourceWorkingEnvironmentName=json_data.get("SourceWorkingEnvironmentName"),
            Throughput=json_data.get("Throughput"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


