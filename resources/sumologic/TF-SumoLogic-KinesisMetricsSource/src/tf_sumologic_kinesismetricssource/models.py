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
    AutomaticDateParsing: Optional[bool]
    Category: Optional[str]
    CollectorId: Optional[float]
    ContentType: Optional[str]
    CutoffRelativeTime: Optional[str]
    CutoffTimestamp: Optional[float]
    Description: Optional[str]
    Fields: Optional[Sequence["_FieldsDefinition"]]
    ForceTimezone: Optional[bool]
    HostName: Optional[str]
    Id: Optional[str]
    ManualPrefixRegexp: Optional[str]
    MessagePerRequest: Optional[bool]
    MultilineProcessingEnabled: Optional[bool]
    Name: Optional[str]
    Timezone: Optional[str]
    Url: Optional[str]
    UseAutolineMatching: Optional[bool]
    Authentication: Optional[Sequence["_AuthenticationDefinition"]]
    DefaultDateFormats: Optional[Sequence["_DefaultDateFormatsDefinition"]]
    Filters: Optional[Sequence["_FiltersDefinition"]]
    Path: Optional[Sequence["_PathDefinition"]]

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
            AutomaticDateParsing=json_data.get("AutomaticDateParsing"),
            Category=json_data.get("Category"),
            CollectorId=json_data.get("CollectorId"),
            ContentType=json_data.get("ContentType"),
            CutoffRelativeTime=json_data.get("CutoffRelativeTime"),
            CutoffTimestamp=json_data.get("CutoffTimestamp"),
            Description=json_data.get("Description"),
            Fields=deserialize_list(json_data.get("Fields"), FieldsDefinition),
            ForceTimezone=json_data.get("ForceTimezone"),
            HostName=json_data.get("HostName"),
            Id=json_data.get("Id"),
            ManualPrefixRegexp=json_data.get("ManualPrefixRegexp"),
            MessagePerRequest=json_data.get("MessagePerRequest"),
            MultilineProcessingEnabled=json_data.get("MultilineProcessingEnabled"),
            Name=json_data.get("Name"),
            Timezone=json_data.get("Timezone"),
            Url=json_data.get("Url"),
            UseAutolineMatching=json_data.get("UseAutolineMatching"),
            Authentication=deserialize_list(json_data.get("Authentication"), AuthenticationDefinition),
            DefaultDateFormats=deserialize_list(json_data.get("DefaultDateFormats"), DefaultDateFormatsDefinition),
            Filters=deserialize_list(json_data.get("Filters"), FiltersDefinition),
            Path=deserialize_list(json_data.get("Path"), PathDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class FieldsDefinition(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_FieldsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_FieldsDefinition"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_FieldsDefinition = FieldsDefinition


@dataclass
class AuthenticationDefinition(BaseModel):
    AccessKey: Optional[str]
    RoleArn: Optional[str]
    SecretKey: Optional[str]
    Type: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_AuthenticationDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AuthenticationDefinition"]:
        if not json_data:
            return None
        return cls(
            AccessKey=json_data.get("AccessKey"),
            RoleArn=json_data.get("RoleArn"),
            SecretKey=json_data.get("SecretKey"),
            Type=json_data.get("Type"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AuthenticationDefinition = AuthenticationDefinition


@dataclass
class DefaultDateFormatsDefinition(BaseModel):
    Format: Optional[str]
    Locator: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_DefaultDateFormatsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DefaultDateFormatsDefinition"]:
        if not json_data:
            return None
        return cls(
            Format=json_data.get("Format"),
            Locator=json_data.get("Locator"),
        )


# work around possible type aliasing issues when variable has same name as a model
_DefaultDateFormatsDefinition = DefaultDateFormatsDefinition


@dataclass
class FiltersDefinition(BaseModel):
    FilterType: Optional[str]
    Mask: Optional[str]
    Name: Optional[str]
    Regexp: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_FiltersDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_FiltersDefinition"]:
        if not json_data:
            return None
        return cls(
            FilterType=json_data.get("FilterType"),
            Mask=json_data.get("Mask"),
            Name=json_data.get("Name"),
            Regexp=json_data.get("Regexp"),
        )


# work around possible type aliasing issues when variable has same name as a model
_FiltersDefinition = FiltersDefinition


@dataclass
class PathDefinition(BaseModel):
    Type: Optional[str]
    TagFilters: Optional[Sequence["_TagFiltersDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_PathDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_PathDefinition"]:
        if not json_data:
            return None
        return cls(
            Type=json_data.get("Type"),
            TagFilters=deserialize_list(json_data.get("TagFilters"), TagFiltersDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_PathDefinition = PathDefinition


@dataclass
class TagFiltersDefinition(BaseModel):
    Namespace: Optional[str]
    Tags: Optional[Sequence[str]]
    Type: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_TagFiltersDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TagFiltersDefinition"]:
        if not json_data:
            return None
        return cls(
            Namespace=json_data.get("Namespace"),
            Tags=json_data.get("Tags"),
            Type=json_data.get("Type"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TagFiltersDefinition = TagFiltersDefinition


