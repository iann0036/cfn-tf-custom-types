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
    Category: Optional[str]
    ChangeTime: Optional[str]
    CreateTime: Optional[str]
    Id: Optional[str]
    ImportUniqueHash: Optional[str]
    IsApplicationOwner: Optional[bool]
    IsPublishGlobal: Optional[bool]
    IsPublishGlobalRequested: Optional[bool]
    IsPublishRequested: Optional[bool]
    IsPublished: Optional[bool]
    MetaAdvices: Optional[str]
    MetaAuthor: Optional[str]
    MetaComponents: Optional[Sequence[str]]
    MetaFeatures: Optional[str]
    MetaHints: Optional[str]
    MetaIcon: Optional[str]
    MetaLicense: Optional[str]
    MetaOs: Optional[str]
    MetaOverview: Optional[str]
    MetaTermsOfUse: Optional[str]
    Name: Optional[str]
    ObjectStoragePath: Optional[str]
    PublishGlobalRequestedDate: Optional[str]
    PublishRequestedDate: Optional[str]
    PublishedDate: Optional[str]
    PublishedGlobalDate: Optional[str]
    SetupCores: Optional[float]
    SetupMemory: Optional[float]
    SetupStorageCapacity: Optional[float]
    Status: Optional[str]
    Type: Optional[str]
    UniqueHash: Optional[str]
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
            Category=json_data.get("Category"),
            ChangeTime=json_data.get("ChangeTime"),
            CreateTime=json_data.get("CreateTime"),
            Id=json_data.get("Id"),
            ImportUniqueHash=json_data.get("ImportUniqueHash"),
            IsApplicationOwner=json_data.get("IsApplicationOwner"),
            IsPublishGlobal=json_data.get("IsPublishGlobal"),
            IsPublishGlobalRequested=json_data.get("IsPublishGlobalRequested"),
            IsPublishRequested=json_data.get("IsPublishRequested"),
            IsPublished=json_data.get("IsPublished"),
            MetaAdvices=json_data.get("MetaAdvices"),
            MetaAuthor=json_data.get("MetaAuthor"),
            MetaComponents=json_data.get("MetaComponents"),
            MetaFeatures=json_data.get("MetaFeatures"),
            MetaHints=json_data.get("MetaHints"),
            MetaIcon=json_data.get("MetaIcon"),
            MetaLicense=json_data.get("MetaLicense"),
            MetaOs=json_data.get("MetaOs"),
            MetaOverview=json_data.get("MetaOverview"),
            MetaTermsOfUse=json_data.get("MetaTermsOfUse"),
            Name=json_data.get("Name"),
            ObjectStoragePath=json_data.get("ObjectStoragePath"),
            PublishGlobalRequestedDate=json_data.get("PublishGlobalRequestedDate"),
            PublishRequestedDate=json_data.get("PublishRequestedDate"),
            PublishedDate=json_data.get("PublishedDate"),
            PublishedGlobalDate=json_data.get("PublishedGlobalDate"),
            SetupCores=json_data.get("SetupCores"),
            SetupMemory=json_data.get("SetupMemory"),
            SetupStorageCapacity=json_data.get("SetupStorageCapacity"),
            Status=json_data.get("Status"),
            Type=json_data.get("Type"),
            UniqueHash=json_data.get("UniqueHash"),
            Timeouts=TimeoutsDefinition._deserialize(json_data.get("Timeouts")),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


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


