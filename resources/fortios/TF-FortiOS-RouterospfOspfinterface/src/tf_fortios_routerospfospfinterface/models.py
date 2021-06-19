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
    AuthenticationKey: Optional[str]
    Bfd: Optional[str]
    Cost: Optional[float]
    DatabaseFilterOut: Optional[str]
    DeadInterval: Optional[float]
    DynamicSortSubtable: Optional[str]
    HelloInterval: Optional[float]
    HelloMultiplier: Optional[float]
    Id: Optional[str]
    Interface: Optional[str]
    Ip: Optional[str]
    Md5Key: Optional[str]
    Md5Keychain: Optional[str]
    Mtu: Optional[float]
    MtuIgnore: Optional[str]
    Name: Optional[str]
    NetworkType: Optional[str]
    PrefixLength: Optional[float]
    Priority: Optional[float]
    ResyncTimeout: Optional[float]
    RetransmitInterval: Optional[float]
    Status: Optional[str]
    TransmitDelay: Optional[float]
    Vdomparam: Optional[str]
    Md5Keys: Optional[Sequence["_Md5KeysDefinition"]]

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
            AuthenticationKey=json_data.get("AuthenticationKey"),
            Bfd=json_data.get("Bfd"),
            Cost=json_data.get("Cost"),
            DatabaseFilterOut=json_data.get("DatabaseFilterOut"),
            DeadInterval=json_data.get("DeadInterval"),
            DynamicSortSubtable=json_data.get("DynamicSortSubtable"),
            HelloInterval=json_data.get("HelloInterval"),
            HelloMultiplier=json_data.get("HelloMultiplier"),
            Id=json_data.get("Id"),
            Interface=json_data.get("Interface"),
            Ip=json_data.get("Ip"),
            Md5Key=json_data.get("Md5Key"),
            Md5Keychain=json_data.get("Md5Keychain"),
            Mtu=json_data.get("Mtu"),
            MtuIgnore=json_data.get("MtuIgnore"),
            Name=json_data.get("Name"),
            NetworkType=json_data.get("NetworkType"),
            PrefixLength=json_data.get("PrefixLength"),
            Priority=json_data.get("Priority"),
            ResyncTimeout=json_data.get("ResyncTimeout"),
            RetransmitInterval=json_data.get("RetransmitInterval"),
            Status=json_data.get("Status"),
            TransmitDelay=json_data.get("TransmitDelay"),
            Vdomparam=json_data.get("Vdomparam"),
            Md5Keys=deserialize_list(json_data.get("Md5Keys"), Md5KeysDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class Md5KeysDefinition(BaseModel):
    Id: Optional[float]
    KeyString: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Md5KeysDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Md5KeysDefinition"]:
        if not json_data:
            return None
        return cls(
            Id=json_data.get("Id"),
            KeyString=json_data.get("KeyString"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Md5KeysDefinition = Md5KeysDefinition


