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
    RtbList1: Optional[Sequence[str]]
    RtbList1Output: Optional[Sequence[str]]
    RtbList2: Optional[Sequence[str]]
    RtbList2Output: Optional[Sequence[str]]
    VpcId1: Optional[str]
    VpcId2: Optional[str]
    VpcReg1: Optional[str]
    VpcReg2: Optional[str]

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
            RtbList1=json_data.get("RtbList1"),
            RtbList1Output=json_data.get("RtbList1Output"),
            RtbList2=json_data.get("RtbList2"),
            RtbList2Output=json_data.get("RtbList2Output"),
            VpcId1=json_data.get("VpcId1"),
            VpcId2=json_data.get("VpcId2"),
            VpcReg1=json_data.get("VpcReg1"),
            VpcReg2=json_data.get("VpcReg2"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


