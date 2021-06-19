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
    ApplicationFailureFeedbackRoleArn: Optional[str]
    ApplicationSuccessFeedbackRoleArn: Optional[str]
    ApplicationSuccessFeedbackSampleRate: Optional[float]
    Arn: Optional[str]
    ContentBasedDeduplication: Optional[bool]
    DeliveryPolicy: Optional[str]
    DisplayName: Optional[str]
    FifoTopic: Optional[bool]
    FirehoseFailureFeedbackRoleArn: Optional[str]
    FirehoseSuccessFeedbackRoleArn: Optional[str]
    FirehoseSuccessFeedbackSampleRate: Optional[float]
    HttpFailureFeedbackRoleArn: Optional[str]
    HttpSuccessFeedbackRoleArn: Optional[str]
    HttpSuccessFeedbackSampleRate: Optional[float]
    Id: Optional[str]
    KmsMasterKeyId: Optional[str]
    LambdaFailureFeedbackRoleArn: Optional[str]
    LambdaSuccessFeedbackRoleArn: Optional[str]
    LambdaSuccessFeedbackSampleRate: Optional[float]
    Name: Optional[str]
    NamePrefix: Optional[str]
    Owner: Optional[str]
    Policy: Optional[str]
    SqsFailureFeedbackRoleArn: Optional[str]
    SqsSuccessFeedbackRoleArn: Optional[str]
    SqsSuccessFeedbackSampleRate: Optional[float]
    Tags: Optional[Sequence["_TagsDefinition"]]
    TagsAll: Optional[Sequence["_TagsAllDefinition"]]

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
            ApplicationFailureFeedbackRoleArn=json_data.get("ApplicationFailureFeedbackRoleArn"),
            ApplicationSuccessFeedbackRoleArn=json_data.get("ApplicationSuccessFeedbackRoleArn"),
            ApplicationSuccessFeedbackSampleRate=json_data.get("ApplicationSuccessFeedbackSampleRate"),
            Arn=json_data.get("Arn"),
            ContentBasedDeduplication=json_data.get("ContentBasedDeduplication"),
            DeliveryPolicy=json_data.get("DeliveryPolicy"),
            DisplayName=json_data.get("DisplayName"),
            FifoTopic=json_data.get("FifoTopic"),
            FirehoseFailureFeedbackRoleArn=json_data.get("FirehoseFailureFeedbackRoleArn"),
            FirehoseSuccessFeedbackRoleArn=json_data.get("FirehoseSuccessFeedbackRoleArn"),
            FirehoseSuccessFeedbackSampleRate=json_data.get("FirehoseSuccessFeedbackSampleRate"),
            HttpFailureFeedbackRoleArn=json_data.get("HttpFailureFeedbackRoleArn"),
            HttpSuccessFeedbackRoleArn=json_data.get("HttpSuccessFeedbackRoleArn"),
            HttpSuccessFeedbackSampleRate=json_data.get("HttpSuccessFeedbackSampleRate"),
            Id=json_data.get("Id"),
            KmsMasterKeyId=json_data.get("KmsMasterKeyId"),
            LambdaFailureFeedbackRoleArn=json_data.get("LambdaFailureFeedbackRoleArn"),
            LambdaSuccessFeedbackRoleArn=json_data.get("LambdaSuccessFeedbackRoleArn"),
            LambdaSuccessFeedbackSampleRate=json_data.get("LambdaSuccessFeedbackSampleRate"),
            Name=json_data.get("Name"),
            NamePrefix=json_data.get("NamePrefix"),
            Owner=json_data.get("Owner"),
            Policy=json_data.get("Policy"),
            SqsFailureFeedbackRoleArn=json_data.get("SqsFailureFeedbackRoleArn"),
            SqsSuccessFeedbackRoleArn=json_data.get("SqsSuccessFeedbackRoleArn"),
            SqsSuccessFeedbackSampleRate=json_data.get("SqsSuccessFeedbackSampleRate"),
            Tags=deserialize_list(json_data.get("Tags"), TagsDefinition),
            TagsAll=deserialize_list(json_data.get("TagsAll"), TagsAllDefinition),
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


