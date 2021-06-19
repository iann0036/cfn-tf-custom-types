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
    AwsAccountId: Optional[str]
    Email: Optional[str]
    IamArn: Optional[str]
    Id: Optional[str]
    IdentityType: Optional[str]
    Namespace: Optional[str]
    SessionName: Optional[str]
    UserName: Optional[str]
    UserRole: Optional[str]

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
            AwsAccountId=json_data.get("AwsAccountId"),
            Email=json_data.get("Email"),
            IamArn=json_data.get("IamArn"),
            Id=json_data.get("Id"),
            IdentityType=json_data.get("IdentityType"),
            Namespace=json_data.get("Namespace"),
            SessionName=json_data.get("SessionName"),
            UserName=json_data.get("UserName"),
            UserRole=json_data.get("UserRole"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


