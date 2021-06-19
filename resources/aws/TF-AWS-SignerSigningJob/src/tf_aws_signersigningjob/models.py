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
    CompletedAt: Optional[str]
    CreatedAt: Optional[str]
    Id: Optional[str]
    IgnoreSigningJobFailure: Optional[bool]
    JobId: Optional[str]
    JobInvoker: Optional[str]
    JobOwner: Optional[str]
    PlatformDisplayName: Optional[str]
    PlatformId: Optional[str]
    ProfileName: Optional[str]
    ProfileVersion: Optional[str]
    RequestedBy: Optional[str]
    RevocationRecord: Optional[Sequence["_RevocationRecordDefinition"]]
    SignatureExpiresAt: Optional[str]
    SignedObject: Optional[Sequence["_SignedObjectDefinition2"]]
    Status: Optional[str]
    StatusReason: Optional[str]
    Destination: Optional[Sequence["_DestinationDefinition"]]
    Source: Optional[Sequence["_SourceDefinition"]]

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
            CompletedAt=json_data.get("CompletedAt"),
            CreatedAt=json_data.get("CreatedAt"),
            Id=json_data.get("Id"),
            IgnoreSigningJobFailure=json_data.get("IgnoreSigningJobFailure"),
            JobId=json_data.get("JobId"),
            JobInvoker=json_data.get("JobInvoker"),
            JobOwner=json_data.get("JobOwner"),
            PlatformDisplayName=json_data.get("PlatformDisplayName"),
            PlatformId=json_data.get("PlatformId"),
            ProfileName=json_data.get("ProfileName"),
            ProfileVersion=json_data.get("ProfileVersion"),
            RequestedBy=json_data.get("RequestedBy"),
            RevocationRecord=deserialize_list(json_data.get("RevocationRecord"), RevocationRecordDefinition),
            SignatureExpiresAt=json_data.get("SignatureExpiresAt"),
            SignedObject=deserialize_list(json_data.get("SignedObject"), SignedObjectDefinition2),
            Status=json_data.get("Status"),
            StatusReason=json_data.get("StatusReason"),
            Destination=deserialize_list(json_data.get("Destination"), DestinationDefinition),
            Source=deserialize_list(json_data.get("Source"), SourceDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class RevocationRecordDefinition(BaseModel):
    Reason: Optional[str]
    RevokedAt: Optional[str]
    RevokedBy: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_RevocationRecordDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_RevocationRecordDefinition"]:
        if not json_data:
            return None
        return cls(
            Reason=json_data.get("Reason"),
            RevokedAt=json_data.get("RevokedAt"),
            RevokedBy=json_data.get("RevokedBy"),
        )


# work around possible type aliasing issues when variable has same name as a model
_RevocationRecordDefinition = RevocationRecordDefinition


@dataclass
class SignedObjectDefinition2(BaseModel):
    S3: Optional[Sequence["_SignedObjectDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_SignedObjectDefinition2"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SignedObjectDefinition2"]:
        if not json_data:
            return None
        return cls(
            S3=deserialize_list(json_data.get("S3"), SignedObjectDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_SignedObjectDefinition2 = SignedObjectDefinition2


@dataclass
class SignedObjectDefinition(BaseModel):
    Bucket: Optional[str]
    Key: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_SignedObjectDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SignedObjectDefinition"]:
        if not json_data:
            return None
        return cls(
            Bucket=json_data.get("Bucket"),
            Key=json_data.get("Key"),
        )


# work around possible type aliasing issues when variable has same name as a model
_SignedObjectDefinition = SignedObjectDefinition


@dataclass
class DestinationDefinition(BaseModel):
    S3: Optional[Sequence["_S3Definition"]]

    @classmethod
    def _deserialize(
        cls: Type["_DestinationDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DestinationDefinition"]:
        if not json_data:
            return None
        return cls(
            S3=deserialize_list(json_data.get("S3"), S3Definition),
        )


# work around possible type aliasing issues when variable has same name as a model
_DestinationDefinition = DestinationDefinition


@dataclass
class S3Definition(BaseModel):
    Bucket: Optional[str]
    Key: Optional[str]
    Version: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_S3Definition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_S3Definition"]:
        if not json_data:
            return None
        return cls(
            Bucket=json_data.get("Bucket"),
            Key=json_data.get("Key"),
            Version=json_data.get("Version"),
        )


# work around possible type aliasing issues when variable has same name as a model
_S3Definition = S3Definition


@dataclass
class SourceDefinition(BaseModel):
    S3: Optional[Sequence["_S3Definition"]]

    @classmethod
    def _deserialize(
        cls: Type["_SourceDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SourceDefinition"]:
        if not json_data:
            return None
        return cls(
            S3=deserialize_list(json_data.get("S3"), S3Definition),
        )


# work around possible type aliasing issues when variable has same name as a model
_SourceDefinition = SourceDefinition


