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
    Description: Optional[str]
    DisplayName: Optional[str]
    Id: Optional[str]
    LastRunTime: Optional[str]
    Name: Optional[str]
    Parent: Optional[str]
    Status: Optional[str]
    InspectJob: Optional[Sequence["_InspectJobDefinition"]]
    Timeouts: Optional["_TimeoutsDefinition"]
    Triggers: Optional[Sequence["_TriggersDefinition"]]

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
            Description=json_data.get("Description"),
            DisplayName=json_data.get("DisplayName"),
            Id=json_data.get("Id"),
            LastRunTime=json_data.get("LastRunTime"),
            Name=json_data.get("Name"),
            Parent=json_data.get("Parent"),
            Status=json_data.get("Status"),
            InspectJob=deserialize_list(json_data.get("InspectJob"), InspectJobDefinition),
            Timeouts=TimeoutsDefinition._deserialize(json_data.get("Timeouts")),
            Triggers=deserialize_list(json_data.get("Triggers"), TriggersDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class InspectJobDefinition(BaseModel):
    InspectTemplateName: Optional[str]
    Actions: Optional[Sequence["_ActionsDefinition"]]
    StorageConfig: Optional[Sequence["_StorageConfigDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_InspectJobDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_InspectJobDefinition"]:
        if not json_data:
            return None
        return cls(
            InspectTemplateName=json_data.get("InspectTemplateName"),
            Actions=deserialize_list(json_data.get("Actions"), ActionsDefinition),
            StorageConfig=deserialize_list(json_data.get("StorageConfig"), StorageConfigDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_InspectJobDefinition = InspectJobDefinition


@dataclass
class ActionsDefinition(BaseModel):
    SaveFindings: Optional[Sequence["_SaveFindingsDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_ActionsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ActionsDefinition"]:
        if not json_data:
            return None
        return cls(
            SaveFindings=deserialize_list(json_data.get("SaveFindings"), SaveFindingsDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ActionsDefinition = ActionsDefinition


@dataclass
class SaveFindingsDefinition(BaseModel):
    OutputConfig: Optional[Sequence["_OutputConfigDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_SaveFindingsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SaveFindingsDefinition"]:
        if not json_data:
            return None
        return cls(
            OutputConfig=deserialize_list(json_data.get("OutputConfig"), OutputConfigDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_SaveFindingsDefinition = SaveFindingsDefinition


@dataclass
class OutputConfigDefinition(BaseModel):
    OutputSchema: Optional[str]
    Table: Optional[Sequence["_TableDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_OutputConfigDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_OutputConfigDefinition"]:
        if not json_data:
            return None
        return cls(
            OutputSchema=json_data.get("OutputSchema"),
            Table=deserialize_list(json_data.get("Table"), TableDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_OutputConfigDefinition = OutputConfigDefinition


@dataclass
class TableDefinition(BaseModel):
    DatasetId: Optional[str]
    ProjectId: Optional[str]
    TableId: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_TableDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TableDefinition"]:
        if not json_data:
            return None
        return cls(
            DatasetId=json_data.get("DatasetId"),
            ProjectId=json_data.get("ProjectId"),
            TableId=json_data.get("TableId"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TableDefinition = TableDefinition


@dataclass
class StorageConfigDefinition(BaseModel):
    BigQueryOptions: Optional[Sequence["_BigQueryOptionsDefinition"]]
    CloudStorageOptions: Optional[Sequence["_CloudStorageOptionsDefinition"]]
    DatastoreOptions: Optional[Sequence["_DatastoreOptionsDefinition"]]
    TimespanConfig: Optional[Sequence["_TimespanConfigDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_StorageConfigDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_StorageConfigDefinition"]:
        if not json_data:
            return None
        return cls(
            BigQueryOptions=deserialize_list(json_data.get("BigQueryOptions"), BigQueryOptionsDefinition),
            CloudStorageOptions=deserialize_list(json_data.get("CloudStorageOptions"), CloudStorageOptionsDefinition),
            DatastoreOptions=deserialize_list(json_data.get("DatastoreOptions"), DatastoreOptionsDefinition),
            TimespanConfig=deserialize_list(json_data.get("TimespanConfig"), TimespanConfigDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_StorageConfigDefinition = StorageConfigDefinition


@dataclass
class BigQueryOptionsDefinition(BaseModel):
    TableReference: Optional[Sequence["_TableReferenceDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_BigQueryOptionsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_BigQueryOptionsDefinition"]:
        if not json_data:
            return None
        return cls(
            TableReference=deserialize_list(json_data.get("TableReference"), TableReferenceDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_BigQueryOptionsDefinition = BigQueryOptionsDefinition


@dataclass
class TableReferenceDefinition(BaseModel):
    DatasetId: Optional[str]
    ProjectId: Optional[str]
    TableId: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_TableReferenceDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TableReferenceDefinition"]:
        if not json_data:
            return None
        return cls(
            DatasetId=json_data.get("DatasetId"),
            ProjectId=json_data.get("ProjectId"),
            TableId=json_data.get("TableId"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TableReferenceDefinition = TableReferenceDefinition


@dataclass
class CloudStorageOptionsDefinition(BaseModel):
    BytesLimitPerFile: Optional[float]
    BytesLimitPerFilePercent: Optional[float]
    FileTypes: Optional[Sequence[str]]
    FilesLimitPercent: Optional[float]
    SampleMethod: Optional[str]
    FileSet: Optional[Sequence["_FileSetDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_CloudStorageOptionsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_CloudStorageOptionsDefinition"]:
        if not json_data:
            return None
        return cls(
            BytesLimitPerFile=json_data.get("BytesLimitPerFile"),
            BytesLimitPerFilePercent=json_data.get("BytesLimitPerFilePercent"),
            FileTypes=json_data.get("FileTypes"),
            FilesLimitPercent=json_data.get("FilesLimitPercent"),
            SampleMethod=json_data.get("SampleMethod"),
            FileSet=deserialize_list(json_data.get("FileSet"), FileSetDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_CloudStorageOptionsDefinition = CloudStorageOptionsDefinition


@dataclass
class FileSetDefinition(BaseModel):
    Url: Optional[str]
    RegexFileSet: Optional[Sequence["_RegexFileSetDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_FileSetDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_FileSetDefinition"]:
        if not json_data:
            return None
        return cls(
            Url=json_data.get("Url"),
            RegexFileSet=deserialize_list(json_data.get("RegexFileSet"), RegexFileSetDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_FileSetDefinition = FileSetDefinition


@dataclass
class RegexFileSetDefinition(BaseModel):
    BucketName: Optional[str]
    ExcludeRegex: Optional[Sequence[str]]
    IncludeRegex: Optional[Sequence[str]]

    @classmethod
    def _deserialize(
        cls: Type["_RegexFileSetDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_RegexFileSetDefinition"]:
        if not json_data:
            return None
        return cls(
            BucketName=json_data.get("BucketName"),
            ExcludeRegex=json_data.get("ExcludeRegex"),
            IncludeRegex=json_data.get("IncludeRegex"),
        )


# work around possible type aliasing issues when variable has same name as a model
_RegexFileSetDefinition = RegexFileSetDefinition


@dataclass
class DatastoreOptionsDefinition(BaseModel):
    Kind: Optional[Sequence["_KindDefinition"]]
    PartitionId: Optional[Sequence["_PartitionIdDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_DatastoreOptionsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DatastoreOptionsDefinition"]:
        if not json_data:
            return None
        return cls(
            Kind=deserialize_list(json_data.get("Kind"), KindDefinition),
            PartitionId=deserialize_list(json_data.get("PartitionId"), PartitionIdDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_DatastoreOptionsDefinition = DatastoreOptionsDefinition


@dataclass
class KindDefinition(BaseModel):
    Name: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_KindDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_KindDefinition"]:
        if not json_data:
            return None
        return cls(
            Name=json_data.get("Name"),
        )


# work around possible type aliasing issues when variable has same name as a model
_KindDefinition = KindDefinition


@dataclass
class PartitionIdDefinition(BaseModel):
    NamespaceId: Optional[str]
    ProjectId: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_PartitionIdDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_PartitionIdDefinition"]:
        if not json_data:
            return None
        return cls(
            NamespaceId=json_data.get("NamespaceId"),
            ProjectId=json_data.get("ProjectId"),
        )


# work around possible type aliasing issues when variable has same name as a model
_PartitionIdDefinition = PartitionIdDefinition


@dataclass
class TimespanConfigDefinition(BaseModel):
    EnableAutoPopulationOfTimespanConfig: Optional[bool]
    EndTime: Optional[str]
    StartTime: Optional[str]
    TimestampField: Optional[Sequence["_TimestampFieldDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_TimespanConfigDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TimespanConfigDefinition"]:
        if not json_data:
            return None
        return cls(
            EnableAutoPopulationOfTimespanConfig=json_data.get("EnableAutoPopulationOfTimespanConfig"),
            EndTime=json_data.get("EndTime"),
            StartTime=json_data.get("StartTime"),
            TimestampField=deserialize_list(json_data.get("TimestampField"), TimestampFieldDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_TimespanConfigDefinition = TimespanConfigDefinition


@dataclass
class TimestampFieldDefinition(BaseModel):
    Name: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_TimestampFieldDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TimestampFieldDefinition"]:
        if not json_data:
            return None
        return cls(
            Name=json_data.get("Name"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TimestampFieldDefinition = TimestampFieldDefinition


@dataclass
class TimeoutsDefinition(BaseModel):
    Create: Optional[str]
    Delete: Optional[str]
    Update: Optional[str]

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
            Update=json_data.get("Update"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TimeoutsDefinition = TimeoutsDefinition


@dataclass
class TriggersDefinition(BaseModel):
    Schedule: Optional[Sequence["_ScheduleDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_TriggersDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TriggersDefinition"]:
        if not json_data:
            return None
        return cls(
            Schedule=deserialize_list(json_data.get("Schedule"), ScheduleDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_TriggersDefinition = TriggersDefinition


@dataclass
class ScheduleDefinition(BaseModel):
    RecurrencePeriodDuration: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ScheduleDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ScheduleDefinition"]:
        if not json_data:
            return None
        return cls(
            RecurrencePeriodDuration=json_data.get("RecurrencePeriodDuration"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ScheduleDefinition = ScheduleDefinition


