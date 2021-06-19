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
    DestinationPort: Optional[str]
    DeviceGroup: Optional[str]
    Id: Optional[str]
    Name: Optional[str]
    OverrideHalfClosedTimeout: Optional[float]
    OverrideSessionTimeout: Optional[bool]
    OverrideTimeWaitTimeout: Optional[float]
    OverrideTimeout: Optional[float]
    Protocol: Optional[str]
    SourcePort: Optional[str]
    Tags: Optional[Sequence[str]]

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
            DestinationPort=json_data.get("DestinationPort"),
            DeviceGroup=json_data.get("DeviceGroup"),
            Id=json_data.get("Id"),
            Name=json_data.get("Name"),
            OverrideHalfClosedTimeout=json_data.get("OverrideHalfClosedTimeout"),
            OverrideSessionTimeout=json_data.get("OverrideSessionTimeout"),
            OverrideTimeWaitTimeout=json_data.get("OverrideTimeWaitTimeout"),
            OverrideTimeout=json_data.get("OverrideTimeout"),
            Protocol=json_data.get("Protocol"),
            SourcePort=json_data.get("SourcePort"),
            Tags=json_data.get("Tags"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


