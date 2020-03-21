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
    Arn: Optional[str]
    Destination: Optional[str]
    DestinationId: Optional[str]
    Id: Optional[str]
    Name: Optional[str]
    Tags: Optional[Sequence["_Tags"]]
    VersionId: Optional[str]
    ElasticsearchConfiguration: Optional[Sequence["_ElasticsearchConfiguration"]]
    ExtendedS3Configuration: Optional[Sequence["_ExtendedS3Configuration"]]
    KinesisSourceConfiguration: Optional[Sequence["_KinesisSourceConfiguration"]]
    RedshiftConfiguration: Optional[Sequence["_RedshiftConfiguration"]]
    S3Configuration: Optional[Sequence["_S3Configuration"]]
    ServerSideEncryption: Optional[Sequence["_ServerSideEncryption"]]
    SplunkConfiguration: Optional[Sequence["_SplunkConfiguration"]]
    CloudwatchLoggingOptions: Optional[Sequence["_CloudwatchLoggingOptions"]]
    ProcessingConfiguration: Optional[Sequence["_ProcessingConfiguration"]]
    DataFormatConversionConfiguration: Optional[Sequence["_DataFormatConversionConfiguration"]]
    S3BackupConfiguration: Optional[Sequence["_S3BackupConfiguration"]]
    Processors: Optional[Sequence["_Processors"]]
    InputFormatConfiguration: Optional[Sequence["_InputFormatConfiguration"]]
    OutputFormatConfiguration: Optional[Sequence["_OutputFormatConfiguration"]]
    SchemaConfiguration: Optional[Sequence["_SchemaConfiguration"]]
    Parameters: Optional[Sequence["_Parameters"]]
    Deserializer: Optional[Sequence["_Deserializer"]]
    Serializer: Optional[Sequence["_Serializer"]]
    HiveJsonSerDe: Optional[Sequence["_HiveJsonSerDe"]]
    OpenXJsonSerDe: Optional[Sequence["_OpenXJsonSerDe"]]
    OrcSerDe: Optional[Sequence["_OrcSerDe"]]
    ParquetSerDe: Optional[Sequence["_ParquetSerDe"]]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceModel"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceModel"]:
        if not json_data:
            return None
        return cls(
            tfcfnid=json_data.get("tfcfnid"),
            Arn=json_data.get("Arn"),
            Destination=json_data.get("Destination"),
            DestinationId=json_data.get("DestinationId"),
            Id=json_data.get("Id"),
            Name=json_data.get("Name"),
            Tags=json_data.get("Tags"),
            VersionId=json_data.get("VersionId"),
            ElasticsearchConfiguration=json_data.get("ElasticsearchConfiguration"),
            ExtendedS3Configuration=json_data.get("ExtendedS3Configuration"),
            KinesisSourceConfiguration=json_data.get("KinesisSourceConfiguration"),
            RedshiftConfiguration=json_data.get("RedshiftConfiguration"),
            S3Configuration=json_data.get("S3Configuration"),
            ServerSideEncryption=json_data.get("ServerSideEncryption"),
            SplunkConfiguration=json_data.get("SplunkConfiguration"),
            CloudwatchLoggingOptions=json_data.get("CloudwatchLoggingOptions"),
            ProcessingConfiguration=json_data.get("ProcessingConfiguration"),
            DataFormatConversionConfiguration=json_data.get("DataFormatConversionConfiguration"),
            S3BackupConfiguration=json_data.get("S3BackupConfiguration"),
            Processors=json_data.get("Processors"),
            InputFormatConfiguration=json_data.get("InputFormatConfiguration"),
            OutputFormatConfiguration=json_data.get("OutputFormatConfiguration"),
            SchemaConfiguration=json_data.get("SchemaConfiguration"),
            Parameters=json_data.get("Parameters"),
            Deserializer=json_data.get("Deserializer"),
            Serializer=json_data.get("Serializer"),
            HiveJsonSerDe=json_data.get("HiveJsonSerDe"),
            OpenXJsonSerDe=json_data.get("OpenXJsonSerDe"),
            OrcSerDe=json_data.get("OrcSerDe"),
            ParquetSerDe=json_data.get("ParquetSerDe"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class Tags:
    Key: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Tags"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Tags"]:
        if not json_data:
            return None
        return cls(
            Key=json_data.get("Key"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Tags = Tags


@dataclass
class ElasticsearchConfiguration:
    BufferingInterval: Optional[float]
    BufferingSize: Optional[float]
    DomainArn: Optional[str]
    IndexName: Optional[str]
    IndexRotationPeriod: Optional[str]
    RetryDuration: Optional[float]
    RoleArn: Optional[str]
    S3BackupMode: Optional[str]
    TypeName: Optional[str]
    CloudwatchLoggingOptions: Optional[Sequence["_CloudwatchLoggingOptions"]]
    ProcessingConfiguration: Optional[Sequence["_ProcessingConfiguration"]]

    @classmethod
    def _deserialize(
        cls: Type["_ElasticsearchConfiguration"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ElasticsearchConfiguration"]:
        if not json_data:
            return None
        return cls(
            BufferingInterval=json_data.get("BufferingInterval"),
            BufferingSize=json_data.get("BufferingSize"),
            DomainArn=json_data.get("DomainArn"),
            IndexName=json_data.get("IndexName"),
            IndexRotationPeriod=json_data.get("IndexRotationPeriod"),
            RetryDuration=json_data.get("RetryDuration"),
            RoleArn=json_data.get("RoleArn"),
            S3BackupMode=json_data.get("S3BackupMode"),
            TypeName=json_data.get("TypeName"),
            CloudwatchLoggingOptions=json_data.get("CloudwatchLoggingOptions"),
            ProcessingConfiguration=json_data.get("ProcessingConfiguration"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ElasticsearchConfiguration = ElasticsearchConfiguration


@dataclass
class CloudwatchLoggingOptions:
    Enabled: Optional[bool]
    LogGroupName: Optional[str]
    LogStreamName: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_CloudwatchLoggingOptions"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_CloudwatchLoggingOptions"]:
        if not json_data:
            return None
        return cls(
            Enabled=json_data.get("Enabled"),
            LogGroupName=json_data.get("LogGroupName"),
            LogStreamName=json_data.get("LogStreamName"),
        )


# work around possible type aliasing issues when variable has same name as a model
_CloudwatchLoggingOptions = CloudwatchLoggingOptions


@dataclass
class ProcessingConfiguration:
    Enabled: Optional[bool]
    Processors: Optional[Sequence["_Processors"]]

    @classmethod
    def _deserialize(
        cls: Type["_ProcessingConfiguration"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ProcessingConfiguration"]:
        if not json_data:
            return None
        return cls(
            Enabled=json_data.get("Enabled"),
            Processors=json_data.get("Processors"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ProcessingConfiguration = ProcessingConfiguration


@dataclass
class Processors:
    Type: Optional[str]
    Parameters: Optional[Sequence["_Parameters"]]

    @classmethod
    def _deserialize(
        cls: Type["_Processors"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Processors"]:
        if not json_data:
            return None
        return cls(
            Type=json_data.get("Type"),
            Parameters=json_data.get("Parameters"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Processors = Processors


@dataclass
class Parameters:
    ParameterName: Optional[str]
    ParameterValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Parameters"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Parameters"]:
        if not json_data:
            return None
        return cls(
            ParameterName=json_data.get("ParameterName"),
            ParameterValue=json_data.get("ParameterValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Parameters = Parameters


@dataclass
class ExtendedS3Configuration:
    BucketArn: Optional[str]
    BufferInterval: Optional[float]
    BufferSize: Optional[float]
    CompressionFormat: Optional[str]
    ErrorOutputPrefix: Optional[str]
    KmsKeyArn: Optional[str]
    Prefix: Optional[str]
    RoleArn: Optional[str]
    S3BackupMode: Optional[str]
    CloudwatchLoggingOptions: Optional[Sequence["_CloudwatchLoggingOptions"]]
    DataFormatConversionConfiguration: Optional[Sequence["_DataFormatConversionConfiguration"]]
    ProcessingConfiguration: Optional[Sequence["_ProcessingConfiguration"]]
    S3BackupConfiguration: Optional[Sequence["_S3BackupConfiguration"]]

    @classmethod
    def _deserialize(
        cls: Type["_ExtendedS3Configuration"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ExtendedS3Configuration"]:
        if not json_data:
            return None
        return cls(
            BucketArn=json_data.get("BucketArn"),
            BufferInterval=json_data.get("BufferInterval"),
            BufferSize=json_data.get("BufferSize"),
            CompressionFormat=json_data.get("CompressionFormat"),
            ErrorOutputPrefix=json_data.get("ErrorOutputPrefix"),
            KmsKeyArn=json_data.get("KmsKeyArn"),
            Prefix=json_data.get("Prefix"),
            RoleArn=json_data.get("RoleArn"),
            S3BackupMode=json_data.get("S3BackupMode"),
            CloudwatchLoggingOptions=json_data.get("CloudwatchLoggingOptions"),
            DataFormatConversionConfiguration=json_data.get("DataFormatConversionConfiguration"),
            ProcessingConfiguration=json_data.get("ProcessingConfiguration"),
            S3BackupConfiguration=json_data.get("S3BackupConfiguration"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ExtendedS3Configuration = ExtendedS3Configuration


@dataclass
class DataFormatConversionConfiguration:
    Enabled: Optional[bool]
    InputFormatConfiguration: Optional[Sequence["_InputFormatConfiguration"]]
    OutputFormatConfiguration: Optional[Sequence["_OutputFormatConfiguration"]]
    SchemaConfiguration: Optional[Sequence["_SchemaConfiguration"]]

    @classmethod
    def _deserialize(
        cls: Type["_DataFormatConversionConfiguration"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DataFormatConversionConfiguration"]:
        if not json_data:
            return None
        return cls(
            Enabled=json_data.get("Enabled"),
            InputFormatConfiguration=json_data.get("InputFormatConfiguration"),
            OutputFormatConfiguration=json_data.get("OutputFormatConfiguration"),
            SchemaConfiguration=json_data.get("SchemaConfiguration"),
        )


# work around possible type aliasing issues when variable has same name as a model
_DataFormatConversionConfiguration = DataFormatConversionConfiguration


@dataclass
class InputFormatConfiguration:
    Deserializer: Optional[Sequence["_Deserializer"]]

    @classmethod
    def _deserialize(
        cls: Type["_InputFormatConfiguration"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_InputFormatConfiguration"]:
        if not json_data:
            return None
        return cls(
            Deserializer=json_data.get("Deserializer"),
        )


# work around possible type aliasing issues when variable has same name as a model
_InputFormatConfiguration = InputFormatConfiguration


@dataclass
class Deserializer:
    HiveJsonSerDe: Optional[Sequence["_HiveJsonSerDe"]]
    OpenXJsonSerDe: Optional[Sequence["_OpenXJsonSerDe"]]

    @classmethod
    def _deserialize(
        cls: Type["_Deserializer"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Deserializer"]:
        if not json_data:
            return None
        return cls(
            HiveJsonSerDe=json_data.get("HiveJsonSerDe"),
            OpenXJsonSerDe=json_data.get("OpenXJsonSerDe"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Deserializer = Deserializer


@dataclass
class HiveJsonSerDe:
    TimestampFormats: Optional[Sequence[str]]

    @classmethod
    def _deserialize(
        cls: Type["_HiveJsonSerDe"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_HiveJsonSerDe"]:
        if not json_data:
            return None
        return cls(
            TimestampFormats=json_data.get("TimestampFormats"),
        )


# work around possible type aliasing issues when variable has same name as a model
_HiveJsonSerDe = HiveJsonSerDe


@dataclass
class OpenXJsonSerDe:
    CaseInsensitive: Optional[bool]
    ColumnToJsonKeyMappings: Optional[Sequence["_ColumnToJsonKeyMappings"]]
    ConvertDotsInJsonKeysToUnderscores: Optional[bool]

    @classmethod
    def _deserialize(
        cls: Type["_OpenXJsonSerDe"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_OpenXJsonSerDe"]:
        if not json_data:
            return None
        return cls(
            CaseInsensitive=json_data.get("CaseInsensitive"),
            ColumnToJsonKeyMappings=json_data.get("ColumnToJsonKeyMappings"),
            ConvertDotsInJsonKeysToUnderscores=json_data.get("ConvertDotsInJsonKeysToUnderscores"),
        )


# work around possible type aliasing issues when variable has same name as a model
_OpenXJsonSerDe = OpenXJsonSerDe


@dataclass
class ColumnToJsonKeyMappings:
    Key: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ColumnToJsonKeyMappings"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ColumnToJsonKeyMappings"]:
        if not json_data:
            return None
        return cls(
            Key=json_data.get("Key"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ColumnToJsonKeyMappings = ColumnToJsonKeyMappings


@dataclass
class OutputFormatConfiguration:
    Serializer: Optional[Sequence["_Serializer"]]

    @classmethod
    def _deserialize(
        cls: Type["_OutputFormatConfiguration"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_OutputFormatConfiguration"]:
        if not json_data:
            return None
        return cls(
            Serializer=json_data.get("Serializer"),
        )


# work around possible type aliasing issues when variable has same name as a model
_OutputFormatConfiguration = OutputFormatConfiguration


@dataclass
class Serializer:
    OrcSerDe: Optional[Sequence["_OrcSerDe"]]
    ParquetSerDe: Optional[Sequence["_ParquetSerDe"]]

    @classmethod
    def _deserialize(
        cls: Type["_Serializer"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Serializer"]:
        if not json_data:
            return None
        return cls(
            OrcSerDe=json_data.get("OrcSerDe"),
            ParquetSerDe=json_data.get("ParquetSerDe"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Serializer = Serializer


@dataclass
class OrcSerDe:
    BlockSizeBytes: Optional[float]
    BloomFilterColumns: Optional[Sequence[str]]
    BloomFilterFalsePositiveProbability: Optional[float]
    Compression: Optional[str]
    DictionaryKeyThreshold: Optional[float]
    EnablePadding: Optional[bool]
    FormatVersion: Optional[str]
    PaddingTolerance: Optional[float]
    RowIndexStride: Optional[float]
    StripeSizeBytes: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_OrcSerDe"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_OrcSerDe"]:
        if not json_data:
            return None
        return cls(
            BlockSizeBytes=json_data.get("BlockSizeBytes"),
            BloomFilterColumns=json_data.get("BloomFilterColumns"),
            BloomFilterFalsePositiveProbability=json_data.get("BloomFilterFalsePositiveProbability"),
            Compression=json_data.get("Compression"),
            DictionaryKeyThreshold=json_data.get("DictionaryKeyThreshold"),
            EnablePadding=json_data.get("EnablePadding"),
            FormatVersion=json_data.get("FormatVersion"),
            PaddingTolerance=json_data.get("PaddingTolerance"),
            RowIndexStride=json_data.get("RowIndexStride"),
            StripeSizeBytes=json_data.get("StripeSizeBytes"),
        )


# work around possible type aliasing issues when variable has same name as a model
_OrcSerDe = OrcSerDe


@dataclass
class ParquetSerDe:
    BlockSizeBytes: Optional[float]
    Compression: Optional[str]
    EnableDictionaryCompression: Optional[bool]
    MaxPaddingBytes: Optional[float]
    PageSizeBytes: Optional[float]
    WriterVersion: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ParquetSerDe"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ParquetSerDe"]:
        if not json_data:
            return None
        return cls(
            BlockSizeBytes=json_data.get("BlockSizeBytes"),
            Compression=json_data.get("Compression"),
            EnableDictionaryCompression=json_data.get("EnableDictionaryCompression"),
            MaxPaddingBytes=json_data.get("MaxPaddingBytes"),
            PageSizeBytes=json_data.get("PageSizeBytes"),
            WriterVersion=json_data.get("WriterVersion"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ParquetSerDe = ParquetSerDe


@dataclass
class SchemaConfiguration:
    CatalogId: Optional[str]
    DatabaseName: Optional[str]
    Region: Optional[str]
    RoleArn: Optional[str]
    TableName: Optional[str]
    VersionId: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_SchemaConfiguration"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SchemaConfiguration"]:
        if not json_data:
            return None
        return cls(
            CatalogId=json_data.get("CatalogId"),
            DatabaseName=json_data.get("DatabaseName"),
            Region=json_data.get("Region"),
            RoleArn=json_data.get("RoleArn"),
            TableName=json_data.get("TableName"),
            VersionId=json_data.get("VersionId"),
        )


# work around possible type aliasing issues when variable has same name as a model
_SchemaConfiguration = SchemaConfiguration


@dataclass
class S3BackupConfiguration:
    BucketArn: Optional[str]
    BufferInterval: Optional[float]
    BufferSize: Optional[float]
    CompressionFormat: Optional[str]
    KmsKeyArn: Optional[str]
    Prefix: Optional[str]
    RoleArn: Optional[str]
    CloudwatchLoggingOptions: Optional[Sequence["_CloudwatchLoggingOptions"]]

    @classmethod
    def _deserialize(
        cls: Type["_S3BackupConfiguration"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_S3BackupConfiguration"]:
        if not json_data:
            return None
        return cls(
            BucketArn=json_data.get("BucketArn"),
            BufferInterval=json_data.get("BufferInterval"),
            BufferSize=json_data.get("BufferSize"),
            CompressionFormat=json_data.get("CompressionFormat"),
            KmsKeyArn=json_data.get("KmsKeyArn"),
            Prefix=json_data.get("Prefix"),
            RoleArn=json_data.get("RoleArn"),
            CloudwatchLoggingOptions=json_data.get("CloudwatchLoggingOptions"),
        )


# work around possible type aliasing issues when variable has same name as a model
_S3BackupConfiguration = S3BackupConfiguration


@dataclass
class KinesisSourceConfiguration:
    KinesisStreamArn: Optional[str]
    RoleArn: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_KinesisSourceConfiguration"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_KinesisSourceConfiguration"]:
        if not json_data:
            return None
        return cls(
            KinesisStreamArn=json_data.get("KinesisStreamArn"),
            RoleArn=json_data.get("RoleArn"),
        )


# work around possible type aliasing issues when variable has same name as a model
_KinesisSourceConfiguration = KinesisSourceConfiguration


@dataclass
class RedshiftConfiguration:
    ClusterJdbcurl: Optional[str]
    CopyOptions: Optional[str]
    DataTableColumns: Optional[str]
    DataTableName: Optional[str]
    Password: Optional[str]
    RetryDuration: Optional[float]
    RoleArn: Optional[str]
    S3BackupMode: Optional[str]
    Username: Optional[str]
    CloudwatchLoggingOptions: Optional[Sequence["_CloudwatchLoggingOptions"]]
    ProcessingConfiguration: Optional[Sequence["_ProcessingConfiguration"]]
    S3BackupConfiguration: Optional[Sequence["_S3BackupConfiguration"]]

    @classmethod
    def _deserialize(
        cls: Type["_RedshiftConfiguration"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_RedshiftConfiguration"]:
        if not json_data:
            return None
        return cls(
            ClusterJdbcurl=json_data.get("ClusterJdbcurl"),
            CopyOptions=json_data.get("CopyOptions"),
            DataTableColumns=json_data.get("DataTableColumns"),
            DataTableName=json_data.get("DataTableName"),
            Password=json_data.get("Password"),
            RetryDuration=json_data.get("RetryDuration"),
            RoleArn=json_data.get("RoleArn"),
            S3BackupMode=json_data.get("S3BackupMode"),
            Username=json_data.get("Username"),
            CloudwatchLoggingOptions=json_data.get("CloudwatchLoggingOptions"),
            ProcessingConfiguration=json_data.get("ProcessingConfiguration"),
            S3BackupConfiguration=json_data.get("S3BackupConfiguration"),
        )


# work around possible type aliasing issues when variable has same name as a model
_RedshiftConfiguration = RedshiftConfiguration


@dataclass
class S3Configuration:
    BucketArn: Optional[str]
    BufferInterval: Optional[float]
    BufferSize: Optional[float]
    CompressionFormat: Optional[str]
    KmsKeyArn: Optional[str]
    Prefix: Optional[str]
    RoleArn: Optional[str]
    CloudwatchLoggingOptions: Optional[Sequence["_CloudwatchLoggingOptions"]]

    @classmethod
    def _deserialize(
        cls: Type["_S3Configuration"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_S3Configuration"]:
        if not json_data:
            return None
        return cls(
            BucketArn=json_data.get("BucketArn"),
            BufferInterval=json_data.get("BufferInterval"),
            BufferSize=json_data.get("BufferSize"),
            CompressionFormat=json_data.get("CompressionFormat"),
            KmsKeyArn=json_data.get("KmsKeyArn"),
            Prefix=json_data.get("Prefix"),
            RoleArn=json_data.get("RoleArn"),
            CloudwatchLoggingOptions=json_data.get("CloudwatchLoggingOptions"),
        )


# work around possible type aliasing issues when variable has same name as a model
_S3Configuration = S3Configuration


@dataclass
class ServerSideEncryption:
    Enabled: Optional[bool]

    @classmethod
    def _deserialize(
        cls: Type["_ServerSideEncryption"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ServerSideEncryption"]:
        if not json_data:
            return None
        return cls(
            Enabled=json_data.get("Enabled"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ServerSideEncryption = ServerSideEncryption


@dataclass
class SplunkConfiguration:
    HecAcknowledgmentTimeout: Optional[float]
    HecEndpoint: Optional[str]
    HecEndpointType: Optional[str]
    HecToken: Optional[str]
    RetryDuration: Optional[float]
    S3BackupMode: Optional[str]
    CloudwatchLoggingOptions: Optional[Sequence["_CloudwatchLoggingOptions"]]
    ProcessingConfiguration: Optional[Sequence["_ProcessingConfiguration"]]

    @classmethod
    def _deserialize(
        cls: Type["_SplunkConfiguration"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SplunkConfiguration"]:
        if not json_data:
            return None
        return cls(
            HecAcknowledgmentTimeout=json_data.get("HecAcknowledgmentTimeout"),
            HecEndpoint=json_data.get("HecEndpoint"),
            HecEndpointType=json_data.get("HecEndpointType"),
            HecToken=json_data.get("HecToken"),
            RetryDuration=json_data.get("RetryDuration"),
            S3BackupMode=json_data.get("S3BackupMode"),
            CloudwatchLoggingOptions=json_data.get("CloudwatchLoggingOptions"),
            ProcessingConfiguration=json_data.get("ProcessingConfiguration"),
        )


# work around possible type aliasing issues when variable has same name as a model
_SplunkConfiguration = SplunkConfiguration


