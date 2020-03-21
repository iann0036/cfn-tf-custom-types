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
    S3BucketName: Optional[str]
    S3KeyPrefix: Optional[str]
    SnsTopicArn: Optional[str]
    SnapshotDeliveryProperties: Optional[Sequence["_SnapshotDeliveryProperties"]]

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
            S3BucketName=json_data.get("S3BucketName"),
            S3KeyPrefix=json_data.get("S3KeyPrefix"),
            SnsTopicArn=json_data.get("SnsTopicArn"),
            SnapshotDeliveryProperties=json_data.get("SnapshotDeliveryProperties"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class SnapshotDeliveryProperties:
    DeliveryFrequency: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_SnapshotDeliveryProperties"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SnapshotDeliveryProperties"]:
        if not json_data:
            return None
        return cls(
            DeliveryFrequency=json_data.get("DeliveryFrequency"),
        )


# work around possible type aliasing issues when variable has same name as a model
_SnapshotDeliveryProperties = SnapshotDeliveryProperties


