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
    ClusterType: Optional[str]
    CreatedAt: Optional[str]
    Domain: Optional[str]
    Enabled: Optional[bool]
    EnvironmentScope: Optional[str]
    Id: Optional[str]
    KubernetesApiUrl: Optional[str]
    KubernetesAuthorizationType: Optional[str]
    KubernetesCaCert: Optional[str]
    KubernetesNamespace: Optional[str]
    KubernetesToken: Optional[str]
    Managed: Optional[bool]
    ManagementProjectId: Optional[str]
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
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            tfcfnid=json_data.get("tfcfnid"),
            ClusterType=json_data.get("ClusterType"),
            CreatedAt=json_data.get("CreatedAt"),
            Domain=json_data.get("Domain"),
            Enabled=json_data.get("Enabled"),
            EnvironmentScope=json_data.get("EnvironmentScope"),
            Id=json_data.get("Id"),
            KubernetesApiUrl=json_data.get("KubernetesApiUrl"),
            KubernetesAuthorizationType=json_data.get("KubernetesAuthorizationType"),
            KubernetesCaCert=json_data.get("KubernetesCaCert"),
            KubernetesNamespace=json_data.get("KubernetesNamespace"),
            KubernetesToken=json_data.get("KubernetesToken"),
            Managed=json_data.get("Managed"),
            ManagementProjectId=json_data.get("ManagementProjectId"),
            Name=json_data.get("Name"),
            PlatformType=json_data.get("PlatformType"),
            ProviderType=json_data.get("ProviderType"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


