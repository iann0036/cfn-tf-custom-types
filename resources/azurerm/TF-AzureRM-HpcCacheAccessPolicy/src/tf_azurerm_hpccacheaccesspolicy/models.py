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
    HpcCacheId: Optional[str]
    Id: Optional[str]
    Name: Optional[str]
    AccessRule: Optional[Sequence["_AccessRuleDefinition"]]
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
            HpcCacheId=json_data.get("HpcCacheId"),
            Id=json_data.get("Id"),
            Name=json_data.get("Name"),
            AccessRule=deserialize_list(json_data.get("AccessRule"), AccessRuleDefinition),
            Timeouts=TimeoutsDefinition._deserialize(json_data.get("Timeouts")),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class AccessRuleDefinition(BaseModel):
    Access: Optional[str]
    AnonymousGid: Optional[float]
    AnonymousUid: Optional[float]
    Filter: Optional[str]
    RootSquashEnabled: Optional[bool]
    Scope: Optional[str]
    SubmountAccessEnabled: Optional[bool]
    SuidEnabled: Optional[bool]

    @classmethod
    def _deserialize(
        cls: Type["_AccessRuleDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AccessRuleDefinition"]:
        if not json_data:
            return None
        return cls(
            Access=json_data.get("Access"),
            AnonymousGid=json_data.get("AnonymousGid"),
            AnonymousUid=json_data.get("AnonymousUid"),
            Filter=json_data.get("Filter"),
            RootSquashEnabled=json_data.get("RootSquashEnabled"),
            Scope=json_data.get("Scope"),
            SubmountAccessEnabled=json_data.get("SubmountAccessEnabled"),
            SuidEnabled=json_data.get("SuidEnabled"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AccessRuleDefinition = AccessRuleDefinition


@dataclass
class TimeoutsDefinition(BaseModel):
    Create: Optional[str]
    Delete: Optional[str]
    Read: Optional[str]
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
            Read=json_data.get("Read"),
            Update=json_data.get("Update"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TimeoutsDefinition = TimeoutsDefinition


