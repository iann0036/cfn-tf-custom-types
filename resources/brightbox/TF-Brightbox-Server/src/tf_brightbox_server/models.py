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
    DiskEncrypted: Optional[bool]
    Fqdn: Optional[str]
    Hostname: Optional[str]
    Id: Optional[str]
    Image: Optional[str]
    Interface: Optional[str]
    Ipv4Address: Optional[str]
    Ipv4AddressPrivate: Optional[str]
    Ipv6Address: Optional[str]
    Ipv6Hostname: Optional[str]
    Locked: Optional[bool]
    Name: Optional[str]
    PublicHostname: Optional[str]
    ServerGroups: Optional[Sequence[str]]
    Status: Optional[str]
    Type: Optional[str]
    UserData: Optional[str]
    UserDataBase64: Optional[str]
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
            DiskEncrypted=json_data.get("DiskEncrypted"),
            Fqdn=json_data.get("Fqdn"),
            Hostname=json_data.get("Hostname"),
            Id=json_data.get("Id"),
            Image=json_data.get("Image"),
            Interface=json_data.get("Interface"),
            Ipv4Address=json_data.get("Ipv4Address"),
            Ipv4AddressPrivate=json_data.get("Ipv4AddressPrivate"),
            Ipv6Address=json_data.get("Ipv6Address"),
            Ipv6Hostname=json_data.get("Ipv6Hostname"),
            Locked=json_data.get("Locked"),
            Name=json_data.get("Name"),
            PublicHostname=json_data.get("PublicHostname"),
            ServerGroups=json_data.get("ServerGroups"),
            Status=json_data.get("Status"),
            Type=json_data.get("Type"),
            UserData=json_data.get("UserData"),
            UserDataBase64=json_data.get("UserDataBase64"),
            Username=json_data.get("Username"),
            Zone=json_data.get("Zone"),
            Timeouts=TimeoutsDefinition._deserialize(json_data.get("Timeouts")),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class TimeoutsDefinition(BaseModel):
    Create: Optional[str]
    Delete: Optional[str]

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
        )


# work around possible type aliasing issues when variable has same name as a model
_TimeoutsDefinition = TimeoutsDefinition


