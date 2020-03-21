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
    Arn: Optional[str]
    AwsKmsKeyArn: Optional[str]
    InputBucket: Optional[str]
    Name: Optional[str]
    OutputBucket: Optional[str]
    Role: Optional[str]
    ContentConfig: Optional[Sequence["_ContentConfig"]]
    ContentConfigPermissions: Optional[Sequence["_ContentConfigPermissions"]]
    Notifications: Optional[Sequence["_Notifications"]]
    ThumbnailConfig: Optional[Sequence["_ThumbnailConfig"]]
    ThumbnailConfigPermissions: Optional[Sequence["_ThumbnailConfigPermissions"]]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceModel"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceModel"]:
        if not json_data:
            return None
        return cls(
            tfcfnid=json_data.get("tfcfnid"),
            Arn=json_data.get("Arn"),
            AwsKmsKeyArn=json_data.get("AwsKmsKeyArn"),
            InputBucket=json_data.get("InputBucket"),
            Name=json_data.get("Name"),
            OutputBucket=json_data.get("OutputBucket"),
            Role=json_data.get("Role"),
            ContentConfig=json_data.get("ContentConfig"),
            ContentConfigPermissions=json_data.get("ContentConfigPermissions"),
            Notifications=json_data.get("Notifications"),
            ThumbnailConfig=json_data.get("ThumbnailConfig"),
            ThumbnailConfigPermissions=json_data.get("ThumbnailConfigPermissions"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class ContentConfig:
    Bucket: Optional[str]
    StorageClass: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ContentConfig"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ContentConfig"]:
        if not json_data:
            return None
        return cls(
            Bucket=json_data.get("Bucket"),
            StorageClass=json_data.get("StorageClass"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ContentConfig = ContentConfig


@dataclass
class ContentConfigPermissions:
    Access: Optional[Sequence[str]]
    Grantee: Optional[str]
    GranteeType: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ContentConfigPermissions"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ContentConfigPermissions"]:
        if not json_data:
            return None
        return cls(
            Access=json_data.get("Access"),
            Grantee=json_data.get("Grantee"),
            GranteeType=json_data.get("GranteeType"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ContentConfigPermissions = ContentConfigPermissions


@dataclass
class Notifications:
    Completed: Optional[str]
    Error: Optional[str]
    Progressing: Optional[str]
    Warning: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Notifications"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Notifications"]:
        if not json_data:
            return None
        return cls(
            Completed=json_data.get("Completed"),
            Error=json_data.get("Error"),
            Progressing=json_data.get("Progressing"),
            Warning=json_data.get("Warning"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Notifications = Notifications


@dataclass
class ThumbnailConfig:
    Bucket: Optional[str]
    StorageClass: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ThumbnailConfig"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ThumbnailConfig"]:
        if not json_data:
            return None
        return cls(
            Bucket=json_data.get("Bucket"),
            StorageClass=json_data.get("StorageClass"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ThumbnailConfig = ThumbnailConfig


@dataclass
class ThumbnailConfigPermissions:
    Access: Optional[Sequence[str]]
    Grantee: Optional[str]
    GranteeType: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ThumbnailConfigPermissions"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ThumbnailConfigPermissions"]:
        if not json_data:
            return None
        return cls(
            Access=json_data.get("Access"),
            Grantee=json_data.get("Grantee"),
            GranteeType=json_data.get("GranteeType"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ThumbnailConfigPermissions = ThumbnailConfigPermissions


