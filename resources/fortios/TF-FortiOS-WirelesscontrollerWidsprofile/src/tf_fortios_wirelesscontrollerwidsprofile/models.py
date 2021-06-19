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
    ApAutoSuppress: Optional[str]
    ApBgscanDisableDay: Optional[str]
    ApBgscanDisableEnd: Optional[str]
    ApBgscanDisableStart: Optional[str]
    ApBgscanDuration: Optional[float]
    ApBgscanIdle: Optional[float]
    ApBgscanIntv: Optional[float]
    ApBgscanPeriod: Optional[float]
    ApBgscanReportIntv: Optional[float]
    ApFgscanReportIntv: Optional[float]
    ApScan: Optional[str]
    ApScanPassive: Optional[str]
    ApScanThreshold: Optional[str]
    AsleapAttack: Optional[str]
    AssocFloodThresh: Optional[float]
    AssocFloodTime: Optional[float]
    AssocFrameFlood: Optional[str]
    AuthFloodThresh: Optional[float]
    AuthFloodTime: Optional[float]
    AuthFrameFlood: Optional[str]
    Comment: Optional[str]
    DeauthBroadcast: Optional[str]
    DeauthUnknownSrcThresh: Optional[float]
    DynamicSortSubtable: Optional[str]
    EapolFailFlood: Optional[str]
    EapolFailIntv: Optional[float]
    EapolFailThresh: Optional[float]
    EapolLogoffFlood: Optional[str]
    EapolLogoffIntv: Optional[float]
    EapolLogoffThresh: Optional[float]
    EapolPreFailFlood: Optional[str]
    EapolPreFailIntv: Optional[float]
    EapolPreFailThresh: Optional[float]
    EapolPreSuccFlood: Optional[str]
    EapolPreSuccIntv: Optional[float]
    EapolPreSuccThresh: Optional[float]
    EapolStartFlood: Optional[str]
    EapolStartIntv: Optional[float]
    EapolStartThresh: Optional[float]
    EapolSuccFlood: Optional[str]
    EapolSuccIntv: Optional[float]
    EapolSuccThresh: Optional[float]
    Id: Optional[str]
    InvalidMacOui: Optional[str]
    LongDurationAttack: Optional[str]
    LongDurationThresh: Optional[float]
    Name: Optional[str]
    NullSsidProbeResp: Optional[str]
    SensorMode: Optional[str]
    SpoofedDeauth: Optional[str]
    Vdomparam: Optional[str]
    WeakWepIv: Optional[str]
    WirelessBridge: Optional[str]
    ApBgscanDisableSchedules: Optional[Sequence["_ApBgscanDisableSchedulesDefinition"]]

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
            ApAutoSuppress=json_data.get("ApAutoSuppress"),
            ApBgscanDisableDay=json_data.get("ApBgscanDisableDay"),
            ApBgscanDisableEnd=json_data.get("ApBgscanDisableEnd"),
            ApBgscanDisableStart=json_data.get("ApBgscanDisableStart"),
            ApBgscanDuration=json_data.get("ApBgscanDuration"),
            ApBgscanIdle=json_data.get("ApBgscanIdle"),
            ApBgscanIntv=json_data.get("ApBgscanIntv"),
            ApBgscanPeriod=json_data.get("ApBgscanPeriod"),
            ApBgscanReportIntv=json_data.get("ApBgscanReportIntv"),
            ApFgscanReportIntv=json_data.get("ApFgscanReportIntv"),
            ApScan=json_data.get("ApScan"),
            ApScanPassive=json_data.get("ApScanPassive"),
            ApScanThreshold=json_data.get("ApScanThreshold"),
            AsleapAttack=json_data.get("AsleapAttack"),
            AssocFloodThresh=json_data.get("AssocFloodThresh"),
            AssocFloodTime=json_data.get("AssocFloodTime"),
            AssocFrameFlood=json_data.get("AssocFrameFlood"),
            AuthFloodThresh=json_data.get("AuthFloodThresh"),
            AuthFloodTime=json_data.get("AuthFloodTime"),
            AuthFrameFlood=json_data.get("AuthFrameFlood"),
            Comment=json_data.get("Comment"),
            DeauthBroadcast=json_data.get("DeauthBroadcast"),
            DeauthUnknownSrcThresh=json_data.get("DeauthUnknownSrcThresh"),
            DynamicSortSubtable=json_data.get("DynamicSortSubtable"),
            EapolFailFlood=json_data.get("EapolFailFlood"),
            EapolFailIntv=json_data.get("EapolFailIntv"),
            EapolFailThresh=json_data.get("EapolFailThresh"),
            EapolLogoffFlood=json_data.get("EapolLogoffFlood"),
            EapolLogoffIntv=json_data.get("EapolLogoffIntv"),
            EapolLogoffThresh=json_data.get("EapolLogoffThresh"),
            EapolPreFailFlood=json_data.get("EapolPreFailFlood"),
            EapolPreFailIntv=json_data.get("EapolPreFailIntv"),
            EapolPreFailThresh=json_data.get("EapolPreFailThresh"),
            EapolPreSuccFlood=json_data.get("EapolPreSuccFlood"),
            EapolPreSuccIntv=json_data.get("EapolPreSuccIntv"),
            EapolPreSuccThresh=json_data.get("EapolPreSuccThresh"),
            EapolStartFlood=json_data.get("EapolStartFlood"),
            EapolStartIntv=json_data.get("EapolStartIntv"),
            EapolStartThresh=json_data.get("EapolStartThresh"),
            EapolSuccFlood=json_data.get("EapolSuccFlood"),
            EapolSuccIntv=json_data.get("EapolSuccIntv"),
            EapolSuccThresh=json_data.get("EapolSuccThresh"),
            Id=json_data.get("Id"),
            InvalidMacOui=json_data.get("InvalidMacOui"),
            LongDurationAttack=json_data.get("LongDurationAttack"),
            LongDurationThresh=json_data.get("LongDurationThresh"),
            Name=json_data.get("Name"),
            NullSsidProbeResp=json_data.get("NullSsidProbeResp"),
            SensorMode=json_data.get("SensorMode"),
            SpoofedDeauth=json_data.get("SpoofedDeauth"),
            Vdomparam=json_data.get("Vdomparam"),
            WeakWepIv=json_data.get("WeakWepIv"),
            WirelessBridge=json_data.get("WirelessBridge"),
            ApBgscanDisableSchedules=deserialize_list(json_data.get("ApBgscanDisableSchedules"), ApBgscanDisableSchedulesDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class ApBgscanDisableSchedulesDefinition(BaseModel):
    Name: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ApBgscanDisableSchedulesDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ApBgscanDisableSchedulesDefinition"]:
        if not json_data:
            return None
        return cls(
            Name=json_data.get("Name"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ApBgscanDisableSchedulesDefinition = ApBgscanDisableSchedulesDefinition


