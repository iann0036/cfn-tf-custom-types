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
    BgpCommunities: Optional[Sequence[str]]
    BgpExtendedCommunities: Optional[Sequence[str]]
    Destinations: Optional[Sequence[str]]
    Id: Optional[str]
    Interfaces: Optional[Sequence[str]]
    Name: Optional[str]
    NextHops: Optional[Sequence[str]]
    OspfAreas: Optional[Sequence[str]]
    OspfPathTypes: Optional[Sequence[str]]
    OspfTags: Optional[Sequence[str]]
    Priority: Optional[float]
    Types: Optional[Sequence[str]]
    VirtualRouter: Optional[str]

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
            BgpCommunities=json_data.get("BgpCommunities"),
            BgpExtendedCommunities=json_data.get("BgpExtendedCommunities"),
            Destinations=json_data.get("Destinations"),
            Id=json_data.get("Id"),
            Interfaces=json_data.get("Interfaces"),
            Name=json_data.get("Name"),
            NextHops=json_data.get("NextHops"),
            OspfAreas=json_data.get("OspfAreas"),
            OspfPathTypes=json_data.get("OspfPathTypes"),
            OspfTags=json_data.get("OspfTags"),
            Priority=json_data.get("Priority"),
            Types=json_data.get("Types"),
            VirtualRouter=json_data.get("VirtualRouter"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


