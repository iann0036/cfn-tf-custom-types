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
    Code: Optional[str]
    CreateTimestamp: Optional[str]
    Description: Optional[str]
    Id: Optional[str]
    LastUpdateTimestamp: Optional[str]
    Name: Optional[str]
    Status: Optional[str]
    Tags: Optional[Sequence["_Tags"]]
    Version: Optional[float]
    CloudwatchLoggingOptions: Optional[Sequence["_CloudwatchLoggingOptions"]]
    Inputs: Optional[Sequence["_Inputs"]]
    Outputs: Optional[Sequence["_Outputs"]]
    ReferenceDataSources: Optional[Sequence["_ReferenceDataSources"]]
    KinesisFirehose: Optional[Sequence["_KinesisFirehose"]]
    KinesisStream: Optional[Sequence["_KinesisStream"]]
    Parallelism: Optional[Sequence["_Parallelism"]]
    ProcessingConfiguration: Optional[Sequence["_ProcessingConfiguration"]]
    Schema: Optional[Sequence["_Schema"]]
    Lambda: Optional[Sequence["_Lambda"]]
    S3: Optional[Sequence["_S3"]]
    RecordColumns: Optional[Sequence["_RecordColumns"]]
    RecordFormat: Optional[Sequence["_RecordFormat"]]
    MappingParameters: Optional[Sequence["_MappingParameters"]]
    Csv: Optional[Sequence["_Csv"]]
    Json: Optional[Sequence["_Json"]]

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
            Code=json_data.get("Code"),
            CreateTimestamp=json_data.get("CreateTimestamp"),
            Description=json_data.get("Description"),
            Id=json_data.get("Id"),
            LastUpdateTimestamp=json_data.get("LastUpdateTimestamp"),
            Name=json_data.get("Name"),
            Status=json_data.get("Status"),
            Tags=json_data.get("Tags"),
            Version=json_data.get("Version"),
            CloudwatchLoggingOptions=json_data.get("CloudwatchLoggingOptions"),
            Inputs=json_data.get("Inputs"),
            Outputs=json_data.get("Outputs"),
            ReferenceDataSources=json_data.get("ReferenceDataSources"),
            KinesisFirehose=json_data.get("KinesisFirehose"),
            KinesisStream=json_data.get("KinesisStream"),
            Parallelism=json_data.get("Parallelism"),
            ProcessingConfiguration=json_data.get("ProcessingConfiguration"),
            Schema=json_data.get("Schema"),
            Lambda=json_data.get("Lambda"),
            S3=json_data.get("S3"),
            RecordColumns=json_data.get("RecordColumns"),
            RecordFormat=json_data.get("RecordFormat"),
            MappingParameters=json_data.get("MappingParameters"),
            Csv=json_data.get("Csv"),
            Json=json_data.get("Json"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class Tags:
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Tags"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Tags"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Tags = Tags


@dataclass
class CloudwatchLoggingOptions:
    LogStreamArn: Optional[str]
    RoleArn: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_CloudwatchLoggingOptions"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_CloudwatchLoggingOptions"]:
        if not json_data:
            return None
        return cls(
            LogStreamArn=json_data.get("LogStreamArn"),
            RoleArn=json_data.get("RoleArn"),
        )


# work around possible type aliasing issues when variable has same name as a model
_CloudwatchLoggingOptions = CloudwatchLoggingOptions


@dataclass
class Inputs:
    NamePrefix: Optional[str]
    KinesisFirehose: Optional[Sequence["_KinesisFirehose"]]
    KinesisStream: Optional[Sequence["_KinesisStream"]]
    Parallelism: Optional[Sequence["_Parallelism"]]
    ProcessingConfiguration: Optional[Sequence["_ProcessingConfiguration"]]
    Schema: Optional[Sequence["_Schema"]]

    @classmethod
    def _deserialize(
        cls: Type["_Inputs"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Inputs"]:
        if not json_data:
            return None
        return cls(
            NamePrefix=json_data.get("NamePrefix"),
            KinesisFirehose=json_data.get("KinesisFirehose"),
            KinesisStream=json_data.get("KinesisStream"),
            Parallelism=json_data.get("Parallelism"),
            ProcessingConfiguration=json_data.get("ProcessingConfiguration"),
            Schema=json_data.get("Schema"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Inputs = Inputs


@dataclass
class KinesisFirehose:
    ResourceArn: Optional[str]
    RoleArn: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_KinesisFirehose"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_KinesisFirehose"]:
        if not json_data:
            return None
        return cls(
            ResourceArn=json_data.get("ResourceArn"),
            RoleArn=json_data.get("RoleArn"),
        )


# work around possible type aliasing issues when variable has same name as a model
_KinesisFirehose = KinesisFirehose


@dataclass
class KinesisStream:
    ResourceArn: Optional[str]
    RoleArn: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_KinesisStream"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_KinesisStream"]:
        if not json_data:
            return None
        return cls(
            ResourceArn=json_data.get("ResourceArn"),
            RoleArn=json_data.get("RoleArn"),
        )


# work around possible type aliasing issues when variable has same name as a model
_KinesisStream = KinesisStream


@dataclass
class Parallelism:
    Count: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_Parallelism"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Parallelism"]:
        if not json_data:
            return None
        return cls(
            Count=json_data.get("Count"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Parallelism = Parallelism


@dataclass
class ProcessingConfiguration:
    Lambda: Optional[Sequence["_Lambda"]]

    @classmethod
    def _deserialize(
        cls: Type["_ProcessingConfiguration"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ProcessingConfiguration"]:
        if not json_data:
            return None
        return cls(
            Lambda=json_data.get("Lambda"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ProcessingConfiguration = ProcessingConfiguration


@dataclass
class Lambda:
    ResourceArn: Optional[str]
    RoleArn: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Lambda"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Lambda"]:
        if not json_data:
            return None
        return cls(
            ResourceArn=json_data.get("ResourceArn"),
            RoleArn=json_data.get("RoleArn"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Lambda = Lambda


@dataclass
class Schema:
    RecordEncoding: Optional[str]
    RecordColumns: Optional[Sequence["_RecordColumns"]]
    RecordFormat: Optional[Sequence["_RecordFormat"]]

    @classmethod
    def _deserialize(
        cls: Type["_Schema"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Schema"]:
        if not json_data:
            return None
        return cls(
            RecordEncoding=json_data.get("RecordEncoding"),
            RecordColumns=json_data.get("RecordColumns"),
            RecordFormat=json_data.get("RecordFormat"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Schema = Schema


@dataclass
class RecordColumns:
    Mapping: Optional[str]
    Name: Optional[str]
    SqlType: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_RecordColumns"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_RecordColumns"]:
        if not json_data:
            return None
        return cls(
            Mapping=json_data.get("Mapping"),
            Name=json_data.get("Name"),
            SqlType=json_data.get("SqlType"),
        )


# work around possible type aliasing issues when variable has same name as a model
_RecordColumns = RecordColumns


@dataclass
class RecordFormat:
    MappingParameters: Optional[Sequence["_MappingParameters"]]

    @classmethod
    def _deserialize(
        cls: Type["_RecordFormat"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_RecordFormat"]:
        if not json_data:
            return None
        return cls(
            MappingParameters=json_data.get("MappingParameters"),
        )


# work around possible type aliasing issues when variable has same name as a model
_RecordFormat = RecordFormat


@dataclass
class MappingParameters:
    Csv: Optional[Sequence["_Csv"]]
    Json: Optional[Sequence["_Json"]]

    @classmethod
    def _deserialize(
        cls: Type["_MappingParameters"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_MappingParameters"]:
        if not json_data:
            return None
        return cls(
            Csv=json_data.get("Csv"),
            Json=json_data.get("Json"),
        )


# work around possible type aliasing issues when variable has same name as a model
_MappingParameters = MappingParameters


@dataclass
class Csv:
    RecordColumnDelimiter: Optional[str]
    RecordRowDelimiter: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Csv"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Csv"]:
        if not json_data:
            return None
        return cls(
            RecordColumnDelimiter=json_data.get("RecordColumnDelimiter"),
            RecordRowDelimiter=json_data.get("RecordRowDelimiter"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Csv = Csv


@dataclass
class Json:
    RecordRowPath: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Json"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Json"]:
        if not json_data:
            return None
        return cls(
            RecordRowPath=json_data.get("RecordRowPath"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Json = Json


@dataclass
class Outputs:
    Name: Optional[str]
    KinesisFirehose: Optional[Sequence["_KinesisFirehose"]]
    KinesisStream: Optional[Sequence["_KinesisStream"]]
    Lambda: Optional[Sequence["_Lambda"]]
    Schema: Optional[Sequence["_Schema"]]

    @classmethod
    def _deserialize(
        cls: Type["_Outputs"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Outputs"]:
        if not json_data:
            return None
        return cls(
            Name=json_data.get("Name"),
            KinesisFirehose=json_data.get("KinesisFirehose"),
            KinesisStream=json_data.get("KinesisStream"),
            Lambda=json_data.get("Lambda"),
            Schema=json_data.get("Schema"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Outputs = Outputs


@dataclass
class ReferenceDataSources:
    TableName: Optional[str]
    S3: Optional[Sequence["_S3"]]
    Schema: Optional[Sequence["_Schema"]]

    @classmethod
    def _deserialize(
        cls: Type["_ReferenceDataSources"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ReferenceDataSources"]:
        if not json_data:
            return None
        return cls(
            TableName=json_data.get("TableName"),
            S3=json_data.get("S3"),
            Schema=json_data.get("Schema"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ReferenceDataSources = ReferenceDataSources


@dataclass
class S3:
    BucketArn: Optional[str]
    FileKey: Optional[str]
    RoleArn: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_S3"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_S3"]:
        if not json_data:
            return None
        return cls(
            BucketArn=json_data.get("BucketArn"),
            FileKey=json_data.get("FileKey"),
            RoleArn=json_data.get("RoleArn"),
        )


# work around possible type aliasing issues when variable has same name as a model
_S3 = S3


