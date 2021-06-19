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
    Id: Optional[str]
    JobId: Optional[str]
    JobTimeoutMs: Optional[str]
    JobType: Optional[str]
    Labels: Optional[Sequence["_LabelsDefinition"]]
    Location: Optional[str]
    Project: Optional[str]
    Status: Optional[Sequence["_StatusDefinition3"]]
    UserEmail: Optional[str]
    Copy: Optional[Sequence["_CopyDefinition"]]
    Extract: Optional[Sequence["_ExtractDefinition"]]
    Load: Optional[Sequence["_LoadDefinition"]]
    Query: Optional[Sequence["_QueryDefinition"]]
    Timeouts: Optional["_TimeoutsDefinition"]

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
            Id=json_data.get("Id"),
            JobId=json_data.get("JobId"),
            JobTimeoutMs=json_data.get("JobTimeoutMs"),
            JobType=json_data.get("JobType"),
            Labels=deserialize_list(json_data.get("Labels"), LabelsDefinition),
            Location=json_data.get("Location"),
            Project=json_data.get("Project"),
            Status=deserialize_list(json_data.get("Status"), StatusDefinition3),
            UserEmail=json_data.get("UserEmail"),
            Copy=deserialize_list(json_data.get("Copy"), CopyDefinition),
            Extract=deserialize_list(json_data.get("Extract"), ExtractDefinition),
            Load=deserialize_list(json_data.get("Load"), LoadDefinition),
            Query=deserialize_list(json_data.get("Query"), QueryDefinition),
            Timeouts=TimeoutsDefinition._deserialize(json_data.get("Timeouts")),
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
class StatusDefinition3(BaseModel):
    ErrorResult: Optional[Sequence["_StatusDefinition"]]
    Errors: Optional[Sequence["_StatusDefinition2"]]
    State: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_StatusDefinition3"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_StatusDefinition3"]:
        if not json_data:
            return None
        return cls(
            ErrorResult=deserialize_list(json_data.get("ErrorResult"), StatusDefinition),
            Errors=deserialize_list(json_data.get("Errors"), StatusDefinition2),
            State=json_data.get("State"),
        )


# work around possible type aliasing issues when variable has same name as a model
_StatusDefinition3 = StatusDefinition3


@dataclass
class StatusDefinition(BaseModel):
    Location: Optional[str]
    Message: Optional[str]
    Reason: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_StatusDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_StatusDefinition"]:
        if not json_data:
            return None
        return cls(
            Location=json_data.get("Location"),
            Message=json_data.get("Message"),
            Reason=json_data.get("Reason"),
        )


# work around possible type aliasing issues when variable has same name as a model
_StatusDefinition = StatusDefinition


@dataclass
class StatusDefinition2(BaseModel):
    Location: Optional[str]
    Message: Optional[str]
    Reason: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_StatusDefinition2"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_StatusDefinition2"]:
        if not json_data:
            return None
        return cls(
            Location=json_data.get("Location"),
            Message=json_data.get("Message"),
            Reason=json_data.get("Reason"),
        )


# work around possible type aliasing issues when variable has same name as a model
_StatusDefinition2 = StatusDefinition2


@dataclass
class CopyDefinition(BaseModel):
    CreateDisposition: Optional[str]
    WriteDisposition: Optional[str]
    DestinationEncryptionConfiguration: Optional[Sequence["_DestinationEncryptionConfigurationDefinition"]]
    DestinationTable: Optional[Sequence["_DestinationTableDefinition"]]
    SourceTables: Optional[Sequence["_SourceTablesDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_CopyDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_CopyDefinition"]:
        if not json_data:
            return None
        return cls(
            CreateDisposition=json_data.get("CreateDisposition"),
            WriteDisposition=json_data.get("WriteDisposition"),
            DestinationEncryptionConfiguration=deserialize_list(json_data.get("DestinationEncryptionConfiguration"), DestinationEncryptionConfigurationDefinition),
            DestinationTable=deserialize_list(json_data.get("DestinationTable"), DestinationTableDefinition),
            SourceTables=deserialize_list(json_data.get("SourceTables"), SourceTablesDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_CopyDefinition = CopyDefinition


@dataclass
class DestinationEncryptionConfigurationDefinition(BaseModel):
    KmsKeyName: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_DestinationEncryptionConfigurationDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DestinationEncryptionConfigurationDefinition"]:
        if not json_data:
            return None
        return cls(
            KmsKeyName=json_data.get("KmsKeyName"),
        )


# work around possible type aliasing issues when variable has same name as a model
_DestinationEncryptionConfigurationDefinition = DestinationEncryptionConfigurationDefinition


@dataclass
class DestinationTableDefinition(BaseModel):
    DatasetId: Optional[str]
    ProjectId: Optional[str]
    TableId: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_DestinationTableDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DestinationTableDefinition"]:
        if not json_data:
            return None
        return cls(
            DatasetId=json_data.get("DatasetId"),
            ProjectId=json_data.get("ProjectId"),
            TableId=json_data.get("TableId"),
        )


# work around possible type aliasing issues when variable has same name as a model
_DestinationTableDefinition = DestinationTableDefinition


@dataclass
class SourceTablesDefinition(BaseModel):
    DatasetId: Optional[str]
    ProjectId: Optional[str]
    TableId: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_SourceTablesDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SourceTablesDefinition"]:
        if not json_data:
            return None
        return cls(
            DatasetId=json_data.get("DatasetId"),
            ProjectId=json_data.get("ProjectId"),
            TableId=json_data.get("TableId"),
        )


# work around possible type aliasing issues when variable has same name as a model
_SourceTablesDefinition = SourceTablesDefinition


@dataclass
class ExtractDefinition(BaseModel):
    Compression: Optional[str]
    DestinationFormat: Optional[str]
    DestinationUris: Optional[Sequence[str]]
    FieldDelimiter: Optional[str]
    PrintHeader: Optional[bool]
    UseAvroLogicalTypes: Optional[bool]
    SourceModel: Optional[Sequence["_SourceModelDefinition"]]
    SourceTable: Optional[Sequence["_SourceTableDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_ExtractDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ExtractDefinition"]:
        if not json_data:
            return None
        return cls(
            Compression=json_data.get("Compression"),
            DestinationFormat=json_data.get("DestinationFormat"),
            DestinationUris=json_data.get("DestinationUris"),
            FieldDelimiter=json_data.get("FieldDelimiter"),
            PrintHeader=json_data.get("PrintHeader"),
            UseAvroLogicalTypes=json_data.get("UseAvroLogicalTypes"),
            SourceModel=deserialize_list(json_data.get("SourceModel"), SourceModelDefinition),
            SourceTable=deserialize_list(json_data.get("SourceTable"), SourceTableDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ExtractDefinition = ExtractDefinition


@dataclass
class SourceModelDefinition(BaseModel):
    DatasetId: Optional[str]
    ModelId: Optional[str]
    ProjectId: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_SourceModelDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SourceModelDefinition"]:
        if not json_data:
            return None
        return cls(
            DatasetId=json_data.get("DatasetId"),
            ModelId=json_data.get("ModelId"),
            ProjectId=json_data.get("ProjectId"),
        )


# work around possible type aliasing issues when variable has same name as a model
_SourceModelDefinition = SourceModelDefinition


@dataclass
class SourceTableDefinition(BaseModel):
    DatasetId: Optional[str]
    ProjectId: Optional[str]
    TableId: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_SourceTableDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SourceTableDefinition"]:
        if not json_data:
            return None
        return cls(
            DatasetId=json_data.get("DatasetId"),
            ProjectId=json_data.get("ProjectId"),
            TableId=json_data.get("TableId"),
        )


# work around possible type aliasing issues when variable has same name as a model
_SourceTableDefinition = SourceTableDefinition


@dataclass
class LoadDefinition(BaseModel):
    AllowJaggedRows: Optional[bool]
    AllowQuotedNewlines: Optional[bool]
    Autodetect: Optional[bool]
    CreateDisposition: Optional[str]
    Encoding: Optional[str]
    FieldDelimiter: Optional[str]
    IgnoreUnknownValues: Optional[bool]
    MaxBadRecords: Optional[float]
    NullMarker: Optional[str]
    ProjectionFields: Optional[Sequence[str]]
    Quote: Optional[str]
    SchemaUpdateOptions: Optional[Sequence[str]]
    SkipLeadingRows: Optional[float]
    SourceFormat: Optional[str]
    SourceUris: Optional[Sequence[str]]
    WriteDisposition: Optional[str]
    DestinationEncryptionConfiguration: Optional[Sequence["_DestinationEncryptionConfigurationDefinition"]]
    DestinationTable: Optional[Sequence["_DestinationTableDefinition"]]
    TimePartitioning: Optional[Sequence["_TimePartitioningDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_LoadDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_LoadDefinition"]:
        if not json_data:
            return None
        return cls(
            AllowJaggedRows=json_data.get("AllowJaggedRows"),
            AllowQuotedNewlines=json_data.get("AllowQuotedNewlines"),
            Autodetect=json_data.get("Autodetect"),
            CreateDisposition=json_data.get("CreateDisposition"),
            Encoding=json_data.get("Encoding"),
            FieldDelimiter=json_data.get("FieldDelimiter"),
            IgnoreUnknownValues=json_data.get("IgnoreUnknownValues"),
            MaxBadRecords=json_data.get("MaxBadRecords"),
            NullMarker=json_data.get("NullMarker"),
            ProjectionFields=json_data.get("ProjectionFields"),
            Quote=json_data.get("Quote"),
            SchemaUpdateOptions=json_data.get("SchemaUpdateOptions"),
            SkipLeadingRows=json_data.get("SkipLeadingRows"),
            SourceFormat=json_data.get("SourceFormat"),
            SourceUris=json_data.get("SourceUris"),
            WriteDisposition=json_data.get("WriteDisposition"),
            DestinationEncryptionConfiguration=deserialize_list(json_data.get("DestinationEncryptionConfiguration"), DestinationEncryptionConfigurationDefinition),
            DestinationTable=deserialize_list(json_data.get("DestinationTable"), DestinationTableDefinition),
            TimePartitioning=deserialize_list(json_data.get("TimePartitioning"), TimePartitioningDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_LoadDefinition = LoadDefinition


@dataclass
class TimePartitioningDefinition(BaseModel):
    ExpirationMs: Optional[str]
    Field: Optional[str]
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
            Type=json_data.get("Type"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TimePartitioningDefinition = TimePartitioningDefinition


@dataclass
class QueryDefinition(BaseModel):
    AllowLargeResults: Optional[bool]
    CreateDisposition: Optional[str]
    FlattenResults: Optional[bool]
    MaximumBillingTier: Optional[float]
    MaximumBytesBilled: Optional[str]
    ParameterMode: Optional[str]
    Priority: Optional[str]
    Query: Optional[str]
    SchemaUpdateOptions: Optional[Sequence[str]]
    UseLegacySql: Optional[bool]
    UseQueryCache: Optional[bool]
    WriteDisposition: Optional[str]
    DefaultDataset: Optional[Sequence["_DefaultDatasetDefinition"]]
    DestinationEncryptionConfiguration: Optional[Sequence["_DestinationEncryptionConfigurationDefinition"]]
    DestinationTable: Optional[Sequence["_DestinationTableDefinition"]]
    ScriptOptions: Optional[Sequence["_ScriptOptionsDefinition"]]
    UserDefinedFunctionResources: Optional[Sequence["_UserDefinedFunctionResourcesDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_QueryDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_QueryDefinition"]:
        if not json_data:
            return None
        return cls(
            AllowLargeResults=json_data.get("AllowLargeResults"),
            CreateDisposition=json_data.get("CreateDisposition"),
            FlattenResults=json_data.get("FlattenResults"),
            MaximumBillingTier=json_data.get("MaximumBillingTier"),
            MaximumBytesBilled=json_data.get("MaximumBytesBilled"),
            ParameterMode=json_data.get("ParameterMode"),
            Priority=json_data.get("Priority"),
            Query=json_data.get("Query"),
            SchemaUpdateOptions=json_data.get("SchemaUpdateOptions"),
            UseLegacySql=json_data.get("UseLegacySql"),
            UseQueryCache=json_data.get("UseQueryCache"),
            WriteDisposition=json_data.get("WriteDisposition"),
            DefaultDataset=deserialize_list(json_data.get("DefaultDataset"), DefaultDatasetDefinition),
            DestinationEncryptionConfiguration=deserialize_list(json_data.get("DestinationEncryptionConfiguration"), DestinationEncryptionConfigurationDefinition),
            DestinationTable=deserialize_list(json_data.get("DestinationTable"), DestinationTableDefinition),
            ScriptOptions=deserialize_list(json_data.get("ScriptOptions"), ScriptOptionsDefinition),
            UserDefinedFunctionResources=deserialize_list(json_data.get("UserDefinedFunctionResources"), UserDefinedFunctionResourcesDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_QueryDefinition = QueryDefinition


@dataclass
class DefaultDatasetDefinition(BaseModel):
    DatasetId: Optional[str]
    ProjectId: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_DefaultDatasetDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DefaultDatasetDefinition"]:
        if not json_data:
            return None
        return cls(
            DatasetId=json_data.get("DatasetId"),
            ProjectId=json_data.get("ProjectId"),
        )


# work around possible type aliasing issues when variable has same name as a model
_DefaultDatasetDefinition = DefaultDatasetDefinition


@dataclass
class ScriptOptionsDefinition(BaseModel):
    KeyResultStatement: Optional[str]
    StatementByteBudget: Optional[str]
    StatementTimeoutMs: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ScriptOptionsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ScriptOptionsDefinition"]:
        if not json_data:
            return None
        return cls(
            KeyResultStatement=json_data.get("KeyResultStatement"),
            StatementByteBudget=json_data.get("StatementByteBudget"),
            StatementTimeoutMs=json_data.get("StatementTimeoutMs"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ScriptOptionsDefinition = ScriptOptionsDefinition


@dataclass
class UserDefinedFunctionResourcesDefinition(BaseModel):
    InlineCode: Optional[str]
    ResourceUri: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_UserDefinedFunctionResourcesDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_UserDefinedFunctionResourcesDefinition"]:
        if not json_data:
            return None
        return cls(
            InlineCode=json_data.get("InlineCode"),
            ResourceUri=json_data.get("ResourceUri"),
        )


# work around possible type aliasing issues when variable has same name as a model
_UserDefinedFunctionResourcesDefinition = UserDefinedFunctionResourcesDefinition


@dataclass
class TimeoutsDefinition(BaseModel):
    Create: Optional[str]
    Delete: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_TimeoutsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TimeoutsDefinition"]:
        if not json_data:
            return None
        return cls(
            Create=json_data.get("Create"),
            Delete=json_data.get("Delete"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TimeoutsDefinition = TimeoutsDefinition


