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
    Description: Optional[str]
    Id: Optional[str]
    InternetAccess: Optional[bool]
    LastModified: Optional[str]
    Name: Optional[str]
    NamePrefix: Optional[str]
    Publish: Optional[bool]
    Role: Optional[str]
    ServiceId: Optional[str]
    Version: Optional[str]
    LogConfig: Optional[Sequence["_LogConfigDefinition"]]
    NasConfig: Optional[Sequence["_NasConfigDefinition"]]
    VpcConfig: Optional[Sequence["_VpcConfigDefinition"]]

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
            Description=json_data.get("Description"),
            Id=json_data.get("Id"),
            InternetAccess=json_data.get("InternetAccess"),
            LastModified=json_data.get("LastModified"),
            Name=json_data.get("Name"),
            NamePrefix=json_data.get("NamePrefix"),
            Publish=json_data.get("Publish"),
            Role=json_data.get("Role"),
            ServiceId=json_data.get("ServiceId"),
            Version=json_data.get("Version"),
            LogConfig=deserialize_list(json_data.get("LogConfig"), LogConfigDefinition),
            NasConfig=deserialize_list(json_data.get("NasConfig"), NasConfigDefinition),
            VpcConfig=deserialize_list(json_data.get("VpcConfig"), VpcConfigDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class LogConfigDefinition(BaseModel):
    Logstore: Optional[str]
    Project: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_LogConfigDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_LogConfigDefinition"]:
        if not json_data:
            return None
        return cls(
            Logstore=json_data.get("Logstore"),
            Project=json_data.get("Project"),
        )


# work around possible type aliasing issues when variable has same name as a model
_LogConfigDefinition = LogConfigDefinition


@dataclass
class NasConfigDefinition(BaseModel):
    GroupId: Optional[float]
    UserId: Optional[float]
    MountPoints: Optional[Sequence["_MountPointsDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_NasConfigDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_NasConfigDefinition"]:
        if not json_data:
            return None
        return cls(
            GroupId=json_data.get("GroupId"),
            UserId=json_data.get("UserId"),
            MountPoints=deserialize_list(json_data.get("MountPoints"), MountPointsDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_NasConfigDefinition = NasConfigDefinition


@dataclass
class MountPointsDefinition(BaseModel):
    MountDir: Optional[str]
    ServerAddr: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_MountPointsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_MountPointsDefinition"]:
        if not json_data:
            return None
        return cls(
            MountDir=json_data.get("MountDir"),
            ServerAddr=json_data.get("ServerAddr"),
        )


# work around possible type aliasing issues when variable has same name as a model
_MountPointsDefinition = MountPointsDefinition


@dataclass
class VpcConfigDefinition(BaseModel):
    SecurityGroupId: Optional[str]
    VswitchIds: Optional[Sequence[str]]

    @classmethod
    def _deserialize(
        cls: Type["_VpcConfigDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_VpcConfigDefinition"]:
        if not json_data:
            return None
        return cls(
            SecurityGroupId=json_data.get("SecurityGroupId"),
            VswitchIds=json_data.get("VswitchIds"),
        )


# work around possible type aliasing issues when variable has same name as a model
_VpcConfigDefinition = VpcConfigDefinition


