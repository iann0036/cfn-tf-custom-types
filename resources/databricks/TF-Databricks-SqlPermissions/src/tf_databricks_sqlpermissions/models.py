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
    AnonymousFunction: Optional[bool]
    AnyFile: Optional[bool]
    Catalog: Optional[bool]
    ClusterId: Optional[str]
    Database: Optional[str]
    Id: Optional[str]
    Table: Optional[str]
    View: Optional[str]
    PrivilegeAssignments: Optional[Sequence["_PrivilegeAssignmentsDefinition"]]

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
            AnonymousFunction=json_data.get("AnonymousFunction"),
            AnyFile=json_data.get("AnyFile"),
            Catalog=json_data.get("Catalog"),
            ClusterId=json_data.get("ClusterId"),
            Database=json_data.get("Database"),
            Id=json_data.get("Id"),
            Table=json_data.get("Table"),
            View=json_data.get("View"),
            PrivilegeAssignments=deserialize_list(json_data.get("PrivilegeAssignments"), PrivilegeAssignmentsDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class PrivilegeAssignmentsDefinition(BaseModel):
    Principal: Optional[str]
    Privileges: Optional[Sequence[str]]

    @classmethod
    def _deserialize(
        cls: Type["_PrivilegeAssignmentsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_PrivilegeAssignmentsDefinition"]:
        if not json_data:
            return None
        return cls(
            Principal=json_data.get("Principal"),
            Privileges=json_data.get("Privileges"),
        )


# work around possible type aliasing issues when variable has same name as a model
_PrivilegeAssignmentsDefinition = PrivilegeAssignmentsDefinition


