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
    Department: Optional[str]
    Email: Optional[str]
    FirstName: Optional[str]
    Id: Optional[str]
    Language: Optional[str]
    LastName: Optional[str]
    Position: Optional[str]
    Role: Optional[str]
    SubscribedIncidentUpdateNotificationTypes: Optional[Sequence[str]]
    SubscribedIncidentUpdateStates: Optional[Sequence[str]]
    Timezone: Optional[str]
    Username: Optional[str]
    HighPriorityNotificationPreference: Optional[Sequence["_HighPriorityNotificationPreferenceDefinition"]]
    Landline: Optional[Sequence["_LandlineDefinition"]]
    LowPriorityNotificationPreference: Optional[Sequence["_LowPriorityNotificationPreferenceDefinition"]]
    Mobile: Optional[Sequence["_MobileDefinition"]]
    OnCallNotificationPreference: Optional[Sequence["_OnCallNotificationPreferenceDefinition"]]

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
            Department=json_data.get("Department"),
            Email=json_data.get("Email"),
            FirstName=json_data.get("FirstName"),
            Id=json_data.get("Id"),
            Language=json_data.get("Language"),
            LastName=json_data.get("LastName"),
            Position=json_data.get("Position"),
            Role=json_data.get("Role"),
            SubscribedIncidentUpdateNotificationTypes=json_data.get("SubscribedIncidentUpdateNotificationTypes"),
            SubscribedIncidentUpdateStates=json_data.get("SubscribedIncidentUpdateStates"),
            Timezone=json_data.get("Timezone"),
            Username=json_data.get("Username"),
            HighPriorityNotificationPreference=deserialize_list(json_data.get("HighPriorityNotificationPreference"), HighPriorityNotificationPreferenceDefinition),
            Landline=deserialize_list(json_data.get("Landline"), LandlineDefinition),
            LowPriorityNotificationPreference=deserialize_list(json_data.get("LowPriorityNotificationPreference"), LowPriorityNotificationPreferenceDefinition),
            Mobile=deserialize_list(json_data.get("Mobile"), MobileDefinition),
            OnCallNotificationPreference=deserialize_list(json_data.get("OnCallNotificationPreference"), OnCallNotificationPreferenceDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class HighPriorityNotificationPreferenceDefinition(BaseModel):
    Delay: Optional[float]
    Method: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_HighPriorityNotificationPreferenceDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_HighPriorityNotificationPreferenceDefinition"]:
        if not json_data:
            return None
        return cls(
            Delay=json_data.get("Delay"),
            Method=json_data.get("Method"),
        )


# work around possible type aliasing issues when variable has same name as a model
_HighPriorityNotificationPreferenceDefinition = HighPriorityNotificationPreferenceDefinition


@dataclass
class LandlineDefinition(BaseModel):
    Number: Optional[str]
    RegionCode: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_LandlineDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_LandlineDefinition"]:
        if not json_data:
            return None
        return cls(
            Number=json_data.get("Number"),
            RegionCode=json_data.get("RegionCode"),
        )


# work around possible type aliasing issues when variable has same name as a model
_LandlineDefinition = LandlineDefinition


@dataclass
class LowPriorityNotificationPreferenceDefinition(BaseModel):
    Delay: Optional[float]
    Method: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_LowPriorityNotificationPreferenceDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_LowPriorityNotificationPreferenceDefinition"]:
        if not json_data:
            return None
        return cls(
            Delay=json_data.get("Delay"),
            Method=json_data.get("Method"),
        )


# work around possible type aliasing issues when variable has same name as a model
_LowPriorityNotificationPreferenceDefinition = LowPriorityNotificationPreferenceDefinition


@dataclass
class MobileDefinition(BaseModel):
    Number: Optional[str]
    RegionCode: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_MobileDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_MobileDefinition"]:
        if not json_data:
            return None
        return cls(
            Number=json_data.get("Number"),
            RegionCode=json_data.get("RegionCode"),
        )


# work around possible type aliasing issues when variable has same name as a model
_MobileDefinition = MobileDefinition


@dataclass
class OnCallNotificationPreferenceDefinition(BaseModel):
    BeforeMin: Optional[float]
    Method: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_OnCallNotificationPreferenceDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_OnCallNotificationPreferenceDefinition"]:
        if not json_data:
            return None
        return cls(
            BeforeMin=json_data.get("BeforeMin"),
            Method=json_data.get("Method"),
        )


# work around possible type aliasing issues when variable has same name as a model
_OnCallNotificationPreferenceDefinition = OnCallNotificationPreferenceDefinition


