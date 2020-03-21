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
    CreationTime: Optional[str]
    DeletionTime: Optional[str]
    Description: Optional[str]
    LastModificationTime: Optional[str]
    Name: Optional[str]
    Project: Optional[str]
    Status: Optional[str]
    Schedule: Optional[Sequence["_Schedule"]]
    TransferSpec: Optional[Sequence["_TransferSpec"]]
    ScheduleEndDate: Optional[Sequence["_ScheduleEndDate"]]
    ScheduleStartDate: Optional[Sequence["_ScheduleStartDate"]]
    StartTimeOfDay: Optional[Sequence["_StartTimeOfDay"]]
    AwsS3DataSource: Optional[Sequence["_AwsS3DataSource"]]
    GcsDataSink: Optional[Sequence["_GcsDataSink"]]
    GcsDataSource: Optional[Sequence["_GcsDataSource"]]
    HttpDataSource: Optional[Sequence["_HttpDataSource"]]
    ObjectConditions: Optional[Sequence["_ObjectConditions"]]
    TransferOptions: Optional[Sequence["_TransferOptions"]]
    AwsAccessKey: Optional[Sequence["_AwsAccessKey"]]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceModel"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceModel"]:
        if not json_data:
            return None
        return cls(
            tfcfnid=json_data.get("tfcfnid"),
            CreationTime=json_data.get("CreationTime"),
            DeletionTime=json_data.get("DeletionTime"),
            Description=json_data.get("Description"),
            LastModificationTime=json_data.get("LastModificationTime"),
            Name=json_data.get("Name"),
            Project=json_data.get("Project"),
            Status=json_data.get("Status"),
            Schedule=json_data.get("Schedule"),
            TransferSpec=json_data.get("TransferSpec"),
            ScheduleEndDate=json_data.get("ScheduleEndDate"),
            ScheduleStartDate=json_data.get("ScheduleStartDate"),
            StartTimeOfDay=json_data.get("StartTimeOfDay"),
            AwsS3DataSource=json_data.get("AwsS3DataSource"),
            GcsDataSink=json_data.get("GcsDataSink"),
            GcsDataSource=json_data.get("GcsDataSource"),
            HttpDataSource=json_data.get("HttpDataSource"),
            ObjectConditions=json_data.get("ObjectConditions"),
            TransferOptions=json_data.get("TransferOptions"),
            AwsAccessKey=json_data.get("AwsAccessKey"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class Schedule:
    ScheduleEndDate: Optional[Sequence["_ScheduleEndDate"]]
    ScheduleStartDate: Optional[Sequence["_ScheduleStartDate"]]
    StartTimeOfDay: Optional[Sequence["_StartTimeOfDay"]]

    @classmethod
    def _deserialize(
        cls: Type["_Schedule"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Schedule"]:
        if not json_data:
            return None
        return cls(
            ScheduleEndDate=json_data.get("ScheduleEndDate"),
            ScheduleStartDate=json_data.get("ScheduleStartDate"),
            StartTimeOfDay=json_data.get("StartTimeOfDay"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Schedule = Schedule


@dataclass
class ScheduleEndDate:
    Day: Optional[float]
    Month: Optional[float]
    Year: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_ScheduleEndDate"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ScheduleEndDate"]:
        if not json_data:
            return None
        return cls(
            Day=json_data.get("Day"),
            Month=json_data.get("Month"),
            Year=json_data.get("Year"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ScheduleEndDate = ScheduleEndDate


@dataclass
class ScheduleStartDate:
    Day: Optional[float]
    Month: Optional[float]
    Year: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_ScheduleStartDate"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ScheduleStartDate"]:
        if not json_data:
            return None
        return cls(
            Day=json_data.get("Day"),
            Month=json_data.get("Month"),
            Year=json_data.get("Year"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ScheduleStartDate = ScheduleStartDate


@dataclass
class StartTimeOfDay:
    Hours: Optional[float]
    Minutes: Optional[float]
    Nanos: Optional[float]
    Seconds: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_StartTimeOfDay"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_StartTimeOfDay"]:
        if not json_data:
            return None
        return cls(
            Hours=json_data.get("Hours"),
            Minutes=json_data.get("Minutes"),
            Nanos=json_data.get("Nanos"),
            Seconds=json_data.get("Seconds"),
        )


# work around possible type aliasing issues when variable has same name as a model
_StartTimeOfDay = StartTimeOfDay


@dataclass
class TransferSpec:
    AwsS3DataSource: Optional[Sequence["_AwsS3DataSource"]]
    GcsDataSink: Optional[Sequence["_GcsDataSink"]]
    GcsDataSource: Optional[Sequence["_GcsDataSource"]]
    HttpDataSource: Optional[Sequence["_HttpDataSource"]]
    ObjectConditions: Optional[Sequence["_ObjectConditions"]]
    TransferOptions: Optional[Sequence["_TransferOptions"]]

    @classmethod
    def _deserialize(
        cls: Type["_TransferSpec"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TransferSpec"]:
        if not json_data:
            return None
        return cls(
            AwsS3DataSource=json_data.get("AwsS3DataSource"),
            GcsDataSink=json_data.get("GcsDataSink"),
            GcsDataSource=json_data.get("GcsDataSource"),
            HttpDataSource=json_data.get("HttpDataSource"),
            ObjectConditions=json_data.get("ObjectConditions"),
            TransferOptions=json_data.get("TransferOptions"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TransferSpec = TransferSpec


@dataclass
class AwsS3DataSource:
    BucketName: Optional[str]
    AwsAccessKey: Optional[Sequence["_AwsAccessKey"]]

    @classmethod
    def _deserialize(
        cls: Type["_AwsS3DataSource"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsS3DataSource"]:
        if not json_data:
            return None
        return cls(
            BucketName=json_data.get("BucketName"),
            AwsAccessKey=json_data.get("AwsAccessKey"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsS3DataSource = AwsS3DataSource


@dataclass
class AwsAccessKey:
    AccessKeyId: Optional[str]
    SecretAccessKey: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_AwsAccessKey"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsAccessKey"]:
        if not json_data:
            return None
        return cls(
            AccessKeyId=json_data.get("AccessKeyId"),
            SecretAccessKey=json_data.get("SecretAccessKey"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsAccessKey = AwsAccessKey


@dataclass
class GcsDataSink:
    BucketName: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_GcsDataSink"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_GcsDataSink"]:
        if not json_data:
            return None
        return cls(
            BucketName=json_data.get("BucketName"),
        )


# work around possible type aliasing issues when variable has same name as a model
_GcsDataSink = GcsDataSink


@dataclass
class GcsDataSource:
    BucketName: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_GcsDataSource"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_GcsDataSource"]:
        if not json_data:
            return None
        return cls(
            BucketName=json_data.get("BucketName"),
        )


# work around possible type aliasing issues when variable has same name as a model
_GcsDataSource = GcsDataSource


@dataclass
class HttpDataSource:
    ListUrl: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_HttpDataSource"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_HttpDataSource"]:
        if not json_data:
            return None
        return cls(
            ListUrl=json_data.get("ListUrl"),
        )


# work around possible type aliasing issues when variable has same name as a model
_HttpDataSource = HttpDataSource


@dataclass
class ObjectConditions:
    ExcludePrefixes: Optional[Sequence[str]]
    IncludePrefixes: Optional[Sequence[str]]
    MaxTimeElapsedSinceLastModification: Optional[str]
    MinTimeElapsedSinceLastModification: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ObjectConditions"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ObjectConditions"]:
        if not json_data:
            return None
        return cls(
            ExcludePrefixes=json_data.get("ExcludePrefixes"),
            IncludePrefixes=json_data.get("IncludePrefixes"),
            MaxTimeElapsedSinceLastModification=json_data.get("MaxTimeElapsedSinceLastModification"),
            MinTimeElapsedSinceLastModification=json_data.get("MinTimeElapsedSinceLastModification"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ObjectConditions = ObjectConditions


@dataclass
class TransferOptions:
    DeleteObjectsFromSourceAfterTransfer: Optional[bool]
    DeleteObjectsUniqueInSink: Optional[bool]
    OverwriteObjectsAlreadyExistingInSink: Optional[bool]

    @classmethod
    def _deserialize(
        cls: Type["_TransferOptions"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TransferOptions"]:
        if not json_data:
            return None
        return cls(
            DeleteObjectsFromSourceAfterTransfer=json_data.get("DeleteObjectsFromSourceAfterTransfer"),
            DeleteObjectsUniqueInSink=json_data.get("DeleteObjectsUniqueInSink"),
            OverwriteObjectsAlreadyExistingInSink=json_data.get("OverwriteObjectsAlreadyExistingInSink"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TransferOptions = TransferOptions


