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
    GroupPollInterval: Optional[float]
    Id: Optional[str]
    Interface: Optional[str]
    InterfaceSelectMethod: Optional[str]
    LdapPoll: Optional[str]
    LdapPollFilter: Optional[str]
    LdapPollInterval: Optional[float]
    LdapServer: Optional[str]
    Name: Optional[str]
    Password: Optional[str]
    Password2: Optional[str]
    Password3: Optional[str]
    Password4: Optional[str]
    Password5: Optional[str]
    Port: Optional[float]
    Port2: Optional[float]
    Port3: Optional[float]
    Port4: Optional[float]
    Port5: Optional[float]
    Server: Optional[str]
    Server2: Optional[str]
    Server3: Optional[str]
    Server4: Optional[str]
    Server5: Optional[str]
    SourceIp: Optional[str]
    SourceIp6: Optional[str]
    Ssl: Optional[str]
    SslTrustedCert: Optional[str]
    Type: Optional[str]
    UserInfoServer: Optional[str]
    Vdomparam: Optional[str]

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
            GroupPollInterval=json_data.get("GroupPollInterval"),
            Id=json_data.get("Id"),
            Interface=json_data.get("Interface"),
            InterfaceSelectMethod=json_data.get("InterfaceSelectMethod"),
            LdapPoll=json_data.get("LdapPoll"),
            LdapPollFilter=json_data.get("LdapPollFilter"),
            LdapPollInterval=json_data.get("LdapPollInterval"),
            LdapServer=json_data.get("LdapServer"),
            Name=json_data.get("Name"),
            Password=json_data.get("Password"),
            Password2=json_data.get("Password2"),
            Password3=json_data.get("Password3"),
            Password4=json_data.get("Password4"),
            Password5=json_data.get("Password5"),
            Port=json_data.get("Port"),
            Port2=json_data.get("Port2"),
            Port3=json_data.get("Port3"),
            Port4=json_data.get("Port4"),
            Port5=json_data.get("Port5"),
            Server=json_data.get("Server"),
            Server2=json_data.get("Server2"),
            Server3=json_data.get("Server3"),
            Server4=json_data.get("Server4"),
            Server5=json_data.get("Server5"),
            SourceIp=json_data.get("SourceIp"),
            SourceIp6=json_data.get("SourceIp6"),
            Ssl=json_data.get("Ssl"),
            SslTrustedCert=json_data.get("SslTrustedCert"),
            Type=json_data.get("Type"),
            UserInfoServer=json_data.get("UserInfoServer"),
            Vdomparam=json_data.get("Vdomparam"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


