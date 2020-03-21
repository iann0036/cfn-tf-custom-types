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
    CookieFallback: Optional[bool]
    CookieGarble: Optional[bool]
    CookieMode: Optional[str]
    CookieName: Optional[str]
    Description: Optional[str]
    DisplayName: Optional[str]
    PersistenceShared: Optional[bool]
    Revision: Optional[float]
    InsertModeParams: Optional[Sequence["_InsertModeParams"]]
    Tag: Optional[Sequence["_Tag"]]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceModel"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceModel"]:
        if not json_data:
            return None
        return cls(
            tfcfnid=json_data.get("tfcfnid"),
            CookieFallback=json_data.get("CookieFallback"),
            CookieGarble=json_data.get("CookieGarble"),
            CookieMode=json_data.get("CookieMode"),
            CookieName=json_data.get("CookieName"),
            Description=json_data.get("Description"),
            DisplayName=json_data.get("DisplayName"),
            PersistenceShared=json_data.get("PersistenceShared"),
            Revision=json_data.get("Revision"),
            InsertModeParams=json_data.get("InsertModeParams"),
            Tag=json_data.get("Tag"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class InsertModeParams:
    CookieDomain: Optional[str]
    CookieExpiryType: Optional[str]
    CookiePath: Optional[str]
    MaxIdleTime: Optional[float]
    MaxLifeTime: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_InsertModeParams"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_InsertModeParams"]:
        if not json_data:
            return None
        return cls(
            CookieDomain=json_data.get("CookieDomain"),
            CookieExpiryType=json_data.get("CookieExpiryType"),
            CookiePath=json_data.get("CookiePath"),
            MaxIdleTime=json_data.get("MaxIdleTime"),
            MaxLifeTime=json_data.get("MaxLifeTime"),
        )


# work around possible type aliasing issues when variable has same name as a model
_InsertModeParams = InsertModeParams


@dataclass
class Tag:
    Scope: Optional[str]
    Tag: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Tag"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Tag"]:
        if not json_data:
            return None
        return cls(
            Scope=json_data.get("Scope"),
            Tag=json_data.get("Tag"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Tag = Tag


