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
    AppId: Optional[str]
    Id: Optional[str]
    Index: Optional[str]
    Master: Optional[str]
    Pattern: Optional[str]
    Permissions: Optional[str]
    Required: Optional[bool]
    Title: Optional[str]
    Type: Optional[str]
    UserType: Optional[str]

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
            AppId=json_data.get("AppId"),
            Id=json_data.get("Id"),
            Index=json_data.get("Index"),
            Master=json_data.get("Master"),
            Pattern=json_data.get("Pattern"),
            Permissions=json_data.get("Permissions"),
            Required=json_data.get("Required"),
            Title=json_data.get("Title"),
            Type=json_data.get("Type"),
            UserType=json_data.get("UserType"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel

