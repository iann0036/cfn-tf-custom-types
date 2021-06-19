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
    EnableLogsSample: Optional[bool]
    EscalationMessage: Optional[str]
    EvaluationDelay: Optional[float]
    ForceDelete: Optional[bool]
    GroupbySimpleMonitor: Optional[bool]
    Id: Optional[str]
    IncludeTags: Optional[bool]
    Locked: Optional[bool]
    Message: Optional[str]
    Name: Optional[str]
    NewHostDelay: Optional[float]
    NoDataTimeframe: Optional[float]
    NotifyAudit: Optional[bool]
    NotifyNoData: Optional[bool]
    Priority: Optional[float]
    Query: Optional[str]
    RenotifyInterval: Optional[float]
    RequireFullWindow: Optional[bool]
    RestrictedRoles: Optional[Sequence[str]]
    Tags: Optional[Sequence[str]]
    TimeoutH: Optional[float]
    Type: Optional[str]
    Validate: Optional[bool]
    MonitorThresholdWindows: Optional[Sequence["_MonitorThresholdWindowsDefinition"]]
    MonitorThresholds: Optional[Sequence["_MonitorThresholdsDefinition"]]

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
            EnableLogsSample=json_data.get("EnableLogsSample"),
            EscalationMessage=json_data.get("EscalationMessage"),
            EvaluationDelay=json_data.get("EvaluationDelay"),
            ForceDelete=json_data.get("ForceDelete"),
            GroupbySimpleMonitor=json_data.get("GroupbySimpleMonitor"),
            Id=json_data.get("Id"),
            IncludeTags=json_data.get("IncludeTags"),
            Locked=json_data.get("Locked"),
            Message=json_data.get("Message"),
            Name=json_data.get("Name"),
            NewHostDelay=json_data.get("NewHostDelay"),
            NoDataTimeframe=json_data.get("NoDataTimeframe"),
            NotifyAudit=json_data.get("NotifyAudit"),
            NotifyNoData=json_data.get("NotifyNoData"),
            Priority=json_data.get("Priority"),
            Query=json_data.get("Query"),
            RenotifyInterval=json_data.get("RenotifyInterval"),
            RequireFullWindow=json_data.get("RequireFullWindow"),
            RestrictedRoles=json_data.get("RestrictedRoles"),
            Tags=json_data.get("Tags"),
            TimeoutH=json_data.get("TimeoutH"),
            Type=json_data.get("Type"),
            Validate=json_data.get("Validate"),
            MonitorThresholdWindows=deserialize_list(json_data.get("MonitorThresholdWindows"), MonitorThresholdWindowsDefinition),
            MonitorThresholds=deserialize_list(json_data.get("MonitorThresholds"), MonitorThresholdsDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class MonitorThresholdWindowsDefinition(BaseModel):
    RecoveryWindow: Optional[str]
    TriggerWindow: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_MonitorThresholdWindowsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_MonitorThresholdWindowsDefinition"]:
        if not json_data:
            return None
        return cls(
            RecoveryWindow=json_data.get("RecoveryWindow"),
            TriggerWindow=json_data.get("TriggerWindow"),
        )


# work around possible type aliasing issues when variable has same name as a model
_MonitorThresholdWindowsDefinition = MonitorThresholdWindowsDefinition


@dataclass
class MonitorThresholdsDefinition(BaseModel):
    Critical: Optional[str]
    CriticalRecovery: Optional[str]
    Ok: Optional[str]
    Unknown: Optional[str]
    Warning: Optional[str]
    WarningRecovery: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_MonitorThresholdsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_MonitorThresholdsDefinition"]:
        if not json_data:
            return None
        return cls(
            Critical=json_data.get("Critical"),
            CriticalRecovery=json_data.get("CriticalRecovery"),
            Ok=json_data.get("Ok"),
            Unknown=json_data.get("Unknown"),
            Warning=json_data.get("Warning"),
            WarningRecovery=json_data.get("WarningRecovery"),
        )


# work around possible type aliasing issues when variable has same name as a model
_MonitorThresholdsDefinition = MonitorThresholdsDefinition


