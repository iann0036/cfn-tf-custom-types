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
    CreatedTime: Optional[str]
    CustomOssBucket: Optional[str]
    EndTime: Optional[str]
    Id: Optional[str]
    InstanceName: Optional[str]
    InstanceType: Optional[str]
    PaymentType: Optional[str]
    Period: Optional[float]
    RenewPeriod: Optional[float]
    RenewalStatus: Optional[str]
    Status: Optional[str]

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
            CreatedTime=json_data.get("CreatedTime"),
            CustomOssBucket=json_data.get("CustomOssBucket"),
            EndTime=json_data.get("EndTime"),
            Id=json_data.get("Id"),
            InstanceName=json_data.get("InstanceName"),
            InstanceType=json_data.get("InstanceType"),
            PaymentType=json_data.get("PaymentType"),
            Period=json_data.get("Period"),
            RenewPeriod=json_data.get("RenewPeriod"),
            RenewalStatus=json_data.get("RenewalStatus"),
            Status=json_data.get("Status"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


