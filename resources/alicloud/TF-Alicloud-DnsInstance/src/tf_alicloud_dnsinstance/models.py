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
    DnsSecurity: Optional[str]
    DomainNumbers: Optional[str]
    Id: Optional[str]
    PaymentType: Optional[str]
    Period: Optional[float]
    RenewPeriod: Optional[float]
    RenewalStatus: Optional[str]
    VersionCode: Optional[str]
    VersionName: Optional[str]

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
            DnsSecurity=json_data.get("DnsSecurity"),
            DomainNumbers=json_data.get("DomainNumbers"),
            Id=json_data.get("Id"),
            PaymentType=json_data.get("PaymentType"),
            Period=json_data.get("Period"),
            RenewPeriod=json_data.get("RenewPeriod"),
            RenewalStatus=json_data.get("RenewalStatus"),
            VersionCode=json_data.get("VersionCode"),
            VersionName=json_data.get("VersionName"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


