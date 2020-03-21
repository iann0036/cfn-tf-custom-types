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
    ContentBasedDeduplication: Optional[bool]
    DelaySeconds: Optional[float]
    FifoQueue: Optional[bool]
    Id: Optional[str]
    KmsDataKeyReusePeriodSeconds: Optional[float]
    KmsMasterKeyId: Optional[str]
    MaxMessageSize: Optional[float]
    MessageRetentionSeconds: Optional[float]
    Name: Optional[str]
    NamePrefix: Optional[str]
    Policy: Optional[str]
    ReceiveWaitTimeSeconds: Optional[float]
    RedrivePolicy: Optional[str]
    Tags: Optional[Sequence["_Tags"]]
    VisibilityTimeoutSeconds: Optional[float]

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
            ContentBasedDeduplication=json_data.get("ContentBasedDeduplication"),
            DelaySeconds=json_data.get("DelaySeconds"),
            FifoQueue=json_data.get("FifoQueue"),
            Id=json_data.get("Id"),
            KmsDataKeyReusePeriodSeconds=json_data.get("KmsDataKeyReusePeriodSeconds"),
            KmsMasterKeyId=json_data.get("KmsMasterKeyId"),
            MaxMessageSize=json_data.get("MaxMessageSize"),
            MessageRetentionSeconds=json_data.get("MessageRetentionSeconds"),
            Name=json_data.get("Name"),
            NamePrefix=json_data.get("NamePrefix"),
            Policy=json_data.get("Policy"),
            ReceiveWaitTimeSeconds=json_data.get("ReceiveWaitTimeSeconds"),
            RedrivePolicy=json_data.get("RedrivePolicy"),
            Tags=json_data.get("Tags"),
            VisibilityTimeoutSeconds=json_data.get("VisibilityTimeoutSeconds"),
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


