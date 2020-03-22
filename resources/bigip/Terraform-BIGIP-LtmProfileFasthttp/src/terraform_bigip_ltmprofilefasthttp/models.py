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
    ConnpoolMaxreuse: Optional[float]
    ConnpoolMaxsize: Optional[float]
    ConnpoolMinsize: Optional[float]
    ConnpoolReplenish: Optional[str]
    ConnpoolStep: Optional[float]
    ConnpoolidleTimeoutoverride: Optional[float]
    DefaultsFrom: Optional[str]
    Forcehttp10response: Optional[str]
    Id: Optional[str]
    IdleTimeout: Optional[float]
    MaxheaderSize: Optional[float]
    Name: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceModel"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceModel"]:
        if not json_data:
            return None
        return cls(
            tfcfnid=json_data.get("tfcfnid"),
            ConnpoolMaxreuse=json_data.get("ConnpoolMaxreuse"),
            ConnpoolMaxsize=json_data.get("ConnpoolMaxsize"),
            ConnpoolMinsize=json_data.get("ConnpoolMinsize"),
            ConnpoolReplenish=json_data.get("ConnpoolReplenish"),
            ConnpoolStep=json_data.get("ConnpoolStep"),
            ConnpoolidleTimeoutoverride=json_data.get("ConnpoolidleTimeoutoverride"),
            DefaultsFrom=json_data.get("DefaultsFrom"),
            Forcehttp10response=json_data.get("Forcehttp10response"),
            Id=json_data.get("Id"),
            IdleTimeout=json_data.get("IdleTimeout"),
            MaxheaderSize=json_data.get("MaxheaderSize"),
            Name=json_data.get("Name"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


