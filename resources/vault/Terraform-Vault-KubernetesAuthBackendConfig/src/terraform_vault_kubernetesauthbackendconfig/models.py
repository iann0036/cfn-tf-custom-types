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
    Backend: Optional[str]
    Issuer: Optional[str]
    KubernetesCaCert: Optional[str]
    KubernetesHost: Optional[str]
    PemKeys: Optional[Sequence[str]]
    TokenReviewerJwt: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceModel"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceModel"]:
        if not json_data:
            return None
        return cls(
            tfcfnid=json_data.get("tfcfnid"),
            Backend=json_data.get("Backend"),
            Issuer=json_data.get("Issuer"),
            KubernetesCaCert=json_data.get("KubernetesCaCert"),
            KubernetesHost=json_data.get("KubernetesHost"),
            PemKeys=json_data.get("PemKeys"),
            TokenReviewerJwt=json_data.get("TokenReviewerJwt"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


