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
    Comment: Optional[str]
    Id: Optional[str]
    IncludeDfsChannel: Optional[str]
    IncludeWeatherChannel: Optional[str]
    MonitorPeriod: Optional[float]
    Name: Optional[str]
    SelectionPeriod: Optional[float]
    ThresholdAp: Optional[float]
    ThresholdChannelLoad: Optional[float]
    ThresholdNoiseFloor: Optional[str]
    ThresholdRxErrors: Optional[float]
    ThresholdSpectralRssi: Optional[str]
    ThresholdTxRetries: Optional[float]
    Vdomparam: Optional[str]
    WeightChannelLoad: Optional[float]
    WeightDfsChannel: Optional[float]
    WeightManagedAp: Optional[float]
    WeightNoiseFloor: Optional[float]
    WeightRogueAp: Optional[float]
    WeightSpectralRssi: Optional[float]
    WeightWeatherChannel: Optional[float]

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
            Comment=json_data.get("Comment"),
            Id=json_data.get("Id"),
            IncludeDfsChannel=json_data.get("IncludeDfsChannel"),
            IncludeWeatherChannel=json_data.get("IncludeWeatherChannel"),
            MonitorPeriod=json_data.get("MonitorPeriod"),
            Name=json_data.get("Name"),
            SelectionPeriod=json_data.get("SelectionPeriod"),
            ThresholdAp=json_data.get("ThresholdAp"),
            ThresholdChannelLoad=json_data.get("ThresholdChannelLoad"),
            ThresholdNoiseFloor=json_data.get("ThresholdNoiseFloor"),
            ThresholdRxErrors=json_data.get("ThresholdRxErrors"),
            ThresholdSpectralRssi=json_data.get("ThresholdSpectralRssi"),
            ThresholdTxRetries=json_data.get("ThresholdTxRetries"),
            Vdomparam=json_data.get("Vdomparam"),
            WeightChannelLoad=json_data.get("WeightChannelLoad"),
            WeightDfsChannel=json_data.get("WeightDfsChannel"),
            WeightManagedAp=json_data.get("WeightManagedAp"),
            WeightNoiseFloor=json_data.get("WeightNoiseFloor"),
            WeightRogueAp=json_data.get("WeightRogueAp"),
            WeightSpectralRssi=json_data.get("WeightSpectralRssi"),
            WeightWeatherChannel=json_data.get("WeightWeatherChannel"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


