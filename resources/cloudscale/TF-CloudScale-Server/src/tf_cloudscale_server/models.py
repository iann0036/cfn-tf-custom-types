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
    AllowStoppingForUpdate: Optional[bool]
    BulkVolumeSizeGb: Optional[float]
    FlavorSlug: Optional[str]
    Href: Optional[str]
    Id: Optional[str]
    ImageSlug: Optional[str]
    Name: Optional[str]
    Password: Optional[str]
    PrivateIpv4Address: Optional[str]
    PublicIpv4Address: Optional[str]
    PublicIpv6Address: Optional[str]
    ServerGroupIds: Optional[Sequence[str]]
    ServerGroups: Optional[Sequence["_ServerGroupsDefinition"]]
    SshFingerprints: Optional[Sequence[str]]
    SshHostKeys: Optional[Sequence[str]]
    SshKeys: Optional[Sequence[str]]
    Status: Optional[str]
    UseIpv6: Optional[bool]
    UsePrivateNetwork: Optional[bool]
    UsePublicNetwork: Optional[bool]
    UserData: Optional[str]
    VolumeSizeGb: Optional[float]
    Volumes: Optional[Sequence["_VolumesDefinition"]]
    ZoneSlug: Optional[str]
    Interfaces: Optional[Sequence["_InterfacesDefinition"]]

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
            AllowStoppingForUpdate=json_data.get("AllowStoppingForUpdate"),
            BulkVolumeSizeGb=json_data.get("BulkVolumeSizeGb"),
            FlavorSlug=json_data.get("FlavorSlug"),
            Href=json_data.get("Href"),
            Id=json_data.get("Id"),
            ImageSlug=json_data.get("ImageSlug"),
            Name=json_data.get("Name"),
            Password=json_data.get("Password"),
            PrivateIpv4Address=json_data.get("PrivateIpv4Address"),
            PublicIpv4Address=json_data.get("PublicIpv4Address"),
            PublicIpv6Address=json_data.get("PublicIpv6Address"),
            ServerGroupIds=json_data.get("ServerGroupIds"),
            ServerGroups=deserialize_list(json_data.get("ServerGroups"), ServerGroupsDefinition),
            SshFingerprints=json_data.get("SshFingerprints"),
            SshHostKeys=json_data.get("SshHostKeys"),
            SshKeys=json_data.get("SshKeys"),
            Status=json_data.get("Status"),
            UseIpv6=json_data.get("UseIpv6"),
            UsePrivateNetwork=json_data.get("UsePrivateNetwork"),
            UsePublicNetwork=json_data.get("UsePublicNetwork"),
            UserData=json_data.get("UserData"),
            VolumeSizeGb=json_data.get("VolumeSizeGb"),
            Volumes=deserialize_list(json_data.get("Volumes"), VolumesDefinition),
            ZoneSlug=json_data.get("ZoneSlug"),
            Interfaces=deserialize_list(json_data.get("Interfaces"), InterfacesDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class ServerGroupsDefinition(BaseModel):
    Href: Optional[str]
    Name: Optional[str]
    Uuid: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ServerGroupsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ServerGroupsDefinition"]:
        if not json_data:
            return None
        return cls(
            Href=json_data.get("Href"),
            Name=json_data.get("Name"),
            Uuid=json_data.get("Uuid"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ServerGroupsDefinition = ServerGroupsDefinition


@dataclass
class VolumesDefinition(BaseModel):
    DevicePath: Optional[str]
    SizeGb: Optional[float]
    Type: Optional[str]
    Uuid: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_VolumesDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_VolumesDefinition"]:
        if not json_data:
            return None
        return cls(
            DevicePath=json_data.get("DevicePath"),
            SizeGb=json_data.get("SizeGb"),
            Type=json_data.get("Type"),
            Uuid=json_data.get("Uuid"),
        )


# work around possible type aliasing issues when variable has same name as a model
_VolumesDefinition = VolumesDefinition


@dataclass
class InterfacesDefinition(BaseModel):
    NetworkUuid: Optional[str]
    NoAddress: Optional[bool]
    Type: Optional[str]
    Addresses: Optional[Sequence["_AddressesDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_InterfacesDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_InterfacesDefinition"]:
        if not json_data:
            return None
        return cls(
            NetworkUuid=json_data.get("NetworkUuid"),
            NoAddress=json_data.get("NoAddress"),
            Type=json_data.get("Type"),
            Addresses=deserialize_list(json_data.get("Addresses"), AddressesDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_InterfacesDefinition = InterfacesDefinition


@dataclass
class AddressesDefinition(BaseModel):
    Address: Optional[str]
    SubnetUuid: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_AddressesDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AddressesDefinition"]:
        if not json_data:
            return None
        return cls(
            Address=json_data.get("Address"),
            SubnetUuid=json_data.get("SubnetUuid"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AddressesDefinition = AddressesDefinition


