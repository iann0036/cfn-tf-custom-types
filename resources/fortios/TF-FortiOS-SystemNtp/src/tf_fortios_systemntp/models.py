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
    Authentication: Optional[str]
    DynamicSortSubtable: Optional[str]
    Id: Optional[str]
    Key: Optional[str]
    KeyId: Optional[float]
    KeyType: Optional[str]
    Ntpsync: Optional[str]
    ServerMode: Optional[str]
    SourceIp: Optional[str]
    SourceIp6: Optional[str]
    Syncinterval: Optional[float]
    Type: Optional[str]
    Vdomparam: Optional[str]
    Interface: Optional[Sequence["_InterfaceDefinition"]]
    Ntpserver: Optional[Sequence["_NtpserverDefinition"]]

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
            Authentication=json_data.get("Authentication"),
            DynamicSortSubtable=json_data.get("DynamicSortSubtable"),
            Id=json_data.get("Id"),
            Key=json_data.get("Key"),
            KeyId=json_data.get("KeyId"),
            KeyType=json_data.get("KeyType"),
            Ntpsync=json_data.get("Ntpsync"),
            ServerMode=json_data.get("ServerMode"),
            SourceIp=json_data.get("SourceIp"),
            SourceIp6=json_data.get("SourceIp6"),
            Syncinterval=json_data.get("Syncinterval"),
            Type=json_data.get("Type"),
            Vdomparam=json_data.get("Vdomparam"),
            Interface=deserialize_list(json_data.get("Interface"), InterfaceDefinition),
            Ntpserver=deserialize_list(json_data.get("Ntpserver"), NtpserverDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class InterfaceDefinition(BaseModel):
    InterfaceName: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_InterfaceDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_InterfaceDefinition"]:
        if not json_data:
            return None
        return cls(
            InterfaceName=json_data.get("InterfaceName"),
        )


# work around possible type aliasing issues when variable has same name as a model
_InterfaceDefinition = InterfaceDefinition


@dataclass
class NtpserverDefinition(BaseModel):
    Authentication: Optional[str]
    Id: Optional[float]
    Interface: Optional[str]
    InterfaceSelectMethod: Optional[str]
    Key: Optional[str]
    KeyId: Optional[float]
    Ntpv3: Optional[str]
    Server: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_NtpserverDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_NtpserverDefinition"]:
        if not json_data:
            return None
        return cls(
            Authentication=json_data.get("Authentication"),
            Id=json_data.get("Id"),
            Interface=json_data.get("Interface"),
            InterfaceSelectMethod=json_data.get("InterfaceSelectMethod"),
            Key=json_data.get("Key"),
            KeyId=json_data.get("KeyId"),
            Ntpv3=json_data.get("Ntpv3"),
            Server=json_data.get("Server"),
        )


# work around possible type aliasing issues when variable has same name as a model
_NtpserverDefinition = NtpserverDefinition


