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
    Aggregate: Optional[str]
    Annotation: Optional[str]
    Description: Optional[str]
    FabricNodeDn: Optional[str]
    Id: Optional[str]
    Ip: Optional[str]
    NameAlias: Optional[str]
    Pref: Optional[str]
    RelationIpRsRouteTrack: Optional[str]
    RtCtrl: Optional[str]

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
            Aggregate=json_data.get("Aggregate"),
            Annotation=json_data.get("Annotation"),
            Description=json_data.get("Description"),
            FabricNodeDn=json_data.get("FabricNodeDn"),
            Id=json_data.get("Id"),
            Ip=json_data.get("Ip"),
            NameAlias=json_data.get("NameAlias"),
            Pref=json_data.get("Pref"),
            RelationIpRsRouteTrack=json_data.get("RelationIpRsRouteTrack"),
            RtCtrl=json_data.get("RtCtrl"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


