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
    ContentType: Optional[str]
    CustomHeaders: Optional[Sequence["_CustomHeadersDefinition"]]
    Description: Optional[str]
    EmailSubject: Optional[str]
    Id: Optional[str]
    IsHtmlContent: Optional[bool]
    Method: Optional[str]
    Name: Optional[str]
    Recipient: Optional[str]
    TargetId: Optional[str]
    Template: Optional[str]
    Triggers: Optional[Sequence[str]]
    Route: Optional[Sequence["_RouteDefinition"]]

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
            ContentType=json_data.get("ContentType"),
            CustomHeaders=deserialize_list(json_data.get("CustomHeaders"), CustomHeadersDefinition),
            Description=json_data.get("Description"),
            EmailSubject=json_data.get("EmailSubject"),
            Id=json_data.get("Id"),
            IsHtmlContent=json_data.get("IsHtmlContent"),
            Method=json_data.get("Method"),
            Name=json_data.get("Name"),
            Recipient=json_data.get("Recipient"),
            TargetId=json_data.get("TargetId"),
            Template=json_data.get("Template"),
            Triggers=json_data.get("Triggers"),
            Route=deserialize_list(json_data.get("Route"), RouteDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class CustomHeadersDefinition(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_CustomHeadersDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_CustomHeadersDefinition"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_CustomHeadersDefinition = CustomHeadersDefinition


@dataclass
class RouteDefinition(BaseModel):
    Filter: Optional[Sequence["_FilterDefinition"]]
    Method: Optional[str]
    Target: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_RouteDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_RouteDefinition"]:
        if not json_data:
            return None
        return cls(
            Filter=deserialize_list(json_data.get("Filter"), FilterDefinition),
            Method=json_data.get("Method"),
            Target=json_data.get("Target"),
        )


# work around possible type aliasing issues when variable has same name as a model
_RouteDefinition = RouteDefinition


@dataclass
class FilterDefinition(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_FilterDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_FilterDefinition"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_FilterDefinition = FilterDefinition


