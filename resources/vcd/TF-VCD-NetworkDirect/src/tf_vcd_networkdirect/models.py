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
    ExternalNetwork: Optional[str]
    ExternalNetworkDns1: Optional[str]
    ExternalNetworkDns2: Optional[str]
    ExternalNetworkDnsSuffix: Optional[str]
    ExternalNetworkGateway: Optional[str]
    ExternalNetworkNetmask: Optional[str]
    Href: Optional[str]
    Id: Optional[str]
    Name: Optional[str]
    Org: Optional[str]
    Shared: Optional[bool]
    Vdc: Optional[str]

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
            ExternalNetwork=json_data.get("ExternalNetwork"),
            ExternalNetworkDns1=json_data.get("ExternalNetworkDns1"),
            ExternalNetworkDns2=json_data.get("ExternalNetworkDns2"),
            ExternalNetworkDnsSuffix=json_data.get("ExternalNetworkDnsSuffix"),
            ExternalNetworkGateway=json_data.get("ExternalNetworkGateway"),
            ExternalNetworkNetmask=json_data.get("ExternalNetworkNetmask"),
            Href=json_data.get("Href"),
            Id=json_data.get("Id"),
            Name=json_data.get("Name"),
            Org=json_data.get("Org"),
            Shared=json_data.get("Shared"),
            Vdc=json_data.get("Vdc"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


