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
    Id: Optional[str]
    Name: Optional[str]
    EncryptionConfiguration: Optional[Sequence["_EncryptionConfigurationDefinition"]]

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
            Id=json_data.get("Id"),
            Name=json_data.get("Name"),
            EncryptionConfiguration=deserialize_list(json_data.get("EncryptionConfiguration"), EncryptionConfigurationDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class EncryptionConfigurationDefinition(BaseModel):
    CloudwatchEncryption: Optional[Sequence["_CloudwatchEncryptionDefinition"]]
    JobBookmarksEncryption: Optional[Sequence["_JobBookmarksEncryptionDefinition"]]
    S3Encryption: Optional[Sequence["_S3EncryptionDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_EncryptionConfigurationDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_EncryptionConfigurationDefinition"]:
        if not json_data:
            return None
        return cls(
            CloudwatchEncryption=deserialize_list(json_data.get("CloudwatchEncryption"), CloudwatchEncryptionDefinition),
            JobBookmarksEncryption=deserialize_list(json_data.get("JobBookmarksEncryption"), JobBookmarksEncryptionDefinition),
            S3Encryption=deserialize_list(json_data.get("S3Encryption"), S3EncryptionDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_EncryptionConfigurationDefinition = EncryptionConfigurationDefinition


@dataclass
class CloudwatchEncryptionDefinition(BaseModel):
    CloudwatchEncryptionMode: Optional[str]
    KmsKeyArn: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_CloudwatchEncryptionDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_CloudwatchEncryptionDefinition"]:
        if not json_data:
            return None
        return cls(
            CloudwatchEncryptionMode=json_data.get("CloudwatchEncryptionMode"),
            KmsKeyArn=json_data.get("KmsKeyArn"),
        )


# work around possible type aliasing issues when variable has same name as a model
_CloudwatchEncryptionDefinition = CloudwatchEncryptionDefinition


@dataclass
class JobBookmarksEncryptionDefinition(BaseModel):
    JobBookmarksEncryptionMode: Optional[str]
    KmsKeyArn: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_JobBookmarksEncryptionDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_JobBookmarksEncryptionDefinition"]:
        if not json_data:
            return None
        return cls(
            JobBookmarksEncryptionMode=json_data.get("JobBookmarksEncryptionMode"),
            KmsKeyArn=json_data.get("KmsKeyArn"),
        )


# work around possible type aliasing issues when variable has same name as a model
_JobBookmarksEncryptionDefinition = JobBookmarksEncryptionDefinition


@dataclass
class S3EncryptionDefinition(BaseModel):
    KmsKeyArn: Optional[str]
    S3EncryptionMode: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_S3EncryptionDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_S3EncryptionDefinition"]:
        if not json_data:
            return None
        return cls(
            KmsKeyArn=json_data.get("KmsKeyArn"),
            S3EncryptionMode=json_data.get("S3EncryptionMode"),
        )


# work around possible type aliasing issues when variable has same name as a model
_S3EncryptionDefinition = S3EncryptionDefinition


