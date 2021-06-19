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
    ArpIntf: Optional[str]
    ArpReply: Optional[str]
    AssociatedInterface: Optional[str]
    BlockSize: Optional[float]
    Comments: Optional[str]
    Endip: Optional[str]
    Endport: Optional[float]
    Id: Optional[str]
    Name: Optional[str]
    NumBlocksPerUser: Optional[float]
    PbaTimeout: Optional[float]
    PermitAnyHost: Optional[str]
    PortPerUser: Optional[float]
    SourceEndip: Optional[str]
    SourceStartip: Optional[str]
    Startip: Optional[str]
    Startport: Optional[float]
    Type: Optional[str]
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
            ArpIntf=json_data.get("ArpIntf"),
            ArpReply=json_data.get("ArpReply"),
            AssociatedInterface=json_data.get("AssociatedInterface"),
            BlockSize=json_data.get("BlockSize"),
            Comments=json_data.get("Comments"),
            Endip=json_data.get("Endip"),
            Endport=json_data.get("Endport"),
            Id=json_data.get("Id"),
            Name=json_data.get("Name"),
            NumBlocksPerUser=json_data.get("NumBlocksPerUser"),
            PbaTimeout=json_data.get("PbaTimeout"),
            PermitAnyHost=json_data.get("PermitAnyHost"),
            PortPerUser=json_data.get("PortPerUser"),
            SourceEndip=json_data.get("SourceEndip"),
            SourceStartip=json_data.get("SourceStartip"),
            Startip=json_data.get("Startip"),
            Startport=json_data.get("Startport"),
            Type=json_data.get("Type"),
            Vdomparam=json_data.get("Vdomparam"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


