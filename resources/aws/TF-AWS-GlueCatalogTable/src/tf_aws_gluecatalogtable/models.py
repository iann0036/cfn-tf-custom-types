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
    CatalogId: Optional[str]
    DatabaseName: Optional[str]
    Description: Optional[str]
    Id: Optional[str]
    Name: Optional[str]
    Owner: Optional[str]
    Parameters: Optional[Sequence["_ParametersDefinition"]]
    Retention: Optional[float]
    TableType: Optional[str]
    ViewExpandedText: Optional[str]
    ViewOriginalText: Optional[str]
    PartitionIndex: Optional[Sequence["_PartitionIndexDefinition"]]
    PartitionKeys: Optional[Sequence["_PartitionKeysDefinition"]]
    StorageDescriptor: Optional[Sequence["_StorageDescriptorDefinition"]]
    TargetTable: Optional[Sequence["_TargetTableDefinition"]]

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
            CatalogId=json_data.get("CatalogId"),
            DatabaseName=json_data.get("DatabaseName"),
            Description=json_data.get("Description"),
            Id=json_data.get("Id"),
            Name=json_data.get("Name"),
            Owner=json_data.get("Owner"),
            Parameters=deserialize_list(json_data.get("Parameters"), ParametersDefinition),
            Retention=json_data.get("Retention"),
            TableType=json_data.get("TableType"),
            ViewExpandedText=json_data.get("ViewExpandedText"),
            ViewOriginalText=json_data.get("ViewOriginalText"),
            PartitionIndex=deserialize_list(json_data.get("PartitionIndex"), PartitionIndexDefinition),
            PartitionKeys=deserialize_list(json_data.get("PartitionKeys"), PartitionKeysDefinition),
            StorageDescriptor=deserialize_list(json_data.get("StorageDescriptor"), StorageDescriptorDefinition),
            TargetTable=deserialize_list(json_data.get("TargetTable"), TargetTableDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


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
class PartitionIndexDefinition(BaseModel):
    IndexName: Optional[str]
    Keys: Optional[Sequence[str]]

    @classmethod
    def _deserialize(
        cls: Type["_PartitionIndexDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_PartitionIndexDefinition"]:
        if not json_data:
            return None
        return cls(
            IndexName=json_data.get("IndexName"),
            Keys=json_data.get("Keys"),
        )


# work around possible type aliasing issues when variable has same name as a model
_PartitionIndexDefinition = PartitionIndexDefinition


@dataclass
class PartitionKeysDefinition(BaseModel):
    Comment: Optional[str]
    Name: Optional[str]
    Type: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_PartitionKeysDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_PartitionKeysDefinition"]:
        if not json_data:
            return None
        return cls(
            Comment=json_data.get("Comment"),
            Name=json_data.get("Name"),
            Type=json_data.get("Type"),
        )


# work around possible type aliasing issues when variable has same name as a model
_PartitionKeysDefinition = PartitionKeysDefinition


@dataclass
class StorageDescriptorDefinition(BaseModel):
    BucketColumns: Optional[Sequence[str]]
    Compressed: Optional[bool]
    InputFormat: Optional[str]
    Location: Optional[str]
    NumberOfBuckets: Optional[float]
    OutputFormat: Optional[str]
    Parameters: Optional[Sequence["_ParametersDefinition2"]]
    StoredAsSubDirectories: Optional[bool]
    Columns: Optional[Sequence["_ColumnsDefinition"]]
    SchemaReference: Optional[Sequence["_SchemaReferenceDefinition"]]
    SerDeInfo: Optional[Sequence["_SerDeInfoDefinition"]]
    SkewedInfo: Optional[Sequence["_SkewedInfoDefinition"]]
    SortColumns: Optional[Sequence["_SortColumnsDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_StorageDescriptorDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_StorageDescriptorDefinition"]:
        if not json_data:
            return None
        return cls(
            BucketColumns=json_data.get("BucketColumns"),
            Compressed=json_data.get("Compressed"),
            InputFormat=json_data.get("InputFormat"),
            Location=json_data.get("Location"),
            NumberOfBuckets=json_data.get("NumberOfBuckets"),
            OutputFormat=json_data.get("OutputFormat"),
            Parameters=deserialize_list(json_data.get("Parameters"), ParametersDefinition2),
            StoredAsSubDirectories=json_data.get("StoredAsSubDirectories"),
            Columns=deserialize_list(json_data.get("Columns"), ColumnsDefinition),
            SchemaReference=deserialize_list(json_data.get("SchemaReference"), SchemaReferenceDefinition),
            SerDeInfo=deserialize_list(json_data.get("SerDeInfo"), SerDeInfoDefinition),
            SkewedInfo=deserialize_list(json_data.get("SkewedInfo"), SkewedInfoDefinition),
            SortColumns=deserialize_list(json_data.get("SortColumns"), SortColumnsDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_StorageDescriptorDefinition = StorageDescriptorDefinition


@dataclass
class ParametersDefinition2(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ParametersDefinition2"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ParametersDefinition2"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ParametersDefinition2 = ParametersDefinition2


@dataclass
class ColumnsDefinition(BaseModel):
    Comment: Optional[str]
    Name: Optional[str]
    Parameters: Optional[Sequence["_ParametersDefinition3"]]
    Type: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ColumnsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ColumnsDefinition"]:
        if not json_data:
            return None
        return cls(
            Comment=json_data.get("Comment"),
            Name=json_data.get("Name"),
            Parameters=deserialize_list(json_data.get("Parameters"), ParametersDefinition3),
            Type=json_data.get("Type"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ColumnsDefinition = ColumnsDefinition


@dataclass
class ParametersDefinition3(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ParametersDefinition3"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ParametersDefinition3"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ParametersDefinition3 = ParametersDefinition3


@dataclass
class SchemaReferenceDefinition(BaseModel):
    SchemaVersionId: Optional[str]
    SchemaVersionNumber: Optional[float]
    SchemaId: Optional[Sequence["_SchemaIdDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_SchemaReferenceDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SchemaReferenceDefinition"]:
        if not json_data:
            return None
        return cls(
            SchemaVersionId=json_data.get("SchemaVersionId"),
            SchemaVersionNumber=json_data.get("SchemaVersionNumber"),
            SchemaId=deserialize_list(json_data.get("SchemaId"), SchemaIdDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_SchemaReferenceDefinition = SchemaReferenceDefinition


@dataclass
class SchemaIdDefinition(BaseModel):
    RegistryName: Optional[str]
    SchemaArn: Optional[str]
    SchemaName: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_SchemaIdDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SchemaIdDefinition"]:
        if not json_data:
            return None
        return cls(
            RegistryName=json_data.get("RegistryName"),
            SchemaArn=json_data.get("SchemaArn"),
            SchemaName=json_data.get("SchemaName"),
        )


# work around possible type aliasing issues when variable has same name as a model
_SchemaIdDefinition = SchemaIdDefinition


@dataclass
class SerDeInfoDefinition(BaseModel):
    Name: Optional[str]
    Parameters: Optional[Sequence["_ParametersDefinition4"]]
    SerializationLibrary: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_SerDeInfoDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SerDeInfoDefinition"]:
        if not json_data:
            return None
        return cls(
            Name=json_data.get("Name"),
            Parameters=deserialize_list(json_data.get("Parameters"), ParametersDefinition4),
            SerializationLibrary=json_data.get("SerializationLibrary"),
        )


# work around possible type aliasing issues when variable has same name as a model
_SerDeInfoDefinition = SerDeInfoDefinition


@dataclass
class ParametersDefinition4(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ParametersDefinition4"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ParametersDefinition4"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ParametersDefinition4 = ParametersDefinition4


@dataclass
class SkewedInfoDefinition(BaseModel):
    SkewedColumnNames: Optional[Sequence[str]]
    SkewedColumnValueLocationMaps: Optional[Sequence["_SkewedColumnValueLocationMapsDefinition"]]
    SkewedColumnValues: Optional[Sequence[str]]

    @classmethod
    def _deserialize(
        cls: Type["_SkewedInfoDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SkewedInfoDefinition"]:
        if not json_data:
            return None
        return cls(
            SkewedColumnNames=json_data.get("SkewedColumnNames"),
            SkewedColumnValueLocationMaps=deserialize_list(json_data.get("SkewedColumnValueLocationMaps"), SkewedColumnValueLocationMapsDefinition),
            SkewedColumnValues=json_data.get("SkewedColumnValues"),
        )


# work around possible type aliasing issues when variable has same name as a model
_SkewedInfoDefinition = SkewedInfoDefinition


@dataclass
class SkewedColumnValueLocationMapsDefinition(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_SkewedColumnValueLocationMapsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SkewedColumnValueLocationMapsDefinition"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_SkewedColumnValueLocationMapsDefinition = SkewedColumnValueLocationMapsDefinition


@dataclass
class SortColumnsDefinition(BaseModel):
    Column: Optional[str]
    SortOrder: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_SortColumnsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SortColumnsDefinition"]:
        if not json_data:
            return None
        return cls(
            Column=json_data.get("Column"),
            SortOrder=json_data.get("SortOrder"),
        )


# work around possible type aliasing issues when variable has same name as a model
_SortColumnsDefinition = SortColumnsDefinition


@dataclass
class TargetTableDefinition(BaseModel):
    CatalogId: Optional[str]
    DatabaseName: Optional[str]
    Name: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_TargetTableDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TargetTableDefinition"]:
        if not json_data:
            return None
        return cls(
            CatalogId=json_data.get("CatalogId"),
            DatabaseName=json_data.get("DatabaseName"),
            Name=json_data.get("Name"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TargetTableDefinition = TargetTableDefinition


