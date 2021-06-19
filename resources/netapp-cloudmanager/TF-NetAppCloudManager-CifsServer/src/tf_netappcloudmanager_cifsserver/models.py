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
    ClientId: Optional[str]
    DnsDomain: Optional[str]
    Domain: Optional[str]
    Id: Optional[str]
    IpAddresses: Optional[Sequence[str]]
    IsWorkgroup: Optional[bool]
    Netbios: Optional[str]
    OrganizationalUnit: Optional[str]
    Password: Optional[str]
    ServerName: Optional[str]
    SvmName: Optional[str]
    Username: Optional[str]
    WorkgroupName: Optional[str]
    WorkingEnvironmentId: Optional[str]
    WorkingEnvironmentName: Optional[str]

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
            ClientId=json_data.get("ClientId"),
            DnsDomain=json_data.get("DnsDomain"),
            Domain=json_data.get("Domain"),
            Id=json_data.get("Id"),
            IpAddresses=json_data.get("IpAddresses"),
            IsWorkgroup=json_data.get("IsWorkgroup"),
            Netbios=json_data.get("Netbios"),
            OrganizationalUnit=json_data.get("OrganizationalUnit"),
            Password=json_data.get("Password"),
            ServerName=json_data.get("ServerName"),
            SvmName=json_data.get("SvmName"),
            Username=json_data.get("Username"),
            WorkgroupName=json_data.get("WorkgroupName"),
            WorkingEnvironmentId=json_data.get("WorkingEnvironmentId"),
            WorkingEnvironmentName=json_data.get("WorkingEnvironmentName"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


