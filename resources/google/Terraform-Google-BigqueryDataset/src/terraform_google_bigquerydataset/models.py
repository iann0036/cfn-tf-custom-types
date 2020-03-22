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
    CreationTime: Optional[float]
    DatasetId: Optional[str]
    DefaultPartitionExpirationMs: Optional[float]
    DefaultTableExpirationMs: Optional[float]
    DeleteContentsOnDestroy: Optional[bool]
    Description: Optional[str]
    Etag: Optional[str]
    FriendlyName: Optional[str]
    Id: Optional[str]
    Labels: Optional[Sequence["_Labels"]]
    LastModifiedTime: Optional[float]
    Location: Optional[str]
    Project: Optional[str]
    SelfLink: Optional[str]
    Access: Optional[Sequence["_Access"]]
    DefaultEncryptionConfiguration: Optional[Sequence["_DefaultEncryptionConfiguration"]]
    Timeouts: Optional["_Timeouts"]
    View: Optional[Sequence["_View"]]

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
            DatasetId=json_data.get("DatasetId"),
            DefaultPartitionExpirationMs=json_data.get("DefaultPartitionExpirationMs"),
            DefaultTableExpirationMs=json_data.get("DefaultTableExpirationMs"),
            DeleteContentsOnDestroy=json_data.get("DeleteContentsOnDestroy"),
            Description=json_data.get("Description"),
            Etag=json_data.get("Etag"),
            FriendlyName=json_data.get("FriendlyName"),
            Id=json_data.get("Id"),
            Labels=json_data.get("Labels"),
            LastModifiedTime=json_data.get("LastModifiedTime"),
            Location=json_data.get("Location"),
            Project=json_data.get("Project"),
            SelfLink=json_data.get("SelfLink"),
            Access=json_data.get("Access"),
            DefaultEncryptionConfiguration=json_data.get("DefaultEncryptionConfiguration"),
            Timeouts=Timeouts._deserialize(json_data.get("Timeouts")),
            View=json_data.get("View"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class Labels:
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Labels"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Labels"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Labels = Labels


@dataclass
class Access:
    Domain: Optional[str]
    GroupByEmail: Optional[str]
    Role: Optional[str]
    SpecialGroup: Optional[str]
    UserByEmail: Optional[str]
    View: Optional[Sequence["_View"]]

    @classmethod
    def _deserialize(
        cls: Type["_Access"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Access"]:
        if not json_data:
            return None
        return cls(
            Domain=json_data.get("Domain"),
            GroupByEmail=json_data.get("GroupByEmail"),
            Role=json_data.get("Role"),
            SpecialGroup=json_data.get("SpecialGroup"),
            UserByEmail=json_data.get("UserByEmail"),
            View=json_data.get("View"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Access = Access


@dataclass
class View:
    DatasetId: Optional[str]
    ProjectId: Optional[str]
    TableId: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_View"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_View"]:
        if not json_data:
            return None
        return cls(
            DatasetId=json_data.get("DatasetId"),
            ProjectId=json_data.get("ProjectId"),
            TableId=json_data.get("TableId"),
        )


# work around possible type aliasing issues when variable has same name as a model
_View = View


@dataclass
class DefaultEncryptionConfiguration:
    KmsKeyName: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_DefaultEncryptionConfiguration"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DefaultEncryptionConfiguration"]:
        if not json_data:
            return None
        return cls(
            KmsKeyName=json_data.get("KmsKeyName"),
        )


# work around possible type aliasing issues when variable has same name as a model
_DefaultEncryptionConfiguration = DefaultEncryptionConfiguration


@dataclass
class Timeouts:
    Create: Optional[str]
    Delete: Optional[str]
    Update: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Timeouts"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Timeouts"]:
        if not json_data:
            return None
        return cls(
            Create=json_data.get("Create"),
            Delete=json_data.get("Delete"),
            Update=json_data.get("Update"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Timeouts = Timeouts


