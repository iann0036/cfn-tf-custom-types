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
    Action: Optional[str]
    Description: Optional[str]
    Id: Optional[str]
    Key: Optional[str]
    Labels: Optional[Sequence[str]]
    ModSecurityRuleIds: Optional[Sequence[str]]
    Name: Optional[str]
    WaasPolicyId: Optional[str]
    Exclusions: Optional[Sequence["_ExclusionsDefinition"]]
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
            Action=json_data.get("Action"),
            Description=json_data.get("Description"),
            Id=json_data.get("Id"),
            Key=json_data.get("Key"),
            Labels=json_data.get("Labels"),
            ModSecurityRuleIds=json_data.get("ModSecurityRuleIds"),
            Name=json_data.get("Name"),
            WaasPolicyId=json_data.get("WaasPolicyId"),
            Exclusions=deserialize_list(json_data.get("Exclusions"), ExclusionsDefinition),
            Timeouts=TimeoutsDefinition._deserialize(json_data.get("Timeouts")),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class ExclusionsDefinition(BaseModel):
    Exclusions: Optional[Sequence[str]]
    Target: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ExclusionsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ExclusionsDefinition"]:
        if not json_data:
            return None
        return cls(
            Exclusions=json_data.get("Exclusions"),
            Target=json_data.get("Target"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ExclusionsDefinition = ExclusionsDefinition


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


