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
    DefaultDatacenter: Optional[Sequence["_DefaultDatacenterDefinition"]]
    Domain: Optional[str]
    Id: Optional[str]
    Name: Optional[str]
    WaitOnComplete: Optional[bool]
    Assignment: Optional[Sequence["_AssignmentDefinition"]]

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
            DefaultDatacenter=deserialize_list(json_data.get("DefaultDatacenter"), DefaultDatacenterDefinition),
            Domain=json_data.get("Domain"),
            Id=json_data.get("Id"),
            Name=json_data.get("Name"),
            WaitOnComplete=json_data.get("WaitOnComplete"),
            Assignment=deserialize_list(json_data.get("Assignment"), AssignmentDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class DefaultDatacenterDefinition(BaseModel):
    DatacenterId: Optional[float]
    Nickname: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_DefaultDatacenterDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DefaultDatacenterDefinition"]:
        if not json_data:
            return None
        return cls(
            DatacenterId=json_data.get("DatacenterId"),
            Nickname=json_data.get("Nickname"),
        )


# work around possible type aliasing issues when variable has same name as a model
_DefaultDatacenterDefinition = DefaultDatacenterDefinition


@dataclass
class AssignmentDefinition(BaseModel):
    AsNumbers: Optional[Sequence[float]]
    DatacenterId: Optional[float]
    Nickname: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_AssignmentDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AssignmentDefinition"]:
        if not json_data:
            return None
        return cls(
            AsNumbers=json_data.get("AsNumbers"),
            DatacenterId=json_data.get("DatacenterId"),
            Nickname=json_data.get("Nickname"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AssignmentDefinition = AssignmentDefinition


