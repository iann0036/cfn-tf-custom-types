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
    Domain: Optional[str]
    DomainOwner: Optional[str]
    Id: Optional[str]
    PolicyDocument: Optional[str]
    PolicyRevision: Optional[str]
    Repository: Optional[str]
    ResourceArn: Optional[str]

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
            Domain=json_data.get("Domain"),
            DomainOwner=json_data.get("DomainOwner"),
            Id=json_data.get("Id"),
            PolicyDocument=json_data.get("PolicyDocument"),
            PolicyRevision=json_data.get("PolicyRevision"),
            Repository=json_data.get("Repository"),
            ResourceArn=json_data.get("ResourceArn"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


