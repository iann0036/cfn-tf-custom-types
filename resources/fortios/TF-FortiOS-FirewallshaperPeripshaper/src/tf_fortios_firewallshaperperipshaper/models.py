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
    BandwidthUnit: Optional[str]
    DiffservForward: Optional[str]
    DiffservReverse: Optional[str]
    DiffservcodeForward: Optional[str]
    DiffservcodeRev: Optional[str]
    Id: Optional[str]
    MaxBandwidth: Optional[float]
    MaxConcurrentSession: Optional[float]
    MaxConcurrentTcpSession: Optional[float]
    MaxConcurrentUdpSession: Optional[float]
    Name: Optional[str]
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
            BandwidthUnit=json_data.get("BandwidthUnit"),
            DiffservForward=json_data.get("DiffservForward"),
            DiffservReverse=json_data.get("DiffservReverse"),
            DiffservcodeForward=json_data.get("DiffservcodeForward"),
            DiffservcodeRev=json_data.get("DiffservcodeRev"),
            Id=json_data.get("Id"),
            MaxBandwidth=json_data.get("MaxBandwidth"),
            MaxConcurrentSession=json_data.get("MaxConcurrentSession"),
            MaxConcurrentTcpSession=json_data.get("MaxConcurrentTcpSession"),
            MaxConcurrentUdpSession=json_data.get("MaxConcurrentUdpSession"),
            Name=json_data.get("Name"),
            Vdomparam=json_data.get("Vdomparam"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


