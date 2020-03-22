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
    AuthorizedResourceIds: Optional[Sequence[str]]
    DataSourceId: Optional[str]
    Description: Optional[str]
    Enabled: Optional[bool]
    Id: Optional[str]
    Location: Optional[str]
    Name: Optional[str]
    ResourceGroupName: Optional[str]
    Tags: Optional[Sequence["_Tags"]]
    Criteria: Optional[Sequence["_Criteria"]]
    Timeouts: Optional["_Timeouts"]
    Dimension: Optional[Sequence["_Dimension"]]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceModel"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceModel"]:
        if not json_data:
            return None
        return cls(
            tfcfnid=json_data.get("tfcfnid"),
            AuthorizedResourceIds=json_data.get("AuthorizedResourceIds"),
            DataSourceId=json_data.get("DataSourceId"),
            Description=json_data.get("Description"),
            Enabled=json_data.get("Enabled"),
            Id=json_data.get("Id"),
            Location=json_data.get("Location"),
            Name=json_data.get("Name"),
            ResourceGroupName=json_data.get("ResourceGroupName"),
            Tags=json_data.get("Tags"),
            Criteria=json_data.get("Criteria"),
            Timeouts=Timeouts._deserialize(json_data.get("Timeouts")),
            Dimension=json_data.get("Dimension"),
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
class Criteria:
    MetricName: Optional[str]
    Dimension: Optional[Sequence["_Dimension"]]

    @classmethod
    def _deserialize(
        cls: Type["_Criteria"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Criteria"]:
        if not json_data:
            return None
        return cls(
            MetricName=json_data.get("MetricName"),
            Dimension=json_data.get("Dimension"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Criteria = Criteria


@dataclass
class Dimension:
    Name: Optional[str]
    Operator: Optional[str]
    Values: Optional[Sequence[str]]

    @classmethod
    def _deserialize(
        cls: Type["_Dimension"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Dimension"]:
        if not json_data:
            return None
        return cls(
            Name=json_data.get("Name"),
            Operator=json_data.get("Operator"),
            Values=json_data.get("Values"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Dimension = Dimension


@dataclass
class Timeouts:
    Create: Optional[str]
    Delete: Optional[str]
    Read: Optional[str]
    Update: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Timeouts"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Timeouts"]:
        if not json_data:
            return None
        return cls(
            Create=json_data.get("Create"),
            Delete=json_data.get("Delete"),
            Read=json_data.get("Read"),
            Update=json_data.get("Update"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Timeouts = Timeouts


