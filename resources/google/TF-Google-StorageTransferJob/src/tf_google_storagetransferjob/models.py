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
    CreationTime: Optional[str]
    DeletionTime: Optional[str]
    Description: Optional[str]
    Id: Optional[str]
    LastModificationTime: Optional[str]
    Name: Optional[str]
    Project: Optional[str]
    Status: Optional[str]
    Schedule: Optional[Sequence["_ScheduleDefinition"]]
    TransferSpec: Optional[Sequence["_TransferSpecDefinition"]]

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
            CreationTime=json_data.get("CreationTime"),
            DeletionTime=json_data.get("DeletionTime"),
            Description=json_data.get("Description"),
            Id=json_data.get("Id"),
            LastModificationTime=json_data.get("LastModificationTime"),
            Name=json_data.get("Name"),
            Project=json_data.get("Project"),
            Status=json_data.get("Status"),
            Schedule=deserialize_list(json_data.get("Schedule"), ScheduleDefinition),
            TransferSpec=deserialize_list(json_data.get("TransferSpec"), TransferSpecDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class ScheduleDefinition(BaseModel):
    ScheduleEndDate: Optional[Sequence["_ScheduleEndDateDefinition"]]
    ScheduleStartDate: Optional[Sequence["_ScheduleStartDateDefinition"]]
    StartTimeOfDay: Optional[Sequence["_StartTimeOfDayDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_ScheduleDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ScheduleDefinition"]:
        if not json_data:
            return None
        return cls(
            ScheduleEndDate=deserialize_list(json_data.get("ScheduleEndDate"), ScheduleEndDateDefinition),
            ScheduleStartDate=deserialize_list(json_data.get("ScheduleStartDate"), ScheduleStartDateDefinition),
            StartTimeOfDay=deserialize_list(json_data.get("StartTimeOfDay"), StartTimeOfDayDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ScheduleDefinition = ScheduleDefinition


@dataclass
class ScheduleEndDateDefinition(BaseModel):
    Day: Optional[float]
    Month: Optional[float]
    Year: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_ScheduleEndDateDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ScheduleEndDateDefinition"]:
        if not json_data:
            return None
        return cls(
            Day=json_data.get("Day"),
            Month=json_data.get("Month"),
            Year=json_data.get("Year"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ScheduleEndDateDefinition = ScheduleEndDateDefinition


@dataclass
class ScheduleStartDateDefinition(BaseModel):
    Day: Optional[float]
    Month: Optional[float]
    Year: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_ScheduleStartDateDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ScheduleStartDateDefinition"]:
        if not json_data:
            return None
        return cls(
            Day=json_data.get("Day"),
            Month=json_data.get("Month"),
            Year=json_data.get("Year"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ScheduleStartDateDefinition = ScheduleStartDateDefinition


@dataclass
class StartTimeOfDayDefinition(BaseModel):
    Hours: Optional[float]
    Minutes: Optional[float]
    Nanos: Optional[float]
    Seconds: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_StartTimeOfDayDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_StartTimeOfDayDefinition"]:
        if not json_data:
            return None
        return cls(
            Hours=json_data.get("Hours"),
            Minutes=json_data.get("Minutes"),
            Nanos=json_data.get("Nanos"),
            Seconds=json_data.get("Seconds"),
        )


# work around possible type aliasing issues when variable has same name as a model
_StartTimeOfDayDefinition = StartTimeOfDayDefinition


@dataclass
class TransferSpecDefinition(BaseModel):
    AwsS3DataSource: Optional[Sequence["_AwsS3DataSourceDefinition"]]
    AzureBlobStorageDataSource: Optional[Sequence["_AzureBlobStorageDataSourceDefinition"]]
    GcsDataSink: Optional[Sequence["_GcsDataSinkDefinition"]]
    GcsDataSource: Optional[Sequence["_GcsDataSourceDefinition"]]
    HttpDataSource: Optional[Sequence["_HttpDataSourceDefinition"]]
    ObjectConditions: Optional[Sequence["_ObjectConditionsDefinition"]]
    TransferOptions: Optional[Sequence["_TransferOptionsDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_TransferSpecDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TransferSpecDefinition"]:
        if not json_data:
            return None
        return cls(
            AwsS3DataSource=deserialize_list(json_data.get("AwsS3DataSource"), AwsS3DataSourceDefinition),
            AzureBlobStorageDataSource=deserialize_list(json_data.get("AzureBlobStorageDataSource"), AzureBlobStorageDataSourceDefinition),
            GcsDataSink=deserialize_list(json_data.get("GcsDataSink"), GcsDataSinkDefinition),
            GcsDataSource=deserialize_list(json_data.get("GcsDataSource"), GcsDataSourceDefinition),
            HttpDataSource=deserialize_list(json_data.get("HttpDataSource"), HttpDataSourceDefinition),
            ObjectConditions=deserialize_list(json_data.get("ObjectConditions"), ObjectConditionsDefinition),
            TransferOptions=deserialize_list(json_data.get("TransferOptions"), TransferOptionsDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_TransferSpecDefinition = TransferSpecDefinition


@dataclass
class AwsS3DataSourceDefinition(BaseModel):
    BucketName: Optional[str]
    AwsAccessKey: Optional[Sequence["_AwsAccessKeyDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_AwsS3DataSourceDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsS3DataSourceDefinition"]:
        if not json_data:
            return None
        return cls(
            BucketName=json_data.get("BucketName"),
            AwsAccessKey=deserialize_list(json_data.get("AwsAccessKey"), AwsAccessKeyDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsS3DataSourceDefinition = AwsS3DataSourceDefinition


@dataclass
class AwsAccessKeyDefinition(BaseModel):
    AccessKeyId: Optional[str]
    SecretAccessKey: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_AwsAccessKeyDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsAccessKeyDefinition"]:
        if not json_data:
            return None
        return cls(
            AccessKeyId=json_data.get("AccessKeyId"),
            SecretAccessKey=json_data.get("SecretAccessKey"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsAccessKeyDefinition = AwsAccessKeyDefinition


@dataclass
class AzureBlobStorageDataSourceDefinition(BaseModel):
    Container: Optional[str]
    Path: Optional[str]
    StorageAccount: Optional[str]
    AzureCredentials: Optional[Sequence["_AzureCredentialsDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_AzureBlobStorageDataSourceDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AzureBlobStorageDataSourceDefinition"]:
        if not json_data:
            return None
        return cls(
            Container=json_data.get("Container"),
            Path=json_data.get("Path"),
            StorageAccount=json_data.get("StorageAccount"),
            AzureCredentials=deserialize_list(json_data.get("AzureCredentials"), AzureCredentialsDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_AzureBlobStorageDataSourceDefinition = AzureBlobStorageDataSourceDefinition


@dataclass
class AzureCredentialsDefinition(BaseModel):
    SasToken: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_AzureCredentialsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AzureCredentialsDefinition"]:
        if not json_data:
            return None
        return cls(
            SasToken=json_data.get("SasToken"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AzureCredentialsDefinition = AzureCredentialsDefinition


@dataclass
class GcsDataSinkDefinition(BaseModel):
    BucketName: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_GcsDataSinkDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_GcsDataSinkDefinition"]:
        if not json_data:
            return None
        return cls(
            BucketName=json_data.get("BucketName"),
        )


# work around possible type aliasing issues when variable has same name as a model
_GcsDataSinkDefinition = GcsDataSinkDefinition


@dataclass
class GcsDataSourceDefinition(BaseModel):
    BucketName: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_GcsDataSourceDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_GcsDataSourceDefinition"]:
        if not json_data:
            return None
        return cls(
            BucketName=json_data.get("BucketName"),
        )


# work around possible type aliasing issues when variable has same name as a model
_GcsDataSourceDefinition = GcsDataSourceDefinition


@dataclass
class HttpDataSourceDefinition(BaseModel):
    ListUrl: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_HttpDataSourceDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_HttpDataSourceDefinition"]:
        if not json_data:
            return None
        return cls(
            ListUrl=json_data.get("ListUrl"),
        )


# work around possible type aliasing issues when variable has same name as a model
_HttpDataSourceDefinition = HttpDataSourceDefinition


@dataclass
class ObjectConditionsDefinition(BaseModel):
    ExcludePrefixes: Optional[Sequence[str]]
    IncludePrefixes: Optional[Sequence[str]]
    MaxTimeElapsedSinceLastModification: Optional[str]
    MinTimeElapsedSinceLastModification: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ObjectConditionsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ObjectConditionsDefinition"]:
        if not json_data:
            return None
        return cls(
            ExcludePrefixes=json_data.get("ExcludePrefixes"),
            IncludePrefixes=json_data.get("IncludePrefixes"),
            MaxTimeElapsedSinceLastModification=json_data.get("MaxTimeElapsedSinceLastModification"),
            MinTimeElapsedSinceLastModification=json_data.get("MinTimeElapsedSinceLastModification"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ObjectConditionsDefinition = ObjectConditionsDefinition


@dataclass
class TransferOptionsDefinition(BaseModel):
    DeleteObjectsFromSourceAfterTransfer: Optional[bool]
    DeleteObjectsUniqueInSink: Optional[bool]
    OverwriteObjectsAlreadyExistingInSink: Optional[bool]

    @classmethod
    def _deserialize(
        cls: Type["_TransferOptionsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TransferOptionsDefinition"]:
        if not json_data:
            return None
        return cls(
            DeleteObjectsFromSourceAfterTransfer=json_data.get("DeleteObjectsFromSourceAfterTransfer"),
            DeleteObjectsUniqueInSink=json_data.get("DeleteObjectsUniqueInSink"),
            OverwriteObjectsAlreadyExistingInSink=json_data.get("OverwriteObjectsAlreadyExistingInSink"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TransferOptionsDefinition = TransferOptionsDefinition


