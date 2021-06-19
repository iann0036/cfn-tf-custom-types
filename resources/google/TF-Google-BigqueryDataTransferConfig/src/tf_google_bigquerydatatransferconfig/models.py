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
    DataRefreshWindowDays: Optional[float]
    DataSourceId: Optional[str]
    DestinationDatasetId: Optional[str]
    Disabled: Optional[bool]
    DisplayName: Optional[str]
    Id: Optional[str]
    Location: Optional[str]
    Name: Optional[str]
    NotificationPubsubTopic: Optional[str]
    Params: Optional[Sequence["_ParamsDefinition"]]
    Project: Optional[str]
    Schedule: Optional[str]
    ServiceAccountName: Optional[str]
    EmailPreferences: Optional[Sequence["_EmailPreferencesDefinition"]]
    ScheduleOptions: Optional[Sequence["_ScheduleOptionsDefinition"]]
    SensitiveParams: Optional[Sequence["_SensitiveParamsDefinition"]]
    Timeouts: Optional["_TimeoutsDefinition"]

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
            DataRefreshWindowDays=json_data.get("DataRefreshWindowDays"),
            DataSourceId=json_data.get("DataSourceId"),
            DestinationDatasetId=json_data.get("DestinationDatasetId"),
            Disabled=json_data.get("Disabled"),
            DisplayName=json_data.get("DisplayName"),
            Id=json_data.get("Id"),
            Location=json_data.get("Location"),
            Name=json_data.get("Name"),
            NotificationPubsubTopic=json_data.get("NotificationPubsubTopic"),
            Params=deserialize_list(json_data.get("Params"), ParamsDefinition),
            Project=json_data.get("Project"),
            Schedule=json_data.get("Schedule"),
            ServiceAccountName=json_data.get("ServiceAccountName"),
            EmailPreferences=deserialize_list(json_data.get("EmailPreferences"), EmailPreferencesDefinition),
            ScheduleOptions=deserialize_list(json_data.get("ScheduleOptions"), ScheduleOptionsDefinition),
            SensitiveParams=deserialize_list(json_data.get("SensitiveParams"), SensitiveParamsDefinition),
            Timeouts=TimeoutsDefinition._deserialize(json_data.get("Timeouts")),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class ParamsDefinition(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ParamsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ParamsDefinition"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ParamsDefinition = ParamsDefinition


@dataclass
class EmailPreferencesDefinition(BaseModel):
    EnableFailureEmail: Optional[bool]

    @classmethod
    def _deserialize(
        cls: Type["_EmailPreferencesDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_EmailPreferencesDefinition"]:
        if not json_data:
            return None
        return cls(
            EnableFailureEmail=json_data.get("EnableFailureEmail"),
        )


# work around possible type aliasing issues when variable has same name as a model
_EmailPreferencesDefinition = EmailPreferencesDefinition


@dataclass
class ScheduleOptionsDefinition(BaseModel):
    DisableAutoScheduling: Optional[bool]
    EndTime: Optional[str]
    StartTime: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ScheduleOptionsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ScheduleOptionsDefinition"]:
        if not json_data:
            return None
        return cls(
            DisableAutoScheduling=json_data.get("DisableAutoScheduling"),
            EndTime=json_data.get("EndTime"),
            StartTime=json_data.get("StartTime"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ScheduleOptionsDefinition = ScheduleOptionsDefinition


@dataclass
class SensitiveParamsDefinition(BaseModel):
    SecretAccessKey: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_SensitiveParamsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SensitiveParamsDefinition"]:
        if not json_data:
            return None
        return cls(
            SecretAccessKey=json_data.get("SecretAccessKey"),
        )


# work around possible type aliasing issues when variable has same name as a model
_SensitiveParamsDefinition = SensitiveParamsDefinition


@dataclass
class TimeoutsDefinition(BaseModel):
    Create: Optional[str]
    Delete: Optional[str]
    Update: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_TimeoutsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TimeoutsDefinition"]:
        if not json_data:
            return None
        return cls(
            Create=json_data.get("Create"),
            Delete=json_data.get("Delete"),
            Update=json_data.get("Update"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TimeoutsDefinition = TimeoutsDefinition


