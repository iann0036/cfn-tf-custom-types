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
    Id: Optional[str]
    Name: Optional[str]
    EncryptionConfiguration: Optional[Sequence["_EncryptionConfiguration"]]
    CloudwatchEncryption: Optional[Sequence["_CloudwatchEncryption"]]
    JobBookmarksEncryption: Optional[Sequence["_JobBookmarksEncryption"]]
    S3Encryption: Optional[Sequence["_S3Encryption"]]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceModel"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceModel"]:
        if not json_data:
            return None
        return cls(
            tfcfnid=json_data.get("tfcfnid"),
            Id=json_data.get("Id"),
            Name=json_data.get("Name"),
            EncryptionConfiguration=json_data.get("EncryptionConfiguration"),
            CloudwatchEncryption=json_data.get("CloudwatchEncryption"),
            JobBookmarksEncryption=json_data.get("JobBookmarksEncryption"),
            S3Encryption=json_data.get("S3Encryption"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class EncryptionConfiguration:
    CloudwatchEncryption: Optional[Sequence["_CloudwatchEncryption"]]
    JobBookmarksEncryption: Optional[Sequence["_JobBookmarksEncryption"]]
    S3Encryption: Optional[Sequence["_S3Encryption"]]

    @classmethod
    def _deserialize(
        cls: Type["_EncryptionConfiguration"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_EncryptionConfiguration"]:
        if not json_data:
            return None
        return cls(
            CloudwatchEncryption=json_data.get("CloudwatchEncryption"),
            JobBookmarksEncryption=json_data.get("JobBookmarksEncryption"),
            S3Encryption=json_data.get("S3Encryption"),
        )


# work around possible type aliasing issues when variable has same name as a model
_EncryptionConfiguration = EncryptionConfiguration


@dataclass
class CloudwatchEncryption:
    CloudwatchEncryptionMode: Optional[str]
    KmsKeyArn: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_CloudwatchEncryption"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_CloudwatchEncryption"]:
        if not json_data:
            return None
        return cls(
            CloudwatchEncryptionMode=json_data.get("CloudwatchEncryptionMode"),
            KmsKeyArn=json_data.get("KmsKeyArn"),
        )


# work around possible type aliasing issues when variable has same name as a model
_CloudwatchEncryption = CloudwatchEncryption


@dataclass
class JobBookmarksEncryption:
    JobBookmarksEncryptionMode: Optional[str]
    KmsKeyArn: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_JobBookmarksEncryption"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_JobBookmarksEncryption"]:
        if not json_data:
            return None
        return cls(
            JobBookmarksEncryptionMode=json_data.get("JobBookmarksEncryptionMode"),
            KmsKeyArn=json_data.get("KmsKeyArn"),
        )


# work around possible type aliasing issues when variable has same name as a model
_JobBookmarksEncryption = JobBookmarksEncryption


@dataclass
class S3Encryption:
    KmsKeyArn: Optional[str]
    S3EncryptionMode: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_S3Encryption"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_S3Encryption"]:
        if not json_data:
            return None
        return cls(
            KmsKeyArn=json_data.get("KmsKeyArn"),
            S3EncryptionMode=json_data.get("S3EncryptionMode"),
        )


# work around possible type aliasing issues when variable has same name as a model
_S3Encryption = S3Encryption


