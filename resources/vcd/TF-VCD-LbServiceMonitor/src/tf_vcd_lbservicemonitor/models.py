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
    EdgeGateway: Optional[str]
    Expected: Optional[str]
    Extension: Optional[Sequence["_ExtensionDefinition"]]
    Id: Optional[str]
    Interval: Optional[float]
    MaxRetries: Optional[float]
    Method: Optional[str]
    Name: Optional[str]
    Org: Optional[str]
    Receive: Optional[str]
    Send: Optional[str]
    Timeout: Optional[float]
    Type: Optional[str]
    Url: Optional[str]
    Vdc: Optional[str]

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
            EdgeGateway=json_data.get("EdgeGateway"),
            Expected=json_data.get("Expected"),
            Extension=deserialize_list(json_data.get("Extension"), ExtensionDefinition),
            Id=json_data.get("Id"),
            Interval=json_data.get("Interval"),
            MaxRetries=json_data.get("MaxRetries"),
            Method=json_data.get("Method"),
            Name=json_data.get("Name"),
            Org=json_data.get("Org"),
            Receive=json_data.get("Receive"),
            Send=json_data.get("Send"),
            Timeout=json_data.get("Timeout"),
            Type=json_data.get("Type"),
            Url=json_data.get("Url"),
            Vdc=json_data.get("Vdc"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class ExtensionDefinition(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ExtensionDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ExtensionDefinition"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ExtensionDefinition = ExtensionDefinition


