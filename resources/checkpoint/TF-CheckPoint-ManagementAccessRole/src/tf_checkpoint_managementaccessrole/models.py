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
    Color: Optional[str]
    Comments: Optional[str]
    Id: Optional[str]
    IgnoreErrors: Optional[bool]
    IgnoreWarnings: Optional[bool]
    Name: Optional[str]
    Networks: Optional[Sequence[str]]
    RemoteAccessClients: Optional[str]
    Tags: Optional[Sequence[str]]
    Machines: Optional[Sequence["_MachinesDefinition"]]
    Users: Optional[Sequence["_UsersDefinition"]]

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
            Color=json_data.get("Color"),
            Comments=json_data.get("Comments"),
            Id=json_data.get("Id"),
            IgnoreErrors=json_data.get("IgnoreErrors"),
            IgnoreWarnings=json_data.get("IgnoreWarnings"),
            Name=json_data.get("Name"),
            Networks=json_data.get("Networks"),
            RemoteAccessClients=json_data.get("RemoteAccessClients"),
            Tags=json_data.get("Tags"),
            Machines=deserialize_list(json_data.get("Machines"), MachinesDefinition),
            Users=deserialize_list(json_data.get("Users"), UsersDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class MachinesDefinition(BaseModel):
    BaseDn: Optional[str]
    Selection: Optional[Sequence[str]]
    Source: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_MachinesDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_MachinesDefinition"]:
        if not json_data:
            return None
        return cls(
            BaseDn=json_data.get("BaseDn"),
            Selection=json_data.get("Selection"),
            Source=json_data.get("Source"),
        )


# work around possible type aliasing issues when variable has same name as a model
_MachinesDefinition = MachinesDefinition


@dataclass
class UsersDefinition(BaseModel):
    BaseDn: Optional[str]
    Selection: Optional[Sequence[str]]
    Source: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_UsersDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_UsersDefinition"]:
        if not json_data:
            return None
        return cls(
            BaseDn=json_data.get("BaseDn"),
            Selection=json_data.get("Selection"),
            Source=json_data.get("Source"),
        )


# work around possible type aliasing issues when variable has same name as a model
_UsersDefinition = UsersDefinition


