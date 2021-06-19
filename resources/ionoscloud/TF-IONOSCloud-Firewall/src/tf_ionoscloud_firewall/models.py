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
    DatacenterId: Optional[str]
    IcmpCode: Optional[str]
    IcmpType: Optional[str]
    Id: Optional[str]
    Name: Optional[str]
    NicId: Optional[str]
    PortRangeEnd: Optional[float]
    PortRangeStart: Optional[float]
    Protocol: Optional[str]
    ServerId: Optional[str]
    SourceIp: Optional[str]
    SourceMac: Optional[str]
    TargetIp: Optional[str]
    Timeouts: Optional["_TimeoutsDefinition"]

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
            DatacenterId=json_data.get("DatacenterId"),
            IcmpCode=json_data.get("IcmpCode"),
            IcmpType=json_data.get("IcmpType"),
            Id=json_data.get("Id"),
            Name=json_data.get("Name"),
            NicId=json_data.get("NicId"),
            PortRangeEnd=json_data.get("PortRangeEnd"),
            PortRangeStart=json_data.get("PortRangeStart"),
            Protocol=json_data.get("Protocol"),
            ServerId=json_data.get("ServerId"),
            SourceIp=json_data.get("SourceIp"),
            SourceMac=json_data.get("SourceMac"),
            TargetIp=json_data.get("TargetIp"),
            Timeouts=TimeoutsDefinition._deserialize(json_data.get("Timeouts")),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class TimeoutsDefinition(BaseModel):
    Create: Optional[str]
    Default: Optional[str]
    Delete: Optional[str]
    Update: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_TimeoutsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TimeoutsDefinition"]:
        if not json_data:
            return None
        return cls(
            Create=json_data.get("Create"),
            Default=json_data.get("Default"),
            Delete=json_data.get("Delete"),
            Update=json_data.get("Update"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TimeoutsDefinition = TimeoutsDefinition


