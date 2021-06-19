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
    AllowAutoRemediate: Optional[bool]
    DelayNotificationMs: Optional[float]
    Description: Optional[str]
    Enabled: Optional[bool]
    ExcludedPolicies: Optional[Sequence[str]]
    Id: Optional[str]
    LastModifiedBy: Optional[str]
    LastModifiedOn: Optional[float]
    Name: Optional[str]
    NotificationChannels: Optional[Sequence[str]]
    NotifyOnDismissed: Optional[bool]
    NotifyOnOpen: Optional[bool]
    NotifyOnResolved: Optional[bool]
    NotifyOnSnoozed: Optional[bool]
    OpenAlertsCount: Optional[float]
    Owner: Optional[str]
    Policies: Optional[Sequence[str]]
    PolicyLabels: Optional[Sequence[str]]
    PolicyScanConfigId: Optional[str]
    ReadOnly: Optional[bool]
    ScanAll: Optional[bool]
    NotificationConfig: Optional[Sequence["_NotificationConfigDefinition"]]
    Target: Optional[Sequence["_TargetDefinition"]]

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
            AllowAutoRemediate=json_data.get("AllowAutoRemediate"),
            DelayNotificationMs=json_data.get("DelayNotificationMs"),
            Description=json_data.get("Description"),
            Enabled=json_data.get("Enabled"),
            ExcludedPolicies=json_data.get("ExcludedPolicies"),
            Id=json_data.get("Id"),
            LastModifiedBy=json_data.get("LastModifiedBy"),
            LastModifiedOn=json_data.get("LastModifiedOn"),
            Name=json_data.get("Name"),
            NotificationChannels=json_data.get("NotificationChannels"),
            NotifyOnDismissed=json_data.get("NotifyOnDismissed"),
            NotifyOnOpen=json_data.get("NotifyOnOpen"),
            NotifyOnResolved=json_data.get("NotifyOnResolved"),
            NotifyOnSnoozed=json_data.get("NotifyOnSnoozed"),
            OpenAlertsCount=json_data.get("OpenAlertsCount"),
            Owner=json_data.get("Owner"),
            Policies=json_data.get("Policies"),
            PolicyLabels=json_data.get("PolicyLabels"),
            PolicyScanConfigId=json_data.get("PolicyScanConfigId"),
            ReadOnly=json_data.get("ReadOnly"),
            ScanAll=json_data.get("ScanAll"),
            NotificationConfig=deserialize_list(json_data.get("NotificationConfig"), NotificationConfigDefinition),
            Target=deserialize_list(json_data.get("Target"), TargetDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class NotificationConfigDefinition(BaseModel):
    ConfigId: Optional[str]
    ConfigType: Optional[str]
    DayOfMonth: Optional[float]
    DetailedReport: Optional[bool]
    Enabled: Optional[bool]
    Frequency: Optional[str]
    FrequencyFromRRule: Optional[str]
    HourOfDay: Optional[float]
    IncludeRemediation: Optional[bool]
    RRuleSchedule: Optional[str]
    Recipients: Optional[Sequence[str]]
    TemplateId: Optional[str]
    TimezoneId: Optional[str]
    WithCompression: Optional[bool]
    DaysOfWeek: Optional[Sequence["_DaysOfWeekDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_NotificationConfigDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_NotificationConfigDefinition"]:
        if not json_data:
            return None
        return cls(
            ConfigId=json_data.get("ConfigId"),
            ConfigType=json_data.get("ConfigType"),
            DayOfMonth=json_data.get("DayOfMonth"),
            DetailedReport=json_data.get("DetailedReport"),
            Enabled=json_data.get("Enabled"),
            Frequency=json_data.get("Frequency"),
            FrequencyFromRRule=json_data.get("FrequencyFromRRule"),
            HourOfDay=json_data.get("HourOfDay"),
            IncludeRemediation=json_data.get("IncludeRemediation"),
            RRuleSchedule=json_data.get("RRuleSchedule"),
            Recipients=json_data.get("Recipients"),
            TemplateId=json_data.get("TemplateId"),
            TimezoneId=json_data.get("TimezoneId"),
            WithCompression=json_data.get("WithCompression"),
            DaysOfWeek=deserialize_list(json_data.get("DaysOfWeek"), DaysOfWeekDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_NotificationConfigDefinition = NotificationConfigDefinition


@dataclass
class DaysOfWeekDefinition(BaseModel):
    Day: Optional[str]
    Offset: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_DaysOfWeekDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DaysOfWeekDefinition"]:
        if not json_data:
            return None
        return cls(
            Day=json_data.get("Day"),
            Offset=json_data.get("Offset"),
        )


# work around possible type aliasing issues when variable has same name as a model
_DaysOfWeekDefinition = DaysOfWeekDefinition


@dataclass
class TargetDefinition(BaseModel):
    AccountGroups: Optional[Sequence[str]]
    ExcludedAccounts: Optional[Sequence[str]]
    Regions: Optional[Sequence[str]]
    Tags: Optional[Sequence["_TagsDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_TargetDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TargetDefinition"]:
        if not json_data:
            return None
        return cls(
            AccountGroups=json_data.get("AccountGroups"),
            ExcludedAccounts=json_data.get("ExcludedAccounts"),
            Regions=json_data.get("Regions"),
            Tags=deserialize_list(json_data.get("Tags"), TagsDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_TargetDefinition = TargetDefinition


@dataclass
class TagsDefinition(BaseModel):
    Key: Optional[str]
    Values: Optional[Sequence[str]]

    @classmethod
    def _deserialize(
        cls: Type["_TagsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TagsDefinition"]:
        if not json_data:
            return None
        return cls(
            Key=json_data.get("Key"),
            Values=json_data.get("Values"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TagsDefinition = TagsDefinition


