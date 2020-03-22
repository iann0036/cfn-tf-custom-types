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
    EventDeliveryFailureTopicArn: Optional[str]
    EventEndpointCreatedTopicArn: Optional[str]
    EventEndpointDeletedTopicArn: Optional[str]
    EventEndpointUpdatedTopicArn: Optional[str]
    FailureFeedbackRoleArn: Optional[str]
    Id: Optional[str]
    Name: Optional[str]
    Platform: Optional[str]
    PlatformCredential: Optional[str]
    PlatformPrincipal: Optional[str]
    SuccessFeedbackRoleArn: Optional[str]
    SuccessFeedbackSampleRate: Optional[str]

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
            EventDeliveryFailureTopicArn=json_data.get("EventDeliveryFailureTopicArn"),
            EventEndpointCreatedTopicArn=json_data.get("EventEndpointCreatedTopicArn"),
            EventEndpointDeletedTopicArn=json_data.get("EventEndpointDeletedTopicArn"),
            EventEndpointUpdatedTopicArn=json_data.get("EventEndpointUpdatedTopicArn"),
            FailureFeedbackRoleArn=json_data.get("FailureFeedbackRoleArn"),
            Id=json_data.get("Id"),
            Name=json_data.get("Name"),
            Platform=json_data.get("Platform"),
            PlatformCredential=json_data.get("PlatformCredential"),
            PlatformPrincipal=json_data.get("PlatformPrincipal"),
            SuccessFeedbackRoleArn=json_data.get("SuccessFeedbackRoleArn"),
            SuccessFeedbackSampleRate=json_data.get("SuccessFeedbackSampleRate"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


