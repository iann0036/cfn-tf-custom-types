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
    CheckRegions: Optional[Sequence[str]]
    CreatedOn: Optional[str]
    Description: Optional[str]
    Enabled: Optional[bool]
    Id: Optional[str]
    MinimumOrigins: Optional[float]
    ModifiedOn: Optional[str]
    Monitor: Optional[str]
    Name: Optional[str]
    NotificationEmail: Optional[str]
    Origins: Optional[Sequence["_OriginsDefinition"]]

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
            CheckRegions=json_data.get("CheckRegions"),
            CreatedOn=json_data.get("CreatedOn"),
            Description=json_data.get("Description"),
            Enabled=json_data.get("Enabled"),
            Id=json_data.get("Id"),
            MinimumOrigins=json_data.get("MinimumOrigins"),
            ModifiedOn=json_data.get("ModifiedOn"),
            Monitor=json_data.get("Monitor"),
            Name=json_data.get("Name"),
            NotificationEmail=json_data.get("NotificationEmail"),
            Origins=deserialize_list(json_data.get("Origins"), OriginsDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class OriginsDefinition(BaseModel):
    Address: Optional[str]
    Enabled: Optional[bool]
    Name: Optional[str]
    Weight: Optional[float]
    Header: Optional[Sequence["_HeaderDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_OriginsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_OriginsDefinition"]:
        if not json_data:
            return None
        return cls(
            Address=json_data.get("Address"),
            Enabled=json_data.get("Enabled"),
            Name=json_data.get("Name"),
            Weight=json_data.get("Weight"),
            Header=deserialize_list(json_data.get("Header"), HeaderDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_OriginsDefinition = OriginsDefinition


@dataclass
class HeaderDefinition(BaseModel):
    Header: Optional[str]
    Values: Optional[Sequence[str]]

    @classmethod
    def _deserialize(
        cls: Type["_HeaderDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_HeaderDefinition"]:
        if not json_data:
            return None
        return cls(
            Header=json_data.get("Header"),
            Values=json_data.get("Values"),
        )


# work around possible type aliasing issues when variable has same name as a model
_HeaderDefinition = HeaderDefinition


