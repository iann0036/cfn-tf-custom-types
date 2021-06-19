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
    Http: Optional[bool]
    HttpOcsp: Optional[bool]
    Https: Optional[bool]
    Id: Optional[str]
    Name: Optional[str]
    PermittedIps: Optional[Sequence[str]]
    Ping: Optional[bool]
    ResponsePages: Optional[bool]
    Snmp: Optional[bool]
    Ssh: Optional[bool]
    Telnet: Optional[bool]
    UseridService: Optional[bool]
    UseridSyslogListenerSsl: Optional[bool]
    UseridSyslogListenerUdp: Optional[bool]

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
            Http=json_data.get("Http"),
            HttpOcsp=json_data.get("HttpOcsp"),
            Https=json_data.get("Https"),
            Id=json_data.get("Id"),
            Name=json_data.get("Name"),
            PermittedIps=json_data.get("PermittedIps"),
            Ping=json_data.get("Ping"),
            ResponsePages=json_data.get("ResponsePages"),
            Snmp=json_data.get("Snmp"),
            Ssh=json_data.get("Ssh"),
            Telnet=json_data.get("Telnet"),
            UseridService=json_data.get("UseridService"),
            UseridSyslogListenerSsl=json_data.get("UseridSyslogListenerSsl"),
            UseridSyslogListenerUdp=json_data.get("UseridSyslogListenerUdp"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


