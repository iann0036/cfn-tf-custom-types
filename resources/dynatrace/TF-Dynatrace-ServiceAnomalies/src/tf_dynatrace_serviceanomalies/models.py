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
    Id: Optional[str]
    FailureRates: Optional[Sequence["_FailureRatesDefinition"]]
    Load: Optional[Sequence["_LoadDefinition"]]
    LoadDrops: Optional[Sequence["_LoadDropsDefinition"]]
    ResponseTimes: Optional[Sequence["_ResponseTimesDefinition"]]

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
            Id=json_data.get("Id"),
            FailureRates=deserialize_list(json_data.get("FailureRates"), FailureRatesDefinition),
            Load=deserialize_list(json_data.get("Load"), LoadDefinition),
            LoadDrops=deserialize_list(json_data.get("LoadDrops"), LoadDropsDefinition),
            ResponseTimes=deserialize_list(json_data.get("ResponseTimes"), ResponseTimesDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class FailureRatesDefinition(BaseModel):
    Auto: Optional[Sequence["_AutoDefinition"]]
    Thresholds: Optional[Sequence["_ThresholdsDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_FailureRatesDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_FailureRatesDefinition"]:
        if not json_data:
            return None
        return cls(
            Auto=deserialize_list(json_data.get("Auto"), AutoDefinition),
            Thresholds=deserialize_list(json_data.get("Thresholds"), ThresholdsDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_FailureRatesDefinition = FailureRatesDefinition


@dataclass
class AutoDefinition(BaseModel):
    Load: Optional[str]
    Milliseconds: Optional[float]
    Percent: Optional[float]
    SlowestMilliseconds: Optional[float]
    SlowestPercent: Optional[float]
    Unknowns: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_AutoDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AutoDefinition"]:
        if not json_data:
            return None
        return cls(
            Load=json_data.get("Load"),
            Milliseconds=json_data.get("Milliseconds"),
            Percent=json_data.get("Percent"),
            SlowestMilliseconds=json_data.get("SlowestMilliseconds"),
            SlowestPercent=json_data.get("SlowestPercent"),
            Unknowns=json_data.get("Unknowns"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AutoDefinition = AutoDefinition


@dataclass
class ThresholdsDefinition(BaseModel):
    Load: Optional[str]
    Milliseconds: Optional[float]
    Sensitivity: Optional[str]
    SlowestMilliseconds: Optional[float]
    Unknowns: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ThresholdsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ThresholdsDefinition"]:
        if not json_data:
            return None
        return cls(
            Load=json_data.get("Load"),
            Milliseconds=json_data.get("Milliseconds"),
            Sensitivity=json_data.get("Sensitivity"),
            SlowestMilliseconds=json_data.get("SlowestMilliseconds"),
            Unknowns=json_data.get("Unknowns"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ThresholdsDefinition = ThresholdsDefinition


@dataclass
class LoadDefinition(BaseModel):
    Drops: Optional[Sequence["_DropsDefinition"]]
    Spikes: Optional[Sequence["_SpikesDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_LoadDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_LoadDefinition"]:
        if not json_data:
            return None
        return cls(
            Drops=deserialize_list(json_data.get("Drops"), DropsDefinition),
            Spikes=deserialize_list(json_data.get("Spikes"), SpikesDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_LoadDefinition = LoadDefinition


@dataclass
class DropsDefinition(BaseModel):
    Minutes: Optional[float]
    Percent: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_DropsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DropsDefinition"]:
        if not json_data:
            return None
        return cls(
            Minutes=json_data.get("Minutes"),
            Percent=json_data.get("Percent"),
        )


# work around possible type aliasing issues when variable has same name as a model
_DropsDefinition = DropsDefinition


@dataclass
class SpikesDefinition(BaseModel):
    Minutes: Optional[float]
    Percent: Optional[float]
    Unknowns: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_SpikesDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SpikesDefinition"]:
        if not json_data:
            return None
        return cls(
            Minutes=json_data.get("Minutes"),
            Percent=json_data.get("Percent"),
            Unknowns=json_data.get("Unknowns"),
        )


# work around possible type aliasing issues when variable has same name as a model
_SpikesDefinition = SpikesDefinition


@dataclass
class LoadDropsDefinition(BaseModel):
    Minutes: Optional[float]
    Percent: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_LoadDropsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_LoadDropsDefinition"]:
        if not json_data:
            return None
        return cls(
            Minutes=json_data.get("Minutes"),
            Percent=json_data.get("Percent"),
        )


# work around possible type aliasing issues when variable has same name as a model
_LoadDropsDefinition = LoadDropsDefinition


@dataclass
class ResponseTimesDefinition(BaseModel):
    Auto: Optional[Sequence["_AutoDefinition"]]
    Thresholds: Optional[Sequence["_ThresholdsDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_ResponseTimesDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResponseTimesDefinition"]:
        if not json_data:
            return None
        return cls(
            Auto=deserialize_list(json_data.get("Auto"), AutoDefinition),
            Thresholds=deserialize_list(json_data.get("Thresholds"), ThresholdsDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResponseTimesDefinition = ResponseTimesDefinition


