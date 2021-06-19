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
    Annotations: Optional[Sequence["_AnnotationsDefinition"]]
    ClusterId: Optional[str]
    Filename: Optional[str]
    Id: Optional[str]
    Labels: Optional[Sequence["_LabelsDefinition"]]
    Manual: Optional[bool]
    Name: Optional[str]
    NamespaceId: Optional[str]
    BackupConfig: Optional[Sequence["_BackupConfigDefinition"]]
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
            Annotations=deserialize_list(json_data.get("Annotations"), AnnotationsDefinition),
            ClusterId=json_data.get("ClusterId"),
            Filename=json_data.get("Filename"),
            Id=json_data.get("Id"),
            Labels=deserialize_list(json_data.get("Labels"), LabelsDefinition),
            Manual=json_data.get("Manual"),
            Name=json_data.get("Name"),
            NamespaceId=json_data.get("NamespaceId"),
            BackupConfig=deserialize_list(json_data.get("BackupConfig"), BackupConfigDefinition),
            Timeouts=TimeoutsDefinition._deserialize(json_data.get("Timeouts")),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class AnnotationsDefinition(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_AnnotationsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AnnotationsDefinition"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AnnotationsDefinition = AnnotationsDefinition


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
class BackupConfigDefinition(BaseModel):
    Enabled: Optional[bool]
    IntervalHours: Optional[float]
    Retention: Optional[float]
    SafeTimestamp: Optional[bool]
    Timeout: Optional[float]
    S3BackupConfig: Optional[Sequence["_S3BackupConfigDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_BackupConfigDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_BackupConfigDefinition"]:
        if not json_data:
            return None
        return cls(
            Enabled=json_data.get("Enabled"),
            IntervalHours=json_data.get("IntervalHours"),
            Retention=json_data.get("Retention"),
            SafeTimestamp=json_data.get("SafeTimestamp"),
            Timeout=json_data.get("Timeout"),
            S3BackupConfig=deserialize_list(json_data.get("S3BackupConfig"), S3BackupConfigDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_BackupConfigDefinition = BackupConfigDefinition


@dataclass
class S3BackupConfigDefinition(BaseModel):
    AccessKey: Optional[str]
    BucketName: Optional[str]
    CustomCa: Optional[str]
    Endpoint: Optional[str]
    Folder: Optional[str]
    Region: Optional[str]
    SecretKey: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_S3BackupConfigDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_S3BackupConfigDefinition"]:
        if not json_data:
            return None
        return cls(
            AccessKey=json_data.get("AccessKey"),
            BucketName=json_data.get("BucketName"),
            CustomCa=json_data.get("CustomCa"),
            Endpoint=json_data.get("Endpoint"),
            Folder=json_data.get("Folder"),
            Region=json_data.get("Region"),
            SecretKey=json_data.get("SecretKey"),
        )


# work around possible type aliasing issues when variable has same name as a model
_S3BackupConfigDefinition = S3BackupConfigDefinition


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


