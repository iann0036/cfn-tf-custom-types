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
    Id: Optional[str]
    Properties: Optional[str]
    RestApiId: Optional[str]
    Location: Optional[Sequence["_LocationDefinition"]]

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
            Id=json_data.get("Id"),
            Properties=json_data.get("Properties"),
            RestApiId=json_data.get("RestApiId"),
            Location=deserialize_list(json_data.get("Location"), LocationDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class LocationDefinition(BaseModel):
    Method: Optional[str]
    Name: Optional[str]
    Path: Optional[str]
    StatusCode: Optional[str]
    Type: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_LocationDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_LocationDefinition"]:
        if not json_data:
            return None
        return cls(
            Method=json_data.get("Method"),
            Name=json_data.get("Name"),
            Path=json_data.get("Path"),
            StatusCode=json_data.get("StatusCode"),
            Type=json_data.get("Type"),
        )


# work around possible type aliasing issues when variable has same name as a model
_LocationDefinition = LocationDefinition


