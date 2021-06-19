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
    DefaultOriginate: Optional[bool]
    Description: Optional[str]
    DisplayName: Optional[str]
    Ecmp: Optional[bool]
    Enabled: Optional[bool]
    GatewayId: Optional[str]
    GatewayPath: Optional[str]
    GracefulRestartMode: Optional[str]
    Id: Optional[str]
    LocaleServiceId: Optional[str]
    Path: Optional[str]
    Revision: Optional[float]
    SummaryAddress: Optional[Sequence["_SummaryAddressDefinition"]]
    Tag: Optional[Sequence["_TagDefinition"]]

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
            DefaultOriginate=json_data.get("DefaultOriginate"),
            Description=json_data.get("Description"),
            DisplayName=json_data.get("DisplayName"),
            Ecmp=json_data.get("Ecmp"),
            Enabled=json_data.get("Enabled"),
            GatewayId=json_data.get("GatewayId"),
            GatewayPath=json_data.get("GatewayPath"),
            GracefulRestartMode=json_data.get("GracefulRestartMode"),
            Id=json_data.get("Id"),
            LocaleServiceId=json_data.get("LocaleServiceId"),
            Path=json_data.get("Path"),
            Revision=json_data.get("Revision"),
            SummaryAddress=deserialize_list(json_data.get("SummaryAddress"), SummaryAddressDefinition),
            Tag=deserialize_list(json_data.get("Tag"), TagDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class SummaryAddressDefinition(BaseModel):
    Advertise: Optional[bool]
    Prefix: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_SummaryAddressDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SummaryAddressDefinition"]:
        if not json_data:
            return None
        return cls(
            Advertise=json_data.get("Advertise"),
            Prefix=json_data.get("Prefix"),
        )


# work around possible type aliasing issues when variable has same name as a model
_SummaryAddressDefinition = SummaryAddressDefinition


@dataclass
class TagDefinition(BaseModel):
    Scope: Optional[str]
    Tag: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_TagDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TagDefinition"]:
        if not json_data:
            return None
        return cls(
            Scope=json_data.get("Scope"),
            Tag=json_data.get("Tag"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TagDefinition = TagDefinition


