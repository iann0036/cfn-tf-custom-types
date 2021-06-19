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
    Acl: Optional[str]
    Description: Optional[str]
    DstIpAddressPrefixes: Optional[Sequence[str]]
    DstVnicSet: Optional[str]
    Enabled: Optional[bool]
    FlowDirection: Optional[str]
    Id: Optional[str]
    Name: Optional[str]
    SecurityProtocols: Optional[Sequence[str]]
    SrcIpAddressPrefixes: Optional[Sequence[str]]
    SrcVnicSet: Optional[str]
    Tags: Optional[Sequence[str]]
    Uri: Optional[str]

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
            Acl=json_data.get("Acl"),
            Description=json_data.get("Description"),
            DstIpAddressPrefixes=json_data.get("DstIpAddressPrefixes"),
            DstVnicSet=json_data.get("DstVnicSet"),
            Enabled=json_data.get("Enabled"),
            FlowDirection=json_data.get("FlowDirection"),
            Id=json_data.get("Id"),
            Name=json_data.get("Name"),
            SecurityProtocols=json_data.get("SecurityProtocols"),
            SrcIpAddressPrefixes=json_data.get("SrcIpAddressPrefixes"),
            SrcVnicSet=json_data.get("SrcVnicSet"),
            Tags=json_data.get("Tags"),
            Uri=json_data.get("Uri"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


