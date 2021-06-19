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
    Id: Optional[str]
    ImageTagMutability: Optional[str]
    Name: Optional[str]
    RegistryId: Optional[str]
    RepositoryUrl: Optional[str]
    Tags: Optional[Sequence["_TagsDefinition"]]
    TagsAll: Optional[Sequence["_TagsAllDefinition"]]
    EncryptionConfiguration: Optional[Sequence["_EncryptionConfigurationDefinition"]]
    ImageScanningConfiguration: Optional[Sequence["_ImageScanningConfigurationDefinition"]]
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
            Arn=json_data.get("Arn"),
            Id=json_data.get("Id"),
            ImageTagMutability=json_data.get("ImageTagMutability"),
            Name=json_data.get("Name"),
            RegistryId=json_data.get("RegistryId"),
            RepositoryUrl=json_data.get("RepositoryUrl"),
            Tags=deserialize_list(json_data.get("Tags"), TagsDefinition),
            TagsAll=deserialize_list(json_data.get("TagsAll"), TagsAllDefinition),
            EncryptionConfiguration=deserialize_list(json_data.get("EncryptionConfiguration"), EncryptionConfigurationDefinition),
            ImageScanningConfiguration=deserialize_list(json_data.get("ImageScanningConfiguration"), ImageScanningConfigurationDefinition),
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
class EncryptionConfigurationDefinition(BaseModel):
    EncryptionType: Optional[str]
    KmsKey: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_EncryptionConfigurationDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_EncryptionConfigurationDefinition"]:
        if not json_data:
            return None
        return cls(
            EncryptionType=json_data.get("EncryptionType"),
            KmsKey=json_data.get("KmsKey"),
        )


# work around possible type aliasing issues when variable has same name as a model
_EncryptionConfigurationDefinition = EncryptionConfigurationDefinition


@dataclass
class ImageScanningConfigurationDefinition(BaseModel):
    ScanOnPush: Optional[bool]

    @classmethod
    def _deserialize(
        cls: Type["_ImageScanningConfigurationDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ImageScanningConfigurationDefinition"]:
        if not json_data:
            return None
        return cls(
            ScanOnPush=json_data.get("ScanOnPush"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ImageScanningConfigurationDefinition = ImageScanningConfigurationDefinition


@dataclass
class TimeoutsDefinition(BaseModel):
    Delete: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_TimeoutsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TimeoutsDefinition"]:
        if not json_data:
            return None
        return cls(
            Delete=json_data.get("Delete"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TimeoutsDefinition = TimeoutsDefinition


