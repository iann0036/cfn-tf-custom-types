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
    Color: Optional[str]
    Comments: Optional[str]
    Domains: Optional[Sequence[str]]
    GlobalDomains: Optional[Sequence[str]]
    Hardware: Optional[str]
    Id: Optional[str]
    IgnoreErrors: Optional[bool]
    IgnoreWarnings: Optional[bool]
    IpPoolFirst: Optional[str]
    IpPoolLast: Optional[str]
    Ipv4Address: Optional[str]
    Ipv6Address: Optional[str]
    Name: Optional[str]
    OneTimePassword: Optional[str]
    Os: Optional[str]
    ServerType: Optional[str]
    SicName: Optional[str]
    SicState: Optional[str]
    Tags: Optional[Sequence[str]]
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
            Color=json_data.get("Color"),
            Comments=json_data.get("Comments"),
            Domains=json_data.get("Domains"),
            GlobalDomains=json_data.get("GlobalDomains"),
            Hardware=json_data.get("Hardware"),
            Id=json_data.get("Id"),
            IgnoreErrors=json_data.get("IgnoreErrors"),
            IgnoreWarnings=json_data.get("IgnoreWarnings"),
            IpPoolFirst=json_data.get("IpPoolFirst"),
            IpPoolLast=json_data.get("IpPoolLast"),
            Ipv4Address=json_data.get("Ipv4Address"),
            Ipv6Address=json_data.get("Ipv6Address"),
            Name=json_data.get("Name"),
            OneTimePassword=json_data.get("OneTimePassword"),
            Os=json_data.get("Os"),
            ServerType=json_data.get("ServerType"),
            SicName=json_data.get("SicName"),
            SicState=json_data.get("SicState"),
            Tags=json_data.get("Tags"),
            Version=json_data.get("Version"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


