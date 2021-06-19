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
    AffinityGroupIds: Optional[Sequence[str]]
    AffinityGroups: Optional[Sequence[str]]
    DiskSize: Optional[float]
    DisplayName: Optional[str]
    Gateway: Optional[str]
    Hostname: Optional[str]
    Id: Optional[str]
    Ip4: Optional[bool]
    Ip6: Optional[bool]
    Ip6Address: Optional[str]
    Ip6Cidr: Optional[str]
    IpAddress: Optional[str]
    KeyPair: Optional[str]
    Keyboard: Optional[str]
    Name: Optional[str]
    Password: Optional[str]
    ReverseDns: Optional[str]
    SecurityGroupIds: Optional[Sequence[str]]
    SecurityGroups: Optional[Sequence[str]]
    Size: Optional[str]
    State: Optional[str]
    Tags: Optional[Sequence["_TagsDefinition"]]
    Template: Optional[str]
    TemplateId: Optional[str]
    UserData: Optional[str]
    UserDataBase64: Optional[bool]
    Username: Optional[str]
    Zone: Optional[str]
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
            AffinityGroupIds=json_data.get("AffinityGroupIds"),
            AffinityGroups=json_data.get("AffinityGroups"),
            DiskSize=json_data.get("DiskSize"),
            DisplayName=json_data.get("DisplayName"),
            Gateway=json_data.get("Gateway"),
            Hostname=json_data.get("Hostname"),
            Id=json_data.get("Id"),
            Ip4=json_data.get("Ip4"),
            Ip6=json_data.get("Ip6"),
            Ip6Address=json_data.get("Ip6Address"),
            Ip6Cidr=json_data.get("Ip6Cidr"),
            IpAddress=json_data.get("IpAddress"),
            KeyPair=json_data.get("KeyPair"),
            Keyboard=json_data.get("Keyboard"),
            Name=json_data.get("Name"),
            Password=json_data.get("Password"),
            ReverseDns=json_data.get("ReverseDns"),
            SecurityGroupIds=json_data.get("SecurityGroupIds"),
            SecurityGroups=json_data.get("SecurityGroups"),
            Size=json_data.get("Size"),
            State=json_data.get("State"),
            Tags=deserialize_list(json_data.get("Tags"), TagsDefinition),
            Template=json_data.get("Template"),
            TemplateId=json_data.get("TemplateId"),
            UserData=json_data.get("UserData"),
            UserDataBase64=json_data.get("UserDataBase64"),
            Username=json_data.get("Username"),
            Zone=json_data.get("Zone"),
            Timeouts=TimeoutsDefinition._deserialize(json_data.get("Timeouts")),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


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


