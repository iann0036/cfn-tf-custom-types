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
    DataSyncInterval: Optional[float]
    Id: Optional[str]
    IotHoldoff: Optional[float]
    IotMacIdle: Optional[float]
    IotScanInterval: Optional[float]
    IotWeightThreshold: Optional[float]
    NacPeriodicInterval: Optional[float]
    ParallelProcess: Optional[float]
    ParallelProcessOverride: Optional[str]
    Vdomparam: Optional[str]

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
            DataSyncInterval=json_data.get("DataSyncInterval"),
            Id=json_data.get("Id"),
            IotHoldoff=json_data.get("IotHoldoff"),
            IotMacIdle=json_data.get("IotMacIdle"),
            IotScanInterval=json_data.get("IotScanInterval"),
            IotWeightThreshold=json_data.get("IotWeightThreshold"),
            NacPeriodicInterval=json_data.get("NacPeriodicInterval"),
            ParallelProcess=json_data.get("ParallelProcess"),
            ParallelProcessOverride=json_data.get("ParallelProcessOverride"),
            Vdomparam=json_data.get("Vdomparam"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


