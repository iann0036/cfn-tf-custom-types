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
    ClusterType: Optional[str]
    CreatedAt: Optional[str]
    Domain: Optional[str]
    Enabled: Optional[bool]
    EnvironmentScope: Optional[str]
    Group: Optional[str]
    Id: Optional[str]
    KubernetesApiUrl: Optional[str]
    KubernetesAuthorizationType: Optional[str]
    KubernetesCaCert: Optional[str]
    KubernetesToken: Optional[str]
    Managed: Optional[bool]
    Name: Optional[str]
    PlatformType: Optional[str]
    ProviderType: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceModel"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceModel"]:
        if not json_data:
            return None
        return cls(
            tfcfnid=json_data.get("tfcfnid"),
            ClusterType=json_data.get("ClusterType"),
            CreatedAt=json_data.get("CreatedAt"),
            Domain=json_data.get("Domain"),
            Enabled=json_data.get("Enabled"),
            EnvironmentScope=json_data.get("EnvironmentScope"),
            Group=json_data.get("Group"),
            Id=json_data.get("Id"),
            KubernetesApiUrl=json_data.get("KubernetesApiUrl"),
            KubernetesAuthorizationType=json_data.get("KubernetesAuthorizationType"),
            KubernetesCaCert=json_data.get("KubernetesCaCert"),
            KubernetesToken=json_data.get("KubernetesToken"),
            Managed=json_data.get("Managed"),
            Name=json_data.get("Name"),
            PlatformType=json_data.get("PlatformType"),
            ProviderType=json_data.get("ProviderType"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


