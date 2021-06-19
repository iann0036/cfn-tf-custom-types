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
    Clustering: Optional[Sequence[str]]
    CreationTime: Optional[float]
    DatasetId: Optional[str]
    DeletionProtection: Optional[bool]
    Description: Optional[str]
    Etag: Optional[str]
    ExpirationTime: Optional[float]
    FriendlyName: Optional[str]
    Id: Optional[str]
    Labels: Optional[Sequence["_LabelsDefinition"]]
    LastModifiedTime: Optional[float]
    Location: Optional[str]
    NumBytes: Optional[float]
    NumLongTermBytes: Optional[float]
    NumRows: Optional[float]
    Project: Optional[str]
    Schema: Optional[str]
    SelfLink: Optional[str]
    TableId: Optional[str]
    Type: Optional[str]
    EncryptionConfiguration: Optional[Sequence["_EncryptionConfigurationDefinition"]]
    ExternalDataConfiguration: Optional[Sequence["_ExternalDataConfigurationDefinition"]]
    MaterializedView: Optional[Sequence["_MaterializedViewDefinition"]]
    RangePartitioning: Optional[Sequence["_RangePartitioningDefinition"]]
    TimePartitioning: Optional[Sequence["_TimePartitioningDefinition"]]
    View: Optional[Sequence["_ViewDefinition"]]

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
            Clustering=json_data.get("Clustering"),
            CreationTime=json_data.get("CreationTime"),
            DatasetId=json_data.get("DatasetId"),
            DeletionProtection=json_data.get("DeletionProtection"),
            Description=json_data.get("Description"),
            Etag=json_data.get("Etag"),
            ExpirationTime=json_data.get("ExpirationTime"),
            FriendlyName=json_data.get("FriendlyName"),
            Id=json_data.get("Id"),
            Labels=deserialize_list(json_data.get("Labels"), LabelsDefinition),
            LastModifiedTime=json_data.get("LastModifiedTime"),
            Location=json_data.get("Location"),
            NumBytes=json_data.get("NumBytes"),
            NumLongTermBytes=json_data.get("NumLongTermBytes"),
            NumRows=json_data.get("NumRows"),
            Project=json_data.get("Project"),
            Schema=json_data.get("Schema"),
            SelfLink=json_data.get("SelfLink"),
            TableId=json_data.get("TableId"),
            Type=json_data.get("Type"),
            EncryptionConfiguration=deserialize_list(json_data.get("EncryptionConfiguration"), EncryptionConfigurationDefinition),
            ExternalDataConfiguration=deserialize_list(json_data.get("ExternalDataConfiguration"), ExternalDataConfigurationDefinition),
            MaterializedView=deserialize_list(json_data.get("MaterializedView"), MaterializedViewDefinition),
            RangePartitioning=deserialize_list(json_data.get("RangePartitioning"), RangePartitioningDefinition),
            TimePartitioning=deserialize_list(json_data.get("TimePartitioning"), TimePartitioningDefinition),
            View=deserialize_list(json_data.get("View"), ViewDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class LabelsDefinition(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_LabelsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_LabelsDefinition"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_LabelsDefinition = LabelsDefinition


@dataclass
class EncryptionConfigurationDefinition(BaseModel):
    KmsKeyName: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_EncryptionConfigurationDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_EncryptionConfigurationDefinition"]:
        if not json_data:
            return None
        return cls(
            KmsKeyName=json_data.get("KmsKeyName"),
        )


# work around possible type aliasing issues when variable has same name as a model
_EncryptionConfigurationDefinition = EncryptionConfigurationDefinition


@dataclass
class ExternalDataConfigurationDefinition(BaseModel):
    Autodetect: Optional[bool]
    Compression: Optional[str]
    IgnoreUnknownValues: Optional[bool]
    MaxBadRecords: Optional[float]
    Schema: Optional[str]
    SourceFormat: Optional[str]
    SourceUris: Optional[Sequence[str]]
    CsvOptions: Optional[Sequence["_CsvOptionsDefinition"]]
    GoogleSheetsOptions: Optional[Sequence["_GoogleSheetsOptionsDefinition"]]
    HivePartitioningOptions: Optional[Sequence["_HivePartitioningOptionsDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_ExternalDataConfigurationDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ExternalDataConfigurationDefinition"]:
        if not json_data:
            return None
        return cls(
            Autodetect=json_data.get("Autodetect"),
            Compression=json_data.get("Compression"),
            IgnoreUnknownValues=json_data.get("IgnoreUnknownValues"),
            MaxBadRecords=json_data.get("MaxBadRecords"),
            Schema=json_data.get("Schema"),
            SourceFormat=json_data.get("SourceFormat"),
            SourceUris=json_data.get("SourceUris"),
            CsvOptions=deserialize_list(json_data.get("CsvOptions"), CsvOptionsDefinition),
            GoogleSheetsOptions=deserialize_list(json_data.get("GoogleSheetsOptions"), GoogleSheetsOptionsDefinition),
            HivePartitioningOptions=deserialize_list(json_data.get("HivePartitioningOptions"), HivePartitioningOptionsDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ExternalDataConfigurationDefinition = ExternalDataConfigurationDefinition


@dataclass
class CsvOptionsDefinition(BaseModel):
    AllowJaggedRows: Optional[bool]
    AllowQuotedNewlines: Optional[bool]
    Encoding: Optional[str]
    FieldDelimiter: Optional[str]
    Quote: Optional[str]
    SkipLeadingRows: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_CsvOptionsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_CsvOptionsDefinition"]:
        if not json_data:
            return None
        return cls(
            AllowJaggedRows=json_data.get("AllowJaggedRows"),
            AllowQuotedNewlines=json_data.get("AllowQuotedNewlines"),
            Encoding=json_data.get("Encoding"),
            FieldDelimiter=json_data.get("FieldDelimiter"),
            Quote=json_data.get("Quote"),
            SkipLeadingRows=json_data.get("SkipLeadingRows"),
        )


# work around possible type aliasing issues when variable has same name as a model
_CsvOptionsDefinition = CsvOptionsDefinition


@dataclass
class GoogleSheetsOptionsDefinition(BaseModel):
    Range: Optional[str]
    SkipLeadingRows: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_GoogleSheetsOptionsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_GoogleSheetsOptionsDefinition"]:
        if not json_data:
            return None
        return cls(
            Range=json_data.get("Range"),
            SkipLeadingRows=json_data.get("SkipLeadingRows"),
        )


# work around possible type aliasing issues when variable has same name as a model
_GoogleSheetsOptionsDefinition = GoogleSheetsOptionsDefinition


@dataclass
class HivePartitioningOptionsDefinition(BaseModel):
    Mode: Optional[str]
    RequirePartitionFilter: Optional[bool]
    SourceUriPrefix: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_HivePartitioningOptionsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_HivePartitioningOptionsDefinition"]:
        if not json_data:
            return None
        return cls(
            Mode=json_data.get("Mode"),
            RequirePartitionFilter=json_data.get("RequirePartitionFilter"),
            SourceUriPrefix=json_data.get("SourceUriPrefix"),
        )


# work around possible type aliasing issues when variable has same name as a model
_HivePartitioningOptionsDefinition = HivePartitioningOptionsDefinition


@dataclass
class MaterializedViewDefinition(BaseModel):
    EnableRefresh: Optional[bool]
    Query: Optional[str]
    RefreshIntervalMs: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_MaterializedViewDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_MaterializedViewDefinition"]:
        if not json_data:
            return None
        return cls(
            EnableRefresh=json_data.get("EnableRefresh"),
            Query=json_data.get("Query"),
            RefreshIntervalMs=json_data.get("RefreshIntervalMs"),
        )


# work around possible type aliasing issues when variable has same name as a model
_MaterializedViewDefinition = MaterializedViewDefinition


@dataclass
class RangePartitioningDefinition(BaseModel):
    Field: Optional[str]
    Range: Optional[Sequence["_RangeDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_RangePartitioningDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_RangePartitioningDefinition"]:
        if not json_data:
            return None
        return cls(
            Field=json_data.get("Field"),
            Range=deserialize_list(json_data.get("Range"), RangeDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_RangePartitioningDefinition = RangePartitioningDefinition


@dataclass
class RangeDefinition(BaseModel):
    End: Optional[float]
    Interval: Optional[float]
    Start: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_RangeDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_RangeDefinition"]:
        if not json_data:
            return None
        return cls(
            End=json_data.get("End"),
            Interval=json_data.get("Interval"),
            Start=json_data.get("Start"),
        )


# work around possible type aliasing issues when variable has same name as a model
_RangeDefinition = RangeDefinition


@dataclass
class TimePartitioningDefinition(BaseModel):
    ExpirationMs: Optional[float]
    Field: Optional[str]
    RequirePartitionFilter: Optional[bool]
    Type: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_TimePartitioningDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TimePartitioningDefinition"]:
        if not json_data:
            return None
        return cls(
            ExpirationMs=json_data.get("ExpirationMs"),
            Field=json_data.get("Field"),
            RequirePartitionFilter=json_data.get("RequirePartitionFilter"),
            Type=json_data.get("Type"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TimePartitioningDefinition = TimePartitioningDefinition


@dataclass
class ViewDefinition(BaseModel):
    Query: Optional[str]
    UseLegacySql: Optional[bool]

    @classmethod
    def _deserialize(
        cls: Type["_ViewDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ViewDefinition"]:
        if not json_data:
            return None
        return cls(
            Query=json_data.get("Query"),
            UseLegacySql=json_data.get("UseLegacySql"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ViewDefinition = ViewDefinition


