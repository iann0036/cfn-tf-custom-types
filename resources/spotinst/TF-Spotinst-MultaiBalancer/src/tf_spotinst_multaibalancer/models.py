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
    DnsCnameAliases: Optional[Sequence[str]]
    Id: Optional[str]
    Name: Optional[str]
    Scheme: Optional[str]
    ConnectionTimeouts: Optional[Sequence["_ConnectionTimeoutsDefinition"]]
    Tags: Optional[Sequence["_TagsDefinition"]]

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
            DnsCnameAliases=json_data.get("DnsCnameAliases"),
            Id=json_data.get("Id"),
            Name=json_data.get("Name"),
            Scheme=json_data.get("Scheme"),
            ConnectionTimeouts=deserialize_list(json_data.get("ConnectionTimeouts"), ConnectionTimeoutsDefinition),
            Tags=deserialize_list(json_data.get("Tags"), TagsDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class ConnectionTimeoutsDefinition(BaseModel):
    Draining: Optional[float]
    Idle: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_ConnectionTimeoutsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ConnectionTimeoutsDefinition"]:
        if not json_data:
            return None
        return cls(
            Draining=json_data.get("Draining"),
            Idle=json_data.get("Idle"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ConnectionTimeoutsDefinition = ConnectionTimeoutsDefinition


@dataclass
class TagsDefinition(BaseModel):
    Key: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_TagsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TagsDefinition"]:
        if not json_data:
            return None
        return cls(
            Key=json_data.get("Key"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TagsDefinition = TagsDefinition


