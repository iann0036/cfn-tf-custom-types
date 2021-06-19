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
    Backend: Optional[str]
    CredentialType: Optional[str]
    DefaultStsTtl: Optional[float]
    IamGroups: Optional[Sequence[str]]
    Id: Optional[str]
    MaxStsTtl: Optional[float]
    Name: Optional[str]
    Policy: Optional[str]
    PolicyArn: Optional[str]
    PolicyArns: Optional[Sequence[str]]
    PolicyDocument: Optional[str]
    RoleArns: Optional[Sequence[str]]

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
            Backend=json_data.get("Backend"),
            CredentialType=json_data.get("CredentialType"),
            DefaultStsTtl=json_data.get("DefaultStsTtl"),
            IamGroups=json_data.get("IamGroups"),
            Id=json_data.get("Id"),
            MaxStsTtl=json_data.get("MaxStsTtl"),
            Name=json_data.get("Name"),
            Policy=json_data.get("Policy"),
            PolicyArn=json_data.get("PolicyArn"),
            PolicyArns=json_data.get("PolicyArns"),
            PolicyDocument=json_data.get("PolicyDocument"),
            RoleArns=json_data.get("RoleArns"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


