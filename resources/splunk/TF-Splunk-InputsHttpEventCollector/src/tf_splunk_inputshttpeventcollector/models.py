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
    Disabled: Optional[bool]
    Host: Optional[str]
    Id: Optional[str]
    Index: Optional[str]
    Indexes: Optional[Sequence[str]]
    Name: Optional[str]
    Source: Optional[str]
    Sourcetype: Optional[str]
    Token: Optional[str]
    UseAck: Optional[float]
    Acl: Optional[Sequence["_AclDefinition"]]

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
            Disabled=json_data.get("Disabled"),
            Host=json_data.get("Host"),
            Id=json_data.get("Id"),
            Index=json_data.get("Index"),
            Indexes=json_data.get("Indexes"),
            Name=json_data.get("Name"),
            Source=json_data.get("Source"),
            Sourcetype=json_data.get("Sourcetype"),
            Token=json_data.get("Token"),
            UseAck=json_data.get("UseAck"),
            Acl=deserialize_list(json_data.get("Acl"), AclDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class AclDefinition(BaseModel):
    App: Optional[str]
    CanChangePerms: Optional[bool]
    CanShareApp: Optional[bool]
    CanShareGlobal: Optional[bool]
    CanShareUser: Optional[bool]
    CanWrite: Optional[bool]
    Owner: Optional[str]
    Read: Optional[Sequence[str]]
    Removable: Optional[bool]
    Sharing: Optional[str]
    Write: Optional[Sequence[str]]

    @classmethod
    def _deserialize(
        cls: Type["_AclDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AclDefinition"]:
        if not json_data:
            return None
        return cls(
            App=json_data.get("App"),
            CanChangePerms=json_data.get("CanChangePerms"),
            CanShareApp=json_data.get("CanShareApp"),
            CanShareGlobal=json_data.get("CanShareGlobal"),
            CanShareUser=json_data.get("CanShareUser"),
            CanWrite=json_data.get("CanWrite"),
            Owner=json_data.get("Owner"),
            Read=json_data.get("Read"),
            Removable=json_data.get("Removable"),
            Sharing=json_data.get("Sharing"),
            Write=json_data.get("Write"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AclDefinition = AclDefinition


