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
    CatalogId: Optional[str]
    CreationTime: Optional[str]
    DatabaseName: Optional[str]
    Id: Optional[str]
    LastAccessedTime: Optional[str]
    LastAnalyzedTime: Optional[str]
    Parameters: Optional[Sequence["_ParametersDefinition"]]
    PartitionValues: Optional[Sequence[str]]
    TableName: Optional[str]
    StorageDescriptor: Optional[Sequence["_StorageDescriptorDefinition"]]

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
            CatalogId=json_data.get("CatalogId"),
            CreationTime=json_data.get("CreationTime"),
            DatabaseName=json_data.get("DatabaseName"),
            Id=json_data.get("Id"),
            LastAccessedTime=json_data.get("LastAccessedTime"),
            LastAnalyzedTime=json_data.get("LastAnalyzedTime"),
            Parameters=deserialize_list(json_data.get("Parameters"), ParametersDefinition),
            PartitionValues=json_data.get("PartitionValues"),
            TableName=json_data.get("TableName"),
            StorageDescriptor=deserialize_list(json_data.get("StorageDescriptor"), StorageDescriptorDefinition),
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
            Type=json_data.get("Type"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ColumnsDefinition = ColumnsDefinition


@dataclass
class SerDeInfoDefinition(BaseModel):
    Name: Optional[str]
    Parameters: Optional[Sequence["_ParametersDefinition3"]]
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
            Parameters=deserialize_list(json_data.get("Parameters"), ParametersDefinition3),
            SerializationLibrary=json_data.get("SerializationLibrary"),
        )


# work around possible type aliasing issues when variable has same name as a model
_SerDeInfoDefinition = SerDeInfoDefinition


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


