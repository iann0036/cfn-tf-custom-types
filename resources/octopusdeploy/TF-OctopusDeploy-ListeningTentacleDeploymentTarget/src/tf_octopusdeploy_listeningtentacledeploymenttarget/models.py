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
    CertificateSignatureAlgorithm: Optional[str]
    Environments: Optional[Sequence[str]]
    HasLatestCalamari: Optional[bool]
    HealthStatus: Optional[str]
    Id: Optional[str]
    IsDisabled: Optional[bool]
    IsInProcess: Optional[bool]
    MachinePolicyId: Optional[str]
    Name: Optional[str]
    OperatingSystem: Optional[str]
    ProxyId: Optional[str]
    Roles: Optional[Sequence[str]]
    ShellName: Optional[str]
    ShellVersion: Optional[str]
    SpaceId: Optional[str]
    Status: Optional[str]
    StatusSummary: Optional[str]
    TenantTags: Optional[Sequence[str]]
    TenantedDeploymentParticipation: Optional[str]
    Tenants: Optional[Sequence[str]]
    TentacleUrl: Optional[str]
    Thumbprint: Optional[str]
    Uri: Optional[str]
    TentacleVersionDetails: Optional[Sequence["_TentacleVersionDetailsDefinition"]]

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
            CertificateSignatureAlgorithm=json_data.get("CertificateSignatureAlgorithm"),
            Environments=json_data.get("Environments"),
            HasLatestCalamari=json_data.get("HasLatestCalamari"),
            HealthStatus=json_data.get("HealthStatus"),
            Id=json_data.get("Id"),
            IsDisabled=json_data.get("IsDisabled"),
            IsInProcess=json_data.get("IsInProcess"),
            MachinePolicyId=json_data.get("MachinePolicyId"),
            Name=json_data.get("Name"),
            OperatingSystem=json_data.get("OperatingSystem"),
            ProxyId=json_data.get("ProxyId"),
            Roles=json_data.get("Roles"),
            ShellName=json_data.get("ShellName"),
            ShellVersion=json_data.get("ShellVersion"),
            SpaceId=json_data.get("SpaceId"),
            Status=json_data.get("Status"),
            StatusSummary=json_data.get("StatusSummary"),
            TenantTags=json_data.get("TenantTags"),
            TenantedDeploymentParticipation=json_data.get("TenantedDeploymentParticipation"),
            Tenants=json_data.get("Tenants"),
            TentacleUrl=json_data.get("TentacleUrl"),
            Thumbprint=json_data.get("Thumbprint"),
            Uri=json_data.get("Uri"),
            TentacleVersionDetails=deserialize_list(json_data.get("TentacleVersionDetails"), TentacleVersionDetailsDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class TentacleVersionDetailsDefinition(BaseModel):
    UpgradeLocked: Optional[bool]
    UpgradeRequired: Optional[bool]
    UpgradeSuggested: Optional[bool]
    Version: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_TentacleVersionDetailsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TentacleVersionDetailsDefinition"]:
        if not json_data:
            return None
        return cls(
            UpgradeLocked=json_data.get("UpgradeLocked"),
            UpgradeRequired=json_data.get("UpgradeRequired"),
            UpgradeSuggested=json_data.get("UpgradeSuggested"),
            Version=json_data.get("Version"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TentacleVersionDetailsDefinition = TentacleVersionDetailsDefinition


