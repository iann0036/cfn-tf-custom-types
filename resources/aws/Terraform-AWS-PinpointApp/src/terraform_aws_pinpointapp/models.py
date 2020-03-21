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
    ApplicationId: Optional[str]
    Arn: Optional[str]
    Id: Optional[str]
    Name: Optional[str]
    NamePrefix: Optional[str]
    Tags: Optional[Sequence["_Tags"]]
    CampaignHook: Optional[Sequence["_CampaignHook"]]
    Limits: Optional[Sequence["_Limits"]]
    QuietTime: Optional[Sequence["_QuietTime"]]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceModel"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceModel"]:
        if not json_data:
            return None
        return cls(
            tfcfnid=json_data.get("tfcfnid"),
            ApplicationId=json_data.get("ApplicationId"),
            Arn=json_data.get("Arn"),
            Id=json_data.get("Id"),
            Name=json_data.get("Name"),
            NamePrefix=json_data.get("NamePrefix"),
            Tags=json_data.get("Tags"),
            CampaignHook=json_data.get("CampaignHook"),
            Limits=json_data.get("Limits"),
            QuietTime=json_data.get("QuietTime"),
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
class CampaignHook:
    LambdaFunctionName: Optional[str]
    Mode: Optional[str]
    WebUrl: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_CampaignHook"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_CampaignHook"]:
        if not json_data:
            return None
        return cls(
            LambdaFunctionName=json_data.get("LambdaFunctionName"),
            Mode=json_data.get("Mode"),
            WebUrl=json_data.get("WebUrl"),
        )


# work around possible type aliasing issues when variable has same name as a model
_CampaignHook = CampaignHook


@dataclass
class Limits:
    Daily: Optional[float]
    MaximumDuration: Optional[float]
    MessagesPerSecond: Optional[float]
    Total: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_Limits"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Limits"]:
        if not json_data:
            return None
        return cls(
            Daily=json_data.get("Daily"),
            MaximumDuration=json_data.get("MaximumDuration"),
            MessagesPerSecond=json_data.get("MessagesPerSecond"),
            Total=json_data.get("Total"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Limits = Limits


@dataclass
class QuietTime:
    End: Optional[str]
    Start: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_QuietTime"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_QuietTime"]:
        if not json_data:
            return None
        return cls(
            End=json_data.get("End"),
            Start=json_data.get("Start"),
        )


# work around possible type aliasing issues when variable has same name as a model
_QuietTime = QuietTime


