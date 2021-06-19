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
    AccountId: Optional[str]
    Country: Optional[str]
    DarrpOptimize: Optional[float]
    DeviceHoldoff: Optional[float]
    DeviceIdle: Optional[float]
    DeviceWeight: Optional[float]
    DuplicateSsid: Optional[str]
    DynamicSortSubtable: Optional[str]
    FakeSsidAction: Optional[str]
    FapcCompatibility: Optional[str]
    Id: Optional[str]
    PhishingSsidDetect: Optional[str]
    Vdomparam: Optional[str]
    WfaCompatibility: Optional[str]
    DarrpOptimizeSchedules: Optional[Sequence["_DarrpOptimizeSchedulesDefinition"]]
    OffendingSsid: Optional[Sequence["_OffendingSsidDefinition"]]

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
            AccountId=json_data.get("AccountId"),
            Country=json_data.get("Country"),
            DarrpOptimize=json_data.get("DarrpOptimize"),
            DeviceHoldoff=json_data.get("DeviceHoldoff"),
            DeviceIdle=json_data.get("DeviceIdle"),
            DeviceWeight=json_data.get("DeviceWeight"),
            DuplicateSsid=json_data.get("DuplicateSsid"),
            DynamicSortSubtable=json_data.get("DynamicSortSubtable"),
            FakeSsidAction=json_data.get("FakeSsidAction"),
            FapcCompatibility=json_data.get("FapcCompatibility"),
            Id=json_data.get("Id"),
            PhishingSsidDetect=json_data.get("PhishingSsidDetect"),
            Vdomparam=json_data.get("Vdomparam"),
            WfaCompatibility=json_data.get("WfaCompatibility"),
            DarrpOptimizeSchedules=deserialize_list(json_data.get("DarrpOptimizeSchedules"), DarrpOptimizeSchedulesDefinition),
            OffendingSsid=deserialize_list(json_data.get("OffendingSsid"), OffendingSsidDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class DarrpOptimizeSchedulesDefinition(BaseModel):
    Name: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_DarrpOptimizeSchedulesDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DarrpOptimizeSchedulesDefinition"]:
        if not json_data:
            return None
        return cls(
            Name=json_data.get("Name"),
        )


# work around possible type aliasing issues when variable has same name as a model
_DarrpOptimizeSchedulesDefinition = DarrpOptimizeSchedulesDefinition


@dataclass
class OffendingSsidDefinition(BaseModel):
    Action: Optional[str]
    Id: Optional[float]
    SsidPattern: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_OffendingSsidDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_OffendingSsidDefinition"]:
        if not json_data:
            return None
        return cls(
            Action=json_data.get("Action"),
            Id=json_data.get("Id"),
            SsidPattern=json_data.get("SsidPattern"),
        )


# work around possible type aliasing issues when variable has same name as a model
_OffendingSsidDefinition = OffendingSsidDefinition


