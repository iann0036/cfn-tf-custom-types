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
    Content: Optional[str]
    ContentSourceId: Optional[str]
    ContentSourcePath: Optional[str]
    ContentSourceSyncAt: Optional[str]
    ContentSourceSyncMessages: Optional[Sequence[str]]
    ContentSourceSyncStatus: Optional[str]
    ContentSourceType: Optional[str]
    CreatedAt: Optional[str]
    CreatedBy: Optional[str]
    Description: Optional[str]
    Id: Optional[str]
    Name: Optional[str]
    OrgId: Optional[str]
    ProjectId: Optional[str]
    ProjectName: Optional[str]
    RequestScopeOrg: Optional[bool]
    SelfLink: Optional[str]
    Status: Optional[str]
    TotalReleasedVersions: Optional[float]
    TotalVersions: Optional[float]
    UpdatedAt: Optional[str]
    UpdatedBy: Optional[str]
    Valid: Optional[bool]
    ValidationMessages: Optional[Sequence["_ValidationMessagesDefinition2"]]

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
            Content=json_data.get("Content"),
            ContentSourceId=json_data.get("ContentSourceId"),
            ContentSourcePath=json_data.get("ContentSourcePath"),
            ContentSourceSyncAt=json_data.get("ContentSourceSyncAt"),
            ContentSourceSyncMessages=json_data.get("ContentSourceSyncMessages"),
            ContentSourceSyncStatus=json_data.get("ContentSourceSyncStatus"),
            ContentSourceType=json_data.get("ContentSourceType"),
            CreatedAt=json_data.get("CreatedAt"),
            CreatedBy=json_data.get("CreatedBy"),
            Description=json_data.get("Description"),
            Id=json_data.get("Id"),
            Name=json_data.get("Name"),
            OrgId=json_data.get("OrgId"),
            ProjectId=json_data.get("ProjectId"),
            ProjectName=json_data.get("ProjectName"),
            RequestScopeOrg=json_data.get("RequestScopeOrg"),
            SelfLink=json_data.get("SelfLink"),
            Status=json_data.get("Status"),
            TotalReleasedVersions=json_data.get("TotalReleasedVersions"),
            TotalVersions=json_data.get("TotalVersions"),
            UpdatedAt=json_data.get("UpdatedAt"),
            UpdatedBy=json_data.get("UpdatedBy"),
            Valid=json_data.get("Valid"),
            ValidationMessages=deserialize_list(json_data.get("ValidationMessages"), ValidationMessagesDefinition2),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class ValidationMessagesDefinition2(BaseModel):
    Message: Optional[str]
    Metadata: Optional[Sequence["_ValidationMessagesDefinition"]]
    Path: Optional[str]
    ResourceName: Optional[str]
    Type: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ValidationMessagesDefinition2"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ValidationMessagesDefinition2"]:
        if not json_data:
            return None
        return cls(
            Message=json_data.get("Message"),
            Metadata=deserialize_list(json_data.get("Metadata"), ValidationMessagesDefinition),
            Path=json_data.get("Path"),
            ResourceName=json_data.get("ResourceName"),
            Type=json_data.get("Type"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ValidationMessagesDefinition2 = ValidationMessagesDefinition2


@dataclass
class ValidationMessagesDefinition(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ValidationMessagesDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ValidationMessagesDefinition"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ValidationMessagesDefinition = ValidationMessagesDefinition


