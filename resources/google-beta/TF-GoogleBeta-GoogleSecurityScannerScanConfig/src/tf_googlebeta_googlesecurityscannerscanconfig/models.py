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
    BlacklistPatterns: Optional[Sequence[str]]
    DisplayName: Optional[str]
    ExportToSecurityCommandCenter: Optional[str]
    Id: Optional[str]
    MaxQps: Optional[float]
    Name: Optional[str]
    Project: Optional[str]
    StartingUrls: Optional[Sequence[str]]
    TargetPlatforms: Optional[Sequence[str]]
    UserAgent: Optional[str]
    Authentication: Optional[Sequence["_AuthenticationDefinition"]]
    Schedule: Optional[Sequence["_ScheduleDefinition"]]
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
            BlacklistPatterns=json_data.get("BlacklistPatterns"),
            DisplayName=json_data.get("DisplayName"),
            ExportToSecurityCommandCenter=json_data.get("ExportToSecurityCommandCenter"),
            Id=json_data.get("Id"),
            MaxQps=json_data.get("MaxQps"),
            Name=json_data.get("Name"),
            Project=json_data.get("Project"),
            StartingUrls=json_data.get("StartingUrls"),
            TargetPlatforms=json_data.get("TargetPlatforms"),
            UserAgent=json_data.get("UserAgent"),
            Authentication=deserialize_list(json_data.get("Authentication"), AuthenticationDefinition),
            Schedule=deserialize_list(json_data.get("Schedule"), ScheduleDefinition),
            Timeouts=TimeoutsDefinition._deserialize(json_data.get("Timeouts")),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class AuthenticationDefinition(BaseModel):
    CustomAccount: Optional[Sequence["_CustomAccountDefinition"]]
    GoogleAccount: Optional[Sequence["_GoogleAccountDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_AuthenticationDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AuthenticationDefinition"]:
        if not json_data:
            return None
        return cls(
            CustomAccount=deserialize_list(json_data.get("CustomAccount"), CustomAccountDefinition),
            GoogleAccount=deserialize_list(json_data.get("GoogleAccount"), GoogleAccountDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_AuthenticationDefinition = AuthenticationDefinition


@dataclass
class CustomAccountDefinition(BaseModel):
    LoginUrl: Optional[str]
    Password: Optional[str]
    Username: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_CustomAccountDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_CustomAccountDefinition"]:
        if not json_data:
            return None
        return cls(
            LoginUrl=json_data.get("LoginUrl"),
            Password=json_data.get("Password"),
            Username=json_data.get("Username"),
        )


# work around possible type aliasing issues when variable has same name as a model
_CustomAccountDefinition = CustomAccountDefinition


@dataclass
class GoogleAccountDefinition(BaseModel):
    Password: Optional[str]
    Username: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_GoogleAccountDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_GoogleAccountDefinition"]:
        if not json_data:
            return None
        return cls(
            Password=json_data.get("Password"),
            Username=json_data.get("Username"),
        )


# work around possible type aliasing issues when variable has same name as a model
_GoogleAccountDefinition = GoogleAccountDefinition


@dataclass
class ScheduleDefinition(BaseModel):
    IntervalDurationDays: Optional[float]
    ScheduleTime: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ScheduleDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ScheduleDefinition"]:
        if not json_data:
            return None
        return cls(
            IntervalDurationDays=json_data.get("IntervalDurationDays"),
            ScheduleTime=json_data.get("ScheduleTime"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ScheduleDefinition = ScheduleDefinition


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


