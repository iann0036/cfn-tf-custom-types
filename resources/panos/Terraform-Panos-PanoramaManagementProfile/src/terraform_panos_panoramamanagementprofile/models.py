# DO NOT modify this file by hand, changes will be overwritten
from dataclasses import dataclass
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
    BaseResourceHandlerRequest,
    BaseResourceModel,
)

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
class ResourceModel(BaseResourceModel):
    tfcfnid: Optional[str]
    Http: Optional[bool]
    HttpOcsp: Optional[bool]
    Https: Optional[bool]
    Name: Optional[str]
    PermittedIps: Optional[Sequence[str]]
    Ping: Optional[bool]
    ResponsePages: Optional[bool]
    Snmp: Optional[bool]
    Ssh: Optional[bool]
    Telnet: Optional[bool]
    Template: Optional[str]
    TemplateStack: Optional[str]
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
        return cls(
            tfcfnid=json_data.get("tfcfnid"),
            Http=json_data.get("Http"),
            HttpOcsp=json_data.get("HttpOcsp"),
            Https=json_data.get("Https"),
            Name=json_data.get("Name"),
            PermittedIps=json_data.get("PermittedIps"),
            Ping=json_data.get("Ping"),
            ResponsePages=json_data.get("ResponsePages"),
            Snmp=json_data.get("Snmp"),
            Ssh=json_data.get("Ssh"),
            Telnet=json_data.get("Telnet"),
            Template=json_data.get("Template"),
            TemplateStack=json_data.get("TemplateStack"),
            UseridService=json_data.get("UseridService"),
            UseridSyslogListenerSsl=json_data.get("UseridSyslogListenerSsl"),
            UseridSyslogListenerUdp=json_data.get("UseridSyslogListenerUdp"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


