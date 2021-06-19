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
    AccessBasedEnumeration: Optional[bool]
    AdminUserList: Optional[Sequence[str]]
    Arn: Optional[str]
    AuditDestinationArn: Optional[str]
    Authentication: Optional[str]
    CaseSensitivity: Optional[str]
    DefaultStorageClass: Optional[str]
    FileShareName: Optional[str]
    FileshareId: Optional[str]
    GatewayArn: Optional[str]
    GuessMimeTypeEnabled: Optional[bool]
    Id: Optional[str]
    InvalidUserList: Optional[Sequence[str]]
    KmsEncrypted: Optional[bool]
    KmsKeyArn: Optional[str]
    LocationArn: Optional[str]
    NotificationPolicy: Optional[str]
    ObjectAcl: Optional[str]
    Path: Optional[str]
    ReadOnly: Optional[bool]
    RequesterPays: Optional[bool]
    RoleArn: Optional[str]
    SmbAclEnabled: Optional[bool]
    Tags: Optional[Sequence["_TagsDefinition"]]
    TagsAll: Optional[Sequence["_TagsAllDefinition"]]
    ValidUserList: Optional[Sequence[str]]
    CacheAttributes: Optional[Sequence["_CacheAttributesDefinition"]]
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
            AccessBasedEnumeration=json_data.get("AccessBasedEnumeration"),
            AdminUserList=json_data.get("AdminUserList"),
            Arn=json_data.get("Arn"),
            AuditDestinationArn=json_data.get("AuditDestinationArn"),
            Authentication=json_data.get("Authentication"),
            CaseSensitivity=json_data.get("CaseSensitivity"),
            DefaultStorageClass=json_data.get("DefaultStorageClass"),
            FileShareName=json_data.get("FileShareName"),
            FileshareId=json_data.get("FileshareId"),
            GatewayArn=json_data.get("GatewayArn"),
            GuessMimeTypeEnabled=json_data.get("GuessMimeTypeEnabled"),
            Id=json_data.get("Id"),
            InvalidUserList=json_data.get("InvalidUserList"),
            KmsEncrypted=json_data.get("KmsEncrypted"),
            KmsKeyArn=json_data.get("KmsKeyArn"),
            LocationArn=json_data.get("LocationArn"),
            NotificationPolicy=json_data.get("NotificationPolicy"),
            ObjectAcl=json_data.get("ObjectAcl"),
            Path=json_data.get("Path"),
            ReadOnly=json_data.get("ReadOnly"),
            RequesterPays=json_data.get("RequesterPays"),
            RoleArn=json_data.get("RoleArn"),
            SmbAclEnabled=json_data.get("SmbAclEnabled"),
            Tags=deserialize_list(json_data.get("Tags"), TagsDefinition),
            TagsAll=deserialize_list(json_data.get("TagsAll"), TagsAllDefinition),
            ValidUserList=json_data.get("ValidUserList"),
            CacheAttributes=deserialize_list(json_data.get("CacheAttributes"), CacheAttributesDefinition),
            Timeouts=TimeoutsDefinition._deserialize(json_data.get("Timeouts")),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class TagsDefinition(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_TagsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TagsDefinition"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TagsDefinition = TagsDefinition


@dataclass
class TagsAllDefinition(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_TagsAllDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TagsAllDefinition"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TagsAllDefinition = TagsAllDefinition


@dataclass
class CacheAttributesDefinition(BaseModel):
    CacheStaleTimeoutInSeconds: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_CacheAttributesDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_CacheAttributesDefinition"]:
        if not json_data:
            return None
        return cls(
            CacheStaleTimeoutInSeconds=json_data.get("CacheStaleTimeoutInSeconds"),
        )


# work around possible type aliasing issues when variable has same name as a model
_CacheAttributesDefinition = CacheAttributesDefinition


@dataclass
class TimeoutsDefinition(BaseModel):
    Create: Optional[str]
    Delete: Optional[str]
    Update: Optional[str]

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
            Update=json_data.get("Update"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TimeoutsDefinition = TimeoutsDefinition


