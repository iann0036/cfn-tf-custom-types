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
    Clustering: Optional[Sequence[str]]
    CreationTime: Optional[float]
    DatasetId: Optional[str]
    Description: Optional[str]
    Etag: Optional[str]
    ExpirationTime: Optional[float]
    FriendlyName: Optional[str]
    Labels: Optional[Sequence["_Labels"]]
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
    EncryptionConfiguration: Optional[Sequence["_EncryptionConfiguration"]]
    ExternalDataConfiguration: Optional[Sequence["_ExternalDataConfiguration"]]
    TimePartitioning: Optional[Sequence["_TimePartitioning"]]
    View: Optional[Sequence["_View"]]
    CsvOptions: Optional[Sequence["_CsvOptions"]]
    GoogleSheetsOptions: Optional[Sequence["_GoogleSheetsOptions"]]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceModel"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceModel"]:
        if not json_data:
            return None
        return cls(
            tfcfnid=json_data.get("tfcfnid"),
            Clustering=json_data.get("Clustering"),
            CreationTime=json_data.get("CreationTime"),
            DatasetId=json_data.get("DatasetId"),
            Description=json_data.get("Description"),
            Etag=json_data.get("Etag"),
            ExpirationTime=json_data.get("ExpirationTime"),
            FriendlyName=json_data.get("FriendlyName"),
            Labels=json_data.get("Labels"),
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
            EncryptionConfiguration=json_data.get("EncryptionConfiguration"),
            ExternalDataConfiguration=json_data.get("ExternalDataConfiguration"),
            TimePartitioning=json_data.get("TimePartitioning"),
            View=json_data.get("View"),
            CsvOptions=json_data.get("CsvOptions"),
            GoogleSheetsOptions=json_data.get("GoogleSheetsOptions"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class Labels:
    Key: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Labels"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Labels"]:
        if not json_data:
            return None
        return cls(
            Key=json_data.get("Key"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Labels = Labels


@dataclass
class EncryptionConfiguration:
    KmsKeyName: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_EncryptionConfiguration"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_EncryptionConfiguration"]:
        if not json_data:
            return None
        return cls(
            KmsKeyName=json_data.get("KmsKeyName"),
        )


# work around possible type aliasing issues when variable has same name as a model
_EncryptionConfiguration = EncryptionConfiguration


@dataclass
class ExternalDataConfiguration:
    Autodetect: Optional[bool]
    Compression: Optional[str]
    IgnoreUnknownValues: Optional[bool]
    MaxBadRecords: Optional[float]
    SourceFormat: Optional[str]
    SourceUris: Optional[Sequence[str]]
    CsvOptions: Optional[Sequence["_CsvOptions"]]
    GoogleSheetsOptions: Optional[Sequence["_GoogleSheetsOptions"]]

    @classmethod
    def _deserialize(
        cls: Type["_ExternalDataConfiguration"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ExternalDataConfiguration"]:
        if not json_data:
            return None
        return cls(
            Autodetect=json_data.get("Autodetect"),
            Compression=json_data.get("Compression"),
            IgnoreUnknownValues=json_data.get("IgnoreUnknownValues"),
            MaxBadRecords=json_data.get("MaxBadRecords"),
            SourceFormat=json_data.get("SourceFormat"),
            SourceUris=json_data.get("SourceUris"),
            CsvOptions=json_data.get("CsvOptions"),
            GoogleSheetsOptions=json_data.get("GoogleSheetsOptions"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ExternalDataConfiguration = ExternalDataConfiguration


@dataclass
class CsvOptions:
    AllowJaggedRows: Optional[bool]
    AllowQuotedNewlines: Optional[bool]
    Encoding: Optional[str]
    FieldDelimiter: Optional[str]
    Quote: Optional[str]
    SkipLeadingRows: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_CsvOptions"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_CsvOptions"]:
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
_CsvOptions = CsvOptions


@dataclass
class GoogleSheetsOptions:
    Range: Optional[str]
    SkipLeadingRows: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_GoogleSheetsOptions"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_GoogleSheetsOptions"]:
        if not json_data:
            return None
        return cls(
            Range=json_data.get("Range"),
            SkipLeadingRows=json_data.get("SkipLeadingRows"),
        )


# work around possible type aliasing issues when variable has same name as a model
_GoogleSheetsOptions = GoogleSheetsOptions


@dataclass
class TimePartitioning:
    ExpirationMs: Optional[float]
    Field: Optional[str]
    RequirePartitionFilter: Optional[bool]
    Type: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_TimePartitioning"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TimePartitioning"]:
        if not json_data:
            return None
        return cls(
            ExpirationMs=json_data.get("ExpirationMs"),
            Field=json_data.get("Field"),
            RequirePartitionFilter=json_data.get("RequirePartitionFilter"),
            Type=json_data.get("Type"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TimePartitioning = TimePartitioning


@dataclass
class View:
    Query: Optional[str]
    UseLegacySql: Optional[bool]

    @classmethod
    def _deserialize(
        cls: Type["_View"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_View"]:
        if not json_data:
            return None
        return cls(
            Query=json_data.get("Query"),
            UseLegacySql=json_data.get("UseLegacySql"),
        )


# work around possible type aliasing issues when variable has same name as a model
_View = View


