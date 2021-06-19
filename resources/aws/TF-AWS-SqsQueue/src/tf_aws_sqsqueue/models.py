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
    ContentBasedDeduplication: Optional[bool]
    DeduplicationScope: Optional[str]
    DelaySeconds: Optional[float]
    FifoQueue: Optional[bool]
    FifoThroughputLimit: Optional[str]
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
    Tags: Optional[Sequence["_TagsDefinition"]]
    TagsAll: Optional[Sequence["_TagsAllDefinition"]]
    Url: Optional[str]
    VisibilityTimeoutSeconds: Optional[float]

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
            ContentBasedDeduplication=json_data.get("ContentBasedDeduplication"),
            DeduplicationScope=json_data.get("DeduplicationScope"),
            DelaySeconds=json_data.get("DelaySeconds"),
            FifoQueue=json_data.get("FifoQueue"),
            FifoThroughputLimit=json_data.get("FifoThroughputLimit"),
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
            Tags=deserialize_list(json_data.get("Tags"), TagsDefinition),
            TagsAll=deserialize_list(json_data.get("TagsAll"), TagsAllDefinition),
            Url=json_data.get("Url"),
            VisibilityTimeoutSeconds=json_data.get("VisibilityTimeoutSeconds"),
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


