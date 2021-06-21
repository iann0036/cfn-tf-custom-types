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
    AdditionalProperties: Optional[Sequence["_AdditionalPropertiesDefinition"]]
    Annotations: Optional[Sequence[str]]
    DataFactoryName: Optional[str]
    Description: Optional[str]
    Encoding: Optional[str]
    Folder: Optional[str]
    Id: Optional[str]
    LinkedServiceName: Optional[str]
    Name: Optional[str]
    Parameters: Optional[Sequence["_ParametersDefinition"]]
    ResourceGroupName: Optional[str]
    AzureBlobStorageLocation: Optional[Sequence["_AzureBlobStorageLocationDefinition"]]
    HttpServerLocation: Optional[Sequence["_HttpServerLocationDefinition"]]
    SchemaColumn: Optional[Sequence["_SchemaColumnDefinition"]]
    Timeouts: Optional["_TimeoutsDefinition"]

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
            AdditionalProperties=deserialize_list(json_data.get("AdditionalProperties"), AdditionalPropertiesDefinition),
            Annotations=json_data.get("Annotations"),
            DataFactoryName=json_data.get("DataFactoryName"),
            Description=json_data.get("Description"),
            Encoding=json_data.get("Encoding"),
            Folder=json_data.get("Folder"),
            Id=json_data.get("Id"),
            LinkedServiceName=json_data.get("LinkedServiceName"),
            Name=json_data.get("Name"),
            Parameters=deserialize_list(json_data.get("Parameters"), ParametersDefinition),
            ResourceGroupName=json_data.get("ResourceGroupName"),
            AzureBlobStorageLocation=deserialize_list(json_data.get("AzureBlobStorageLocation"), AzureBlobStorageLocationDefinition),
            HttpServerLocation=deserialize_list(json_data.get("HttpServerLocation"), HttpServerLocationDefinition),
            SchemaColumn=deserialize_list(json_data.get("SchemaColumn"), SchemaColumnDefinition),
            Timeouts=TimeoutsDefinition._deserialize(json_data.get("Timeouts")),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class AdditionalPropertiesDefinition(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_AdditionalPropertiesDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AdditionalPropertiesDefinition"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AdditionalPropertiesDefinition = AdditionalPropertiesDefinition


@dataclass
class ParametersDefinition(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ParametersDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ParametersDefinition"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ParametersDefinition = ParametersDefinition


@dataclass
class AzureBlobStorageLocationDefinition(BaseModel):
    Container: Optional[str]
    Filename: Optional[str]
    Path: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_AzureBlobStorageLocationDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AzureBlobStorageLocationDefinition"]:
        if not json_data:
            return None
        return cls(
            Container=json_data.get("Container"),
            Filename=json_data.get("Filename"),
            Path=json_data.get("Path"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AzureBlobStorageLocationDefinition = AzureBlobStorageLocationDefinition


@dataclass
class HttpServerLocationDefinition(BaseModel):
    Filename: Optional[str]
    Path: Optional[str]
    RelativeUrl: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_HttpServerLocationDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_HttpServerLocationDefinition"]:
        if not json_data:
            return None
        return cls(
            Filename=json_data.get("Filename"),
            Path=json_data.get("Path"),
            RelativeUrl=json_data.get("RelativeUrl"),
        )


# work around possible type aliasing issues when variable has same name as a model
_HttpServerLocationDefinition = HttpServerLocationDefinition


@dataclass
class SchemaColumnDefinition(BaseModel):
    Description: Optional[str]
    Name: Optional[str]
    Type: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_SchemaColumnDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SchemaColumnDefinition"]:
        if not json_data:
            return None
        return cls(
            Description=json_data.get("Description"),
            Name=json_data.get("Name"),
            Type=json_data.get("Type"),
        )


# work around possible type aliasing issues when variable has same name as a model
_SchemaColumnDefinition = SchemaColumnDefinition


@dataclass
class TimeoutsDefinition(BaseModel):
    Create: Optional[str]
    Delete: Optional[str]
    Read: Optional[str]
    Update: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_TimeoutsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TimeoutsDefinition"]:
        if not json_data:
            return None
        return cls(
            Create=json_data.get("Create"),
            Delete=json_data.get("Delete"),
            Read=json_data.get("Read"),
            Update=json_data.get("Update"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TimeoutsDefinition = TimeoutsDefinition

