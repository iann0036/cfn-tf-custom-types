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
    AccountName: Optional[str]
    CloudInstanceId: Optional[str]
    CloudType: Optional[float]
    EnableNat: Optional[str]
    GwName: Optional[str]
    HaGwSize: Optional[str]
    HaSubnet: Optional[str]
    HaZone: Optional[str]
    Id: Optional[str]
    SingleAzHa: Optional[str]
    Subnet: Optional[str]
    TagList: Optional[Sequence[str]]
    TransitGw: Optional[str]
    VpcId: Optional[str]
    VpcReg: Optional[str]
    VpcSize: Optional[str]

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
            AccountName=json_data.get("AccountName"),
            CloudInstanceId=json_data.get("CloudInstanceId"),
            CloudType=json_data.get("CloudType"),
            EnableNat=json_data.get("EnableNat"),
            GwName=json_data.get("GwName"),
            HaGwSize=json_data.get("HaGwSize"),
            HaSubnet=json_data.get("HaSubnet"),
            HaZone=json_data.get("HaZone"),
            Id=json_data.get("Id"),
            SingleAzHa=json_data.get("SingleAzHa"),
            Subnet=json_data.get("Subnet"),
            TagList=json_data.get("TagList"),
            TransitGw=json_data.get("TransitGw"),
            VpcId=json_data.get("VpcId"),
            VpcReg=json_data.get("VpcReg"),
            VpcSize=json_data.get("VpcSize"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


