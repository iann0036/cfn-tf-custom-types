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
    CreateTimestamp: Optional[str]
    Description: Optional[str]
    ForceStop: Optional[bool]
    Id: Optional[str]
    LastUpdateTimestamp: Optional[str]
    Name: Optional[str]
    RuntimeEnvironment: Optional[str]
    ServiceExecutionRole: Optional[str]
    StartApplication: Optional[bool]
    Status: Optional[str]
    Tags: Optional[Sequence["_TagsDefinition"]]
    TagsAll: Optional[Sequence["_TagsAllDefinition"]]
    VersionId: Optional[float]
    ApplicationConfiguration: Optional[Sequence["_ApplicationConfigurationDefinition"]]
    CloudwatchLoggingOptions: Optional[Sequence["_CloudwatchLoggingOptionsDefinition"]]

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
            CreateTimestamp=json_data.get("CreateTimestamp"),
            Description=json_data.get("Description"),
            ForceStop=json_data.get("ForceStop"),
            Id=json_data.get("Id"),
            LastUpdateTimestamp=json_data.get("LastUpdateTimestamp"),
            Name=json_data.get("Name"),
            RuntimeEnvironment=json_data.get("RuntimeEnvironment"),
            ServiceExecutionRole=json_data.get("ServiceExecutionRole"),
            StartApplication=json_data.get("StartApplication"),
            Status=json_data.get("Status"),
            Tags=deserialize_list(json_data.get("Tags"), TagsDefinition),
            TagsAll=deserialize_list(json_data.get("TagsAll"), TagsAllDefinition),
            VersionId=json_data.get("VersionId"),
            ApplicationConfiguration=deserialize_list(json_data.get("ApplicationConfiguration"), ApplicationConfigurationDefinition),
            CloudwatchLoggingOptions=deserialize_list(json_data.get("CloudwatchLoggingOptions"), CloudwatchLoggingOptionsDefinition),
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
class ApplicationConfigurationDefinition(BaseModel):
    ApplicationCodeConfiguration: Optional[Sequence["_ApplicationCodeConfigurationDefinition"]]
    ApplicationSnapshotConfiguration: Optional[Sequence["_ApplicationSnapshotConfigurationDefinition"]]
    EnvironmentProperties: Optional[Sequence["_EnvironmentPropertiesDefinition"]]
    FlinkApplicationConfiguration: Optional[Sequence["_FlinkApplicationConfigurationDefinition"]]
    RunConfiguration: Optional[Sequence["_RunConfigurationDefinition"]]
    SqlApplicationConfiguration: Optional[Sequence["_SqlApplicationConfigurationDefinition"]]
    VpcConfiguration: Optional[Sequence["_VpcConfigurationDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_ApplicationConfigurationDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ApplicationConfigurationDefinition"]:
        if not json_data:
            return None
        return cls(
            ApplicationCodeConfiguration=deserialize_list(json_data.get("ApplicationCodeConfiguration"), ApplicationCodeConfigurationDefinition),
            ApplicationSnapshotConfiguration=deserialize_list(json_data.get("ApplicationSnapshotConfiguration"), ApplicationSnapshotConfigurationDefinition),
            EnvironmentProperties=deserialize_list(json_data.get("EnvironmentProperties"), EnvironmentPropertiesDefinition),
            FlinkApplicationConfiguration=deserialize_list(json_data.get("FlinkApplicationConfiguration"), FlinkApplicationConfigurationDefinition),
            RunConfiguration=deserialize_list(json_data.get("RunConfiguration"), RunConfigurationDefinition),
            SqlApplicationConfiguration=deserialize_list(json_data.get("SqlApplicationConfiguration"), SqlApplicationConfigurationDefinition),
            VpcConfiguration=deserialize_list(json_data.get("VpcConfiguration"), VpcConfigurationDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ApplicationConfigurationDefinition = ApplicationConfigurationDefinition


@dataclass
class ApplicationCodeConfigurationDefinition(BaseModel):
    CodeContentType: Optional[str]
    CodeContent: Optional[Sequence["_CodeContentDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_ApplicationCodeConfigurationDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ApplicationCodeConfigurationDefinition"]:
        if not json_data:
            return None
        return cls(
            CodeContentType=json_data.get("CodeContentType"),
            CodeContent=deserialize_list(json_data.get("CodeContent"), CodeContentDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ApplicationCodeConfigurationDefinition = ApplicationCodeConfigurationDefinition


@dataclass
class CodeContentDefinition(BaseModel):
    TextContent: Optional[str]
    S3ContentLocation: Optional[Sequence["_S3ContentLocationDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_CodeContentDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_CodeContentDefinition"]:
        if not json_data:
            return None
        return cls(
            TextContent=json_data.get("TextContent"),
            S3ContentLocation=deserialize_list(json_data.get("S3ContentLocation"), S3ContentLocationDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_CodeContentDefinition = CodeContentDefinition


@dataclass
class S3ContentLocationDefinition(BaseModel):
    BucketArn: Optional[str]
    FileKey: Optional[str]
    ObjectVersion: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_S3ContentLocationDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_S3ContentLocationDefinition"]:
        if not json_data:
            return None
        return cls(
            BucketArn=json_data.get("BucketArn"),
            FileKey=json_data.get("FileKey"),
            ObjectVersion=json_data.get("ObjectVersion"),
        )


# work around possible type aliasing issues when variable has same name as a model
_S3ContentLocationDefinition = S3ContentLocationDefinition


@dataclass
class ApplicationSnapshotConfigurationDefinition(BaseModel):
    SnapshotsEnabled: Optional[bool]

    @classmethod
    def _deserialize(
        cls: Type["_ApplicationSnapshotConfigurationDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ApplicationSnapshotConfigurationDefinition"]:
        if not json_data:
            return None
        return cls(
            SnapshotsEnabled=json_data.get("SnapshotsEnabled"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ApplicationSnapshotConfigurationDefinition = ApplicationSnapshotConfigurationDefinition


@dataclass
class EnvironmentPropertiesDefinition(BaseModel):
    PropertyGroup: Optional[Sequence["_PropertyGroupDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_EnvironmentPropertiesDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_EnvironmentPropertiesDefinition"]:
        if not json_data:
            return None
        return cls(
            PropertyGroup=deserialize_list(json_data.get("PropertyGroup"), PropertyGroupDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_EnvironmentPropertiesDefinition = EnvironmentPropertiesDefinition


@dataclass
class PropertyGroupDefinition(BaseModel):
    PropertyGroupId: Optional[str]
    PropertyMap: Optional[Sequence["_PropertyMapDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_PropertyGroupDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_PropertyGroupDefinition"]:
        if not json_data:
            return None
        return cls(
            PropertyGroupId=json_data.get("PropertyGroupId"),
            PropertyMap=deserialize_list(json_data.get("PropertyMap"), PropertyMapDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_PropertyGroupDefinition = PropertyGroupDefinition


@dataclass
class PropertyMapDefinition(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_PropertyMapDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_PropertyMapDefinition"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_PropertyMapDefinition = PropertyMapDefinition


@dataclass
class FlinkApplicationConfigurationDefinition(BaseModel):
    CheckpointConfiguration: Optional[Sequence["_CheckpointConfigurationDefinition"]]
    MonitoringConfiguration: Optional[Sequence["_MonitoringConfigurationDefinition"]]
    ParallelismConfiguration: Optional[Sequence["_ParallelismConfigurationDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_FlinkApplicationConfigurationDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_FlinkApplicationConfigurationDefinition"]:
        if not json_data:
            return None
        return cls(
            CheckpointConfiguration=deserialize_list(json_data.get("CheckpointConfiguration"), CheckpointConfigurationDefinition),
            MonitoringConfiguration=deserialize_list(json_data.get("MonitoringConfiguration"), MonitoringConfigurationDefinition),
            ParallelismConfiguration=deserialize_list(json_data.get("ParallelismConfiguration"), ParallelismConfigurationDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_FlinkApplicationConfigurationDefinition = FlinkApplicationConfigurationDefinition


@dataclass
class CheckpointConfigurationDefinition(BaseModel):
    CheckpointInterval: Optional[float]
    CheckpointingEnabled: Optional[bool]
    ConfigurationType: Optional[str]
    MinPauseBetweenCheckpoints: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_CheckpointConfigurationDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_CheckpointConfigurationDefinition"]:
        if not json_data:
            return None
        return cls(
            CheckpointInterval=json_data.get("CheckpointInterval"),
            CheckpointingEnabled=json_data.get("CheckpointingEnabled"),
            ConfigurationType=json_data.get("ConfigurationType"),
            MinPauseBetweenCheckpoints=json_data.get("MinPauseBetweenCheckpoints"),
        )


# work around possible type aliasing issues when variable has same name as a model
_CheckpointConfigurationDefinition = CheckpointConfigurationDefinition


@dataclass
class MonitoringConfigurationDefinition(BaseModel):
    ConfigurationType: Optional[str]
    LogLevel: Optional[str]
    MetricsLevel: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_MonitoringConfigurationDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_MonitoringConfigurationDefinition"]:
        if not json_data:
            return None
        return cls(
            ConfigurationType=json_data.get("ConfigurationType"),
            LogLevel=json_data.get("LogLevel"),
            MetricsLevel=json_data.get("MetricsLevel"),
        )


# work around possible type aliasing issues when variable has same name as a model
_MonitoringConfigurationDefinition = MonitoringConfigurationDefinition


@dataclass
class ParallelismConfigurationDefinition(BaseModel):
    AutoScalingEnabled: Optional[bool]
    ConfigurationType: Optional[str]
    Parallelism: Optional[float]
    ParallelismPerKpu: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_ParallelismConfigurationDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ParallelismConfigurationDefinition"]:
        if not json_data:
            return None
        return cls(
            AutoScalingEnabled=json_data.get("AutoScalingEnabled"),
            ConfigurationType=json_data.get("ConfigurationType"),
            Parallelism=json_data.get("Parallelism"),
            ParallelismPerKpu=json_data.get("ParallelismPerKpu"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ParallelismConfigurationDefinition = ParallelismConfigurationDefinition


@dataclass
class RunConfigurationDefinition(BaseModel):
    ApplicationRestoreConfiguration: Optional[Sequence["_ApplicationRestoreConfigurationDefinition"]]
    FlinkRunConfiguration: Optional[Sequence["_FlinkRunConfigurationDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_RunConfigurationDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_RunConfigurationDefinition"]:
        if not json_data:
            return None
        return cls(
            ApplicationRestoreConfiguration=deserialize_list(json_data.get("ApplicationRestoreConfiguration"), ApplicationRestoreConfigurationDefinition),
            FlinkRunConfiguration=deserialize_list(json_data.get("FlinkRunConfiguration"), FlinkRunConfigurationDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_RunConfigurationDefinition = RunConfigurationDefinition


@dataclass
class ApplicationRestoreConfigurationDefinition(BaseModel):
    ApplicationRestoreType: Optional[str]
    SnapshotName: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ApplicationRestoreConfigurationDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ApplicationRestoreConfigurationDefinition"]:
        if not json_data:
            return None
        return cls(
            ApplicationRestoreType=json_data.get("ApplicationRestoreType"),
            SnapshotName=json_data.get("SnapshotName"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ApplicationRestoreConfigurationDefinition = ApplicationRestoreConfigurationDefinition


@dataclass
class FlinkRunConfigurationDefinition(BaseModel):
    AllowNonRestoredState: Optional[bool]

    @classmethod
    def _deserialize(
        cls: Type["_FlinkRunConfigurationDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_FlinkRunConfigurationDefinition"]:
        if not json_data:
            return None
        return cls(
            AllowNonRestoredState=json_data.get("AllowNonRestoredState"),
        )


# work around possible type aliasing issues when variable has same name as a model
_FlinkRunConfigurationDefinition = FlinkRunConfigurationDefinition


@dataclass
class SqlApplicationConfigurationDefinition(BaseModel):
    Input: Optional[Sequence["_InputDefinition"]]
    Output: Optional[Sequence["_OutputDefinition"]]
    ReferenceDataSource: Optional[Sequence["_ReferenceDataSourceDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_SqlApplicationConfigurationDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SqlApplicationConfigurationDefinition"]:
        if not json_data:
            return None
        return cls(
            Input=deserialize_list(json_data.get("Input"), InputDefinition),
            Output=deserialize_list(json_data.get("Output"), OutputDefinition),
            ReferenceDataSource=deserialize_list(json_data.get("ReferenceDataSource"), ReferenceDataSourceDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_SqlApplicationConfigurationDefinition = SqlApplicationConfigurationDefinition


@dataclass
class InputDefinition(BaseModel):
    NamePrefix: Optional[str]
    InputParallelism: Optional[Sequence["_InputParallelismDefinition"]]
    InputProcessingConfiguration: Optional[Sequence["_InputProcessingConfigurationDefinition"]]
    InputSchema: Optional[Sequence["_InputSchemaDefinition"]]
    InputStartingPositionConfiguration: Optional[Sequence["_InputStartingPositionConfigurationDefinition"]]
    KinesisFirehoseInput: Optional[Sequence["_KinesisFirehoseInputDefinition"]]
    KinesisStreamsInput: Optional[Sequence["_KinesisStreamsInputDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_InputDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_InputDefinition"]:
        if not json_data:
            return None
        return cls(
            NamePrefix=json_data.get("NamePrefix"),
            InputParallelism=deserialize_list(json_data.get("InputParallelism"), InputParallelismDefinition),
            InputProcessingConfiguration=deserialize_list(json_data.get("InputProcessingConfiguration"), InputProcessingConfigurationDefinition),
            InputSchema=deserialize_list(json_data.get("InputSchema"), InputSchemaDefinition),
            InputStartingPositionConfiguration=deserialize_list(json_data.get("InputStartingPositionConfiguration"), InputStartingPositionConfigurationDefinition),
            KinesisFirehoseInput=deserialize_list(json_data.get("KinesisFirehoseInput"), KinesisFirehoseInputDefinition),
            KinesisStreamsInput=deserialize_list(json_data.get("KinesisStreamsInput"), KinesisStreamsInputDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_InputDefinition = InputDefinition


@dataclass
class InputParallelismDefinition(BaseModel):
    Count: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_InputParallelismDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_InputParallelismDefinition"]:
        if not json_data:
            return None
        return cls(
            Count=json_data.get("Count"),
        )


# work around possible type aliasing issues when variable has same name as a model
_InputParallelismDefinition = InputParallelismDefinition


@dataclass
class InputProcessingConfigurationDefinition(BaseModel):
    InputLambdaProcessor: Optional[Sequence["_InputLambdaProcessorDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_InputProcessingConfigurationDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_InputProcessingConfigurationDefinition"]:
        if not json_data:
            return None
        return cls(
            InputLambdaProcessor=deserialize_list(json_data.get("InputLambdaProcessor"), InputLambdaProcessorDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_InputProcessingConfigurationDefinition = InputProcessingConfigurationDefinition


@dataclass
class InputLambdaProcessorDefinition(BaseModel):
    ResourceArn: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_InputLambdaProcessorDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_InputLambdaProcessorDefinition"]:
        if not json_data:
            return None
        return cls(
            ResourceArn=json_data.get("ResourceArn"),
        )


# work around possible type aliasing issues when variable has same name as a model
_InputLambdaProcessorDefinition = InputLambdaProcessorDefinition


@dataclass
class InputSchemaDefinition(BaseModel):
    RecordEncoding: Optional[str]
    RecordColumn: Optional[Sequence["_RecordColumnDefinition"]]
    RecordFormat: Optional[Sequence["_RecordFormatDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_InputSchemaDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_InputSchemaDefinition"]:
        if not json_data:
            return None
        return cls(
            RecordEncoding=json_data.get("RecordEncoding"),
            RecordColumn=deserialize_list(json_data.get("RecordColumn"), RecordColumnDefinition),
            RecordFormat=deserialize_list(json_data.get("RecordFormat"), RecordFormatDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_InputSchemaDefinition = InputSchemaDefinition


@dataclass
class RecordColumnDefinition(BaseModel):
    Mapping: Optional[str]
    Name: Optional[str]
    SqlType: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_RecordColumnDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_RecordColumnDefinition"]:
        if not json_data:
            return None
        return cls(
            Mapping=json_data.get("Mapping"),
            Name=json_data.get("Name"),
            SqlType=json_data.get("SqlType"),
        )


# work around possible type aliasing issues when variable has same name as a model
_RecordColumnDefinition = RecordColumnDefinition


@dataclass
class RecordFormatDefinition(BaseModel):
    RecordFormatType: Optional[str]
    MappingParameters: Optional[Sequence["_MappingParametersDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_RecordFormatDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_RecordFormatDefinition"]:
        if not json_data:
            return None
        return cls(
            RecordFormatType=json_data.get("RecordFormatType"),
            MappingParameters=deserialize_list(json_data.get("MappingParameters"), MappingParametersDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_RecordFormatDefinition = RecordFormatDefinition


@dataclass
class MappingParametersDefinition(BaseModel):
    CsvMappingParameters: Optional[Sequence["_CsvMappingParametersDefinition"]]
    JsonMappingParameters: Optional[Sequence["_JsonMappingParametersDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_MappingParametersDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_MappingParametersDefinition"]:
        if not json_data:
            return None
        return cls(
            CsvMappingParameters=deserialize_list(json_data.get("CsvMappingParameters"), CsvMappingParametersDefinition),
            JsonMappingParameters=deserialize_list(json_data.get("JsonMappingParameters"), JsonMappingParametersDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_MappingParametersDefinition = MappingParametersDefinition


@dataclass
class CsvMappingParametersDefinition(BaseModel):
    RecordColumnDelimiter: Optional[str]
    RecordRowDelimiter: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_CsvMappingParametersDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_CsvMappingParametersDefinition"]:
        if not json_data:
            return None
        return cls(
            RecordColumnDelimiter=json_data.get("RecordColumnDelimiter"),
            RecordRowDelimiter=json_data.get("RecordRowDelimiter"),
        )


# work around possible type aliasing issues when variable has same name as a model
_CsvMappingParametersDefinition = CsvMappingParametersDefinition


@dataclass
class JsonMappingParametersDefinition(BaseModel):
    RecordRowPath: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_JsonMappingParametersDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_JsonMappingParametersDefinition"]:
        if not json_data:
            return None
        return cls(
            RecordRowPath=json_data.get("RecordRowPath"),
        )


# work around possible type aliasing issues when variable has same name as a model
_JsonMappingParametersDefinition = JsonMappingParametersDefinition


@dataclass
class InputStartingPositionConfigurationDefinition(BaseModel):
    InputStartingPosition: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_InputStartingPositionConfigurationDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_InputStartingPositionConfigurationDefinition"]:
        if not json_data:
            return None
        return cls(
            InputStartingPosition=json_data.get("InputStartingPosition"),
        )


# work around possible type aliasing issues when variable has same name as a model
_InputStartingPositionConfigurationDefinition = InputStartingPositionConfigurationDefinition


@dataclass
class KinesisFirehoseInputDefinition(BaseModel):
    ResourceArn: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_KinesisFirehoseInputDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_KinesisFirehoseInputDefinition"]:
        if not json_data:
            return None
        return cls(
            ResourceArn=json_data.get("ResourceArn"),
        )


# work around possible type aliasing issues when variable has same name as a model
_KinesisFirehoseInputDefinition = KinesisFirehoseInputDefinition


@dataclass
class KinesisStreamsInputDefinition(BaseModel):
    ResourceArn: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_KinesisStreamsInputDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_KinesisStreamsInputDefinition"]:
        if not json_data:
            return None
        return cls(
            ResourceArn=json_data.get("ResourceArn"),
        )


# work around possible type aliasing issues when variable has same name as a model
_KinesisStreamsInputDefinition = KinesisStreamsInputDefinition


@dataclass
class OutputDefinition(BaseModel):
    Name: Optional[str]
    DestinationSchema: Optional[Sequence["_DestinationSchemaDefinition"]]
    KinesisFirehoseOutput: Optional[Sequence["_KinesisFirehoseOutputDefinition"]]
    KinesisStreamsOutput: Optional[Sequence["_KinesisStreamsOutputDefinition"]]
    LambdaOutput: Optional[Sequence["_LambdaOutputDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_OutputDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_OutputDefinition"]:
        if not json_data:
            return None
        return cls(
            Name=json_data.get("Name"),
            DestinationSchema=deserialize_list(json_data.get("DestinationSchema"), DestinationSchemaDefinition),
            KinesisFirehoseOutput=deserialize_list(json_data.get("KinesisFirehoseOutput"), KinesisFirehoseOutputDefinition),
            KinesisStreamsOutput=deserialize_list(json_data.get("KinesisStreamsOutput"), KinesisStreamsOutputDefinition),
            LambdaOutput=deserialize_list(json_data.get("LambdaOutput"), LambdaOutputDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_OutputDefinition = OutputDefinition


@dataclass
class DestinationSchemaDefinition(BaseModel):
    RecordFormatType: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_DestinationSchemaDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DestinationSchemaDefinition"]:
        if not json_data:
            return None
        return cls(
            RecordFormatType=json_data.get("RecordFormatType"),
        )


# work around possible type aliasing issues when variable has same name as a model
_DestinationSchemaDefinition = DestinationSchemaDefinition


@dataclass
class KinesisFirehoseOutputDefinition(BaseModel):
    ResourceArn: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_KinesisFirehoseOutputDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_KinesisFirehoseOutputDefinition"]:
        if not json_data:
            return None
        return cls(
            ResourceArn=json_data.get("ResourceArn"),
        )


# work around possible type aliasing issues when variable has same name as a model
_KinesisFirehoseOutputDefinition = KinesisFirehoseOutputDefinition


@dataclass
class KinesisStreamsOutputDefinition(BaseModel):
    ResourceArn: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_KinesisStreamsOutputDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_KinesisStreamsOutputDefinition"]:
        if not json_data:
            return None
        return cls(
            ResourceArn=json_data.get("ResourceArn"),
        )


# work around possible type aliasing issues when variable has same name as a model
_KinesisStreamsOutputDefinition = KinesisStreamsOutputDefinition


@dataclass
class LambdaOutputDefinition(BaseModel):
    ResourceArn: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_LambdaOutputDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_LambdaOutputDefinition"]:
        if not json_data:
            return None
        return cls(
            ResourceArn=json_data.get("ResourceArn"),
        )


# work around possible type aliasing issues when variable has same name as a model
_LambdaOutputDefinition = LambdaOutputDefinition


@dataclass
class ReferenceDataSourceDefinition(BaseModel):
    TableName: Optional[str]
    ReferenceSchema: Optional[Sequence["_ReferenceSchemaDefinition"]]
    S3ReferenceDataSource: Optional[Sequence["_S3ReferenceDataSourceDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_ReferenceDataSourceDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ReferenceDataSourceDefinition"]:
        if not json_data:
            return None
        return cls(
            TableName=json_data.get("TableName"),
            ReferenceSchema=deserialize_list(json_data.get("ReferenceSchema"), ReferenceSchemaDefinition),
            S3ReferenceDataSource=deserialize_list(json_data.get("S3ReferenceDataSource"), S3ReferenceDataSourceDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ReferenceDataSourceDefinition = ReferenceDataSourceDefinition


@dataclass
class ReferenceSchemaDefinition(BaseModel):
    RecordEncoding: Optional[str]
    RecordColumn: Optional[Sequence["_RecordColumnDefinition"]]
    RecordFormat: Optional[Sequence["_RecordFormatDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_ReferenceSchemaDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ReferenceSchemaDefinition"]:
        if not json_data:
            return None
        return cls(
            RecordEncoding=json_data.get("RecordEncoding"),
            RecordColumn=deserialize_list(json_data.get("RecordColumn"), RecordColumnDefinition),
            RecordFormat=deserialize_list(json_data.get("RecordFormat"), RecordFormatDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ReferenceSchemaDefinition = ReferenceSchemaDefinition


@dataclass
class S3ReferenceDataSourceDefinition(BaseModel):
    BucketArn: Optional[str]
    FileKey: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_S3ReferenceDataSourceDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_S3ReferenceDataSourceDefinition"]:
        if not json_data:
            return None
        return cls(
            BucketArn=json_data.get("BucketArn"),
            FileKey=json_data.get("FileKey"),
        )


# work around possible type aliasing issues when variable has same name as a model
_S3ReferenceDataSourceDefinition = S3ReferenceDataSourceDefinition


@dataclass
class VpcConfigurationDefinition(BaseModel):
    SecurityGroupIds: Optional[Sequence[str]]
    SubnetIds: Optional[Sequence[str]]

    @classmethod
    def _deserialize(
        cls: Type["_VpcConfigurationDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_VpcConfigurationDefinition"]:
        if not json_data:
            return None
        return cls(
            SecurityGroupIds=json_data.get("SecurityGroupIds"),
            SubnetIds=json_data.get("SubnetIds"),
        )


# work around possible type aliasing issues when variable has same name as a model
_VpcConfigurationDefinition = VpcConfigurationDefinition


@dataclass
class CloudwatchLoggingOptionsDefinition(BaseModel):
    LogStreamArn: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_CloudwatchLoggingOptionsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_CloudwatchLoggingOptionsDefinition"]:
        if not json_data:
            return None
        return cls(
            LogStreamArn=json_data.get("LogStreamArn"),
        )


# work around possible type aliasing issues when variable has same name as a model
_CloudwatchLoggingOptionsDefinition = CloudwatchLoggingOptionsDefinition


