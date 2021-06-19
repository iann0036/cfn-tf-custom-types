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
    AllocateBandwidth: Optional[float]
    ApplianceName: Optional[str]
    Burst: Optional[float]
    EnableRequests: Optional[float]
    Enterprise: Optional[str]
    Id: Optional[str]
    Interval: Optional[float]
    Port: Optional[float]
    Token: Optional[str]
    UseMgmtPort: Optional[float]
    Uuid: Optional[str]
    ProxyServer: Optional[Sequence["_ProxyServerDefinition"]]

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
            AllocateBandwidth=json_data.get("AllocateBandwidth"),
            ApplianceName=json_data.get("ApplianceName"),
            Burst=json_data.get("Burst"),
            EnableRequests=json_data.get("EnableRequests"),
            Enterprise=json_data.get("Enterprise"),
            Id=json_data.get("Id"),
            Interval=json_data.get("Interval"),
            Port=json_data.get("Port"),
            Token=json_data.get("Token"),
            UseMgmtPort=json_data.get("UseMgmtPort"),
            Uuid=json_data.get("Uuid"),
            ProxyServer=deserialize_list(json_data.get("ProxyServer"), ProxyServerDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class ProxyServerDefinition(BaseModel):
    Encrypted: Optional[str]
    Host: Optional[str]
    Password: Optional[float]
    Port: Optional[float]
    SecretString: Optional[str]
    Username: Optional[str]
    Uuid: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ProxyServerDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ProxyServerDefinition"]:
        if not json_data:
            return None
        return cls(
            Encrypted=json_data.get("Encrypted"),
            Host=json_data.get("Host"),
            Password=json_data.get("Password"),
            Port=json_data.get("Port"),
            SecretString=json_data.get("SecretString"),
            Username=json_data.get("Username"),
            Uuid=json_data.get("Uuid"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ProxyServerDefinition = ProxyServerDefinition


