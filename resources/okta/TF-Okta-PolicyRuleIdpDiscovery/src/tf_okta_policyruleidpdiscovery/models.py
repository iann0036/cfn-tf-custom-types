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
    Id: Optional[str]
    IdpId: Optional[str]
    IdpType: Optional[str]
    Name: Optional[str]
    NetworkConnection: Optional[str]
    NetworkExcludes: Optional[Sequence[str]]
    NetworkIncludes: Optional[Sequence[str]]
    Policyid: Optional[str]
    Priority: Optional[float]
    Status: Optional[str]
    UserIdentifierAttribute: Optional[str]
    UserIdentifierType: Optional[str]
    AppExclude: Optional[Sequence["_AppExcludeDefinition"]]
    AppInclude: Optional[Sequence["_AppIncludeDefinition"]]
    PlatformInclude: Optional[Sequence["_PlatformIncludeDefinition"]]
    UserIdentifierPatterns: Optional[Sequence["_UserIdentifierPatternsDefinition"]]

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
            Id=json_data.get("Id"),
            IdpId=json_data.get("IdpId"),
            IdpType=json_data.get("IdpType"),
            Name=json_data.get("Name"),
            NetworkConnection=json_data.get("NetworkConnection"),
            NetworkExcludes=json_data.get("NetworkExcludes"),
            NetworkIncludes=json_data.get("NetworkIncludes"),
            Policyid=json_data.get("Policyid"),
            Priority=json_data.get("Priority"),
            Status=json_data.get("Status"),
            UserIdentifierAttribute=json_data.get("UserIdentifierAttribute"),
            UserIdentifierType=json_data.get("UserIdentifierType"),
            AppExclude=deserialize_list(json_data.get("AppExclude"), AppExcludeDefinition),
            AppInclude=deserialize_list(json_data.get("AppInclude"), AppIncludeDefinition),
            PlatformInclude=deserialize_list(json_data.get("PlatformInclude"), PlatformIncludeDefinition),
            UserIdentifierPatterns=deserialize_list(json_data.get("UserIdentifierPatterns"), UserIdentifierPatternsDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class AppExcludeDefinition(BaseModel):
    Id: Optional[str]
    Name: Optional[str]
    Type: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_AppExcludeDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AppExcludeDefinition"]:
        if not json_data:
            return None
        return cls(
            Id=json_data.get("Id"),
            Name=json_data.get("Name"),
            Type=json_data.get("Type"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AppExcludeDefinition = AppExcludeDefinition


@dataclass
class AppIncludeDefinition(BaseModel):
    Id: Optional[str]
    Name: Optional[str]
    Type: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_AppIncludeDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AppIncludeDefinition"]:
        if not json_data:
            return None
        return cls(
            Id=json_data.get("Id"),
            Name=json_data.get("Name"),
            Type=json_data.get("Type"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AppIncludeDefinition = AppIncludeDefinition


@dataclass
class PlatformIncludeDefinition(BaseModel):
    OsExpression: Optional[str]
    OsType: Optional[str]
    Type: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_PlatformIncludeDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_PlatformIncludeDefinition"]:
        if not json_data:
            return None
        return cls(
            OsExpression=json_data.get("OsExpression"),
            OsType=json_data.get("OsType"),
            Type=json_data.get("Type"),
        )


# work around possible type aliasing issues when variable has same name as a model
_PlatformIncludeDefinition = PlatformIncludeDefinition


@dataclass
class UserIdentifierPatternsDefinition(BaseModel):
    MatchType: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_UserIdentifierPatternsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_UserIdentifierPatternsDefinition"]:
        if not json_data:
            return None
        return cls(
            MatchType=json_data.get("MatchType"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_UserIdentifierPatternsDefinition = UserIdentifierPatternsDefinition


