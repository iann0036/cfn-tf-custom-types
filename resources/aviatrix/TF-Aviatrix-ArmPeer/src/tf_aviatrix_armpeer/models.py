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
    AccountName1: Optional[str]
    AccountName2: Optional[str]
    Id: Optional[str]
    VnetCidr1: Optional[Sequence[str]]
    VnetCidr2: Optional[Sequence[str]]
    VnetNameResourceGroup1: Optional[str]
    VnetNameResourceGroup2: Optional[str]
    VnetReg1: Optional[str]
    VnetReg2: Optional[str]

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
            AccountName1=json_data.get("AccountName1"),
            AccountName2=json_data.get("AccountName2"),
            Id=json_data.get("Id"),
            VnetCidr1=json_data.get("VnetCidr1"),
            VnetCidr2=json_data.get("VnetCidr2"),
            VnetNameResourceGroup1=json_data.get("VnetNameResourceGroup1"),
            VnetNameResourceGroup2=json_data.get("VnetNameResourceGroup2"),
            VnetReg1=json_data.get("VnetReg1"),
            VnetReg2=json_data.get("VnetReg2"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


