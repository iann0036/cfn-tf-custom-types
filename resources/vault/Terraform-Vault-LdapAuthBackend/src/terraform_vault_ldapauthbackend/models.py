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
    Accessor: Optional[str]
    Binddn: Optional[str]
    Bindpass: Optional[str]
    Certificate: Optional[str]
    DenyNullBind: Optional[bool]
    Description: Optional[str]
    Discoverdn: Optional[bool]
    Groupattr: Optional[str]
    Groupdn: Optional[str]
    Groupfilter: Optional[str]
    InsecureTls: Optional[bool]
    Path: Optional[str]
    Starttls: Optional[bool]
    TlsMaxVersion: Optional[str]
    TlsMinVersion: Optional[str]
    TokenBoundCidrs: Optional[Sequence[str]]
    TokenExplicitMaxTtl: Optional[float]
    TokenMaxTtl: Optional[float]
    TokenNoDefaultPolicy: Optional[bool]
    TokenNumUses: Optional[float]
    TokenPeriod: Optional[float]
    TokenPolicies: Optional[Sequence[str]]
    TokenTtl: Optional[float]
    TokenType: Optional[str]
    Upndomain: Optional[str]
    Url: Optional[str]
    UseTokenGroups: Optional[bool]
    Userattr: Optional[str]
    Userdn: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceModel"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceModel"]:
        if not json_data:
            return None
        return cls(
            tfcfnid=json_data.get("tfcfnid"),
            Accessor=json_data.get("Accessor"),
            Binddn=json_data.get("Binddn"),
            Bindpass=json_data.get("Bindpass"),
            Certificate=json_data.get("Certificate"),
            DenyNullBind=json_data.get("DenyNullBind"),
            Description=json_data.get("Description"),
            Discoverdn=json_data.get("Discoverdn"),
            Groupattr=json_data.get("Groupattr"),
            Groupdn=json_data.get("Groupdn"),
            Groupfilter=json_data.get("Groupfilter"),
            InsecureTls=json_data.get("InsecureTls"),
            Path=json_data.get("Path"),
            Starttls=json_data.get("Starttls"),
            TlsMaxVersion=json_data.get("TlsMaxVersion"),
            TlsMinVersion=json_data.get("TlsMinVersion"),
            TokenBoundCidrs=json_data.get("TokenBoundCidrs"),
            TokenExplicitMaxTtl=json_data.get("TokenExplicitMaxTtl"),
            TokenMaxTtl=json_data.get("TokenMaxTtl"),
            TokenNoDefaultPolicy=json_data.get("TokenNoDefaultPolicy"),
            TokenNumUses=json_data.get("TokenNumUses"),
            TokenPeriod=json_data.get("TokenPeriod"),
            TokenPolicies=json_data.get("TokenPolicies"),
            TokenTtl=json_data.get("TokenTtl"),
            TokenType=json_data.get("TokenType"),
            Upndomain=json_data.get("Upndomain"),
            Url=json_data.get("Url"),
            UseTokenGroups=json_data.get("UseTokenGroups"),
            Userattr=json_data.get("Userattr"),
            Userdn=json_data.get("Userdn"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


