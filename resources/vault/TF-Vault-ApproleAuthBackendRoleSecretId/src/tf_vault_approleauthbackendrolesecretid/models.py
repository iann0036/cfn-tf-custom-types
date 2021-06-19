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
    Accessor: Optional[str]
    Backend: Optional[str]
    CidrList: Optional[Sequence[str]]
    Id: Optional[str]
    Metadata: Optional[str]
    RoleName: Optional[str]
    SecretId: Optional[str]
    WrappingAccessor: Optional[str]
    WrappingToken: Optional[str]
    WrappingTtl: Optional[str]

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
            Accessor=json_data.get("Accessor"),
            Backend=json_data.get("Backend"),
            CidrList=json_data.get("CidrList"),
            Id=json_data.get("Id"),
            Metadata=json_data.get("Metadata"),
            RoleName=json_data.get("RoleName"),
            SecretId=json_data.get("SecretId"),
            WrappingAccessor=json_data.get("WrappingAccessor"),
            WrappingToken=json_data.get("WrappingToken"),
            WrappingTtl=json_data.get("WrappingTtl"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


