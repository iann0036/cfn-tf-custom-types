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
    ClientId: Optional[str]
    CreationDate: Optional[str]
    Css: Optional[str]
    CssVersion: Optional[str]
    Id: Optional[str]
    ImageFile: Optional[str]
    ImageUrl: Optional[str]
    LastModifiedDate: Optional[str]
    UserPoolId: Optional[str]

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
            ClientId=json_data.get("ClientId"),
            CreationDate=json_data.get("CreationDate"),
            Css=json_data.get("Css"),
            CssVersion=json_data.get("CssVersion"),
            Id=json_data.get("Id"),
            ImageFile=json_data.get("ImageFile"),
            ImageUrl=json_data.get("ImageUrl"),
            LastModifiedDate=json_data.get("LastModifiedDate"),
            UserPoolId=json_data.get("UserPoolId"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


