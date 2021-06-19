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
    Arn: Optional[str]
    AwsKmsKeyArn: Optional[str]
    Id: Optional[str]
    InputBucket: Optional[str]
    Name: Optional[str]
    OutputBucket: Optional[str]
    Role: Optional[str]
    ContentConfig: Optional[Sequence["_ContentConfigDefinition"]]
    ContentConfigPermissions: Optional[Sequence["_ContentConfigPermissionsDefinition"]]
    Notifications: Optional[Sequence["_NotificationsDefinition"]]
    ThumbnailConfig: Optional[Sequence["_ThumbnailConfigDefinition"]]
    ThumbnailConfigPermissions: Optional[Sequence["_ThumbnailConfigPermissionsDefinition"]]

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
            Arn=json_data.get("Arn"),
            AwsKmsKeyArn=json_data.get("AwsKmsKeyArn"),
            Id=json_data.get("Id"),
            InputBucket=json_data.get("InputBucket"),
            Name=json_data.get("Name"),
            OutputBucket=json_data.get("OutputBucket"),
            Role=json_data.get("Role"),
            ContentConfig=deserialize_list(json_data.get("ContentConfig"), ContentConfigDefinition),
            ContentConfigPermissions=deserialize_list(json_data.get("ContentConfigPermissions"), ContentConfigPermissionsDefinition),
            Notifications=deserialize_list(json_data.get("Notifications"), NotificationsDefinition),
            ThumbnailConfig=deserialize_list(json_data.get("ThumbnailConfig"), ThumbnailConfigDefinition),
            ThumbnailConfigPermissions=deserialize_list(json_data.get("ThumbnailConfigPermissions"), ThumbnailConfigPermissionsDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class ContentConfigDefinition(BaseModel):
    Bucket: Optional[str]
    StorageClass: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ContentConfigDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ContentConfigDefinition"]:
        if not json_data:
            return None
        return cls(
            Bucket=json_data.get("Bucket"),
            StorageClass=json_data.get("StorageClass"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ContentConfigDefinition = ContentConfigDefinition


@dataclass
class ContentConfigPermissionsDefinition(BaseModel):
    Access: Optional[Sequence[str]]
    Grantee: Optional[str]
    GranteeType: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ContentConfigPermissionsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ContentConfigPermissionsDefinition"]:
        if not json_data:
            return None
        return cls(
            Access=json_data.get("Access"),
            Grantee=json_data.get("Grantee"),
            GranteeType=json_data.get("GranteeType"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ContentConfigPermissionsDefinition = ContentConfigPermissionsDefinition


@dataclass
class NotificationsDefinition(BaseModel):
    Completed: Optional[str]
    Error: Optional[str]
    Progressing: Optional[str]
    Warning: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_NotificationsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_NotificationsDefinition"]:
        if not json_data:
            return None
        return cls(
            Completed=json_data.get("Completed"),
            Error=json_data.get("Error"),
            Progressing=json_data.get("Progressing"),
            Warning=json_data.get("Warning"),
        )


# work around possible type aliasing issues when variable has same name as a model
_NotificationsDefinition = NotificationsDefinition


@dataclass
class ThumbnailConfigDefinition(BaseModel):
    Bucket: Optional[str]
    StorageClass: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ThumbnailConfigDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ThumbnailConfigDefinition"]:
        if not json_data:
            return None
        return cls(
            Bucket=json_data.get("Bucket"),
            StorageClass=json_data.get("StorageClass"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ThumbnailConfigDefinition = ThumbnailConfigDefinition


@dataclass
class ThumbnailConfigPermissionsDefinition(BaseModel):
    Access: Optional[Sequence[str]]
    Grantee: Optional[str]
    GranteeType: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ThumbnailConfigPermissionsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ThumbnailConfigPermissionsDefinition"]:
        if not json_data:
            return None
        return cls(
            Access=json_data.get("Access"),
            Grantee=json_data.get("Grantee"),
            GranteeType=json_data.get("GranteeType"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ThumbnailConfigPermissionsDefinition = ThumbnailConfigPermissionsDefinition


