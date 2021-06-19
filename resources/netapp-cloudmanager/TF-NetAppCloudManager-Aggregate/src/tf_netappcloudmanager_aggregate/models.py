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
    DiskSizeSize: Optional[float]
    DiskSizeUnit: Optional[str]
    HomeNode: Optional[str]
    Id: Optional[str]
    Iops: Optional[float]
    Name: Optional[str]
    NumberOfDisks: Optional[float]
    ProviderVolumeType: Optional[str]
    Throughput: Optional[float]
    WorkingEnvironmentId: Optional[str]
    WorkingEnvironmentName: Optional[str]

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
            DiskSizeSize=json_data.get("DiskSizeSize"),
            DiskSizeUnit=json_data.get("DiskSizeUnit"),
            HomeNode=json_data.get("HomeNode"),
            Id=json_data.get("Id"),
            Iops=json_data.get("Iops"),
            Name=json_data.get("Name"),
            NumberOfDisks=json_data.get("NumberOfDisks"),
            ProviderVolumeType=json_data.get("ProviderVolumeType"),
            Throughput=json_data.get("Throughput"),
            WorkingEnvironmentId=json_data.get("WorkingEnvironmentId"),
            WorkingEnvironmentName=json_data.get("WorkingEnvironmentName"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


