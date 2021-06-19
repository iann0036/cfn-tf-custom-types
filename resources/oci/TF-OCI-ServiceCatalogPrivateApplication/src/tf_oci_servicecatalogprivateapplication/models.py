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
    CompartmentId: Optional[str]
    DefinedTags: Optional[Sequence["_DefinedTagsDefinition"]]
    DisplayName: Optional[str]
    FreeformTags: Optional[Sequence["_FreeformTagsDefinition"]]
    Id: Optional[str]
    Logo: Optional[Sequence["_LogoDefinition"]]
    LogoFileBase64encoded: Optional[str]
    LongDescription: Optional[str]
    PackageType: Optional[str]
    ShortDescription: Optional[str]
    State: Optional[str]
    TimeCreated: Optional[str]
    TimeUpdated: Optional[str]
    PackageDetails: Optional[Sequence["_PackageDetailsDefinition"]]
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
            CompartmentId=json_data.get("CompartmentId"),
            DefinedTags=deserialize_list(json_data.get("DefinedTags"), DefinedTagsDefinition),
            DisplayName=json_data.get("DisplayName"),
            FreeformTags=deserialize_list(json_data.get("FreeformTags"), FreeformTagsDefinition),
            Id=json_data.get("Id"),
            Logo=deserialize_list(json_data.get("Logo"), LogoDefinition),
            LogoFileBase64encoded=json_data.get("LogoFileBase64encoded"),
            LongDescription=json_data.get("LongDescription"),
            PackageType=json_data.get("PackageType"),
            ShortDescription=json_data.get("ShortDescription"),
            State=json_data.get("State"),
            TimeCreated=json_data.get("TimeCreated"),
            TimeUpdated=json_data.get("TimeUpdated"),
            PackageDetails=deserialize_list(json_data.get("PackageDetails"), PackageDetailsDefinition),
            Timeouts=TimeoutsDefinition._deserialize(json_data.get("Timeouts")),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class DefinedTagsDefinition(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_DefinedTagsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DefinedTagsDefinition"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_DefinedTagsDefinition = DefinedTagsDefinition


@dataclass
class FreeformTagsDefinition(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_FreeformTagsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_FreeformTagsDefinition"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_FreeformTagsDefinition = FreeformTagsDefinition


@dataclass
class LogoDefinition(BaseModel):
    ContentUrl: Optional[str]
    DisplayName: Optional[str]
    MimeType: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_LogoDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_LogoDefinition"]:
        if not json_data:
            return None
        return cls(
            ContentUrl=json_data.get("ContentUrl"),
            DisplayName=json_data.get("DisplayName"),
            MimeType=json_data.get("MimeType"),
        )


# work around possible type aliasing issues when variable has same name as a model
_LogoDefinition = LogoDefinition


@dataclass
class PackageDetailsDefinition(BaseModel):
    PackageType: Optional[str]
    Version: Optional[str]
    ZipFileBase64encoded: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_PackageDetailsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_PackageDetailsDefinition"]:
        if not json_data:
            return None
        return cls(
            PackageType=json_data.get("PackageType"),
            Version=json_data.get("Version"),
            ZipFileBase64encoded=json_data.get("ZipFileBase64encoded"),
        )


# work around possible type aliasing issues when variable has same name as a model
_PackageDetailsDefinition = PackageDetailsDefinition


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


