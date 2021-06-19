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
    BindSecretId: Optional[bool]
    BoundCidrList: Optional[Sequence[str]]
    Id: Optional[str]
    Period: Optional[float]
    Policies: Optional[Sequence[str]]
    RoleId: Optional[str]
    RoleName: Optional[str]
    SecretIdBoundCidrs: Optional[Sequence[str]]
    SecretIdNumUses: Optional[float]
    SecretIdTtl: Optional[float]
    TokenBoundCidrs: Optional[Sequence[str]]
    TokenExplicitMaxTtl: Optional[float]
    TokenMaxTtl: Optional[float]
    TokenNoDefaultPolicy: Optional[bool]
    TokenNumUses: Optional[float]
    TokenPeriod: Optional[float]
    TokenPolicies: Optional[Sequence[str]]
    TokenTtl: Optional[float]
    TokenType: Optional[str]

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
            BindSecretId=json_data.get("BindSecretId"),
            BoundCidrList=json_data.get("BoundCidrList"),
            Id=json_data.get("Id"),
            Period=json_data.get("Period"),
            Policies=json_data.get("Policies"),
            RoleId=json_data.get("RoleId"),
            RoleName=json_data.get("RoleName"),
            SecretIdBoundCidrs=json_data.get("SecretIdBoundCidrs"),
            SecretIdNumUses=json_data.get("SecretIdNumUses"),
            SecretIdTtl=json_data.get("SecretIdTtl"),
            TokenBoundCidrs=json_data.get("TokenBoundCidrs"),
            TokenExplicitMaxTtl=json_data.get("TokenExplicitMaxTtl"),
            TokenMaxTtl=json_data.get("TokenMaxTtl"),
            TokenNoDefaultPolicy=json_data.get("TokenNoDefaultPolicy"),
            TokenNumUses=json_data.get("TokenNumUses"),
            TokenPeriod=json_data.get("TokenPeriod"),
            TokenPolicies=json_data.get("TokenPolicies"),
            TokenTtl=json_data.get("TokenTtl"),
            TokenType=json_data.get("TokenType"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


