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
    CreateTime: Optional[str]
    Description: Optional[str]
    Id: Optional[str]
    Ipv4Count: Optional[float]
    Ipv4Info: Optional[Sequence["_Ipv4InfoDefinition"]]
    Mac: Optional[str]
    Name: Optional[str]
    Primary: Optional[bool]
    SecurityGroups: Optional[Sequence[str]]
    State: Optional[str]
    SubnetId: Optional[str]
    Tags: Optional[Sequence["_TagsDefinition"]]
    VpcId: Optional[str]
    Ipv4s: Optional[Sequence["_Ipv4sDefinition"]]

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
            CreateTime=json_data.get("CreateTime"),
            Description=json_data.get("Description"),
            Id=json_data.get("Id"),
            Ipv4Count=json_data.get("Ipv4Count"),
            Ipv4Info=deserialize_list(json_data.get("Ipv4Info"), Ipv4InfoDefinition),
            Mac=json_data.get("Mac"),
            Name=json_data.get("Name"),
            Primary=json_data.get("Primary"),
            SecurityGroups=json_data.get("SecurityGroups"),
            State=json_data.get("State"),
            SubnetId=json_data.get("SubnetId"),
            Tags=deserialize_list(json_data.get("Tags"), TagsDefinition),
            VpcId=json_data.get("VpcId"),
            Ipv4s=deserialize_list(json_data.get("Ipv4s"), Ipv4sDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class Ipv4InfoDefinition(BaseModel):
    Description: Optional[str]
    Ip: Optional[str]
    Primary: Optional[bool]

    @classmethod
    def _deserialize(
        cls: Type["_Ipv4InfoDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Ipv4InfoDefinition"]:
        if not json_data:
            return None
        return cls(
            Description=json_data.get("Description"),
            Ip=json_data.get("Ip"),
            Primary=json_data.get("Primary"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Ipv4InfoDefinition = Ipv4InfoDefinition


@dataclass
class TagsDefinition(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_TagsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TagsDefinition"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TagsDefinition = TagsDefinition


@dataclass
class Ipv4sDefinition(BaseModel):
    Description: Optional[str]
    Ip: Optional[str]
    Primary: Optional[bool]

    @classmethod
    def _deserialize(
        cls: Type["_Ipv4sDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Ipv4sDefinition"]:
        if not json_data:
            return None
        return cls(
            Description=json_data.get("Description"),
            Ip=json_data.get("Ip"),
            Primary=json_data.get("Primary"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Ipv4sDefinition = Ipv4sDefinition


