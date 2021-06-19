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
    Action: Optional[str]
    AutoAsicOffload: Optional[str]
    Comments: Optional[str]
    Dnat: Optional[str]
    Dstintf: Optional[str]
    DynamicSortSubtable: Optional[str]
    EndPort: Optional[float]
    Fosid: Optional[float]
    Id: Optional[str]
    Logtraffic: Optional[str]
    Name: Optional[str]
    Protocol: Optional[float]
    Snat: Optional[str]
    SnatIp: Optional[str]
    Srcintf: Optional[str]
    StartPort: Optional[float]
    Status: Optional[str]
    Uuid: Optional[str]
    Vdomparam: Optional[str]
    Dstaddr: Optional[Sequence["_DstaddrDefinition"]]
    Srcaddr: Optional[Sequence["_SrcaddrDefinition"]]

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
            Action=json_data.get("Action"),
            AutoAsicOffload=json_data.get("AutoAsicOffload"),
            Comments=json_data.get("Comments"),
            Dnat=json_data.get("Dnat"),
            Dstintf=json_data.get("Dstintf"),
            DynamicSortSubtable=json_data.get("DynamicSortSubtable"),
            EndPort=json_data.get("EndPort"),
            Fosid=json_data.get("Fosid"),
            Id=json_data.get("Id"),
            Logtraffic=json_data.get("Logtraffic"),
            Name=json_data.get("Name"),
            Protocol=json_data.get("Protocol"),
            Snat=json_data.get("Snat"),
            SnatIp=json_data.get("SnatIp"),
            Srcintf=json_data.get("Srcintf"),
            StartPort=json_data.get("StartPort"),
            Status=json_data.get("Status"),
            Uuid=json_data.get("Uuid"),
            Vdomparam=json_data.get("Vdomparam"),
            Dstaddr=deserialize_list(json_data.get("Dstaddr"), DstaddrDefinition),
            Srcaddr=deserialize_list(json_data.get("Srcaddr"), SrcaddrDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class DstaddrDefinition(BaseModel):
    Name: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_DstaddrDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DstaddrDefinition"]:
        if not json_data:
            return None
        return cls(
            Name=json_data.get("Name"),
        )


# work around possible type aliasing issues when variable has same name as a model
_DstaddrDefinition = DstaddrDefinition


@dataclass
class SrcaddrDefinition(BaseModel):
    Name: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_SrcaddrDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SrcaddrDefinition"]:
        if not json_data:
            return None
        return cls(
            Name=json_data.get("Name"),
        )


# work around possible type aliasing issues when variable has same name as a model
_SrcaddrDefinition = SrcaddrDefinition


