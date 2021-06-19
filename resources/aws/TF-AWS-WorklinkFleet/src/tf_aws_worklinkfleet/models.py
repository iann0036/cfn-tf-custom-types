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
    AuditStreamArn: Optional[str]
    CompanyCode: Optional[str]
    CreatedTime: Optional[str]
    DeviceCaCertificate: Optional[str]
    DisplayName: Optional[str]
    Id: Optional[str]
    LastUpdatedTime: Optional[str]
    Name: Optional[str]
    OptimizeForEndUserLocation: Optional[bool]
    IdentityProvider: Optional[Sequence["_IdentityProviderDefinition"]]
    Network: Optional[Sequence["_NetworkDefinition"]]

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
            AuditStreamArn=json_data.get("AuditStreamArn"),
            CompanyCode=json_data.get("CompanyCode"),
            CreatedTime=json_data.get("CreatedTime"),
            DeviceCaCertificate=json_data.get("DeviceCaCertificate"),
            DisplayName=json_data.get("DisplayName"),
            Id=json_data.get("Id"),
            LastUpdatedTime=json_data.get("LastUpdatedTime"),
            Name=json_data.get("Name"),
            OptimizeForEndUserLocation=json_data.get("OptimizeForEndUserLocation"),
            IdentityProvider=deserialize_list(json_data.get("IdentityProvider"), IdentityProviderDefinition),
            Network=deserialize_list(json_data.get("Network"), NetworkDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class IdentityProviderDefinition(BaseModel):
    SamlMetadata: Optional[str]
    Type: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_IdentityProviderDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_IdentityProviderDefinition"]:
        if not json_data:
            return None
        return cls(
            SamlMetadata=json_data.get("SamlMetadata"),
            Type=json_data.get("Type"),
        )


# work around possible type aliasing issues when variable has same name as a model
_IdentityProviderDefinition = IdentityProviderDefinition


@dataclass
class NetworkDefinition(BaseModel):
    SecurityGroupIds: Optional[Sequence[str]]
    SubnetIds: Optional[Sequence[str]]
    VpcId: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_NetworkDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_NetworkDefinition"]:
        if not json_data:
            return None
        return cls(
            SecurityGroupIds=json_data.get("SecurityGroupIds"),
            SubnetIds=json_data.get("SubnetIds"),
            VpcId=json_data.get("VpcId"),
        )


# work around possible type aliasing issues when variable has same name as a model
_NetworkDefinition = NetworkDefinition


