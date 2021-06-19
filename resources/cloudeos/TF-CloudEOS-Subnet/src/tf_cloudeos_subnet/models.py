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
    AvailabilityZone: Optional[str]
    CidrBlock: Optional[str]
    CloudProvider: Optional[str]
    ComputedSubnetId: Optional[str]
    Id: Optional[str]
    SubnetId: Optional[str]
    SubnetName: Optional[str]
    TfId: Optional[str]
    VnetName: Optional[str]
    VpcId: Optional[str]

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
            AvailabilityZone=json_data.get("AvailabilityZone"),
            CidrBlock=json_data.get("CidrBlock"),
            CloudProvider=json_data.get("CloudProvider"),
            ComputedSubnetId=json_data.get("ComputedSubnetId"),
            Id=json_data.get("Id"),
            SubnetId=json_data.get("SubnetId"),
            SubnetName=json_data.get("SubnetName"),
            TfId=json_data.get("TfId"),
            VnetName=json_data.get("VnetName"),
            VpcId=json_data.get("VpcId"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


