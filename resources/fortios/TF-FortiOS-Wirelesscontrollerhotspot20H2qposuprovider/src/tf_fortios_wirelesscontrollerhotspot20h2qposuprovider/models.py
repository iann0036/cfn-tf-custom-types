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
    DynamicSortSubtable: Optional[str]
    Icon: Optional[str]
    Id: Optional[str]
    Name: Optional[str]
    OsuMethod: Optional[str]
    OsuNai: Optional[str]
    ServerUri: Optional[str]
    Vdomparam: Optional[str]
    FriendlyName: Optional[Sequence["_FriendlyNameDefinition"]]
    ServiceDescription: Optional[Sequence["_ServiceDescriptionDefinition"]]

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
            DynamicSortSubtable=json_data.get("DynamicSortSubtable"),
            Icon=json_data.get("Icon"),
            Id=json_data.get("Id"),
            Name=json_data.get("Name"),
            OsuMethod=json_data.get("OsuMethod"),
            OsuNai=json_data.get("OsuNai"),
            ServerUri=json_data.get("ServerUri"),
            Vdomparam=json_data.get("Vdomparam"),
            FriendlyName=deserialize_list(json_data.get("FriendlyName"), FriendlyNameDefinition),
            ServiceDescription=deserialize_list(json_data.get("ServiceDescription"), ServiceDescriptionDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class FriendlyNameDefinition(BaseModel):
    FriendlyName: Optional[str]
    Index: Optional[float]
    Lang: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_FriendlyNameDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_FriendlyNameDefinition"]:
        if not json_data:
            return None
        return cls(
            FriendlyName=json_data.get("FriendlyName"),
            Index=json_data.get("Index"),
            Lang=json_data.get("Lang"),
        )


# work around possible type aliasing issues when variable has same name as a model
_FriendlyNameDefinition = FriendlyNameDefinition


@dataclass
class ServiceDescriptionDefinition(BaseModel):
    Lang: Optional[str]
    ServiceDescription: Optional[str]
    ServiceId: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_ServiceDescriptionDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ServiceDescriptionDefinition"]:
        if not json_data:
            return None
        return cls(
            Lang=json_data.get("Lang"),
            ServiceDescription=json_data.get("ServiceDescription"),
            ServiceId=json_data.get("ServiceId"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ServiceDescriptionDefinition = ServiceDescriptionDefinition


