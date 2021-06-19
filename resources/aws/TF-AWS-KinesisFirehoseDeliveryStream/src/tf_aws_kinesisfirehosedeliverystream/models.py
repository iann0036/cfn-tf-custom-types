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
    Destination: Optional[str]
    DestinationId: Optional[str]
    Id: Optional[str]
    Name: Optional[str]
    Tags: Optional[Sequence["_TagsDefinition"]]
    TagsAll: Optional[Sequence["_TagsAllDefinition"]]
    VersionId: Optional[str]
    ElasticsearchConfiguration: Optional[Sequence["_ElasticsearchConfigurationDefinition"]]
    ExtendedS3Configuration: Optional[Sequence["_ExtendedS3ConfigurationDefinition"]]
    HttpEndpointConfiguration: Optional[Sequence["_HttpEndpointConfigurationDefinition"]]
    KinesisSourceConfiguration: Optional[Sequence["_KinesisSourceConfigurationDefinition"]]
    RedshiftConfiguration: Optional[Sequence["_RedshiftConfigurationDefinition"]]
    S3Configuration: Optional[Sequence["_S3ConfigurationDefinition"]]
    ServerSideEncryption: Optional[Sequence["_ServerSideEncryptionDefinition"]]
    SplunkConfiguration: Optional[Sequence["_SplunkConfigurationDefinition"]]

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
            Destination=json_data.get("Destination"),
            DestinationId=json_data.get("DestinationId"),
            Id=json_data.get("Id"),
            Name=json_data.get("Name"),
            Tags=deserialize_list(json_data.get("Tags"), TagsDefinition),
            TagsAll=deserialize_list(json_data.get("TagsAll"), TagsAllDefinition),
            VersionId=json_data.get("VersionId"),
            ElasticsearchConfiguration=deserialize_list(json_data.get("ElasticsearchConfiguration"), ElasticsearchConfigurationDefinition),
            ExtendedS3Configuration=deserialize_list(json_data.get("ExtendedS3Configuration"), ExtendedS3ConfigurationDefinition),
            HttpEndpointConfiguration=deserialize_list(json_data.get("HttpEndpointConfiguration"), HttpEndpointConfigurationDefinition),
            KinesisSourceConfiguration=deserialize_list(json_data.get("KinesisSourceConfiguration"), KinesisSourceConfigurationDefinition),
            RedshiftConfiguration=deserialize_list(json_data.get("RedshiftConfiguration"), RedshiftConfigurationDefinition),
            S3Configuration=deserialize_list(json_data.get("S3Configuration"), S3ConfigurationDefinition),
            ServerSideEncryption=deserialize_list(json_data.get("ServerSideEncryption"), ServerSideEncryptionDefinition),
            SplunkConfiguration=deserialize_list(json_data.get("SplunkConfiguration"), SplunkConfigurationDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


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
class ElasticsearchConfigurationDefinition(BaseModel):
    BufferingInterval: Optional[float]
    BufferingSize: Optional[float]
    ClusterEndpoint: Optional[str]
    DomainArn: Optional[str]
    IndexName: Optional[str]
    IndexRotationPeriod: Optional[str]
    RetryDuration: Optional[float]
    RoleArn: Optional[str]
    S3BackupMode: Optional[str]
    TypeName: Optional[str]
    CloudwatchLoggingOptions: Optional[Sequence["_CloudwatchLoggingOptionsDefinition"]]
    ProcessingConfiguration: Optional[Sequence["_ProcessingConfigurationDefinition"]]
    VpcConfig: Optional[Sequence["_VpcConfigDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_ElasticsearchConfigurationDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ElasticsearchConfigurationDefinition"]:
        if not json_data:
            return None
        return cls(
            BufferingInterval=json_data.get("BufferingInterval"),
            BufferingSize=json_data.get("BufferingSize"),
            ClusterEndpoint=json_data.get("ClusterEndpoint"),
            DomainArn=json_data.get("DomainArn"),
            IndexName=json_data.get("IndexName"),
            IndexRotationPeriod=json_data.get("IndexRotationPeriod"),
            RetryDuration=json_data.get("RetryDuration"),
            RoleArn=json_data.get("RoleArn"),
            S3BackupMode=json_data.get("S3BackupMode"),
            TypeName=json_data.get("TypeName"),
            CloudwatchLoggingOptions=deserialize_list(json_data.get("CloudwatchLoggingOptions"), CloudwatchLoggingOptionsDefinition),
            ProcessingConfiguration=deserialize_list(json_data.get("ProcessingConfiguration"), ProcessingConfigurationDefinition),
            VpcConfig=deserialize_list(json_data.get("VpcConfig"), VpcConfigDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ElasticsearchConfigurationDefinition = ElasticsearchConfigurationDefinition


@dataclass
class CloudwatchLoggingOptionsDefinition(BaseModel):
    Enabled: Optional[bool]
    LogGroupName: Optional[str]
    LogStreamName: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_CloudwatchLoggingOptionsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_CloudwatchLoggingOptionsDefinition"]:
        if not json_data:
            return None
        return cls(
            Enabled=json_data.get("Enabled"),
            LogGroupName=json_data.get("LogGroupName"),
            LogStreamName=json_data.get("LogStreamName"),
        )


# work around possible type aliasing issues when variable has same name as a model
_CloudwatchLoggingOptionsDefinition = CloudwatchLoggingOptionsDefinition


@dataclass
class ProcessingConfigurationDefinition(BaseModel):
    Enabled: Optional[bool]
    Processors: Optional[Sequence["_ProcessorsDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_ProcessingConfigurationDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ProcessingConfigurationDefinition"]:
        if not json_data:
            return None
        return cls(
            Enabled=json_data.get("Enabled"),
            Processors=deserialize_list(json_data.get("Processors"), ProcessorsDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ProcessingConfigurationDefinition = ProcessingConfigurationDefinition


@dataclass
class ProcessorsDefinition(BaseModel):
    Type: Optional[str]
    Parameters: Optional[Sequence["_ParametersDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_ProcessorsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ProcessorsDefinition"]:
        if not json_data:
            return None
        return cls(
            Type=json_data.get("Type"),
            Parameters=deserialize_list(json_data.get("Parameters"), ParametersDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ProcessorsDefinition = ProcessorsDefinition


@dataclass
class ParametersDefinition(BaseModel):
    ParameterName: Optional[str]
    ParameterValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ParametersDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ParametersDefinition"]:
        if not json_data:
            return None
        return cls(
            ParameterName=json_data.get("ParameterName"),
            ParameterValue=json_data.get("ParameterValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ParametersDefinition = ParametersDefinition


@dataclass
class VpcConfigDefinition(BaseModel):
    RoleArn: Optional[str]
    SecurityGroupIds: Optional[Sequence[str]]
    SubnetIds: Optional[Sequence[str]]

    @classmethod
    def _deserialize(
        cls: Type["_VpcConfigDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_VpcConfigDefinition"]:
        if not json_data:
            return None
        return cls(
            RoleArn=json_data.get("RoleArn"),
            SecurityGroupIds=json_data.get("SecurityGroupIds"),
            SubnetIds=json_data.get("SubnetIds"),
        )


# work around possible type aliasing issues when variable has same name as a model
_VpcConfigDefinition = VpcConfigDefinition


@dataclass
class ExtendedS3ConfigurationDefinition(BaseModel):
    BucketArn: Optional[str]
    BufferInterval: Optional[float]
    BufferSize: Optional[float]
    CompressionFormat: Optional[str]
    ErrorOutputPrefix: Optional[str]
    KmsKeyArn: Optional[str]
    Prefix: Optional[str]
    RoleArn: Optional[str]
    S3BackupMode: Optional[str]
    CloudwatchLoggingOptions: Optional[Sequence["_CloudwatchLoggingOptionsDefinition"]]
    DataFormatConversionConfiguration: Optional[Sequence["_DataFormatConversionConfigurationDefinition"]]
    ProcessingConfiguration: Optional[Sequence["_ProcessingConfigurationDefinition"]]
    S3BackupConfiguration: Optional[Sequence["_S3BackupConfigurationDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_ExtendedS3ConfigurationDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ExtendedS3ConfigurationDefinition"]:
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
            CloudwatchLoggingOptions=deserialize_list(json_data.get("CloudwatchLoggingOptions"), CloudwatchLoggingOptionsDefinition),
            DataFormatConversionConfiguration=deserialize_list(json_data.get("DataFormatConversionConfiguration"), DataFormatConversionConfigurationDefinition),
            ProcessingConfiguration=deserialize_list(json_data.get("ProcessingConfiguration"), ProcessingConfigurationDefinition),
            S3BackupConfiguration=deserialize_list(json_data.get("S3BackupConfiguration"), S3BackupConfigurationDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ExtendedS3ConfigurationDefinition = ExtendedS3ConfigurationDefinition


@dataclass
class DataFormatConversionConfigurationDefinition(BaseModel):
    Enabled: Optional[bool]
    InputFormatConfiguration: Optional[Sequence["_InputFormatConfigurationDefinition"]]
    OutputFormatConfiguration: Optional[Sequence["_OutputFormatConfigurationDefinition"]]
    SchemaConfiguration: Optional[Sequence["_SchemaConfigurationDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_DataFormatConversionConfigurationDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DataFormatConversionConfigurationDefinition"]:
        if not json_data:
            return None
        return cls(
            Enabled=json_data.get("Enabled"),
            InputFormatConfiguration=deserialize_list(json_data.get("InputFormatConfiguration"), InputFormatConfigurationDefinition),
            OutputFormatConfiguration=deserialize_list(json_data.get("OutputFormatConfiguration"), OutputFormatConfigurationDefinition),
            SchemaConfiguration=deserialize_list(json_data.get("SchemaConfiguration"), SchemaConfigurationDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_DataFormatConversionConfigurationDefinition = DataFormatConversionConfigurationDefinition


@dataclass
class InputFormatConfigurationDefinition(BaseModel):
    Deserializer: Optional[Sequence["_DeserializerDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_InputFormatConfigurationDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_InputFormatConfigurationDefinition"]:
        if not json_data:
            return None
        return cls(
            Deserializer=deserialize_list(json_data.get("Deserializer"), DeserializerDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_InputFormatConfigurationDefinition = InputFormatConfigurationDefinition


@dataclass
class DeserializerDefinition(BaseModel):
    HiveJsonSerDe: Optional[Sequence["_HiveJsonSerDeDefinition"]]
    OpenXJsonSerDe: Optional[Sequence["_OpenXJsonSerDeDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_DeserializerDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DeserializerDefinition"]:
        if not json_data:
            return None
        return cls(
            HiveJsonSerDe=deserialize_list(json_data.get("HiveJsonSerDe"), HiveJsonSerDeDefinition),
            OpenXJsonSerDe=deserialize_list(json_data.get("OpenXJsonSerDe"), OpenXJsonSerDeDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_DeserializerDefinition = DeserializerDefinition


@dataclass
class HiveJsonSerDeDefinition(BaseModel):
    TimestampFormats: Optional[Sequence[str]]

    @classmethod
    def _deserialize(
        cls: Type["_HiveJsonSerDeDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_HiveJsonSerDeDefinition"]:
        if not json_data:
            return None
        return cls(
            TimestampFormats=json_data.get("TimestampFormats"),
        )


# work around possible type aliasing issues when variable has same name as a model
_HiveJsonSerDeDefinition = HiveJsonSerDeDefinition


@dataclass
class OpenXJsonSerDeDefinition(BaseModel):
    CaseInsensitive: Optional[bool]
    ColumnToJsonKeyMappings: Optional[Sequence["_ColumnToJsonKeyMappingsDefinition"]]
    ConvertDotsInJsonKeysToUnderscores: Optional[bool]

    @classmethod
    def _deserialize(
        cls: Type["_OpenXJsonSerDeDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_OpenXJsonSerDeDefinition"]:
        if not json_data:
            return None
        return cls(
            CaseInsensitive=json_data.get("CaseInsensitive"),
            ColumnToJsonKeyMappings=deserialize_list(json_data.get("ColumnToJsonKeyMappings"), ColumnToJsonKeyMappingsDefinition),
            ConvertDotsInJsonKeysToUnderscores=json_data.get("ConvertDotsInJsonKeysToUnderscores"),
        )


# work around possible type aliasing issues when variable has same name as a model
_OpenXJsonSerDeDefinition = OpenXJsonSerDeDefinition


@dataclass
class ColumnToJsonKeyMappingsDefinition(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ColumnToJsonKeyMappingsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ColumnToJsonKeyMappingsDefinition"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ColumnToJsonKeyMappingsDefinition = ColumnToJsonKeyMappingsDefinition


@dataclass
class OutputFormatConfigurationDefinition(BaseModel):
    Serializer: Optional[Sequence["_SerializerDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_OutputFormatConfigurationDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_OutputFormatConfigurationDefinition"]:
        if not json_data:
            return None
        return cls(
            Serializer=deserialize_list(json_data.get("Serializer"), SerializerDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_OutputFormatConfigurationDefinition = OutputFormatConfigurationDefinition


@dataclass
class SerializerDefinition(BaseModel):
    OrcSerDe: Optional[Sequence["_OrcSerDeDefinition"]]
    ParquetSerDe: Optional[Sequence["_ParquetSerDeDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_SerializerDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SerializerDefinition"]:
        if not json_data:
            return None
        return cls(
            OrcSerDe=deserialize_list(json_data.get("OrcSerDe"), OrcSerDeDefinition),
            ParquetSerDe=deserialize_list(json_data.get("ParquetSerDe"), ParquetSerDeDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_SerializerDefinition = SerializerDefinition


@dataclass
class OrcSerDeDefinition(BaseModel):
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
        cls: Type["_OrcSerDeDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_OrcSerDeDefinition"]:
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
_OrcSerDeDefinition = OrcSerDeDefinition


@dataclass
class ParquetSerDeDefinition(BaseModel):
    BlockSizeBytes: Optional[float]
    Compression: Optional[str]
    EnableDictionaryCompression: Optional[bool]
    MaxPaddingBytes: Optional[float]
    PageSizeBytes: Optional[float]
    WriterVersion: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ParquetSerDeDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ParquetSerDeDefinition"]:
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
_ParquetSerDeDefinition = ParquetSerDeDefinition


@dataclass
class SchemaConfigurationDefinition(BaseModel):
    CatalogId: Optional[str]
    DatabaseName: Optional[str]
    Region: Optional[str]
    RoleArn: Optional[str]
    TableName: Optional[str]
    VersionId: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_SchemaConfigurationDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SchemaConfigurationDefinition"]:
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
_SchemaConfigurationDefinition = SchemaConfigurationDefinition


@dataclass
class S3BackupConfigurationDefinition(BaseModel):
    BucketArn: Optional[str]
    BufferInterval: Optional[float]
    BufferSize: Optional[float]
    CompressionFormat: Optional[str]
    KmsKeyArn: Optional[str]
    Prefix: Optional[str]
    RoleArn: Optional[str]
    CloudwatchLoggingOptions: Optional[Sequence["_CloudwatchLoggingOptionsDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_S3BackupConfigurationDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_S3BackupConfigurationDefinition"]:
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
            CloudwatchLoggingOptions=deserialize_list(json_data.get("CloudwatchLoggingOptions"), CloudwatchLoggingOptionsDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_S3BackupConfigurationDefinition = S3BackupConfigurationDefinition


@dataclass
class HttpEndpointConfigurationDefinition(BaseModel):
    AccessKey: Optional[str]
    BufferingInterval: Optional[float]
    BufferingSize: Optional[float]
    Name: Optional[str]
    RetryDuration: Optional[float]
    RoleArn: Optional[str]
    S3BackupMode: Optional[str]
    Url: Optional[str]
    CloudwatchLoggingOptions: Optional[Sequence["_CloudwatchLoggingOptionsDefinition"]]
    ProcessingConfiguration: Optional[Sequence["_ProcessingConfigurationDefinition"]]
    RequestConfiguration: Optional[Sequence["_RequestConfigurationDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_HttpEndpointConfigurationDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_HttpEndpointConfigurationDefinition"]:
        if not json_data:
            return None
        return cls(
            AccessKey=json_data.get("AccessKey"),
            BufferingInterval=json_data.get("BufferingInterval"),
            BufferingSize=json_data.get("BufferingSize"),
            Name=json_data.get("Name"),
            RetryDuration=json_data.get("RetryDuration"),
            RoleArn=json_data.get("RoleArn"),
            S3BackupMode=json_data.get("S3BackupMode"),
            Url=json_data.get("Url"),
            CloudwatchLoggingOptions=deserialize_list(json_data.get("CloudwatchLoggingOptions"), CloudwatchLoggingOptionsDefinition),
            ProcessingConfiguration=deserialize_list(json_data.get("ProcessingConfiguration"), ProcessingConfigurationDefinition),
            RequestConfiguration=deserialize_list(json_data.get("RequestConfiguration"), RequestConfigurationDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_HttpEndpointConfigurationDefinition = HttpEndpointConfigurationDefinition


@dataclass
class RequestConfigurationDefinition(BaseModel):
    ContentEncoding: Optional[str]
    CommonAttributes: Optional[Sequence["_CommonAttributesDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_RequestConfigurationDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_RequestConfigurationDefinition"]:
        if not json_data:
            return None
        return cls(
            ContentEncoding=json_data.get("ContentEncoding"),
            CommonAttributes=deserialize_list(json_data.get("CommonAttributes"), CommonAttributesDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_RequestConfigurationDefinition = RequestConfigurationDefinition


@dataclass
class CommonAttributesDefinition(BaseModel):
    Name: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_CommonAttributesDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_CommonAttributesDefinition"]:
        if not json_data:
            return None
        return cls(
            Name=json_data.get("Name"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_CommonAttributesDefinition = CommonAttributesDefinition


@dataclass
class KinesisSourceConfigurationDefinition(BaseModel):
    KinesisStreamArn: Optional[str]
    RoleArn: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_KinesisSourceConfigurationDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_KinesisSourceConfigurationDefinition"]:
        if not json_data:
            return None
        return cls(
            KinesisStreamArn=json_data.get("KinesisStreamArn"),
            RoleArn=json_data.get("RoleArn"),
        )


# work around possible type aliasing issues when variable has same name as a model
_KinesisSourceConfigurationDefinition = KinesisSourceConfigurationDefinition


@dataclass
class RedshiftConfigurationDefinition(BaseModel):
    ClusterJdbcurl: Optional[str]
    CopyOptions: Optional[str]
    DataTableColumns: Optional[str]
    DataTableName: Optional[str]
    Password: Optional[str]
    RetryDuration: Optional[float]
    RoleArn: Optional[str]
    S3BackupMode: Optional[str]
    Username: Optional[str]
    CloudwatchLoggingOptions: Optional[Sequence["_CloudwatchLoggingOptionsDefinition"]]
    ProcessingConfiguration: Optional[Sequence["_ProcessingConfigurationDefinition"]]
    S3BackupConfiguration: Optional[Sequence["_S3BackupConfigurationDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_RedshiftConfigurationDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_RedshiftConfigurationDefinition"]:
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
            CloudwatchLoggingOptions=deserialize_list(json_data.get("CloudwatchLoggingOptions"), CloudwatchLoggingOptionsDefinition),
            ProcessingConfiguration=deserialize_list(json_data.get("ProcessingConfiguration"), ProcessingConfigurationDefinition),
            S3BackupConfiguration=deserialize_list(json_data.get("S3BackupConfiguration"), S3BackupConfigurationDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_RedshiftConfigurationDefinition = RedshiftConfigurationDefinition


@dataclass
class S3ConfigurationDefinition(BaseModel):
    BucketArn: Optional[str]
    BufferInterval: Optional[float]
    BufferSize: Optional[float]
    CompressionFormat: Optional[str]
    KmsKeyArn: Optional[str]
    Prefix: Optional[str]
    RoleArn: Optional[str]
    CloudwatchLoggingOptions: Optional[Sequence["_CloudwatchLoggingOptionsDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_S3ConfigurationDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_S3ConfigurationDefinition"]:
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
            CloudwatchLoggingOptions=deserialize_list(json_data.get("CloudwatchLoggingOptions"), CloudwatchLoggingOptionsDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_S3ConfigurationDefinition = S3ConfigurationDefinition


@dataclass
class ServerSideEncryptionDefinition(BaseModel):
    Enabled: Optional[bool]
    KeyArn: Optional[str]
    KeyType: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ServerSideEncryptionDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ServerSideEncryptionDefinition"]:
        if not json_data:
            return None
        return cls(
            Enabled=json_data.get("Enabled"),
            KeyArn=json_data.get("KeyArn"),
            KeyType=json_data.get("KeyType"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ServerSideEncryptionDefinition = ServerSideEncryptionDefinition


@dataclass
class SplunkConfigurationDefinition(BaseModel):
    HecAcknowledgmentTimeout: Optional[float]
    HecEndpoint: Optional[str]
    HecEndpointType: Optional[str]
    HecToken: Optional[str]
    RetryDuration: Optional[float]
    S3BackupMode: Optional[str]
    CloudwatchLoggingOptions: Optional[Sequence["_CloudwatchLoggingOptionsDefinition"]]
    ProcessingConfiguration: Optional[Sequence["_ProcessingConfigurationDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_SplunkConfigurationDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SplunkConfigurationDefinition"]:
        if not json_data:
            return None
        return cls(
            HecAcknowledgmentTimeout=json_data.get("HecAcknowledgmentTimeout"),
            HecEndpoint=json_data.get("HecEndpoint"),
            HecEndpointType=json_data.get("HecEndpointType"),
            HecToken=json_data.get("HecToken"),
            RetryDuration=json_data.get("RetryDuration"),
            S3BackupMode=json_data.get("S3BackupMode"),
            CloudwatchLoggingOptions=deserialize_list(json_data.get("CloudwatchLoggingOptions"), CloudwatchLoggingOptionsDefinition),
            ProcessingConfiguration=deserialize_list(json_data.get("ProcessingConfiguration"), ProcessingConfigurationDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_SplunkConfigurationDefinition = SplunkConfigurationDefinition


