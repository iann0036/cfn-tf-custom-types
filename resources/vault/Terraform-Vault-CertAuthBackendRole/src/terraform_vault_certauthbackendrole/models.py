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
    AllowedCommonNames: Optional[Sequence[str]]
    AllowedDnsSans: Optional[Sequence[str]]
    AllowedEmailSans: Optional[Sequence[str]]
    AllowedNames: Optional[Sequence[str]]
    AllowedOrganizationUnits: Optional[Sequence[str]]
    AllowedUriSans: Optional[Sequence[str]]
    Backend: Optional[str]
    BoundCidrs: Optional[Sequence[str]]
    Certificate: Optional[str]
    DisplayName: Optional[str]
    Id: Optional[str]
    MaxTtl: Optional[str]
    Name: Optional[str]
    Period: Optional[str]
    Policies: Optional[Sequence[str]]
    RequiredExtensions: Optional[Sequence[str]]
    TokenBoundCidrs: Optional[Sequence[str]]
    TokenExplicitMaxTtl: Optional[float]
    TokenMaxTtl: Optional[float]
    TokenNoDefaultPolicy: Optional[bool]
    TokenNumUses: Optional[float]
    TokenPeriod: Optional[float]
    TokenPolicies: Optional[Sequence[str]]
    TokenTtl: Optional[float]
    TokenType: Optional[str]
    Ttl: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceModel"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceModel"]:
        if not json_data:
            return None
        return cls(
            tfcfnid=json_data.get("tfcfnid"),
            AllowedCommonNames=json_data.get("AllowedCommonNames"),
            AllowedDnsSans=json_data.get("AllowedDnsSans"),
            AllowedEmailSans=json_data.get("AllowedEmailSans"),
            AllowedNames=json_data.get("AllowedNames"),
            AllowedOrganizationUnits=json_data.get("AllowedOrganizationUnits"),
            AllowedUriSans=json_data.get("AllowedUriSans"),
            Backend=json_data.get("Backend"),
            BoundCidrs=json_data.get("BoundCidrs"),
            Certificate=json_data.get("Certificate"),
            DisplayName=json_data.get("DisplayName"),
            Id=json_data.get("Id"),
            MaxTtl=json_data.get("MaxTtl"),
            Name=json_data.get("Name"),
            Period=json_data.get("Period"),
            Policies=json_data.get("Policies"),
            RequiredExtensions=json_data.get("RequiredExtensions"),
            TokenBoundCidrs=json_data.get("TokenBoundCidrs"),
            TokenExplicitMaxTtl=json_data.get("TokenExplicitMaxTtl"),
            TokenMaxTtl=json_data.get("TokenMaxTtl"),
            TokenNoDefaultPolicy=json_data.get("TokenNoDefaultPolicy"),
            TokenNumUses=json_data.get("TokenNumUses"),
            TokenPeriod=json_data.get("TokenPeriod"),
            TokenPolicies=json_data.get("TokenPolicies"),
            TokenTtl=json_data.get("TokenTtl"),
            TokenType=json_data.get("TokenType"),
            Ttl=json_data.get("Ttl"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


