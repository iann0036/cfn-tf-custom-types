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
    CatalogId: Optional[str]
    DatabaseName: Optional[str]
    Description: Optional[str]
    Id: Optional[str]
    Name: Optional[str]
    Owner: Optional[str]
    Parameters: Optional[Sequence["_Parameters"]]
    Retention: Optional[float]
    TableType: Optional[str]
    ViewExpandedText: Optional[str]
    ViewOriginalText: Optional[str]
    PartitionKeys: Optional[Sequence["_PartitionKeys"]]
    StorageDescriptor: Optional[Sequence["_StorageDescriptor"]]
    Columns: Optional[Sequence["_Columns"]]
    SerDeInfo: Optional[Sequence["_SerDeInfo"]]
    SkewedInfo: Optional[Sequence["_SkewedInfo"]]
    SortColumns: Optional[Sequence["_SortColumns"]]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceModel"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceModel"]:
        if not json_data:
            return None
        return cls(
            tfcfnid=json_data.get("tfcfnid"),
            CatalogId=json_data.get("CatalogId"),
            DatabaseName=json_data.get("DatabaseName"),
            Description=json_data.get("Description"),
            Id=json_data.get("Id"),
            Name=json_data.get("Name"),
            Owner=json_data.get("Owner"),
            Parameters=json_data.get("Parameters"),
            Retention=json_data.get("Retention"),
            TableType=json_data.get("TableType"),
            ViewExpandedText=json_data.get("ViewExpandedText"),
            ViewOriginalText=json_data.get("ViewOriginalText"),
            PartitionKeys=json_data.get("PartitionKeys"),
            StorageDescriptor=json_data.get("StorageDescriptor"),
            Columns=json_data.get("Columns"),
            SerDeInfo=json_data.get("SerDeInfo"),
            SkewedInfo=json_data.get("SkewedInfo"),
            SortColumns=json_data.get("SortColumns"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class Parameters:
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Parameters"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Parameters"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Parameters = Parameters


@dataclass
class PartitionKeys:
    Comment: Optional[str]
    Name: Optional[str]
    Type: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_PartitionKeys"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_PartitionKeys"]:
        if not json_data:
            return None
        return cls(
            Comment=json_data.get("Comment"),
            Name=json_data.get("Name"),
            Type=json_data.get("Type"),
        )


# work around possible type aliasing issues when variable has same name as a model
_PartitionKeys = PartitionKeys


@dataclass
class StorageDescriptor:
    BucketColumns: Optional[Sequence[str]]
    Compressed: Optional[bool]
    InputFormat: Optional[str]
    Location: Optional[str]
    NumberOfBuckets: Optional[float]
    OutputFormat: Optional[str]
    Parameters: Optional[Sequence["_Parameters2"]]
    StoredAsSubDirectories: Optional[bool]
    Columns: Optional[Sequence["_Columns"]]
    SerDeInfo: Optional[Sequence["_SerDeInfo"]]
    SkewedInfo: Optional[Sequence["_SkewedInfo"]]
    SortColumns: Optional[Sequence["_SortColumns"]]

    @classmethod
    def _deserialize(
        cls: Type["_StorageDescriptor"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_StorageDescriptor"]:
        if not json_data:
            return None
        return cls(
            BucketColumns=json_data.get("BucketColumns"),
            Compressed=json_data.get("Compressed"),
            InputFormat=json_data.get("InputFormat"),
            Location=json_data.get("Location"),
            NumberOfBuckets=json_data.get("NumberOfBuckets"),
            OutputFormat=json_data.get("OutputFormat"),
            Parameters=json_data.get("Parameters"),
            StoredAsSubDirectories=json_data.get("StoredAsSubDirectories"),
            Columns=json_data.get("Columns"),
            SerDeInfo=json_data.get("SerDeInfo"),
            SkewedInfo=json_data.get("SkewedInfo"),
            SortColumns=json_data.get("SortColumns"),
        )


# work around possible type aliasing issues when variable has same name as a model
_StorageDescriptor = StorageDescriptor


@dataclass
class Parameters2:
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Parameters2"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Parameters2"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Parameters2 = Parameters2


@dataclass
class Columns:
    Comment: Optional[str]
    Name: Optional[str]
    Type: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Columns"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Columns"]:
        if not json_data:
            return None
        return cls(
            Comment=json_data.get("Comment"),
            Name=json_data.get("Name"),
            Type=json_data.get("Type"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Columns = Columns


@dataclass
class SerDeInfo:
    Name: Optional[str]
    Parameters: Optional[Sequence["_Parameters3"]]
    SerializationLibrary: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_SerDeInfo"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SerDeInfo"]:
        if not json_data:
            return None
        return cls(
            Name=json_data.get("Name"),
            Parameters=json_data.get("Parameters"),
            SerializationLibrary=json_data.get("SerializationLibrary"),
        )


# work around possible type aliasing issues when variable has same name as a model
_SerDeInfo = SerDeInfo


@dataclass
class Parameters3:
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Parameters3"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Parameters3"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Parameters3 = Parameters3


@dataclass
class SkewedInfo:
    SkewedColumnNames: Optional[Sequence[str]]
    SkewedColumnValueLocationMaps: Optional[Sequence["_SkewedColumnValueLocationMaps"]]
    SkewedColumnValues: Optional[Sequence[str]]

    @classmethod
    def _deserialize(
        cls: Type["_SkewedInfo"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SkewedInfo"]:
        if not json_data:
            return None
        return cls(
            SkewedColumnNames=json_data.get("SkewedColumnNames"),
            SkewedColumnValueLocationMaps=json_data.get("SkewedColumnValueLocationMaps"),
            SkewedColumnValues=json_data.get("SkewedColumnValues"),
        )


# work around possible type aliasing issues when variable has same name as a model
_SkewedInfo = SkewedInfo


@dataclass
class SkewedColumnValueLocationMaps:
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_SkewedColumnValueLocationMaps"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SkewedColumnValueLocationMaps"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_SkewedColumnValueLocationMaps = SkewedColumnValueLocationMaps


@dataclass
class SortColumns:
    Column: Optional[str]
    SortOrder: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_SortColumns"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SortColumns"]:
        if not json_data:
            return None
        return cls(
            Column=json_data.get("Column"),
            SortOrder=json_data.get("SortOrder"),
        )


# work around possible type aliasing issues when variable has same name as a model
_SortColumns = SortColumns


