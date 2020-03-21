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
    CertificateId: Optional[str]
    CreatedAt: Optional[str]
    CustomDomain: Optional[str]
    Endpoint: Optional[str]
    Id: Optional[str]
    Origin: Optional[str]
    Ttl: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceModel"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceModel"]:
        if not json_data:
            return None
        return cls(
            tfcfnid=json_data.get("tfcfnid"),
            CertificateId=json_data.get("CertificateId"),
            CreatedAt=json_data.get("CreatedAt"),
            CustomDomain=json_data.get("CustomDomain"),
            Endpoint=json_data.get("Endpoint"),
            Id=json_data.get("Id"),
            Origin=json_data.get("Origin"),
            Ttl=json_data.get("Ttl"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


