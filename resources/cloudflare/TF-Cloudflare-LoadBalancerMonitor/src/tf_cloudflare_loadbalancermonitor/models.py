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
    AllowInsecure: Optional[bool]
    CreatedOn: Optional[str]
    Description: Optional[str]
    ExpectedBody: Optional[str]
    ExpectedCodes: Optional[str]
    FollowRedirects: Optional[bool]
    Id: Optional[str]
    Interval: Optional[float]
    Method: Optional[str]
    ModifiedOn: Optional[str]
    Path: Optional[str]
    Port: Optional[float]
    ProbeZone: Optional[str]
    Retries: Optional[float]
    Timeout: Optional[float]
    Type: Optional[str]
    Header: Optional[Sequence["_HeaderDefinition"]]

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
            AllowInsecure=json_data.get("AllowInsecure"),
            CreatedOn=json_data.get("CreatedOn"),
            Description=json_data.get("Description"),
            ExpectedBody=json_data.get("ExpectedBody"),
            ExpectedCodes=json_data.get("ExpectedCodes"),
            FollowRedirects=json_data.get("FollowRedirects"),
            Id=json_data.get("Id"),
            Interval=json_data.get("Interval"),
            Method=json_data.get("Method"),
            ModifiedOn=json_data.get("ModifiedOn"),
            Path=json_data.get("Path"),
            Port=json_data.get("Port"),
            ProbeZone=json_data.get("ProbeZone"),
            Retries=json_data.get("Retries"),
            Timeout=json_data.get("Timeout"),
            Type=json_data.get("Type"),
            Header=deserialize_list(json_data.get("Header"), HeaderDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class HeaderDefinition(BaseModel):
    Header: Optional[str]
    Values: Optional[Sequence[str]]

    @classmethod
    def _deserialize(
        cls: Type["_HeaderDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_HeaderDefinition"]:
        if not json_data:
            return None
        return cls(
            Header=json_data.get("Header"),
            Values=json_data.get("Values"),
        )


# work around possible type aliasing issues when variable has same name as a model
_HeaderDefinition = HeaderDefinition


