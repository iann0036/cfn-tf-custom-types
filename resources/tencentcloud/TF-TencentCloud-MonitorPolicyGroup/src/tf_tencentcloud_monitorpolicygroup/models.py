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
    BindingObjects: Optional[Sequence["_BindingObjectsDefinition"]]
    DimensionGroup: Optional[Sequence[str]]
    GroupName: Optional[str]
    Id: Optional[str]
    IsUnionRule: Optional[float]
    LastEditUin: Optional[str]
    PolicyViewName: Optional[str]
    ProjectId: Optional[float]
    Receivers: Optional[Sequence["_ReceiversDefinition"]]
    Remark: Optional[str]
    SupportRegions: Optional[Sequence[str]]
    UpdateTime: Optional[str]
    Conditions: Optional[Sequence["_ConditionsDefinition"]]
    EventConditions: Optional[Sequence["_EventConditionsDefinition"]]

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
            BindingObjects=deserialize_list(json_data.get("BindingObjects"), BindingObjectsDefinition),
            DimensionGroup=json_data.get("DimensionGroup"),
            GroupName=json_data.get("GroupName"),
            Id=json_data.get("Id"),
            IsUnionRule=json_data.get("IsUnionRule"),
            LastEditUin=json_data.get("LastEditUin"),
            PolicyViewName=json_data.get("PolicyViewName"),
            ProjectId=json_data.get("ProjectId"),
            Receivers=deserialize_list(json_data.get("Receivers"), ReceiversDefinition),
            Remark=json_data.get("Remark"),
            SupportRegions=json_data.get("SupportRegions"),
            UpdateTime=json_data.get("UpdateTime"),
            Conditions=deserialize_list(json_data.get("Conditions"), ConditionsDefinition),
            EventConditions=deserialize_list(json_data.get("EventConditions"), EventConditionsDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class BindingObjectsDefinition(BaseModel):
    DimensionsJson: Optional[str]
    IsShielded: Optional[float]
    Region: Optional[str]
    UniqueId: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_BindingObjectsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_BindingObjectsDefinition"]:
        if not json_data:
            return None
        return cls(
            DimensionsJson=json_data.get("DimensionsJson"),
            IsShielded=json_data.get("IsShielded"),
            Region=json_data.get("Region"),
            UniqueId=json_data.get("UniqueId"),
        )


# work around possible type aliasing issues when variable has same name as a model
_BindingObjectsDefinition = BindingObjectsDefinition


@dataclass
class ReceiversDefinition(BaseModel):
    EndTime: Optional[float]
    NeedSendNotice: Optional[float]
    NotifyWay: Optional[Sequence[str]]
    PersonInterval: Optional[float]
    ReceiveLanguage: Optional[str]
    ReceiverGroupList: Optional[Sequence[float]]
    ReceiverType: Optional[str]
    ReceiverUserList: Optional[Sequence[float]]
    RecoverNotify: Optional[Sequence[str]]
    RoundInterval: Optional[float]
    RoundNumber: Optional[float]
    SendFor: Optional[Sequence[str]]
    StartTime: Optional[float]
    UidList: Optional[Sequence[float]]

    @classmethod
    def _deserialize(
        cls: Type["_ReceiversDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ReceiversDefinition"]:
        if not json_data:
            return None
        return cls(
            EndTime=json_data.get("EndTime"),
            NeedSendNotice=json_data.get("NeedSendNotice"),
            NotifyWay=json_data.get("NotifyWay"),
            PersonInterval=json_data.get("PersonInterval"),
            ReceiveLanguage=json_data.get("ReceiveLanguage"),
            ReceiverGroupList=json_data.get("ReceiverGroupList"),
            ReceiverType=json_data.get("ReceiverType"),
            ReceiverUserList=json_data.get("ReceiverUserList"),
            RecoverNotify=json_data.get("RecoverNotify"),
            RoundInterval=json_data.get("RoundInterval"),
            RoundNumber=json_data.get("RoundNumber"),
            SendFor=json_data.get("SendFor"),
            StartTime=json_data.get("StartTime"),
            UidList=json_data.get("UidList"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ReceiversDefinition = ReceiversDefinition


@dataclass
class ConditionsDefinition(BaseModel):
    AlarmNotifyPeriod: Optional[float]
    AlarmNotifyType: Optional[float]
    CalcPeriod: Optional[float]
    CalcType: Optional[float]
    CalcValue: Optional[float]
    ContinuePeriod: Optional[float]
    MetricId: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_ConditionsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ConditionsDefinition"]:
        if not json_data:
            return None
        return cls(
            AlarmNotifyPeriod=json_data.get("AlarmNotifyPeriod"),
            AlarmNotifyType=json_data.get("AlarmNotifyType"),
            CalcPeriod=json_data.get("CalcPeriod"),
            CalcType=json_data.get("CalcType"),
            CalcValue=json_data.get("CalcValue"),
            ContinuePeriod=json_data.get("ContinuePeriod"),
            MetricId=json_data.get("MetricId"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ConditionsDefinition = ConditionsDefinition


@dataclass
class EventConditionsDefinition(BaseModel):
    AlarmNotifyPeriod: Optional[float]
    AlarmNotifyType: Optional[float]
    EventId: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_EventConditionsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_EventConditionsDefinition"]:
        if not json_data:
            return None
        return cls(
            AlarmNotifyPeriod=json_data.get("AlarmNotifyPeriod"),
            AlarmNotifyType=json_data.get("AlarmNotifyType"),
            EventId=json_data.get("EventId"),
        )


# work around possible type aliasing issues when variable has same name as a model
_EventConditionsDefinition = EventConditionsDefinition


