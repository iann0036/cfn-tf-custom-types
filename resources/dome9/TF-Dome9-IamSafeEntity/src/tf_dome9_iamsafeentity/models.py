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
    Arn: Optional[str]
    AttachedDome9Users: Optional[Sequence[str]]
    AwsCloudAccountId: Optional[str]
    Dome9UsersIdToProtect: Optional[Sequence[str]]
    EntityName: Optional[str]
    EntityType: Optional[str]
    ExistsInAws: Optional[bool]
    Id: Optional[str]
    ProtectionMode: Optional[str]
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
            Arn=json_data.get("Arn"),
            AttachedDome9Users=json_data.get("AttachedDome9Users"),
            AwsCloudAccountId=json_data.get("AwsCloudAccountId"),
            Dome9UsersIdToProtect=json_data.get("Dome9UsersIdToProtect"),
            EntityName=json_data.get("EntityName"),
            EntityType=json_data.get("EntityType"),
            ExistsInAws=json_data.get("ExistsInAws"),
            Id=json_data.get("Id"),
            ProtectionMode=json_data.get("ProtectionMode"),
            State=json_data.get("State"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


