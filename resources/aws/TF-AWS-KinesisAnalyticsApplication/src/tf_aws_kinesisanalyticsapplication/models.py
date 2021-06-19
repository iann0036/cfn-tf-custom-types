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
    Code: Optional[str]
    CreateTimestamp: Optional[str]
    Description: Optional[str]
    Id: Optional[str]
    LastUpdateTimestamp: Optional[str]
    Name: Optional[str]
    StartApplication: Optional[bool]
    Status: Optional[str]
    Tags: Optional[Sequence["_TagsDefinition"]]
    TagsAll: Optional[Sequence["_TagsAllDefinition"]]
    Version: Optional[float]
    CloudwatchLoggingOptions: Optional[Sequence["_CloudwatchLoggingOptionsDefinition"]]
    Inputs: Optional[Sequence["_InputsDefinition"]]
    Outputs: Optional[Sequence["_OutputsDefinition"]]
    ReferenceDataSources: Optional[Sequence["_ReferenceDataSourcesDefinition"]]

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
            Code=json_data.get("Code"),
            CreateTimestamp=json_data.get("CreateTimestamp"),
            Description=json_data.get("Description"),
            Id=json_data.get("Id"),
            LastUpdateTimestamp=json_data.get("LastUpdateTimestamp"),
            Name=json_data.get("Name"),
            StartApplication=json_data.get("StartApplication"),
            Status=json_data.get("Status"),
            Tags=deserialize_list(json_data.get("Tags"), TagsDefinition),
            TagsAll=deserialize_list(json_data.get("TagsAll"), TagsAllDefinition),
            Version=json_data.get("Version"),
            CloudwatchLoggingOptions=deserialize_list(json_data.get("CloudwatchLoggingOptions"), CloudwatchLoggingOptionsDefinition),
            Inputs=deserialize_list(json_data.get("Inputs"), InputsDefinition),
            Outputs=deserialize_list(json_data.get("Outputs"), OutputsDefinition),
            ReferenceDataSources=deserialize_list(json_data.get("ReferenceDataSources"), ReferenceDataSourcesDefinition),
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
class CloudwatchLoggingOptionsDefinition(BaseModel):
    LogStreamArn: Optional[str]
    RoleArn: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_CloudwatchLoggingOptionsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_CloudwatchLoggingOptionsDefinition"]:
        if not json_data:
            return None
        return cls(
            LogStreamArn=json_data.get("LogStreamArn"),
            RoleArn=json_data.get("RoleArn"),
        )


# work around possible type aliasing issues when variable has same name as a model
_CloudwatchLoggingOptionsDefinition = CloudwatchLoggingOptionsDefinition


@dataclass
class InputsDefinition(BaseModel):
    NamePrefix: Optional[str]
    KinesisFirehose: Optional[Sequence["_KinesisFirehoseDefinition"]]
    KinesisStream: Optional[Sequence["_KinesisStreamDefinition"]]
    Parallelism: Optional[Sequence["_ParallelismDefinition"]]
    ProcessingConfiguration: Optional[Sequence["_ProcessingConfigurationDefinition"]]
    Schema: Optional[Sequence["_SchemaDefinition"]]
    StartingPositionConfiguration: Optional[Sequence["_StartingPositionConfigurationDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_InputsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_InputsDefinition"]:
        if not json_data:
            return None
        return cls(
            NamePrefix=json_data.get("NamePrefix"),
            KinesisFirehose=deserialize_list(json_data.get("KinesisFirehose"), KinesisFirehoseDefinition),
            KinesisStream=deserialize_list(json_data.get("KinesisStream"), KinesisStreamDefinition),
            Parallelism=deserialize_list(json_data.get("Parallelism"), ParallelismDefinition),
            ProcessingConfiguration=deserialize_list(json_data.get("ProcessingConfiguration"), ProcessingConfigurationDefinition),
            Schema=deserialize_list(json_data.get("Schema"), SchemaDefinition),
            StartingPositionConfiguration=deserialize_list(json_data.get("StartingPositionConfiguration"), StartingPositionConfigurationDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_InputsDefinition = InputsDefinition


@dataclass
class KinesisFirehoseDefinition(BaseModel):
    ResourceArn: Optional[str]
    RoleArn: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_KinesisFirehoseDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_KinesisFirehoseDefinition"]:
        if not json_data:
            return None
        return cls(
            ResourceArn=json_data.get("ResourceArn"),
            RoleArn=json_data.get("RoleArn"),
        )


# work around possible type aliasing issues when variable has same name as a model
_KinesisFirehoseDefinition = KinesisFirehoseDefinition


@dataclass
class KinesisStreamDefinition(BaseModel):
    ResourceArn: Optional[str]
    RoleArn: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_KinesisStreamDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_KinesisStreamDefinition"]:
        if not json_data:
            return None
        return cls(
            ResourceArn=json_data.get("ResourceArn"),
            RoleArn=json_data.get("RoleArn"),
        )


# work around possible type aliasing issues when variable has same name as a model
_KinesisStreamDefinition = KinesisStreamDefinition


@dataclass
class ParallelismDefinition(BaseModel):
    Count: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_ParallelismDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ParallelismDefinition"]:
        if not json_data:
            return None
        return cls(
            Count=json_data.get("Count"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ParallelismDefinition = ParallelismDefinition


@dataclass
class ProcessingConfigurationDefinition(BaseModel):
    Lambda: Optional[Sequence["_LambdaDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_ProcessingConfigurationDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ProcessingConfigurationDefinition"]:
        if not json_data:
            return None
        return cls(
            Lambda=deserialize_list(json_data.get("Lambda"), LambdaDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ProcessingConfigurationDefinition = ProcessingConfigurationDefinition


@dataclass
class LambdaDefinition(BaseModel):
    ResourceArn: Optional[str]
    RoleArn: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_LambdaDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_LambdaDefinition"]:
        if not json_data:
            return None
        return cls(
            ResourceArn=json_data.get("ResourceArn"),
            RoleArn=json_data.get("RoleArn"),
        )


# work around possible type aliasing issues when variable has same name as a model
_LambdaDefinition = LambdaDefinition


@dataclass
class SchemaDefinition(BaseModel):
    RecordEncoding: Optional[str]
    RecordColumns: Optional[Sequence["_RecordColumnsDefinition"]]
    RecordFormat: Optional[Sequence["_RecordFormatDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_SchemaDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SchemaDefinition"]:
        if not json_data:
            return None
        return cls(
            RecordEncoding=json_data.get("RecordEncoding"),
            RecordColumns=deserialize_list(json_data.get("RecordColumns"), RecordColumnsDefinition),
            RecordFormat=deserialize_list(json_data.get("RecordFormat"), RecordFormatDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_SchemaDefinition = SchemaDefinition


@dataclass
class RecordColumnsDefinition(BaseModel):
    Mapping: Optional[str]
    Name: Optional[str]
    SqlType: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_RecordColumnsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_RecordColumnsDefinition"]:
        if not json_data:
            return None
        return cls(
            Mapping=json_data.get("Mapping"),
            Name=json_data.get("Name"),
            SqlType=json_data.get("SqlType"),
        )


# work around possible type aliasing issues when variable has same name as a model
_RecordColumnsDefinition = RecordColumnsDefinition


@dataclass
class RecordFormatDefinition(BaseModel):
    MappingParameters: Optional[Sequence["_MappingParametersDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_RecordFormatDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_RecordFormatDefinition"]:
        if not json_data:
            return None
        return cls(
            MappingParameters=deserialize_list(json_data.get("MappingParameters"), MappingParametersDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_RecordFormatDefinition = RecordFormatDefinition


@dataclass
class MappingParametersDefinition(BaseModel):
    Csv: Optional[Sequence["_CsvDefinition"]]
    Json: Optional[Sequence["_JsonDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_MappingParametersDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_MappingParametersDefinition"]:
        if not json_data:
            return None
        return cls(
            Csv=deserialize_list(json_data.get("Csv"), CsvDefinition),
            Json=deserialize_list(json_data.get("Json"), JsonDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_MappingParametersDefinition = MappingParametersDefinition


@dataclass
class CsvDefinition(BaseModel):
    RecordColumnDelimiter: Optional[str]
    RecordRowDelimiter: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_CsvDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_CsvDefinition"]:
        if not json_data:
            return None
        return cls(
            RecordColumnDelimiter=json_data.get("RecordColumnDelimiter"),
            RecordRowDelimiter=json_data.get("RecordRowDelimiter"),
        )


# work around possible type aliasing issues when variable has same name as a model
_CsvDefinition = CsvDefinition


@dataclass
class JsonDefinition(BaseModel):
    RecordRowPath: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_JsonDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_JsonDefinition"]:
        if not json_data:
            return None
        return cls(
            RecordRowPath=json_data.get("RecordRowPath"),
        )


# work around possible type aliasing issues when variable has same name as a model
_JsonDefinition = JsonDefinition


@dataclass
class StartingPositionConfigurationDefinition(BaseModel):
    StartingPosition: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_StartingPositionConfigurationDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_StartingPositionConfigurationDefinition"]:
        if not json_data:
            return None
        return cls(
            StartingPosition=json_data.get("StartingPosition"),
        )


# work around possible type aliasing issues when variable has same name as a model
_StartingPositionConfigurationDefinition = StartingPositionConfigurationDefinition


@dataclass
class OutputsDefinition(BaseModel):
    Name: Optional[str]
    KinesisFirehose: Optional[Sequence["_KinesisFirehoseDefinition"]]
    KinesisStream: Optional[Sequence["_KinesisStreamDefinition"]]
    Lambda: Optional[Sequence["_LambdaDefinition"]]
    Schema: Optional[Sequence["_SchemaDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_OutputsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_OutputsDefinition"]:
        if not json_data:
            return None
        return cls(
            Name=json_data.get("Name"),
            KinesisFirehose=deserialize_list(json_data.get("KinesisFirehose"), KinesisFirehoseDefinition),
            KinesisStream=deserialize_list(json_data.get("KinesisStream"), KinesisStreamDefinition),
            Lambda=deserialize_list(json_data.get("Lambda"), LambdaDefinition),
            Schema=deserialize_list(json_data.get("Schema"), SchemaDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_OutputsDefinition = OutputsDefinition


@dataclass
class ReferenceDataSourcesDefinition(BaseModel):
    TableName: Optional[str]
    S3: Optional[Sequence["_S3Definition"]]
    Schema: Optional[Sequence["_SchemaDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_ReferenceDataSourcesDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ReferenceDataSourcesDefinition"]:
        if not json_data:
            return None
        return cls(
            TableName=json_data.get("TableName"),
            S3=deserialize_list(json_data.get("S3"), S3Definition),
            Schema=deserialize_list(json_data.get("Schema"), SchemaDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ReferenceDataSourcesDefinition = ReferenceDataSourcesDefinition


@dataclass
class S3Definition(BaseModel):
    BucketArn: Optional[str]
    FileKey: Optional[str]
    RoleArn: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_S3Definition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_S3Definition"]:
        if not json_data:
            return None
        return cls(
            BucketArn=json_data.get("BucketArn"),
            FileKey=json_data.get("FileKey"),
            RoleArn=json_data.get("RoleArn"),
        )


# work around possible type aliasing issues when variable has same name as a model
_S3Definition = S3Definition


