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
    AutomationAccountName: Optional[str]
    Id: Optional[str]
    Name: Optional[str]
    ResourceGroupName: Optional[str]
    ModuleLink: Optional[Sequence["_ModuleLinkDefinition"]]
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
            AutomationAccountName=json_data.get("AutomationAccountName"),
            Id=json_data.get("Id"),
            Name=json_data.get("Name"),
            ResourceGroupName=json_data.get("ResourceGroupName"),
            ModuleLink=deserialize_list(json_data.get("ModuleLink"), ModuleLinkDefinition),
            Timeouts=TimeoutsDefinition._deserialize(json_data.get("Timeouts")),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class ModuleLinkDefinition(BaseModel):
    Uri: Optional[str]
    Hash: Optional[Sequence["_HashDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_ModuleLinkDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ModuleLinkDefinition"]:
        if not json_data:
            return None
        return cls(
            Uri=json_data.get("Uri"),
            Hash=deserialize_list(json_data.get("Hash"), HashDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ModuleLinkDefinition = ModuleLinkDefinition


@dataclass
class HashDefinition(BaseModel):
    Algorithm: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_HashDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_HashDefinition"]:
        if not json_data:
            return None
        return cls(
            Algorithm=json_data.get("Algorithm"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_HashDefinition = HashDefinition


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


