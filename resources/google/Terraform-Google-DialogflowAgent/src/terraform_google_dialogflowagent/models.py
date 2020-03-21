# DO NOT modify this file by hand, changes will be overwritten
from dataclasses import dataclass
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
    BaseResourceHandlerRequest,
    BaseResourceModel,
)

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
class ResourceModel(BaseResourceModel):
    tfcfnid: Optional[str]
    ApiVersion: Optional[str]
    AvatarUri: Optional[str]
    AvatarUriBackend: Optional[str]
    ClassificationThreshold: Optional[float]
    DefaultLanguageCode: Optional[str]
    Description: Optional[str]
    DisplayName: Optional[str]
    EnableLogging: Optional[bool]
    MatchMode: Optional[str]
    Project: Optional[str]
    SupportedLanguageCodes: Optional[Sequence[str]]
    Tier: Optional[str]
    TimeZone: Optional[str]
    Timeouts: Optional["_Timeouts"]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceModel"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceModel"]:
        if not json_data:
            return None
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
            MatchMode=json_data.get("MatchMode"),
            Project=json_data.get("Project"),
            SupportedLanguageCodes=json_data.get("SupportedLanguageCodes"),
            Tier=json_data.get("Tier"),
            TimeZone=json_data.get("TimeZone"),
            Timeouts=Timeouts._deserialize(json_data.get("Timeouts")),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class Timeouts:
    Create: Optional[str]
    Delete: Optional[str]
    Update: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Timeouts"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Timeouts"]:
        if not json_data:
            return None
        return cls(
            Create=json_data.get("Create"),
            Delete=json_data.get("Delete"),
            Update=json_data.get("Update"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Timeouts = Timeouts


