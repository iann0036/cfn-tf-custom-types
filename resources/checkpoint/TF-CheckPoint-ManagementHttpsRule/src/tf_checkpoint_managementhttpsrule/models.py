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
    Action: Optional[str]
    Blade: Optional[Sequence[str]]
    Certificate: Optional[str]
    Comments: Optional[str]
    Destination: Optional[Sequence[str]]
    DestinationNegate: Optional[bool]
    Enabled: Optional[bool]
    Id: Optional[str]
    IgnoreErrors: Optional[bool]
    IgnoreWarnings: Optional[bool]
    InstallOn: Optional[Sequence[str]]
    Layer: Optional[str]
    Name: Optional[str]
    Position: Optional[Sequence["_PositionDefinition"]]
    Service: Optional[Sequence[str]]
    ServiceNegate: Optional[bool]
    SiteCategory: Optional[Sequence[str]]
    SiteCategoryNegate: Optional[bool]
    Source: Optional[Sequence[str]]
    SourceNegate: Optional[bool]
    Track: Optional[str]

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
            Action=json_data.get("Action"),
            Blade=json_data.get("Blade"),
            Certificate=json_data.get("Certificate"),
            Comments=json_data.get("Comments"),
            Destination=json_data.get("Destination"),
            DestinationNegate=json_data.get("DestinationNegate"),
            Enabled=json_data.get("Enabled"),
            Id=json_data.get("Id"),
            IgnoreErrors=json_data.get("IgnoreErrors"),
            IgnoreWarnings=json_data.get("IgnoreWarnings"),
            InstallOn=json_data.get("InstallOn"),
            Layer=json_data.get("Layer"),
            Name=json_data.get("Name"),
            Position=deserialize_list(json_data.get("Position"), PositionDefinition),
            Service=json_data.get("Service"),
            ServiceNegate=json_data.get("ServiceNegate"),
            SiteCategory=json_data.get("SiteCategory"),
            SiteCategoryNegate=json_data.get("SiteCategoryNegate"),
            Source=json_data.get("Source"),
            SourceNegate=json_data.get("SourceNegate"),
            Track=json_data.get("Track"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class PositionDefinition(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_PositionDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_PositionDefinition"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_PositionDefinition = PositionDefinition


