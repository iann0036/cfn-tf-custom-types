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
    ComputeClusterId: Optional[str]
    HaDatastoreApdRecoveryAction: Optional[str]
    HaDatastoreApdResponse: Optional[str]
    HaDatastoreApdResponseDelay: Optional[float]
    HaDatastorePdlResponse: Optional[str]
    HaHostIsolationResponse: Optional[str]
    HaVmFailureInterval: Optional[float]
    HaVmMaximumFailureWindow: Optional[float]
    HaVmMaximumResets: Optional[float]
    HaVmMinimumUptime: Optional[float]
    HaVmMonitoring: Optional[str]
    HaVmMonitoringUseClusterDefaults: Optional[bool]
    HaVmRestartPriority: Optional[str]
    HaVmRestartTimeout: Optional[float]
    Id: Optional[str]
    VirtualMachineId: Optional[str]

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
            ComputeClusterId=json_data.get("ComputeClusterId"),
            HaDatastoreApdRecoveryAction=json_data.get("HaDatastoreApdRecoveryAction"),
            HaDatastoreApdResponse=json_data.get("HaDatastoreApdResponse"),
            HaDatastoreApdResponseDelay=json_data.get("HaDatastoreApdResponseDelay"),
            HaDatastorePdlResponse=json_data.get("HaDatastorePdlResponse"),
            HaHostIsolationResponse=json_data.get("HaHostIsolationResponse"),
            HaVmFailureInterval=json_data.get("HaVmFailureInterval"),
            HaVmMaximumFailureWindow=json_data.get("HaVmMaximumFailureWindow"),
            HaVmMaximumResets=json_data.get("HaVmMaximumResets"),
            HaVmMinimumUptime=json_data.get("HaVmMinimumUptime"),
            HaVmMonitoring=json_data.get("HaVmMonitoring"),
            HaVmMonitoringUseClusterDefaults=json_data.get("HaVmMonitoringUseClusterDefaults"),
            HaVmRestartPriority=json_data.get("HaVmRestartPriority"),
            HaVmRestartTimeout=json_data.get("HaVmRestartTimeout"),
            Id=json_data.get("Id"),
            VirtualMachineId=json_data.get("VirtualMachineId"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


