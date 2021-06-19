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
    BleScanReportIntv: Optional[float]
    ClientIdleTimeout: Optional[float]
    DarrpDay: Optional[str]
    DarrpOptimize: Optional[float]
    DiscoveryInterval: Optional[float]
    DrmaInterval: Optional[float]
    DynamicSortSubtable: Optional[str]
    EchoInterval: Optional[float]
    FakeApLog: Optional[float]
    Id: Optional[str]
    IpsecIntfCleanup: Optional[float]
    RadioStatsInterval: Optional[float]
    RogueApLog: Optional[float]
    StaCapabilityInterval: Optional[float]
    StaLocateTimer: Optional[float]
    StaStatsInterval: Optional[float]
    VapStatsInterval: Optional[float]
    Vdomparam: Optional[str]
    DarrpTime: Optional[Sequence["_DarrpTimeDefinition"]]

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
            BleScanReportIntv=json_data.get("BleScanReportIntv"),
            ClientIdleTimeout=json_data.get("ClientIdleTimeout"),
            DarrpDay=json_data.get("DarrpDay"),
            DarrpOptimize=json_data.get("DarrpOptimize"),
            DiscoveryInterval=json_data.get("DiscoveryInterval"),
            DrmaInterval=json_data.get("DrmaInterval"),
            DynamicSortSubtable=json_data.get("DynamicSortSubtable"),
            EchoInterval=json_data.get("EchoInterval"),
            FakeApLog=json_data.get("FakeApLog"),
            Id=json_data.get("Id"),
            IpsecIntfCleanup=json_data.get("IpsecIntfCleanup"),
            RadioStatsInterval=json_data.get("RadioStatsInterval"),
            RogueApLog=json_data.get("RogueApLog"),
            StaCapabilityInterval=json_data.get("StaCapabilityInterval"),
            StaLocateTimer=json_data.get("StaLocateTimer"),
            StaStatsInterval=json_data.get("StaStatsInterval"),
            VapStatsInterval=json_data.get("VapStatsInterval"),
            Vdomparam=json_data.get("Vdomparam"),
            DarrpTime=deserialize_list(json_data.get("DarrpTime"), DarrpTimeDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class DarrpTimeDefinition(BaseModel):
    Time: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_DarrpTimeDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DarrpTimeDefinition"]:
        if not json_data:
            return None
        return cls(
            Time=json_data.get("Time"),
        )


# work around possible type aliasing issues when variable has same name as a model
_DarrpTimeDefinition = DarrpTimeDefinition


