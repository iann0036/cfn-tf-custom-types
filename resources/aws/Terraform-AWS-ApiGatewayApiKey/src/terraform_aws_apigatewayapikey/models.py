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
    CreatedDate: Optional[str]
    Description: Optional[str]
    Enabled: Optional[bool]
    Id: Optional[str]
    LastUpdatedDate: Optional[str]
    Name: Optional[str]
    Tags: Optional[Sequence["_Tags"]]
    Value: Optional[str]
    StageKey: Optional[Sequence["_StageKey"]]

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
            CreatedDate=json_data.get("CreatedDate"),
            Description=json_data.get("Description"),
            Enabled=json_data.get("Enabled"),
            Id=json_data.get("Id"),
            LastUpdatedDate=json_data.get("LastUpdatedDate"),
            Name=json_data.get("Name"),
            Tags=json_data.get("Tags"),
            Value=json_data.get("Value"),
            StageKey=json_data.get("StageKey"),
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
class StageKey:
    RestApiId: Optional[str]
    StageName: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_StageKey"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_StageKey"]:
        if not json_data:
            return None
        return cls(
            RestApiId=json_data.get("RestApiId"),
            StageName=json_data.get("StageName"),
        )


# work around possible type aliasing issues when variable has same name as a model
_StageKey = StageKey


