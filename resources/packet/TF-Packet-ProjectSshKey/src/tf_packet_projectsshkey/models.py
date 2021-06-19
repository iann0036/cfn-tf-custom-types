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
    Created: Optional[str]
    Fingerprint: Optional[str]
    Id: Optional[str]
    Name: Optional[str]
    OwnerId: Optional[str]
    ProjectId: Optional[str]
    PublicKey: Optional[str]
    Updated: Optional[str]

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
            Created=json_data.get("Created"),
            Fingerprint=json_data.get("Fingerprint"),
            Id=json_data.get("Id"),
            Name=json_data.get("Name"),
            OwnerId=json_data.get("OwnerId"),
            ProjectId=json_data.get("ProjectId"),
            PublicKey=json_data.get("PublicKey"),
            Updated=json_data.get("Updated"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


