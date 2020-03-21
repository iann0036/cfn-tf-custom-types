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
    Tags: Optional[Sequence["_Tags"]]
    AppversionLifecycle: Optional[Sequence["_AppversionLifecycle"]]

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
            Tags=json_data.get("Tags"),
            AppversionLifecycle=json_data.get("AppversionLifecycle"),
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
class AppversionLifecycle:
    DeleteSourceFromS3: Optional[bool]
    MaxAgeInDays: Optional[float]
    MaxCount: Optional[float]
    ServiceRole: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_AppversionLifecycle"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AppversionLifecycle"]:
        if not json_data:
            return None
        return cls(
            DeleteSourceFromS3=json_data.get("DeleteSourceFromS3"),
            MaxAgeInDays=json_data.get("MaxAgeInDays"),
            MaxCount=json_data.get("MaxCount"),
            ServiceRole=json_data.get("ServiceRole"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AppversionLifecycle = AppversionLifecycle

