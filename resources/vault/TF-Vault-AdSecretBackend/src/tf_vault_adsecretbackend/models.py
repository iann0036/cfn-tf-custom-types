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
    AnonymousGroupSearch: Optional[bool]
    Backend: Optional[str]
    Binddn: Optional[str]
    Bindpass: Optional[str]
    CaseSensitiveNames: Optional[bool]
    Certificate: Optional[str]
    ClientTlsCert: Optional[str]
    ClientTlsKey: Optional[str]
    DefaultLeaseTtlSeconds: Optional[float]
    DenyNullBind: Optional[bool]
    Description: Optional[str]
    Discoverdn: Optional[bool]
    Formatter: Optional[str]
    Groupattr: Optional[str]
    Groupdn: Optional[str]
    Groupfilter: Optional[str]
    Id: Optional[str]
    InsecureTls: Optional[bool]
    LastRotationTolerance: Optional[float]
    Length: Optional[float]
    Local: Optional[bool]
    MaxLeaseTtlSeconds: Optional[float]
    MaxTtl: Optional[float]
    PasswordPolicy: Optional[str]
    RequestTimeout: Optional[float]
    Starttls: Optional[bool]
    TlsMaxVersion: Optional[str]
    TlsMinVersion: Optional[str]
    Ttl: Optional[float]
    Upndomain: Optional[str]
    Url: Optional[str]
    UsePre111GroupCnBehavior: Optional[bool]
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
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            tfcfnid=json_data.get("tfcfnid"),
            AnonymousGroupSearch=json_data.get("AnonymousGroupSearch"),
            Backend=json_data.get("Backend"),
            Binddn=json_data.get("Binddn"),
            Bindpass=json_data.get("Bindpass"),
            CaseSensitiveNames=json_data.get("CaseSensitiveNames"),
            Certificate=json_data.get("Certificate"),
            ClientTlsCert=json_data.get("ClientTlsCert"),
            ClientTlsKey=json_data.get("ClientTlsKey"),
            DefaultLeaseTtlSeconds=json_data.get("DefaultLeaseTtlSeconds"),
            DenyNullBind=json_data.get("DenyNullBind"),
            Description=json_data.get("Description"),
            Discoverdn=json_data.get("Discoverdn"),
            Formatter=json_data.get("Formatter"),
            Groupattr=json_data.get("Groupattr"),
            Groupdn=json_data.get("Groupdn"),
            Groupfilter=json_data.get("Groupfilter"),
            Id=json_data.get("Id"),
            InsecureTls=json_data.get("InsecureTls"),
            LastRotationTolerance=json_data.get("LastRotationTolerance"),
            Length=json_data.get("Length"),
            Local=json_data.get("Local"),
            MaxLeaseTtlSeconds=json_data.get("MaxLeaseTtlSeconds"),
            MaxTtl=json_data.get("MaxTtl"),
            PasswordPolicy=json_data.get("PasswordPolicy"),
            RequestTimeout=json_data.get("RequestTimeout"),
            Starttls=json_data.get("Starttls"),
            TlsMaxVersion=json_data.get("TlsMaxVersion"),
            TlsMinVersion=json_data.get("TlsMinVersion"),
            Ttl=json_data.get("Ttl"),
            Upndomain=json_data.get("Upndomain"),
            Url=json_data.get("Url"),
            UsePre111GroupCnBehavior=json_data.get("UsePre111GroupCnBehavior"),
            UseTokenGroups=json_data.get("UseTokenGroups"),
            Userattr=json_data.get("Userattr"),
            Userdn=json_data.get("Userdn"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


