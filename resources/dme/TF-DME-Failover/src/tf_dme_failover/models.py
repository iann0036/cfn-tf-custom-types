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
    AutoFailover: Optional[str]
    ContactList: Optional[str]
    DnsFqdn: Optional[str]
    DnsTimeout: Optional[str]
    Failover: Optional[str]
    HttpFile: Optional[str]
    HttpFqdn: Optional[str]
    HttpQueryString: Optional[str]
    Id: Optional[str]
    Ip1: Optional[str]
    Ip2: Optional[str]
    Ip3: Optional[str]
    Ip4: Optional[str]
    Ip5: Optional[str]
    MaxEmails: Optional[str]
    Monitor: Optional[str]
    Port: Optional[str]
    ProtocolId: Optional[str]
    RecordId: Optional[str]
    SendString: Optional[str]
    Sensitivity: Optional[str]
    SystemDescription: Optional[str]
    Timeout: Optional[str]

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
            AutoFailover=json_data.get("AutoFailover"),
            ContactList=json_data.get("ContactList"),
            DnsFqdn=json_data.get("DnsFqdn"),
            DnsTimeout=json_data.get("DnsTimeout"),
            Failover=json_data.get("Failover"),
            HttpFile=json_data.get("HttpFile"),
            HttpFqdn=json_data.get("HttpFqdn"),
            HttpQueryString=json_data.get("HttpQueryString"),
            Id=json_data.get("Id"),
            Ip1=json_data.get("Ip1"),
            Ip2=json_data.get("Ip2"),
            Ip3=json_data.get("Ip3"),
            Ip4=json_data.get("Ip4"),
            Ip5=json_data.get("Ip5"),
            MaxEmails=json_data.get("MaxEmails"),
            Monitor=json_data.get("Monitor"),
            Port=json_data.get("Port"),
            ProtocolId=json_data.get("ProtocolId"),
            RecordId=json_data.get("RecordId"),
            SendString=json_data.get("SendString"),
            Sensitivity=json_data.get("Sensitivity"),
            SystemDescription=json_data.get("SystemDescription"),
            Timeout=json_data.get("Timeout"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


