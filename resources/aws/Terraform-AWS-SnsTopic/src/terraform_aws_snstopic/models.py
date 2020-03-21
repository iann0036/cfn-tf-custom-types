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
    ApplicationFailureFeedbackRoleArn: Optional[str]
    ApplicationSuccessFeedbackRoleArn: Optional[str]
    ApplicationSuccessFeedbackSampleRate: Optional[float]
    Arn: Optional[str]
    DeliveryPolicy: Optional[str]
    DisplayName: Optional[str]
    HttpFailureFeedbackRoleArn: Optional[str]
    HttpSuccessFeedbackRoleArn: Optional[str]
    HttpSuccessFeedbackSampleRate: Optional[float]
    KmsMasterKeyId: Optional[str]
    LambdaFailureFeedbackRoleArn: Optional[str]
    LambdaSuccessFeedbackRoleArn: Optional[str]
    LambdaSuccessFeedbackSampleRate: Optional[float]
    Name: Optional[str]
    NamePrefix: Optional[str]
    Policy: Optional[str]
    SqsFailureFeedbackRoleArn: Optional[str]
    SqsSuccessFeedbackRoleArn: Optional[str]
    SqsSuccessFeedbackSampleRate: Optional[float]
    Tags: Optional[Sequence["_Tags"]]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceModel"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceModel"]:
        if not json_data:
            return None
        return cls(
            tfcfnid=json_data.get("tfcfnid"),
            ApplicationFailureFeedbackRoleArn=json_data.get("ApplicationFailureFeedbackRoleArn"),
            ApplicationSuccessFeedbackRoleArn=json_data.get("ApplicationSuccessFeedbackRoleArn"),
            ApplicationSuccessFeedbackSampleRate=json_data.get("ApplicationSuccessFeedbackSampleRate"),
            Arn=json_data.get("Arn"),
            DeliveryPolicy=json_data.get("DeliveryPolicy"),
            DisplayName=json_data.get("DisplayName"),
            HttpFailureFeedbackRoleArn=json_data.get("HttpFailureFeedbackRoleArn"),
            HttpSuccessFeedbackRoleArn=json_data.get("HttpSuccessFeedbackRoleArn"),
            HttpSuccessFeedbackSampleRate=json_data.get("HttpSuccessFeedbackSampleRate"),
            KmsMasterKeyId=json_data.get("KmsMasterKeyId"),
            LambdaFailureFeedbackRoleArn=json_data.get("LambdaFailureFeedbackRoleArn"),
            LambdaSuccessFeedbackRoleArn=json_data.get("LambdaSuccessFeedbackRoleArn"),
            LambdaSuccessFeedbackSampleRate=json_data.get("LambdaSuccessFeedbackSampleRate"),
            Name=json_data.get("Name"),
            NamePrefix=json_data.get("NamePrefix"),
            Policy=json_data.get("Policy"),
            SqsFailureFeedbackRoleArn=json_data.get("SqsFailureFeedbackRoleArn"),
            SqsSuccessFeedbackRoleArn=json_data.get("SqsSuccessFeedbackRoleArn"),
            SqsSuccessFeedbackSampleRate=json_data.get("SqsSuccessFeedbackSampleRate"),
            Tags=json_data.get("Tags"),
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


