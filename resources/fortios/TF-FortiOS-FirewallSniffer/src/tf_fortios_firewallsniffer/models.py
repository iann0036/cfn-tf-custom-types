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
    ApplicationList: Optional[str]
    ApplicationListStatus: Optional[str]
    AvProfile: Optional[str]
    AvProfileStatus: Optional[str]
    DlpSensor: Optional[str]
    DlpSensorStatus: Optional[str]
    Dsri: Optional[str]
    DynamicSortSubtable: Optional[str]
    EmailfilterProfile: Optional[str]
    EmailfilterProfileStatus: Optional[str]
    Fosid: Optional[float]
    Host: Optional[str]
    Id: Optional[str]
    Interface: Optional[str]
    IpThreatfeedStatus: Optional[str]
    IpsDosStatus: Optional[str]
    IpsSensor: Optional[str]
    IpsSensorStatus: Optional[str]
    Ipv6: Optional[str]
    Logtraffic: Optional[str]
    MaxPacketCount: Optional[float]
    NonIp: Optional[str]
    Port: Optional[str]
    Protocol: Optional[str]
    ScanBotnetConnections: Optional[str]
    SpamfilterProfile: Optional[str]
    SpamfilterProfileStatus: Optional[str]
    Status: Optional[str]
    Vdomparam: Optional[str]
    Vlan: Optional[str]
    WebfilterProfile: Optional[str]
    WebfilterProfileStatus: Optional[str]
    Anomaly: Optional[Sequence["_AnomalyDefinition"]]
    IpThreatfeed: Optional[Sequence["_IpThreatfeedDefinition"]]

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
            ApplicationList=json_data.get("ApplicationList"),
            ApplicationListStatus=json_data.get("ApplicationListStatus"),
            AvProfile=json_data.get("AvProfile"),
            AvProfileStatus=json_data.get("AvProfileStatus"),
            DlpSensor=json_data.get("DlpSensor"),
            DlpSensorStatus=json_data.get("DlpSensorStatus"),
            Dsri=json_data.get("Dsri"),
            DynamicSortSubtable=json_data.get("DynamicSortSubtable"),
            EmailfilterProfile=json_data.get("EmailfilterProfile"),
            EmailfilterProfileStatus=json_data.get("EmailfilterProfileStatus"),
            Fosid=json_data.get("Fosid"),
            Host=json_data.get("Host"),
            Id=json_data.get("Id"),
            Interface=json_data.get("Interface"),
            IpThreatfeedStatus=json_data.get("IpThreatfeedStatus"),
            IpsDosStatus=json_data.get("IpsDosStatus"),
            IpsSensor=json_data.get("IpsSensor"),
            IpsSensorStatus=json_data.get("IpsSensorStatus"),
            Ipv6=json_data.get("Ipv6"),
            Logtraffic=json_data.get("Logtraffic"),
            MaxPacketCount=json_data.get("MaxPacketCount"),
            NonIp=json_data.get("NonIp"),
            Port=json_data.get("Port"),
            Protocol=json_data.get("Protocol"),
            ScanBotnetConnections=json_data.get("ScanBotnetConnections"),
            SpamfilterProfile=json_data.get("SpamfilterProfile"),
            SpamfilterProfileStatus=json_data.get("SpamfilterProfileStatus"),
            Status=json_data.get("Status"),
            Vdomparam=json_data.get("Vdomparam"),
            Vlan=json_data.get("Vlan"),
            WebfilterProfile=json_data.get("WebfilterProfile"),
            WebfilterProfileStatus=json_data.get("WebfilterProfileStatus"),
            Anomaly=deserialize_list(json_data.get("Anomaly"), AnomalyDefinition),
            IpThreatfeed=deserialize_list(json_data.get("IpThreatfeed"), IpThreatfeedDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class AnomalyDefinition(BaseModel):
    Action: Optional[str]
    Log: Optional[str]
    Name: Optional[str]
    Quarantine: Optional[str]
    QuarantineExpiry: Optional[str]
    QuarantineLog: Optional[str]
    Status: Optional[str]
    Threshold: Optional[float]
    Thresholddefault: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_AnomalyDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AnomalyDefinition"]:
        if not json_data:
            return None
        return cls(
            Action=json_data.get("Action"),
            Log=json_data.get("Log"),
            Name=json_data.get("Name"),
            Quarantine=json_data.get("Quarantine"),
            QuarantineExpiry=json_data.get("QuarantineExpiry"),
            QuarantineLog=json_data.get("QuarantineLog"),
            Status=json_data.get("Status"),
            Threshold=json_data.get("Threshold"),
            Thresholddefault=json_data.get("Thresholddefault"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AnomalyDefinition = AnomalyDefinition


@dataclass
class IpThreatfeedDefinition(BaseModel):
    Name: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_IpThreatfeedDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_IpThreatfeedDefinition"]:
        if not json_data:
            return None
        return cls(
            Name=json_data.get("Name"),
        )


# work around possible type aliasing issues when variable has same name as a model
_IpThreatfeedDefinition = IpThreatfeedDefinition


