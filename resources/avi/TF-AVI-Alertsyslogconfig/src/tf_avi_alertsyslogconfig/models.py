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
    Description: Optional[str]
    Id: Optional[str]
    Name: Optional[str]
    TenantRef: Optional[str]
    Uuid: Optional[str]
    SyslogServers: Optional[Sequence["_SyslogServersDefinition"]]

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
            Description=json_data.get("Description"),
            Id=json_data.get("Id"),
            Name=json_data.get("Name"),
            TenantRef=json_data.get("TenantRef"),
            Uuid=json_data.get("Uuid"),
            SyslogServers=deserialize_list(json_data.get("SyslogServers"), SyslogServersDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class SyslogServersDefinition(BaseModel):
    AnonAuth: Optional[bool]
    Format: Optional[str]
    PkiprofileRef: Optional[str]
    SslKeyAndCertificateRef: Optional[str]
    SyslogServer: Optional[str]
    SyslogServerPort: Optional[float]
    TlsEnable: Optional[bool]
    Udp: Optional[bool]

    @classmethod
    def _deserialize(
        cls: Type["_SyslogServersDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SyslogServersDefinition"]:
        if not json_data:
            return None
        return cls(
            AnonAuth=json_data.get("AnonAuth"),
            Format=json_data.get("Format"),
            PkiprofileRef=json_data.get("PkiprofileRef"),
            SslKeyAndCertificateRef=json_data.get("SslKeyAndCertificateRef"),
            SyslogServer=json_data.get("SyslogServer"),
            SyslogServerPort=json_data.get("SyslogServerPort"),
            TlsEnable=json_data.get("TlsEnable"),
            Udp=json_data.get("Udp"),
        )


# work around possible type aliasing issues when variable has same name as a model
_SyslogServersDefinition = SyslogServersDefinition


