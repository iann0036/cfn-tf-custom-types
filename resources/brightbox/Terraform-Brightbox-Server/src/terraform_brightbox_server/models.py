# DO NOT modify this file by hand, changes will be overwritten
from dataclasses import dataclass
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
    BaseResourceHandlerRequest,
    BaseResourceModel,
)

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
class ResourceModel(BaseResourceModel):
    tfcfnid: Optional[str]
    Fqdn: Optional[str]
    Hostname: Optional[str]
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
    Timeouts: Optional["_Timeouts"]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceModel"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceModel"]:
        if not json_data:
            return None
        return cls(
            tfcfnid=json_data.get("tfcfnid"),
            Fqdn=json_data.get("Fqdn"),
            Hostname=json_data.get("Hostname"),
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
            Timeouts=Timeouts._deserialize(json_data.get("Timeouts")),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class Timeouts:
    Create: Optional[str]
    Delete: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Timeouts"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Timeouts"]:
        if not json_data:
            return None
        return cls(
            Create=json_data.get("Create"),
            Delete=json_data.get("Delete"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Timeouts = Timeouts


