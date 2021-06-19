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
    DnsPrimary: Optional[str]
    DnsSecondary: Optional[str]
    Domain: Optional[str]
    Hostname: Optional[str]
    Id: Optional[str]
    NtpPrimaryAddress: Optional[str]
    NtpPrimaryAlgorithm: Optional[str]
    NtpPrimaryAuthKey: Optional[str]
    NtpPrimaryAuthType: Optional[str]
    NtpPrimaryKeyId: Optional[float]
    NtpSecondaryAddress: Optional[str]
    NtpSecondaryAlgorithm: Optional[str]
    NtpSecondaryAuthKey: Optional[str]
    NtpSecondaryAuthType: Optional[str]
    NtpSecondaryKeyId: Optional[float]
    ProxyPassword: Optional[str]
    ProxyPasswordEnc: Optional[str]
    ProxyPort: Optional[float]
    ProxyServer: Optional[str]
    ProxyUser: Optional[str]
    Timezone: Optional[str]
    UpdateServer: Optional[str]
    VerifyUpdateServer: Optional[bool]

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
            DnsPrimary=json_data.get("DnsPrimary"),
            DnsSecondary=json_data.get("DnsSecondary"),
            Domain=json_data.get("Domain"),
            Hostname=json_data.get("Hostname"),
            Id=json_data.get("Id"),
            NtpPrimaryAddress=json_data.get("NtpPrimaryAddress"),
            NtpPrimaryAlgorithm=json_data.get("NtpPrimaryAlgorithm"),
            NtpPrimaryAuthKey=json_data.get("NtpPrimaryAuthKey"),
            NtpPrimaryAuthType=json_data.get("NtpPrimaryAuthType"),
            NtpPrimaryKeyId=json_data.get("NtpPrimaryKeyId"),
            NtpSecondaryAddress=json_data.get("NtpSecondaryAddress"),
            NtpSecondaryAlgorithm=json_data.get("NtpSecondaryAlgorithm"),
            NtpSecondaryAuthKey=json_data.get("NtpSecondaryAuthKey"),
            NtpSecondaryAuthType=json_data.get("NtpSecondaryAuthType"),
            NtpSecondaryKeyId=json_data.get("NtpSecondaryKeyId"),
            ProxyPassword=json_data.get("ProxyPassword"),
            ProxyPasswordEnc=json_data.get("ProxyPasswordEnc"),
            ProxyPort=json_data.get("ProxyPort"),
            ProxyServer=json_data.get("ProxyServer"),
            ProxyUser=json_data.get("ProxyUser"),
            Timezone=json_data.get("Timezone"),
            UpdateServer=json_data.get("UpdateServer"),
            VerifyUpdateServer=json_data.get("VerifyUpdateServer"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


