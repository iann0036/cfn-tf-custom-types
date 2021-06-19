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
    AllowUnlabelledAccess: Optional[bool]
    Id: Optional[str]
    Name: Optional[str]
    TenantRef: Optional[str]
    Uuid: Optional[str]
    Filters: Optional[Sequence["_FiltersDefinition"]]
    Privileges: Optional[Sequence["_PrivilegesDefinition"]]

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
            AllowUnlabelledAccess=json_data.get("AllowUnlabelledAccess"),
            Id=json_data.get("Id"),
            Name=json_data.get("Name"),
            TenantRef=json_data.get("TenantRef"),
            Uuid=json_data.get("Uuid"),
            Filters=deserialize_list(json_data.get("Filters"), FiltersDefinition),
            Privileges=deserialize_list(json_data.get("Privileges"), PrivilegesDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class FiltersDefinition(BaseModel):
    Enabled: Optional[bool]
    MatchOperation: Optional[str]
    Name: Optional[str]
    MatchLabel: Optional[Sequence["_MatchLabelDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_FiltersDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_FiltersDefinition"]:
        if not json_data:
            return None
        return cls(
            Enabled=json_data.get("Enabled"),
            MatchOperation=json_data.get("MatchOperation"),
            Name=json_data.get("Name"),
            MatchLabel=deserialize_list(json_data.get("MatchLabel"), MatchLabelDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_FiltersDefinition = FiltersDefinition


@dataclass
class MatchLabelDefinition(BaseModel):
    Key: Optional[str]
    Values: Optional[Sequence[str]]

    @classmethod
    def _deserialize(
        cls: Type["_MatchLabelDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_MatchLabelDefinition"]:
        if not json_data:
            return None
        return cls(
            Key=json_data.get("Key"),
            Values=json_data.get("Values"),
        )


# work around possible type aliasing issues when variable has same name as a model
_MatchLabelDefinition = MatchLabelDefinition


@dataclass
class PrivilegesDefinition(BaseModel):
    Resource: Optional[str]
    Type: Optional[str]
    Subresource: Optional[Sequence["_SubresourceDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_PrivilegesDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_PrivilegesDefinition"]:
        if not json_data:
            return None
        return cls(
            Resource=json_data.get("Resource"),
            Type=json_data.get("Type"),
            Subresource=deserialize_list(json_data.get("Subresource"), SubresourceDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_PrivilegesDefinition = PrivilegesDefinition


@dataclass
class SubresourceDefinition(BaseModel):
    ExcludeSubresources: Optional[bool]
    Subresources: Optional[Sequence[str]]

    @classmethod
    def _deserialize(
        cls: Type["_SubresourceDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SubresourceDefinition"]:
        if not json_data:
            return None
        return cls(
            ExcludeSubresources=json_data.get("ExcludeSubresources"),
            Subresources=json_data.get("Subresources"),
        )


# work around possible type aliasing issues when variable has same name as a model
_SubresourceDefinition = SubresourceDefinition


