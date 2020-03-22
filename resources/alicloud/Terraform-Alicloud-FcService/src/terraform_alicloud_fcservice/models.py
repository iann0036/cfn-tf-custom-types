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
    Description: Optional[str]
    Id: Optional[str]
    InternetAccess: Optional[bool]
    LastModified: Optional[str]
    Name: Optional[str]
    NamePrefix: Optional[str]
    Role: Optional[str]
    ServiceId: Optional[str]
    LogConfig: Optional[Sequence["_LogConfig"]]
    VpcConfig: Optional[Sequence["_VpcConfig"]]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceModel"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceModel"]:
        if not json_data:
            return None
        return cls(
            tfcfnid=json_data.get("tfcfnid"),
            Description=json_data.get("Description"),
            Id=json_data.get("Id"),
            InternetAccess=json_data.get("InternetAccess"),
            LastModified=json_data.get("LastModified"),
            Name=json_data.get("Name"),
            NamePrefix=json_data.get("NamePrefix"),
            Role=json_data.get("Role"),
            ServiceId=json_data.get("ServiceId"),
            LogConfig=json_data.get("LogConfig"),
            VpcConfig=json_data.get("VpcConfig"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class LogConfig:
    Logstore: Optional[str]
    Project: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_LogConfig"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_LogConfig"]:
        if not json_data:
            return None
        return cls(
            Logstore=json_data.get("Logstore"),
            Project=json_data.get("Project"),
        )


# work around possible type aliasing issues when variable has same name as a model
_LogConfig = LogConfig


@dataclass
class VpcConfig:
    SecurityGroupId: Optional[str]
    VswitchIds: Optional[Sequence[str]]

    @classmethod
    def _deserialize(
        cls: Type["_VpcConfig"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_VpcConfig"]:
        if not json_data:
            return None
        return cls(
            SecurityGroupId=json_data.get("SecurityGroupId"),
            VswitchIds=json_data.get("VswitchIds"),
        )


# work around possible type aliasing issues when variable has same name as a model
_VpcConfig = VpcConfig


