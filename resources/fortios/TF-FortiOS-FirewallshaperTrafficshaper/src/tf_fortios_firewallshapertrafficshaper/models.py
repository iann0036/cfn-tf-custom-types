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
    Diffserv: Optional[str]
    Diffservcode: Optional[str]
    DscpMarkingMethod: Optional[str]
    ExceedBandwidth: Optional[float]
    ExceedClassId: Optional[float]
    ExceedDscp: Optional[str]
    GuaranteedBandwidth: Optional[float]
    Id: Optional[str]
    MaximumBandwidth: Optional[float]
    MaximumDscp: Optional[str]
    Name: Optional[str]
    Overhead: Optional[float]
    PerPolicy: Optional[str]
    Priority: Optional[str]
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
            Diffserv=json_data.get("Diffserv"),
            Diffservcode=json_data.get("Diffservcode"),
            DscpMarkingMethod=json_data.get("DscpMarkingMethod"),
            ExceedBandwidth=json_data.get("ExceedBandwidth"),
            ExceedClassId=json_data.get("ExceedClassId"),
            ExceedDscp=json_data.get("ExceedDscp"),
            GuaranteedBandwidth=json_data.get("GuaranteedBandwidth"),
            Id=json_data.get("Id"),
            MaximumBandwidth=json_data.get("MaximumBandwidth"),
            MaximumDscp=json_data.get("MaximumDscp"),
            Name=json_data.get("Name"),
            Overhead=json_data.get("Overhead"),
            PerPolicy=json_data.get("PerPolicy"),
            Priority=json_data.get("Priority"),
            Vdomparam=json_data.get("Vdomparam"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


