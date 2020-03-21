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
    ImageTagMutability: Optional[str]
    Name: Optional[str]
    RegistryId: Optional[str]
    RepositoryUrl: Optional[str]
    Tags: Optional[Sequence["_Tags"]]
    ImageScanningConfiguration: Optional[Sequence["_ImageScanningConfiguration"]]
    Timeouts: Optional["_Timeouts"]

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
            ImageTagMutability=json_data.get("ImageTagMutability"),
            Name=json_data.get("Name"),
            RegistryId=json_data.get("RegistryId"),
            RepositoryUrl=json_data.get("RepositoryUrl"),
            Tags=json_data.get("Tags"),
            ImageScanningConfiguration=json_data.get("ImageScanningConfiguration"),
            Timeouts=Timeouts._deserialize(json_data.get("Timeouts")),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class Tags:
    Key: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Tags"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Tags"]:
        if not json_data:
            return None
        return cls(
            Key=json_data.get("Key"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Tags = Tags


@dataclass
class ImageScanningConfiguration:
    ScanOnPush: Optional[bool]

    @classmethod
    def _deserialize(
        cls: Type["_ImageScanningConfiguration"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ImageScanningConfiguration"]:
        if not json_data:
            return None
        return cls(
            ScanOnPush=json_data.get("ScanOnPush"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ImageScanningConfiguration = ImageScanningConfiguration


@dataclass
class Timeouts:
    Delete: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Timeouts"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Timeouts"]:
        if not json_data:
            return None
        return cls(
            Delete=json_data.get("Delete"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Timeouts = Timeouts


