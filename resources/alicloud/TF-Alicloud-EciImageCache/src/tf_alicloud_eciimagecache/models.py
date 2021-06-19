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
    ContainerGroupId: Optional[str]
    EipInstanceId: Optional[str]
    Id: Optional[str]
    ImageCacheName: Optional[str]
    ImageCacheSize: Optional[float]
    Images: Optional[Sequence[str]]
    ResourceGroupId: Optional[str]
    RetentionDays: Optional[float]
    SecurityGroupId: Optional[str]
    Status: Optional[str]
    VswitchId: Optional[str]
    ZoneId: Optional[str]
    ImageRegistryCredential: Optional[Sequence["_ImageRegistryCredentialDefinition"]]
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
            ContainerGroupId=json_data.get("ContainerGroupId"),
            EipInstanceId=json_data.get("EipInstanceId"),
            Id=json_data.get("Id"),
            ImageCacheName=json_data.get("ImageCacheName"),
            ImageCacheSize=json_data.get("ImageCacheSize"),
            Images=json_data.get("Images"),
            ResourceGroupId=json_data.get("ResourceGroupId"),
            RetentionDays=json_data.get("RetentionDays"),
            SecurityGroupId=json_data.get("SecurityGroupId"),
            Status=json_data.get("Status"),
            VswitchId=json_data.get("VswitchId"),
            ZoneId=json_data.get("ZoneId"),
            ImageRegistryCredential=deserialize_list(json_data.get("ImageRegistryCredential"), ImageRegistryCredentialDefinition),
            Timeouts=TimeoutsDefinition._deserialize(json_data.get("Timeouts")),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class ImageRegistryCredentialDefinition(BaseModel):
    Password: Optional[str]
    Server: Optional[str]
    UserName: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ImageRegistryCredentialDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ImageRegistryCredentialDefinition"]:
        if not json_data:
            return None
        return cls(
            Password=json_data.get("Password"),
            Server=json_data.get("Server"),
            UserName=json_data.get("UserName"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ImageRegistryCredentialDefinition = ImageRegistryCredentialDefinition


@dataclass
class TimeoutsDefinition(BaseModel):
    Create: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_TimeoutsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TimeoutsDefinition"]:
        if not json_data:
            return None
        return cls(
            Create=json_data.get("Create"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TimeoutsDefinition = TimeoutsDefinition


