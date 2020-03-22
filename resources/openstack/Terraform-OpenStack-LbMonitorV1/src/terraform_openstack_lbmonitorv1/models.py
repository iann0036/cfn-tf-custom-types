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
    AdminStateUp: Optional[str]
    Delay: Optional[float]
    ExpectedCodes: Optional[str]
    HttpMethod: Optional[str]
    Id: Optional[str]
    MaxRetries: Optional[float]
    Region: Optional[str]
    TenantId: Optional[str]
    Timeout: Optional[float]
    Type: Optional[str]
    UrlPath: Optional[str]
    Timeouts: Optional["_Timeouts"]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceModel"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceModel"]:
        if not json_data:
            return None
        return cls(
            tfcfnid=json_data.get("tfcfnid"),
            AdminStateUp=json_data.get("AdminStateUp"),
            Delay=json_data.get("Delay"),
            ExpectedCodes=json_data.get("ExpectedCodes"),
            HttpMethod=json_data.get("HttpMethod"),
            Id=json_data.get("Id"),
            MaxRetries=json_data.get("MaxRetries"),
            Region=json_data.get("Region"),
            TenantId=json_data.get("TenantId"),
            Timeout=json_data.get("Timeout"),
            Type=json_data.get("Type"),
            UrlPath=json_data.get("UrlPath"),
            Timeouts=Timeouts._deserialize(json_data.get("Timeouts")),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class Timeouts:
    Create: Optional[str]
    Delete: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Timeouts"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Timeouts"]:
        if not json_data:
            return None
        return cls(
            Create=json_data.get("Create"),
            Delete=json_data.get("Delete"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Timeouts = Timeouts


