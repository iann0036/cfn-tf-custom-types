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
    Capacity: Optional[float]
    ChangeTime: Optional[str]
    CreateTime: Optional[str]
    CurrentPrice: Optional[float]
    Id: Optional[str]
    Labels: Optional[Sequence[str]]
    LicenseProductNo: Optional[float]
    LocationCountry: Optional[str]
    LocationIata: Optional[str]
    LocationName: Optional[str]
    LocationUuid: Optional[str]
    Name: Optional[str]
    Status: Optional[str]
    StorageUuid: Optional[str]
    UsageInMinutes: Optional[float]
    ObjectStorageExport: Optional[Sequence["_ObjectStorageExportDefinition"]]
    Rollback: Optional[Sequence["_RollbackDefinition"]]
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
            Capacity=json_data.get("Capacity"),
            ChangeTime=json_data.get("ChangeTime"),
            CreateTime=json_data.get("CreateTime"),
            CurrentPrice=json_data.get("CurrentPrice"),
            Id=json_data.get("Id"),
            Labels=json_data.get("Labels"),
            LicenseProductNo=json_data.get("LicenseProductNo"),
            LocationCountry=json_data.get("LocationCountry"),
            LocationIata=json_data.get("LocationIata"),
            LocationName=json_data.get("LocationName"),
            LocationUuid=json_data.get("LocationUuid"),
            Name=json_data.get("Name"),
            Status=json_data.get("Status"),
            StorageUuid=json_data.get("StorageUuid"),
            UsageInMinutes=json_data.get("UsageInMinutes"),
            ObjectStorageExport=deserialize_list(json_data.get("ObjectStorageExport"), ObjectStorageExportDefinition),
            Rollback=deserialize_list(json_data.get("Rollback"), RollbackDefinition),
            Timeouts=TimeoutsDefinition._deserialize(json_data.get("Timeouts")),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class ObjectStorageExportDefinition(BaseModel):
    AccessKey: Optional[str]
    Bucket: Optional[str]
    Host: Optional[str]
    Object: Optional[str]
    Private: Optional[bool]
    SecretKey: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ObjectStorageExportDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ObjectStorageExportDefinition"]:
        if not json_data:
            return None
        return cls(
            AccessKey=json_data.get("AccessKey"),
            Bucket=json_data.get("Bucket"),
            Host=json_data.get("Host"),
            Object=json_data.get("Object"),
            Private=json_data.get("Private"),
            SecretKey=json_data.get("SecretKey"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ObjectStorageExportDefinition = ObjectStorageExportDefinition


@dataclass
class RollbackDefinition(BaseModel):
    Id: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_RollbackDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_RollbackDefinition"]:
        if not json_data:
            return None
        return cls(
            Id=json_data.get("Id"),
        )


# work around possible type aliasing issues when variable has same name as a model
_RollbackDefinition = RollbackDefinition


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


