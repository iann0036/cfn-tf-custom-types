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
    BandwidthAdmissionControl: Optional[str]
    BandwidthCapacity: Optional[float]
    Burst: Optional[str]
    CallAdmissionControl: Optional[str]
    CallCapacity: Optional[float]
    Comment: Optional[str]
    Downlink: Optional[float]
    DownlinkSta: Optional[float]
    DscpWmmMapping: Optional[str]
    DynamicSortSubtable: Optional[str]
    Id: Optional[str]
    Name: Optional[str]
    Uplink: Optional[float]
    UplinkSta: Optional[float]
    Vdomparam: Optional[str]
    Wmm: Optional[str]
    WmmBeDscp: Optional[float]
    WmmBkDscp: Optional[float]
    WmmDscpMarking: Optional[str]
    WmmUapsd: Optional[str]
    WmmViDscp: Optional[float]
    WmmVoDscp: Optional[float]
    DscpWmmBe: Optional[Sequence["_DscpWmmBeDefinition"]]
    DscpWmmBk: Optional[Sequence["_DscpWmmBkDefinition"]]
    DscpWmmVi: Optional[Sequence["_DscpWmmViDefinition"]]
    DscpWmmVo: Optional[Sequence["_DscpWmmVoDefinition"]]

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
            BandwidthAdmissionControl=json_data.get("BandwidthAdmissionControl"),
            BandwidthCapacity=json_data.get("BandwidthCapacity"),
            Burst=json_data.get("Burst"),
            CallAdmissionControl=json_data.get("CallAdmissionControl"),
            CallCapacity=json_data.get("CallCapacity"),
            Comment=json_data.get("Comment"),
            Downlink=json_data.get("Downlink"),
            DownlinkSta=json_data.get("DownlinkSta"),
            DscpWmmMapping=json_data.get("DscpWmmMapping"),
            DynamicSortSubtable=json_data.get("DynamicSortSubtable"),
            Id=json_data.get("Id"),
            Name=json_data.get("Name"),
            Uplink=json_data.get("Uplink"),
            UplinkSta=json_data.get("UplinkSta"),
            Vdomparam=json_data.get("Vdomparam"),
            Wmm=json_data.get("Wmm"),
            WmmBeDscp=json_data.get("WmmBeDscp"),
            WmmBkDscp=json_data.get("WmmBkDscp"),
            WmmDscpMarking=json_data.get("WmmDscpMarking"),
            WmmUapsd=json_data.get("WmmUapsd"),
            WmmViDscp=json_data.get("WmmViDscp"),
            WmmVoDscp=json_data.get("WmmVoDscp"),
            DscpWmmBe=deserialize_list(json_data.get("DscpWmmBe"), DscpWmmBeDefinition),
            DscpWmmBk=deserialize_list(json_data.get("DscpWmmBk"), DscpWmmBkDefinition),
            DscpWmmVi=deserialize_list(json_data.get("DscpWmmVi"), DscpWmmViDefinition),
            DscpWmmVo=deserialize_list(json_data.get("DscpWmmVo"), DscpWmmVoDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class DscpWmmBeDefinition(BaseModel):
    Id: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_DscpWmmBeDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DscpWmmBeDefinition"]:
        if not json_data:
            return None
        return cls(
            Id=json_data.get("Id"),
        )


# work around possible type aliasing issues when variable has same name as a model
_DscpWmmBeDefinition = DscpWmmBeDefinition


@dataclass
class DscpWmmBkDefinition(BaseModel):
    Id: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_DscpWmmBkDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DscpWmmBkDefinition"]:
        if not json_data:
            return None
        return cls(
            Id=json_data.get("Id"),
        )


# work around possible type aliasing issues when variable has same name as a model
_DscpWmmBkDefinition = DscpWmmBkDefinition


@dataclass
class DscpWmmViDefinition(BaseModel):
    Id: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_DscpWmmViDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DscpWmmViDefinition"]:
        if not json_data:
            return None
        return cls(
            Id=json_data.get("Id"),
        )


# work around possible type aliasing issues when variable has same name as a model
_DscpWmmViDefinition = DscpWmmViDefinition


@dataclass
class DscpWmmVoDefinition(BaseModel):
    Id: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_DscpWmmVoDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DscpWmmVoDefinition"]:
        if not json_data:
            return None
        return cls(
            Id=json_data.get("Id"),
        )


# work around possible type aliasing issues when variable has same name as a model
_DscpWmmVoDefinition = DscpWmmVoDefinition


