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
    AllowUnassociatedTargets: Optional[bool]
    Cutoff: Optional[float]
    Description: Optional[str]
    Duration: Optional[float]
    Enabled: Optional[bool]
    EndDate: Optional[str]
    Id: Optional[str]
    Name: Optional[str]
    Schedule: Optional[str]
    ScheduleTimezone: Optional[str]
    StartDate: Optional[str]
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
            AllowUnassociatedTargets=json_data.get("AllowUnassociatedTargets"),
            Cutoff=json_data.get("Cutoff"),
            Description=json_data.get("Description"),
            Duration=json_data.get("Duration"),
            Enabled=json_data.get("Enabled"),
            EndDate=json_data.get("EndDate"),
            Id=json_data.get("Id"),
            Name=json_data.get("Name"),
            Schedule=json_data.get("Schedule"),
            ScheduleTimezone=json_data.get("ScheduleTimezone"),
            StartDate=json_data.get("StartDate"),
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


