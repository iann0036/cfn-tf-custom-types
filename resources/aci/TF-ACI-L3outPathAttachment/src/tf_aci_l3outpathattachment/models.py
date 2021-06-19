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
    Addr: Optional[str]
    Annotation: Optional[str]
    Autostate: Optional[str]
    Description: Optional[str]
    Encap: Optional[str]
    EncapScope: Optional[str]
    Id: Optional[str]
    IfInstT: Optional[str]
    Ipv6Dad: Optional[str]
    LlAddr: Optional[str]
    LogicalInterfaceProfileDn: Optional[str]
    Mac: Optional[str]
    Mode: Optional[str]
    Mtu: Optional[str]
    TargetDn: Optional[str]
    TargetDscp: Optional[str]

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
            Addr=json_data.get("Addr"),
            Annotation=json_data.get("Annotation"),
            Autostate=json_data.get("Autostate"),
            Description=json_data.get("Description"),
            Encap=json_data.get("Encap"),
            EncapScope=json_data.get("EncapScope"),
            Id=json_data.get("Id"),
            IfInstT=json_data.get("IfInstT"),
            Ipv6Dad=json_data.get("Ipv6Dad"),
            LlAddr=json_data.get("LlAddr"),
            LogicalInterfaceProfileDn=json_data.get("LogicalInterfaceProfileDn"),
            Mac=json_data.get("Mac"),
            Mode=json_data.get("Mode"),
            Mtu=json_data.get("Mtu"),
            TargetDn=json_data.get("TargetDn"),
            TargetDscp=json_data.get("TargetDscp"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


