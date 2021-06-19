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
    Comments: Optional[str]
    FollowUp: Optional[bool]
    Id: Optional[str]
    Name: Optional[str]
    Overrides: Optional[Sequence["_OverridesDefinition"]]

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
            Comments=json_data.get("Comments"),
            FollowUp=json_data.get("FollowUp"),
            Id=json_data.get("Id"),
            Name=json_data.get("Name"),
            Overrides=deserialize_list(json_data.get("Overrides"), OverridesDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class OverridesDefinition(BaseModel):
    Action: Optional[str]
    CapturePackets: Optional[bool]
    Profile: Optional[str]
    Track: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_OverridesDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_OverridesDefinition"]:
        if not json_data:
            return None
        return cls(
            Action=json_data.get("Action"),
            CapturePackets=json_data.get("CapturePackets"),
            Profile=json_data.get("Profile"),
            Track=json_data.get("Track"),
        )


# work around possible type aliasing issues when variable has same name as a model
_OverridesDefinition = OverridesDefinition


