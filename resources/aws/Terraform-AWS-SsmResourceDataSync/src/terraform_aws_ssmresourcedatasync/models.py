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
    Name: Optional[str]
    S3Destination: Optional[Sequence["_S3Destination"]]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceModel"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceModel"]:
        if not json_data:
            return None
        return cls(
            tfcfnid=json_data.get("tfcfnid"),
            Name=json_data.get("Name"),
            S3Destination=json_data.get("S3Destination"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class S3Destination:
    BucketName: Optional[str]
    KmsKeyArn: Optional[str]
    Prefix: Optional[str]
    Region: Optional[str]
    SyncFormat: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_S3Destination"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_S3Destination"]:
        if not json_data:
            return None
        return cls(
            BucketName=json_data.get("BucketName"),
            KmsKeyArn=json_data.get("KmsKeyArn"),
            Prefix=json_data.get("Prefix"),
            Region=json_data.get("Region"),
            SyncFormat=json_data.get("SyncFormat"),
        )


# work around possible type aliasing issues when variable has same name as a model
_S3Destination = S3Destination


