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
    GlueVersion: Optional[str]
    Id: Optional[str]
    LabelCount: Optional[float]
    MaxCapacity: Optional[float]
    MaxRetries: Optional[float]
    Name: Optional[str]
    NumberOfWorkers: Optional[float]
    RoleArn: Optional[str]
    Schema: Optional[Sequence["_SchemaDefinition"]]
    Tags: Optional[Sequence["_TagsDefinition"]]
    TagsAll: Optional[Sequence["_TagsAllDefinition"]]
    Timeout: Optional[float]
    WorkerType: Optional[str]
    InputRecordTables: Optional[Sequence["_InputRecordTablesDefinition"]]
    Parameters: Optional[Sequence["_ParametersDefinition"]]

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
            GlueVersion=json_data.get("GlueVersion"),
            Id=json_data.get("Id"),
            LabelCount=json_data.get("LabelCount"),
            MaxCapacity=json_data.get("MaxCapacity"),
            MaxRetries=json_data.get("MaxRetries"),
            Name=json_data.get("Name"),
            NumberOfWorkers=json_data.get("NumberOfWorkers"),
            RoleArn=json_data.get("RoleArn"),
            Schema=deserialize_list(json_data.get("Schema"), SchemaDefinition),
            Tags=deserialize_list(json_data.get("Tags"), TagsDefinition),
            TagsAll=deserialize_list(json_data.get("TagsAll"), TagsAllDefinition),
            Timeout=json_data.get("Timeout"),
            WorkerType=json_data.get("WorkerType"),
            InputRecordTables=deserialize_list(json_data.get("InputRecordTables"), InputRecordTablesDefinition),
            Parameters=deserialize_list(json_data.get("Parameters"), ParametersDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class SchemaDefinition(BaseModel):
    DataType: Optional[str]
    Name: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_SchemaDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SchemaDefinition"]:
        if not json_data:
            return None
        return cls(
            DataType=json_data.get("DataType"),
            Name=json_data.get("Name"),
        )


# work around possible type aliasing issues when variable has same name as a model
_SchemaDefinition = SchemaDefinition


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
class InputRecordTablesDefinition(BaseModel):
    CatalogId: Optional[str]
    ConnectionName: Optional[str]
    DatabaseName: Optional[str]
    TableName: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_InputRecordTablesDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_InputRecordTablesDefinition"]:
        if not json_data:
            return None
        return cls(
            CatalogId=json_data.get("CatalogId"),
            ConnectionName=json_data.get("ConnectionName"),
            DatabaseName=json_data.get("DatabaseName"),
            TableName=json_data.get("TableName"),
        )


# work around possible type aliasing issues when variable has same name as a model
_InputRecordTablesDefinition = InputRecordTablesDefinition


@dataclass
class ParametersDefinition(BaseModel):
    TransformType: Optional[str]
    FindMatchesParameters: Optional[Sequence["_FindMatchesParametersDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_ParametersDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ParametersDefinition"]:
        if not json_data:
            return None
        return cls(
            TransformType=json_data.get("TransformType"),
            FindMatchesParameters=deserialize_list(json_data.get("FindMatchesParameters"), FindMatchesParametersDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ParametersDefinition = ParametersDefinition


@dataclass
class FindMatchesParametersDefinition(BaseModel):
    AccuracyCostTradeOff: Optional[float]
    EnforceProvidedLabels: Optional[bool]
    PrecisionRecallTradeOff: Optional[float]
    PrimaryKeyColumnName: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_FindMatchesParametersDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_FindMatchesParametersDefinition"]:
        if not json_data:
            return None
        return cls(
            AccuracyCostTradeOff=json_data.get("AccuracyCostTradeOff"),
            EnforceProvidedLabels=json_data.get("EnforceProvidedLabels"),
            PrecisionRecallTradeOff=json_data.get("PrecisionRecallTradeOff"),
            PrimaryKeyColumnName=json_data.get("PrimaryKeyColumnName"),
        )


# work around possible type aliasing issues when variable has same name as a model
_FindMatchesParametersDefinition = FindMatchesParametersDefinition


