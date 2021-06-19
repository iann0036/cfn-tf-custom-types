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
    AuthKey: Optional[str]
    AuthProto: Optional[str]
    Community: Optional[str]
    ContextEngineId: Optional[str]
    ContextName: Optional[str]
    Host: Optional[str]
    Id: Optional[str]
    Interface: Optional[float]
    Interval: Optional[float]
    Oid: Optional[str]
    Port: Optional[float]
    PrivKey: Optional[str]
    PrivProto: Optional[str]
    SecurityEngineId: Optional[str]
    SecurityLevel: Optional[str]
    SnmpName: Optional[str]
    UserTag: Optional[str]
    Username: Optional[str]
    Uuid: Optional[str]
    Version: Optional[str]

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
            AuthKey=json_data.get("AuthKey"),
            AuthProto=json_data.get("AuthProto"),
            Community=json_data.get("Community"),
            ContextEngineId=json_data.get("ContextEngineId"),
            ContextName=json_data.get("ContextName"),
            Host=json_data.get("Host"),
            Id=json_data.get("Id"),
            Interface=json_data.get("Interface"),
            Interval=json_data.get("Interval"),
            Oid=json_data.get("Oid"),
            Port=json_data.get("Port"),
            PrivKey=json_data.get("PrivKey"),
            PrivProto=json_data.get("PrivProto"),
            SecurityEngineId=json_data.get("SecurityEngineId"),
            SecurityLevel=json_data.get("SecurityLevel"),
            SnmpName=json_data.get("SnmpName"),
            UserTag=json_data.get("UserTag"),
            Username=json_data.get("Username"),
            Uuid=json_data.get("Uuid"),
            Version=json_data.get("Version"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


