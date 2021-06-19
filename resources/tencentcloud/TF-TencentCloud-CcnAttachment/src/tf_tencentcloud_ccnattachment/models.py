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
    AttachedTime: Optional[str]
    CcnId: Optional[str]
    CcnUin: Optional[str]
    CidrBlock: Optional[Sequence[str]]
    Id: Optional[str]
    InstanceId: Optional[str]
    InstanceRegion: Optional[str]
    InstanceType: Optional[str]
    State: Optional[str]

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
            AttachedTime=json_data.get("AttachedTime"),
            CcnId=json_data.get("CcnId"),
            CcnUin=json_data.get("CcnUin"),
            CidrBlock=json_data.get("CidrBlock"),
            Id=json_data.get("Id"),
            InstanceId=json_data.get("InstanceId"),
            InstanceRegion=json_data.get("InstanceRegion"),
            InstanceType=json_data.get("InstanceType"),
            State=json_data.get("State"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


