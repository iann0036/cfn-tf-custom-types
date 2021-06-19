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
    ApplicationId: Optional[str]
    Arn: Optional[str]
    Id: Optional[str]
    Name: Optional[str]
    NamePrefix: Optional[str]
    Tags: Optional[Sequence["_TagsDefinition"]]
    TagsAll: Optional[Sequence["_TagsAllDefinition"]]
    CampaignHook: Optional[Sequence["_CampaignHookDefinition"]]
    Limits: Optional[Sequence["_LimitsDefinition"]]
    QuietTime: Optional[Sequence["_QuietTimeDefinition"]]

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
            ApplicationId=json_data.get("ApplicationId"),
            Arn=json_data.get("Arn"),
            Id=json_data.get("Id"),
            Name=json_data.get("Name"),
            NamePrefix=json_data.get("NamePrefix"),
            Tags=deserialize_list(json_data.get("Tags"), TagsDefinition),
            TagsAll=deserialize_list(json_data.get("TagsAll"), TagsAllDefinition),
            CampaignHook=deserialize_list(json_data.get("CampaignHook"), CampaignHookDefinition),
            Limits=deserialize_list(json_data.get("Limits"), LimitsDefinition),
            QuietTime=deserialize_list(json_data.get("QuietTime"), QuietTimeDefinition),
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
class CampaignHookDefinition(BaseModel):
    LambdaFunctionName: Optional[str]
    Mode: Optional[str]
    WebUrl: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_CampaignHookDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_CampaignHookDefinition"]:
        if not json_data:
            return None
        return cls(
            LambdaFunctionName=json_data.get("LambdaFunctionName"),
            Mode=json_data.get("Mode"),
            WebUrl=json_data.get("WebUrl"),
        )


# work around possible type aliasing issues when variable has same name as a model
_CampaignHookDefinition = CampaignHookDefinition


@dataclass
class LimitsDefinition(BaseModel):
    Daily: Optional[float]
    MaximumDuration: Optional[float]
    MessagesPerSecond: Optional[float]
    Total: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_LimitsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_LimitsDefinition"]:
        if not json_data:
            return None
        return cls(
            Daily=json_data.get("Daily"),
            MaximumDuration=json_data.get("MaximumDuration"),
            MessagesPerSecond=json_data.get("MessagesPerSecond"),
            Total=json_data.get("Total"),
        )


# work around possible type aliasing issues when variable has same name as a model
_LimitsDefinition = LimitsDefinition


@dataclass
class QuietTimeDefinition(BaseModel):
    End: Optional[str]
    Start: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_QuietTimeDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_QuietTimeDefinition"]:
        if not json_data:
            return None
        return cls(
            End=json_data.get("End"),
            Start=json_data.get("Start"),
        )


# work around possible type aliasing issues when variable has same name as a model
_QuietTimeDefinition = QuietTimeDefinition


