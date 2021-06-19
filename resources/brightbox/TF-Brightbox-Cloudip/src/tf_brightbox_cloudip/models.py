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
    Fqdn: Optional[str]
    Id: Optional[str]
    Locked: Optional[str]
    Name: Optional[str]
    PublicIp: Optional[str]
    PublicIpv4: Optional[str]
    PublicIpv6: Optional[str]
    ReverseDns: Optional[str]
    Status: Optional[str]
    Target: Optional[str]
    PortTranslator: Optional[Sequence["_PortTranslatorDefinition"]]
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
            Fqdn=json_data.get("Fqdn"),
            Id=json_data.get("Id"),
            Locked=json_data.get("Locked"),
            Name=json_data.get("Name"),
            PublicIp=json_data.get("PublicIp"),
            PublicIpv4=json_data.get("PublicIpv4"),
            PublicIpv6=json_data.get("PublicIpv6"),
            ReverseDns=json_data.get("ReverseDns"),
            Status=json_data.get("Status"),
            Target=json_data.get("Target"),
            PortTranslator=deserialize_list(json_data.get("PortTranslator"), PortTranslatorDefinition),
            Timeouts=TimeoutsDefinition._deserialize(json_data.get("Timeouts")),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class PortTranslatorDefinition(BaseModel):
    Incoming: Optional[float]
    Outgoing: Optional[float]
    Protocol: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_PortTranslatorDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_PortTranslatorDefinition"]:
        if not json_data:
            return None
        return cls(
            Incoming=json_data.get("Incoming"),
            Outgoing=json_data.get("Outgoing"),
            Protocol=json_data.get("Protocol"),
        )


# work around possible type aliasing issues when variable has same name as a model
_PortTranslatorDefinition = PortTranslatorDefinition


@dataclass
class TimeoutsDefinition(BaseModel):
    Create: Optional[str]
    Delete: Optional[str]

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
        )


# work around possible type aliasing issues when variable has same name as a model
_TimeoutsDefinition = TimeoutsDefinition


