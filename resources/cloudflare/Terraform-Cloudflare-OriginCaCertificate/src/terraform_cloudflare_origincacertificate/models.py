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
    Certificate: Optional[str]
    Csr: Optional[str]
    ExpiresOn: Optional[str]
    Hostnames: Optional[Sequence[str]]
    RequestType: Optional[str]
    RequestedValidity: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceModel"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceModel"]:
        if not json_data:
            return None
        return cls(
            tfcfnid=json_data.get("tfcfnid"),
            Certificate=json_data.get("Certificate"),
            Csr=json_data.get("Csr"),
            ExpiresOn=json_data.get("ExpiresOn"),
            Hostnames=json_data.get("Hostnames"),
            RequestType=json_data.get("RequestType"),
            RequestedValidity=json_data.get("RequestedValidity"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


