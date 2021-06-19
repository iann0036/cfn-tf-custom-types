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
    BlockMaliciousUrl: Optional[str]
    Comment: Optional[str]
    DynamicSortSubtable: Optional[str]
    ExtendedLog: Optional[str]
    Id: Optional[str]
    Name: Optional[str]
    ReplacemsgGroup: Optional[str]
    ScanBotnetConnections: Optional[str]
    Vdomparam: Optional[str]
    Entries: Optional[Sequence["_EntriesDefinition"]]
    Filter: Optional[Sequence["_FilterDefinition"]]
    Override: Optional[Sequence["_OverrideDefinition"]]

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
            BlockMaliciousUrl=json_data.get("BlockMaliciousUrl"),
            Comment=json_data.get("Comment"),
            DynamicSortSubtable=json_data.get("DynamicSortSubtable"),
            ExtendedLog=json_data.get("ExtendedLog"),
            Id=json_data.get("Id"),
            Name=json_data.get("Name"),
            ReplacemsgGroup=json_data.get("ReplacemsgGroup"),
            ScanBotnetConnections=json_data.get("ScanBotnetConnections"),
            Vdomparam=json_data.get("Vdomparam"),
            Entries=deserialize_list(json_data.get("Entries"), EntriesDefinition),
            Filter=deserialize_list(json_data.get("Filter"), FilterDefinition),
            Override=deserialize_list(json_data.get("Override"), OverrideDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class EntriesDefinition(BaseModel):
    Action: Optional[str]
    Application: Optional[str]
    Id: Optional[float]
    Location: Optional[str]
    Log: Optional[str]
    LogAttackContext: Optional[str]
    LogPacket: Optional[str]
    Os: Optional[str]
    Protocol: Optional[str]
    Quarantine: Optional[str]
    QuarantineExpiry: Optional[str]
    QuarantineLog: Optional[str]
    RateCount: Optional[float]
    RateDuration: Optional[float]
    RateMode: Optional[str]
    RateTrack: Optional[str]
    Severity: Optional[str]
    Status: Optional[str]
    Cve: Optional[Sequence["_CveDefinition"]]
    ExemptIp: Optional[Sequence["_ExemptIpDefinition"]]
    Rule: Optional[Sequence["_RuleDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_EntriesDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_EntriesDefinition"]:
        if not json_data:
            return None
        return cls(
            Action=json_data.get("Action"),
            Application=json_data.get("Application"),
            Id=json_data.get("Id"),
            Location=json_data.get("Location"),
            Log=json_data.get("Log"),
            LogAttackContext=json_data.get("LogAttackContext"),
            LogPacket=json_data.get("LogPacket"),
            Os=json_data.get("Os"),
            Protocol=json_data.get("Protocol"),
            Quarantine=json_data.get("Quarantine"),
            QuarantineExpiry=json_data.get("QuarantineExpiry"),
            QuarantineLog=json_data.get("QuarantineLog"),
            RateCount=json_data.get("RateCount"),
            RateDuration=json_data.get("RateDuration"),
            RateMode=json_data.get("RateMode"),
            RateTrack=json_data.get("RateTrack"),
            Severity=json_data.get("Severity"),
            Status=json_data.get("Status"),
            Cve=deserialize_list(json_data.get("Cve"), CveDefinition),
            ExemptIp=deserialize_list(json_data.get("ExemptIp"), ExemptIpDefinition),
            Rule=deserialize_list(json_data.get("Rule"), RuleDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_EntriesDefinition = EntriesDefinition


@dataclass
class CveDefinition(BaseModel):
    CveEntry: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_CveDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_CveDefinition"]:
        if not json_data:
            return None
        return cls(
            CveEntry=json_data.get("CveEntry"),
        )


# work around possible type aliasing issues when variable has same name as a model
_CveDefinition = CveDefinition


@dataclass
class ExemptIpDefinition(BaseModel):
    DstIp: Optional[str]
    Id: Optional[float]
    SrcIp: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ExemptIpDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ExemptIpDefinition"]:
        if not json_data:
            return None
        return cls(
            DstIp=json_data.get("DstIp"),
            Id=json_data.get("Id"),
            SrcIp=json_data.get("SrcIp"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ExemptIpDefinition = ExemptIpDefinition


@dataclass
class RuleDefinition(BaseModel):
    Id: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_RuleDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_RuleDefinition"]:
        if not json_data:
            return None
        return cls(
            Id=json_data.get("Id"),
        )


# work around possible type aliasing issues when variable has same name as a model
_RuleDefinition = RuleDefinition


@dataclass
class FilterDefinition(BaseModel):
    Action: Optional[str]
    Application: Optional[str]
    Location: Optional[str]
    Log: Optional[str]
    LogPacket: Optional[str]
    Name: Optional[str]
    Os: Optional[str]
    Protocol: Optional[str]
    Quarantine: Optional[str]
    QuarantineExpiry: Optional[float]
    QuarantineLog: Optional[str]
    Severity: Optional[str]
    Status: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_FilterDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_FilterDefinition"]:
        if not json_data:
            return None
        return cls(
            Action=json_data.get("Action"),
            Application=json_data.get("Application"),
            Location=json_data.get("Location"),
            Log=json_data.get("Log"),
            LogPacket=json_data.get("LogPacket"),
            Name=json_data.get("Name"),
            Os=json_data.get("Os"),
            Protocol=json_data.get("Protocol"),
            Quarantine=json_data.get("Quarantine"),
            QuarantineExpiry=json_data.get("QuarantineExpiry"),
            QuarantineLog=json_data.get("QuarantineLog"),
            Severity=json_data.get("Severity"),
            Status=json_data.get("Status"),
        )


# work around possible type aliasing issues when variable has same name as a model
_FilterDefinition = FilterDefinition


@dataclass
class OverrideDefinition(BaseModel):
    Action: Optional[str]
    Log: Optional[str]
    LogPacket: Optional[str]
    Quarantine: Optional[str]
    QuarantineExpiry: Optional[float]
    QuarantineLog: Optional[str]
    RuleId: Optional[float]
    Status: Optional[str]
    ExemptIp: Optional[Sequence["_ExemptIpDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_OverrideDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_OverrideDefinition"]:
        if not json_data:
            return None
        return cls(
            Action=json_data.get("Action"),
            Log=json_data.get("Log"),
            LogPacket=json_data.get("LogPacket"),
            Quarantine=json_data.get("Quarantine"),
            QuarantineExpiry=json_data.get("QuarantineExpiry"),
            QuarantineLog=json_data.get("QuarantineLog"),
            RuleId=json_data.get("RuleId"),
            Status=json_data.get("Status"),
            ExemptIp=deserialize_list(json_data.get("ExemptIp"), ExemptIpDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_OverrideDefinition = OverrideDefinition


