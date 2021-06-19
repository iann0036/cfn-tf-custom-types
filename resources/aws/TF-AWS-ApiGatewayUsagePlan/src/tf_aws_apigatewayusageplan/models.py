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
    Description: Optional[str]
    Id: Optional[str]
    Name: Optional[str]
    ProductCode: Optional[str]
    Tags: Optional[Sequence["_TagsDefinition"]]
    TagsAll: Optional[Sequence["_TagsAllDefinition"]]
    ApiStages: Optional[Sequence["_ApiStagesDefinition"]]
    QuotaSettings: Optional[Sequence["_QuotaSettingsDefinition"]]
    ThrottleSettings: Optional[Sequence["_ThrottleSettingsDefinition"]]

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
            Description=json_data.get("Description"),
            Id=json_data.get("Id"),
            Name=json_data.get("Name"),
            ProductCode=json_data.get("ProductCode"),
            Tags=deserialize_list(json_data.get("Tags"), TagsDefinition),
            TagsAll=deserialize_list(json_data.get("TagsAll"), TagsAllDefinition),
            ApiStages=deserialize_list(json_data.get("ApiStages"), ApiStagesDefinition),
            QuotaSettings=deserialize_list(json_data.get("QuotaSettings"), QuotaSettingsDefinition),
            ThrottleSettings=deserialize_list(json_data.get("ThrottleSettings"), ThrottleSettingsDefinition),
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
class ApiStagesDefinition(BaseModel):
    ApiId: Optional[str]
    Stage: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ApiStagesDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ApiStagesDefinition"]:
        if not json_data:
            return None
        return cls(
            ApiId=json_data.get("ApiId"),
            Stage=json_data.get("Stage"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ApiStagesDefinition = ApiStagesDefinition


@dataclass
class QuotaSettingsDefinition(BaseModel):
    Limit: Optional[float]
    Offset: Optional[float]
    Period: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_QuotaSettingsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_QuotaSettingsDefinition"]:
        if not json_data:
            return None
        return cls(
            Limit=json_data.get("Limit"),
            Offset=json_data.get("Offset"),
            Period=json_data.get("Period"),
        )


# work around possible type aliasing issues when variable has same name as a model
_QuotaSettingsDefinition = QuotaSettingsDefinition


@dataclass
class ThrottleSettingsDefinition(BaseModel):
    BurstLimit: Optional[float]
    RateLimit: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_ThrottleSettingsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ThrottleSettingsDefinition"]:
        if not json_data:
            return None
        return cls(
            BurstLimit=json_data.get("BurstLimit"),
            RateLimit=json_data.get("RateLimit"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ThrottleSettingsDefinition = ThrottleSettingsDefinition


