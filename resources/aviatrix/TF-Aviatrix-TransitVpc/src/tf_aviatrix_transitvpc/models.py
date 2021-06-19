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
    CloudType: Optional[float]
    ConnectedTransit: Optional[str]
    EnableFirenetInterfaces: Optional[bool]
    EnableHybridConnection: Optional[bool]
    EnableNat: Optional[str]
    GwName: Optional[str]
    HaGwSize: Optional[str]
    HaInsaneModeAz: Optional[str]
    HaSubnet: Optional[str]
    Id: Optional[str]
    InsaneMode: Optional[bool]
    InsaneModeAz: Optional[str]
    Subnet: Optional[str]
    TagList: Optional[Sequence[str]]
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
            CloudType=json_data.get("CloudType"),
            ConnectedTransit=json_data.get("ConnectedTransit"),
            EnableFirenetInterfaces=json_data.get("EnableFirenetInterfaces"),
            EnableHybridConnection=json_data.get("EnableHybridConnection"),
            EnableNat=json_data.get("EnableNat"),
            GwName=json_data.get("GwName"),
            HaGwSize=json_data.get("HaGwSize"),
            HaInsaneModeAz=json_data.get("HaInsaneModeAz"),
            HaSubnet=json_data.get("HaSubnet"),
            Id=json_data.get("Id"),
            InsaneMode=json_data.get("InsaneMode"),
            InsaneModeAz=json_data.get("InsaneModeAz"),
            Subnet=json_data.get("Subnet"),
            TagList=json_data.get("TagList"),
            VpcId=json_data.get("VpcId"),
            VpcReg=json_data.get("VpcReg"),
            VpcSize=json_data.get("VpcSize"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


