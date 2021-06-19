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
    Behavior: Optional[str]
    Category: Optional[float]
    Comment: Optional[str]
    Fosid: Optional[float]
    Id: Optional[str]
    Name: Optional[str]
    Protocol: Optional[str]
    Signature: Optional[str]
    Tag: Optional[str]
    Technology: Optional[str]
    Vdomparam: Optional[str]
    Vendor: Optional[str]

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
            Behavior=json_data.get("Behavior"),
            Category=json_data.get("Category"),
            Comment=json_data.get("Comment"),
            Fosid=json_data.get("Fosid"),
            Id=json_data.get("Id"),
            Name=json_data.get("Name"),
            Protocol=json_data.get("Protocol"),
            Signature=json_data.get("Signature"),
            Tag=json_data.get("Tag"),
            Technology=json_data.get("Technology"),
            Vdomparam=json_data.get("Vdomparam"),
            Vendor=json_data.get("Vendor"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


