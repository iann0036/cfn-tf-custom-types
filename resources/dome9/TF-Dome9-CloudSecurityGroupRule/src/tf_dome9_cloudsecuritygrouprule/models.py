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
    Dome9SecurityGroupId: Optional[str]
    Id: Optional[str]
    Services: Optional[Sequence["_ServicesDefinition"]]

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
            Dome9SecurityGroupId=json_data.get("Dome9SecurityGroupId"),
            Id=json_data.get("Id"),
            Services=deserialize_list(json_data.get("Services"), ServicesDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class ServicesDefinition(BaseModel):
    Inbound: Optional[Sequence["_InboundDefinition"]]
    Outbound: Optional[Sequence["_OutboundDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_ServicesDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ServicesDefinition"]:
        if not json_data:
            return None
        return cls(
            Inbound=deserialize_list(json_data.get("Inbound"), InboundDefinition),
            Outbound=deserialize_list(json_data.get("Outbound"), OutboundDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ServicesDefinition = ServicesDefinition


@dataclass
class InboundDefinition(BaseModel):
    Description: Optional[str]
    Name: Optional[str]
    OpenForAll: Optional[bool]
    Port: Optional[str]
    ProtocolType: Optional[str]
    Scope: Optional[Sequence["_ScopeDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_InboundDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_InboundDefinition"]:
        if not json_data:
            return None
        return cls(
            Description=json_data.get("Description"),
            Name=json_data.get("Name"),
            OpenForAll=json_data.get("OpenForAll"),
            Port=json_data.get("Port"),
            ProtocolType=json_data.get("ProtocolType"),
            Scope=deserialize_list(json_data.get("Scope"), ScopeDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_InboundDefinition = InboundDefinition


@dataclass
class ScopeDefinition(BaseModel):
    Data: Optional[Sequence["_DataDefinition"]]
    Type: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ScopeDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ScopeDefinition"]:
        if not json_data:
            return None
        return cls(
            Data=deserialize_list(json_data.get("Data"), DataDefinition),
            Type=json_data.get("Type"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ScopeDefinition = ScopeDefinition


@dataclass
class DataDefinition(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_DataDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DataDefinition"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_DataDefinition = DataDefinition


@dataclass
class OutboundDefinition(BaseModel):
    Description: Optional[str]
    Name: Optional[str]
    OpenForAll: Optional[bool]
    Port: Optional[str]
    ProtocolType: Optional[str]
    Scope: Optional[Sequence["_ScopeDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_OutboundDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_OutboundDefinition"]:
        if not json_data:
            return None
        return cls(
            Description=json_data.get("Description"),
            Name=json_data.get("Name"),
            OpenForAll=json_data.get("OpenForAll"),
            Port=json_data.get("Port"),
            ProtocolType=json_data.get("ProtocolType"),
            Scope=deserialize_list(json_data.get("Scope"), ScopeDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_OutboundDefinition = OutboundDefinition


