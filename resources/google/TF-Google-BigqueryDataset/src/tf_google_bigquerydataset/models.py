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
    CreationTime: Optional[float]
    DatasetId: Optional[str]
    DefaultPartitionExpirationMs: Optional[float]
    DefaultTableExpirationMs: Optional[float]
    DeleteContentsOnDestroy: Optional[bool]
    Description: Optional[str]
    Etag: Optional[str]
    FriendlyName: Optional[str]
    Id: Optional[str]
    Labels: Optional[Sequence["_LabelsDefinition"]]
    LastModifiedTime: Optional[float]
    Location: Optional[str]
    Project: Optional[str]
    SelfLink: Optional[str]
    Access: Optional[Sequence["_AccessDefinition"]]
    DefaultEncryptionConfiguration: Optional[Sequence["_DefaultEncryptionConfigurationDefinition"]]
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
            CreationTime=json_data.get("CreationTime"),
            DatasetId=json_data.get("DatasetId"),
            DefaultPartitionExpirationMs=json_data.get("DefaultPartitionExpirationMs"),
            DefaultTableExpirationMs=json_data.get("DefaultTableExpirationMs"),
            DeleteContentsOnDestroy=json_data.get("DeleteContentsOnDestroy"),
            Description=json_data.get("Description"),
            Etag=json_data.get("Etag"),
            FriendlyName=json_data.get("FriendlyName"),
            Id=json_data.get("Id"),
            Labels=deserialize_list(json_data.get("Labels"), LabelsDefinition),
            LastModifiedTime=json_data.get("LastModifiedTime"),
            Location=json_data.get("Location"),
            Project=json_data.get("Project"),
            SelfLink=json_data.get("SelfLink"),
            Access=deserialize_list(json_data.get("Access"), AccessDefinition),
            DefaultEncryptionConfiguration=deserialize_list(json_data.get("DefaultEncryptionConfiguration"), DefaultEncryptionConfigurationDefinition),
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
class AccessDefinition(BaseModel):
    Domain: Optional[str]
    GroupByEmail: Optional[str]
    Role: Optional[str]
    SpecialGroup: Optional[str]
    UserByEmail: Optional[str]
    View: Optional[Sequence["_ViewDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_AccessDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AccessDefinition"]:
        if not json_data:
            return None
        return cls(
            Domain=json_data.get("Domain"),
            GroupByEmail=json_data.get("GroupByEmail"),
            Role=json_data.get("Role"),
            SpecialGroup=json_data.get("SpecialGroup"),
            UserByEmail=json_data.get("UserByEmail"),
            View=deserialize_list(json_data.get("View"), ViewDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_AccessDefinition = AccessDefinition


@dataclass
class ViewDefinition(BaseModel):
    DatasetId: Optional[str]
    ProjectId: Optional[str]
    TableId: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ViewDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ViewDefinition"]:
        if not json_data:
            return None
        return cls(
            DatasetId=json_data.get("DatasetId"),
            ProjectId=json_data.get("ProjectId"),
            TableId=json_data.get("TableId"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ViewDefinition = ViewDefinition


@dataclass
class DefaultEncryptionConfigurationDefinition(BaseModel):
    KmsKeyName: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_DefaultEncryptionConfigurationDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DefaultEncryptionConfigurationDefinition"]:
        if not json_data:
            return None
        return cls(
            KmsKeyName=json_data.get("KmsKeyName"),
        )


# work around possible type aliasing issues when variable has same name as a model
_DefaultEncryptionConfigurationDefinition = DefaultEncryptionConfigurationDefinition


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


