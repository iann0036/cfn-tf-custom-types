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
    CheckRegions: Optional[Sequence[str]]
    CreatedOn: Optional[str]
    Description: Optional[str]
    Enabled: Optional[bool]
    MinimumOrigins: Optional[float]
    ModifiedOn: Optional[str]
    Monitor: Optional[str]
    Name: Optional[str]
    NotificationEmail: Optional[str]
    Origins: Optional[Sequence["_Origins"]]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceModel"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceModel"]:
        if not json_data:
            return None
        return cls(
            tfcfnid=json_data.get("tfcfnid"),
            CheckRegions=json_data.get("CheckRegions"),
            CreatedOn=json_data.get("CreatedOn"),
            Description=json_data.get("Description"),
            Enabled=json_data.get("Enabled"),
            MinimumOrigins=json_data.get("MinimumOrigins"),
            ModifiedOn=json_data.get("ModifiedOn"),
            Monitor=json_data.get("Monitor"),
            Name=json_data.get("Name"),
            NotificationEmail=json_data.get("NotificationEmail"),
            Origins=json_data.get("Origins"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class Origins:
    Address: Optional[str]
    Enabled: Optional[bool]
    Name: Optional[str]
    Weight: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_Origins"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Origins"]:
        if not json_data:
            return None
        return cls(
            Address=json_data.get("Address"),
            Enabled=json_data.get("Enabled"),
            Name=json_data.get("Name"),
            Weight=json_data.get("Weight"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Origins = Origins


