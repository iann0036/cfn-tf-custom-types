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
    AllowMonitor: Optional[str]
    AllowPushConfiguration: Optional[str]
    AllowPushFirmware: Optional[str]
    AllowRemoteFirmwareUpgrade: Optional[str]
    CaCert: Optional[str]
    DynamicSortSubtable: Optional[str]
    EncAlgorithm: Optional[str]
    Fmg: Optional[str]
    FmgSourceIp: Optional[str]
    FmgSourceIp6: Optional[str]
    FmgUpdatePort: Optional[str]
    Id: Optional[str]
    IncludeDefaultServers: Optional[str]
    Interface: Optional[str]
    InterfaceSelectMethod: Optional[str]
    LocalCert: Optional[str]
    Mode: Optional[str]
    ScheduleConfigRestore: Optional[str]
    ScheduleScriptRestore: Optional[str]
    SerialNumber: Optional[str]
    Type: Optional[str]
    Vdom: Optional[str]
    Vdomparam: Optional[str]
    ServerList: Optional[Sequence["_ServerListDefinition"]]

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
            AllowMonitor=json_data.get("AllowMonitor"),
            AllowPushConfiguration=json_data.get("AllowPushConfiguration"),
            AllowPushFirmware=json_data.get("AllowPushFirmware"),
            AllowRemoteFirmwareUpgrade=json_data.get("AllowRemoteFirmwareUpgrade"),
            CaCert=json_data.get("CaCert"),
            DynamicSortSubtable=json_data.get("DynamicSortSubtable"),
            EncAlgorithm=json_data.get("EncAlgorithm"),
            Fmg=json_data.get("Fmg"),
            FmgSourceIp=json_data.get("FmgSourceIp"),
            FmgSourceIp6=json_data.get("FmgSourceIp6"),
            FmgUpdatePort=json_data.get("FmgUpdatePort"),
            Id=json_data.get("Id"),
            IncludeDefaultServers=json_data.get("IncludeDefaultServers"),
            Interface=json_data.get("Interface"),
            InterfaceSelectMethod=json_data.get("InterfaceSelectMethod"),
            LocalCert=json_data.get("LocalCert"),
            Mode=json_data.get("Mode"),
            ScheduleConfigRestore=json_data.get("ScheduleConfigRestore"),
            ScheduleScriptRestore=json_data.get("ScheduleScriptRestore"),
            SerialNumber=json_data.get("SerialNumber"),
            Type=json_data.get("Type"),
            Vdom=json_data.get("Vdom"),
            Vdomparam=json_data.get("Vdomparam"),
            ServerList=deserialize_list(json_data.get("ServerList"), ServerListDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class ServerListDefinition(BaseModel):
    AddrType: Optional[str]
    Fqdn: Optional[str]
    Id: Optional[float]
    ServerAddress: Optional[str]
    ServerAddress6: Optional[str]
    ServerType: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ServerListDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ServerListDefinition"]:
        if not json_data:
            return None
        return cls(
            AddrType=json_data.get("AddrType"),
            Fqdn=json_data.get("Fqdn"),
            Id=json_data.get("Id"),
            ServerAddress=json_data.get("ServerAddress"),
            ServerAddress6=json_data.get("ServerAddress6"),
            ServerType=json_data.get("ServerType"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ServerListDefinition = ServerListDefinition


