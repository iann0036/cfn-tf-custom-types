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
    AdditionalProperties: Optional[Sequence["_AdditionalProperties"]]
    Annotations: Optional[Sequence[str]]
    DataFactoryName: Optional[str]
    Description: Optional[str]
    Folder: Optional[str]
    Id: Optional[str]
    LinkedServiceName: Optional[str]
    Name: Optional[str]
    Parameters: Optional[Sequence["_Parameters"]]
    ResourceGroupName: Optional[str]
    TableName: Optional[str]
    SchemaColumn: Optional[Sequence["_SchemaColumn"]]
    Timeouts: Optional["_Timeouts"]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceModel"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceModel"]:
        if not json_data:
            return None
        return cls(
            tfcfnid=json_data.get("tfcfnid"),
            AdditionalProperties=json_data.get("AdditionalProperties"),
            Annotations=json_data.get("Annotations"),
            DataFactoryName=json_data.get("DataFactoryName"),
            Description=json_data.get("Description"),
            Folder=json_data.get("Folder"),
            Id=json_data.get("Id"),
            LinkedServiceName=json_data.get("LinkedServiceName"),
            Name=json_data.get("Name"),
            Parameters=json_data.get("Parameters"),
            ResourceGroupName=json_data.get("ResourceGroupName"),
            TableName=json_data.get("TableName"),
            SchemaColumn=json_data.get("SchemaColumn"),
            Timeouts=Timeouts._deserialize(json_data.get("Timeouts")),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class AdditionalProperties:
    Key: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_AdditionalProperties"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AdditionalProperties"]:
        if not json_data:
            return None
        return cls(
            Key=json_data.get("Key"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AdditionalProperties = AdditionalProperties


@dataclass
class Parameters:
    Key: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Parameters"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Parameters"]:
        if not json_data:
            return None
        return cls(
            Key=json_data.get("Key"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Parameters = Parameters


@dataclass
class SchemaColumn:
    Description: Optional[str]
    Name: Optional[str]
    Type: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_SchemaColumn"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SchemaColumn"]:
        if not json_data:
            return None
        return cls(
            Description=json_data.get("Description"),
            Name=json_data.get("Name"),
            Type=json_data.get("Type"),
        )


# work around possible type aliasing issues when variable has same name as a model
_SchemaColumn = SchemaColumn


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


