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
    ExtraTemplate: Optional[str]
    Gid: Optional[float]
    Gname: Optional[str]
    Id: Optional[str]
    Name: Optional[str]
    Networks: Optional[Sequence["_NetworksDefinition"]]
    Permissions: Optional[str]
    Roles: Optional[Sequence["_RolesDefinition"]]
    State: Optional[float]
    TemplateId: Optional[float]
    Uid: Optional[float]
    Uname: Optional[str]

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
            ExtraTemplate=json_data.get("ExtraTemplate"),
            Gid=json_data.get("Gid"),
            Gname=json_data.get("Gname"),
            Id=json_data.get("Id"),
            Name=json_data.get("Name"),
            Networks=deserialize_list(json_data.get("Networks"), NetworksDefinition),
            Permissions=json_data.get("Permissions"),
            Roles=deserialize_list(json_data.get("Roles"), RolesDefinition),
            State=json_data.get("State"),
            TemplateId=json_data.get("TemplateId"),
            Uid=json_data.get("Uid"),
            Uname=json_data.get("Uname"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class NetworksDefinition(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_NetworksDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_NetworksDefinition"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_NetworksDefinition = NetworksDefinition


@dataclass
class RolesDefinition(BaseModel):
    Cardinality: Optional[float]
    Name: Optional[str]
    Nodes: Optional[Sequence[float]]
    State: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_RolesDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_RolesDefinition"]:
        if not json_data:
            return None
        return cls(
            Cardinality=json_data.get("Cardinality"),
            Name=json_data.get("Name"),
            Nodes=json_data.get("Nodes"),
            State=json_data.get("State"),
        )


# work around possible type aliasing issues when variable has same name as a model
_RolesDefinition = RolesDefinition


