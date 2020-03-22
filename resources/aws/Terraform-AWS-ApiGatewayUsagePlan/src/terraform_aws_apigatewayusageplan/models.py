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
    Description: Optional[str]
    Id: Optional[str]
    Name: Optional[str]
    ProductCode: Optional[str]
    Tags: Optional[Sequence["_Tags"]]
    ApiStages: Optional[Sequence["_ApiStages"]]
    QuotaSettings: Optional[Sequence["_QuotaSettings"]]
    ThrottleSettings: Optional[Sequence["_ThrottleSettings"]]

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
            Description=json_data.get("Description"),
            Id=json_data.get("Id"),
            Name=json_data.get("Name"),
            ProductCode=json_data.get("ProductCode"),
            Tags=json_data.get("Tags"),
            ApiStages=json_data.get("ApiStages"),
            QuotaSettings=json_data.get("QuotaSettings"),
            ThrottleSettings=json_data.get("ThrottleSettings"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class Tags:
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Tags"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Tags"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Tags = Tags


@dataclass
class ApiStages:
    ApiId: Optional[str]
    Stage: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ApiStages"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ApiStages"]:
        if not json_data:
            return None
        return cls(
            ApiId=json_data.get("ApiId"),
            Stage=json_data.get("Stage"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ApiStages = ApiStages


@dataclass
class QuotaSettings:
    Limit: Optional[float]
    Offset: Optional[float]
    Period: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_QuotaSettings"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_QuotaSettings"]:
        if not json_data:
            return None
        return cls(
            Limit=json_data.get("Limit"),
            Offset=json_data.get("Offset"),
            Period=json_data.get("Period"),
        )


# work around possible type aliasing issues when variable has same name as a model
_QuotaSettings = QuotaSettings


@dataclass
class ThrottleSettings:
    BurstLimit: Optional[float]
    RateLimit: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_ThrottleSettings"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ThrottleSettings"]:
        if not json_data:
            return None
        return cls(
            BurstLimit=json_data.get("BurstLimit"),
            RateLimit=json_data.get("RateLimit"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ThrottleSettings = ThrottleSettings


