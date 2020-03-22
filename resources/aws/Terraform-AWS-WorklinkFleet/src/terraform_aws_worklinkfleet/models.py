# DO NOT modify this file by hand, changes will be overwritten
from dataclasses import dataclass
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
    BaseResourceHandlerRequest,
    BaseResourceModel,
)

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
class ResourceModel(BaseResourceModel):
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
    IdentityProvider: Optional[Sequence["_IdentityProvider"]]
    Network: Optional[Sequence["_Network"]]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceModel"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceModel"]:
        if not json_data:
            return None
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
            IdentityProvider=json_data.get("IdentityProvider"),
            Network=json_data.get("Network"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class IdentityProvider:
    SamlMetadata: Optional[str]
    Type: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_IdentityProvider"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_IdentityProvider"]:
        if not json_data:
            return None
        return cls(
            SamlMetadata=json_data.get("SamlMetadata"),
            Type=json_data.get("Type"),
        )


# work around possible type aliasing issues when variable has same name as a model
_IdentityProvider = IdentityProvider


@dataclass
class Network:
    SecurityGroupIds: Optional[Sequence[str]]
    SubnetIds: Optional[Sequence[str]]
    VpcId: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Network"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Network"]:
        if not json_data:
            return None
        return cls(
            SecurityGroupIds=json_data.get("SecurityGroupIds"),
            SubnetIds=json_data.get("SubnetIds"),
            VpcId=json_data.get("VpcId"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Network = Network


