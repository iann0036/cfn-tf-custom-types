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
    CapacityInGb: Optional[float]
    CreatedAt: Optional[str]
    CustomProperties: Optional[Sequence["_CustomPropertiesDefinition"]]
    DeploymentId: Optional[str]
    Description: Optional[str]
    DiskContentBase64: Optional[str]
    Encrypted: Optional[bool]
    ExpandSnapshots: Optional[bool]
    ExternalId: Optional[str]
    ExternalRegionId: Optional[str]
    ExternalZoneId: Optional[str]
    Id: Optional[str]
    Links: Optional[Sequence["_LinksDefinition"]]
    Name: Optional[str]
    OrgId: Optional[str]
    Owner: Optional[str]
    Persistent: Optional[bool]
    ProjectId: Optional[str]
    Purge: Optional[bool]
    Snapshots: Optional[Sequence["_SnapshotsDefinition2"]]
    SourceReference: Optional[str]
    Status: Optional[str]
    UpdatedAt: Optional[str]
    Constraints: Optional[Sequence["_ConstraintsDefinition"]]
    Tags: Optional[Sequence["_TagsDefinition"]]
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
            CapacityInGb=json_data.get("CapacityInGb"),
            CreatedAt=json_data.get("CreatedAt"),
            CustomProperties=deserialize_list(json_data.get("CustomProperties"), CustomPropertiesDefinition),
            DeploymentId=json_data.get("DeploymentId"),
            Description=json_data.get("Description"),
            DiskContentBase64=json_data.get("DiskContentBase64"),
            Encrypted=json_data.get("Encrypted"),
            ExpandSnapshots=json_data.get("ExpandSnapshots"),
            ExternalId=json_data.get("ExternalId"),
            ExternalRegionId=json_data.get("ExternalRegionId"),
            ExternalZoneId=json_data.get("ExternalZoneId"),
            Id=json_data.get("Id"),
            Links=deserialize_list(json_data.get("Links"), LinksDefinition),
            Name=json_data.get("Name"),
            OrgId=json_data.get("OrgId"),
            Owner=json_data.get("Owner"),
            Persistent=json_data.get("Persistent"),
            ProjectId=json_data.get("ProjectId"),
            Purge=json_data.get("Purge"),
            Snapshots=deserialize_list(json_data.get("Snapshots"), SnapshotsDefinition2),
            SourceReference=json_data.get("SourceReference"),
            Status=json_data.get("Status"),
            UpdatedAt=json_data.get("UpdatedAt"),
            Constraints=deserialize_list(json_data.get("Constraints"), ConstraintsDefinition),
            Tags=deserialize_list(json_data.get("Tags"), TagsDefinition),
            Timeouts=TimeoutsDefinition._deserialize(json_data.get("Timeouts")),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class CustomPropertiesDefinition(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_CustomPropertiesDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_CustomPropertiesDefinition"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_CustomPropertiesDefinition = CustomPropertiesDefinition


@dataclass
class LinksDefinition(BaseModel):
    Href: Optional[str]
    Hrefs: Optional[Sequence[str]]
    Rel: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_LinksDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_LinksDefinition"]:
        if not json_data:
            return None
        return cls(
            Href=json_data.get("Href"),
            Hrefs=json_data.get("Hrefs"),
            Rel=json_data.get("Rel"),
        )


# work around possible type aliasing issues when variable has same name as a model
_LinksDefinition = LinksDefinition


@dataclass
class SnapshotsDefinition2(BaseModel):
    CreatedAt: Optional[str]
    Description: Optional[str]
    Id: Optional[str]
    IsCurrent: Optional[bool]
    Links: Optional[Sequence["_SnapshotsDefinition"]]
    Name: Optional[str]
    OrgId: Optional[str]
    Owner: Optional[str]
    UpdatedAt: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_SnapshotsDefinition2"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SnapshotsDefinition2"]:
        if not json_data:
            return None
        return cls(
            CreatedAt=json_data.get("CreatedAt"),
            Description=json_data.get("Description"),
            Id=json_data.get("Id"),
            IsCurrent=json_data.get("IsCurrent"),
            Links=deserialize_list(json_data.get("Links"), SnapshotsDefinition),
            Name=json_data.get("Name"),
            OrgId=json_data.get("OrgId"),
            Owner=json_data.get("Owner"),
            UpdatedAt=json_data.get("UpdatedAt"),
        )


# work around possible type aliasing issues when variable has same name as a model
_SnapshotsDefinition2 = SnapshotsDefinition2


@dataclass
class SnapshotsDefinition(BaseModel):
    Href: Optional[str]
    Hrefs: Optional[Sequence[str]]
    Rel: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_SnapshotsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SnapshotsDefinition"]:
        if not json_data:
            return None
        return cls(
            Href=json_data.get("Href"),
            Hrefs=json_data.get("Hrefs"),
            Rel=json_data.get("Rel"),
        )


# work around possible type aliasing issues when variable has same name as a model
_SnapshotsDefinition = SnapshotsDefinition


@dataclass
class ConstraintsDefinition(BaseModel):
    Expression: Optional[str]
    Mandatory: Optional[bool]

    @classmethod
    def _deserialize(
        cls: Type["_ConstraintsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ConstraintsDefinition"]:
        if not json_data:
            return None
        return cls(
            Expression=json_data.get("Expression"),
            Mandatory=json_data.get("Mandatory"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ConstraintsDefinition = ConstraintsDefinition


@dataclass
class TagsDefinition(BaseModel):
    Key: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_TagsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TagsDefinition"]:
        if not json_data:
            return None
        return cls(
            Key=json_data.get("Key"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TagsDefinition = TagsDefinition


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


