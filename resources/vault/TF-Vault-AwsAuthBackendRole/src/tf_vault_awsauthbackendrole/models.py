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
    AllowInstanceMigration: Optional[bool]
    AuthType: Optional[str]
    Backend: Optional[str]
    BoundAccountId: Optional[str]
    BoundAccountIds: Optional[Sequence[str]]
    BoundAmiId: Optional[str]
    BoundAmiIds: Optional[Sequence[str]]
    BoundEc2InstanceId: Optional[Sequence[str]]
    BoundEc2InstanceIds: Optional[Sequence[str]]
    BoundIamInstanceProfileArn: Optional[str]
    BoundIamInstanceProfileArns: Optional[Sequence[str]]
    BoundIamPrincipalArn: Optional[str]
    BoundIamPrincipalArns: Optional[Sequence[str]]
    BoundIamRoleArn: Optional[str]
    BoundIamRoleArns: Optional[Sequence[str]]
    BoundRegion: Optional[str]
    BoundRegions: Optional[Sequence[str]]
    BoundSubnetId: Optional[str]
    BoundSubnetIds: Optional[Sequence[str]]
    BoundVpcId: Optional[str]
    BoundVpcIds: Optional[Sequence[str]]
    DisallowReauthentication: Optional[bool]
    Id: Optional[str]
    InferredAwsRegion: Optional[str]
    InferredEntityType: Optional[str]
    MaxTtl: Optional[float]
    Period: Optional[float]
    Policies: Optional[Sequence[str]]
    ResolveAwsUniqueIds: Optional[bool]
    Role: Optional[str]
    RoleTag: Optional[str]
    TokenBoundCidrs: Optional[Sequence[str]]
    TokenExplicitMaxTtl: Optional[float]
    TokenMaxTtl: Optional[float]
    TokenNoDefaultPolicy: Optional[bool]
    TokenNumUses: Optional[float]
    TokenPeriod: Optional[float]
    TokenPolicies: Optional[Sequence[str]]
    TokenTtl: Optional[float]
    TokenType: Optional[str]
    Ttl: Optional[float]

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
            AllowInstanceMigration=json_data.get("AllowInstanceMigration"),
            AuthType=json_data.get("AuthType"),
            Backend=json_data.get("Backend"),
            BoundAccountId=json_data.get("BoundAccountId"),
            BoundAccountIds=json_data.get("BoundAccountIds"),
            BoundAmiId=json_data.get("BoundAmiId"),
            BoundAmiIds=json_data.get("BoundAmiIds"),
            BoundEc2InstanceId=json_data.get("BoundEc2InstanceId"),
            BoundEc2InstanceIds=json_data.get("BoundEc2InstanceIds"),
            BoundIamInstanceProfileArn=json_data.get("BoundIamInstanceProfileArn"),
            BoundIamInstanceProfileArns=json_data.get("BoundIamInstanceProfileArns"),
            BoundIamPrincipalArn=json_data.get("BoundIamPrincipalArn"),
            BoundIamPrincipalArns=json_data.get("BoundIamPrincipalArns"),
            BoundIamRoleArn=json_data.get("BoundIamRoleArn"),
            BoundIamRoleArns=json_data.get("BoundIamRoleArns"),
            BoundRegion=json_data.get("BoundRegion"),
            BoundRegions=json_data.get("BoundRegions"),
            BoundSubnetId=json_data.get("BoundSubnetId"),
            BoundSubnetIds=json_data.get("BoundSubnetIds"),
            BoundVpcId=json_data.get("BoundVpcId"),
            BoundVpcIds=json_data.get("BoundVpcIds"),
            DisallowReauthentication=json_data.get("DisallowReauthentication"),
            Id=json_data.get("Id"),
            InferredAwsRegion=json_data.get("InferredAwsRegion"),
            InferredEntityType=json_data.get("InferredEntityType"),
            MaxTtl=json_data.get("MaxTtl"),
            Period=json_data.get("Period"),
            Policies=json_data.get("Policies"),
            ResolveAwsUniqueIds=json_data.get("ResolveAwsUniqueIds"),
            Role=json_data.get("Role"),
            RoleTag=json_data.get("RoleTag"),
            TokenBoundCidrs=json_data.get("TokenBoundCidrs"),
            TokenExplicitMaxTtl=json_data.get("TokenExplicitMaxTtl"),
            TokenMaxTtl=json_data.get("TokenMaxTtl"),
            TokenNoDefaultPolicy=json_data.get("TokenNoDefaultPolicy"),
            TokenNumUses=json_data.get("TokenNumUses"),
            TokenPeriod=json_data.get("TokenPeriod"),
            TokenPolicies=json_data.get("TokenPolicies"),
            TokenTtl=json_data.get("TokenTtl"),
            TokenType=json_data.get("TokenType"),
            Ttl=json_data.get("Ttl"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


