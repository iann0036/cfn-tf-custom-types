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
    AllowStoppingForUpdate: Optional[bool]
    BulkVolumeSizeGb: Optional[float]
    FlavorSlug: Optional[str]
    Href: Optional[str]
    ImageSlug: Optional[str]
    Name: Optional[str]
    Password: Optional[str]
    PrivateIpv4Address: Optional[str]
    PublicIpv4Address: Optional[str]
    PublicIpv6Address: Optional[str]
    ServerGroupIds: Optional[Sequence[str]]
    ServerGroups: Optional[Sequence["_ServerGroups"]]
    SshFingerprints: Optional[Sequence[str]]
    SshHostKeys: Optional[Sequence[str]]
    SshKeys: Optional[Sequence[str]]
    Status: Optional[str]
    UseIpv6: Optional[bool]
    UsePrivateNetwork: Optional[bool]
    UsePublicNetwork: Optional[bool]
    UserData: Optional[str]
    VolumeSizeGb: Optional[float]
    Volumes: Optional[Sequence["_Volumes"]]
    ZoneSlug: Optional[str]
    Interfaces: Optional[Sequence["_Interfaces"]]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceModel"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceModel"]:
        if not json_data:
            return None
        return cls(
            tfcfnid=json_data.get("tfcfnid"),
            AllowStoppingForUpdate=json_data.get("AllowStoppingForUpdate"),
            BulkVolumeSizeGb=json_data.get("BulkVolumeSizeGb"),
            FlavorSlug=json_data.get("FlavorSlug"),
            Href=json_data.get("Href"),
            ImageSlug=json_data.get("ImageSlug"),
            Name=json_data.get("Name"),
            Password=json_data.get("Password"),
            PrivateIpv4Address=json_data.get("PrivateIpv4Address"),
            PublicIpv4Address=json_data.get("PublicIpv4Address"),
            PublicIpv6Address=json_data.get("PublicIpv6Address"),
            ServerGroupIds=json_data.get("ServerGroupIds"),
            ServerGroups=json_data.get("ServerGroups"),
            SshFingerprints=json_data.get("SshFingerprints"),
            SshHostKeys=json_data.get("SshHostKeys"),
            SshKeys=json_data.get("SshKeys"),
            Status=json_data.get("Status"),
            UseIpv6=json_data.get("UseIpv6"),
            UsePrivateNetwork=json_data.get("UsePrivateNetwork"),
            UsePublicNetwork=json_data.get("UsePublicNetwork"),
            UserData=json_data.get("UserData"),
            VolumeSizeGb=json_data.get("VolumeSizeGb"),
            Volumes=json_data.get("Volumes"),
            ZoneSlug=json_data.get("ZoneSlug"),
            Interfaces=json_data.get("Interfaces"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class ServerGroups:
    Href: Optional[str]
    Name: Optional[str]
    Uuid: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ServerGroups"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ServerGroups"]:
        if not json_data:
            return None
        return cls(
            Href=json_data.get("Href"),
            Name=json_data.get("Name"),
            Uuid=json_data.get("Uuid"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ServerGroups = ServerGroups


@dataclass
class Volumes:
    DevicePath: Optional[str]
    SizeGb: Optional[float]
    Type: Optional[str]
    Uuid: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Volumes"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Volumes"]:
        if not json_data:
            return None
        return cls(
            DevicePath=json_data.get("DevicePath"),
            SizeGb=json_data.get("SizeGb"),
            Type=json_data.get("Type"),
            Uuid=json_data.get("Uuid"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Volumes = Volumes


@dataclass
class Interfaces:
    NetworkUuid: Optional[str]
    Type: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Interfaces"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Interfaces"]:
        if not json_data:
            return None
        return cls(
            NetworkUuid=json_data.get("NetworkUuid"),
            Type=json_data.get("Type"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Interfaces = Interfaces


