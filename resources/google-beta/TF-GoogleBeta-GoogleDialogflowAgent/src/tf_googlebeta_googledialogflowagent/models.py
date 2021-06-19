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
    ApiVersion: Optional[str]
    AvatarUri: Optional[str]
    AvatarUriBackend: Optional[str]
    ClassificationThreshold: Optional[float]
    DefaultLanguageCode: Optional[str]
    Description: Optional[str]
    DisplayName: Optional[str]
    EnableLogging: Optional[bool]
    Id: Optional[str]
    MatchMode: Optional[str]
    Project: Optional[str]
    SupportedLanguageCodes: Optional[Sequence[str]]
    Tier: Optional[str]
    TimeZone: Optional[str]
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
            ApiVersion=json_data.get("ApiVersion"),
            AvatarUri=json_data.get("AvatarUri"),
            AvatarUriBackend=json_data.get("AvatarUriBackend"),
            ClassificationThreshold=json_data.get("ClassificationThreshold"),
            DefaultLanguageCode=json_data.get("DefaultLanguageCode"),
            Description=json_data.get("Description"),
            DisplayName=json_data.get("DisplayName"),
            EnableLogging=json_data.get("EnableLogging"),
            Id=json_data.get("Id"),
            MatchMode=json_data.get("MatchMode"),
            Project=json_data.get("Project"),
            SupportedLanguageCodes=json_data.get("SupportedLanguageCodes"),
            Tier=json_data.get("Tier"),
            TimeZone=json_data.get("TimeZone"),
            Timeouts=TimeoutsDefinition._deserialize(json_data.get("Timeouts")),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


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


