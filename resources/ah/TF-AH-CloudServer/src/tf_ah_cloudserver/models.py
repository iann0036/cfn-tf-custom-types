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
    Backups: Optional[bool]
    CreatePublicIpAddress: Optional[bool]
    CreatedAt: Optional[str]
    Datacenter: Optional[str]
    Disk: Optional[float]
    Id: Optional[str]
    Image: Optional[str]
    Ips: Optional[Sequence["_IpsDefinition"]]
    Name: Optional[str]
    Product: Optional[str]
    Ram: Optional[float]
    SshKeys: Optional[Sequence[str]]
    State: Optional[str]
    UsePassword: Optional[bool]
    Vcpu: Optional[float]

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
            Backups=json_data.get("Backups"),
            CreatePublicIpAddress=json_data.get("CreatePublicIpAddress"),
            CreatedAt=json_data.get("CreatedAt"),
            Datacenter=json_data.get("Datacenter"),
            Disk=json_data.get("Disk"),
            Id=json_data.get("Id"),
            Image=json_data.get("Image"),
            Ips=deserialize_list(json_data.get("Ips"), IpsDefinition),
            Name=json_data.get("Name"),
            Product=json_data.get("Product"),
            Ram=json_data.get("Ram"),
            SshKeys=json_data.get("SshKeys"),
            State=json_data.get("State"),
            UsePassword=json_data.get("UsePassword"),
            Vcpu=json_data.get("Vcpu"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class IpsDefinition(BaseModel):
    AssignmentId: Optional[str]
    IpAddress: Optional[str]
    Primary: Optional[bool]
    ReverseDns: Optional[str]
    Type: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_IpsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_IpsDefinition"]:
        if not json_data:
            return None
        return cls(
            AssignmentId=json_data.get("AssignmentId"),
            IpAddress=json_data.get("IpAddress"),
            Primary=json_data.get("Primary"),
            ReverseDns=json_data.get("ReverseDns"),
            Type=json_data.get("Type"),
        )


# work around possible type aliasing issues when variable has same name as a model
_IpsDefinition = IpsDefinition


