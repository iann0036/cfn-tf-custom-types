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
    Id: Optional[str]
    Name: Optional[str]
    Password: Optional[str]
    PrivateKey: Optional[str]
    PublicKey: Optional[str]
    TenantRef: Optional[str]
    Uuid: Optional[str]
    AzureServiceprincipal: Optional[Sequence["_AzureServiceprincipalDefinition"]]
    AzureUserpass: Optional[Sequence["_AzureUserpassDefinition"]]
    GcpCredentials: Optional[Sequence["_GcpCredentialsDefinition"]]
    NsxtCredentials: Optional[Sequence["_NsxtCredentialsDefinition"]]
    OciCredentials: Optional[Sequence["_OciCredentialsDefinition"]]
    TencentCredentials: Optional[Sequence["_TencentCredentialsDefinition"]]
    VcenterCredentials: Optional[Sequence["_VcenterCredentialsDefinition"]]

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
            Id=json_data.get("Id"),
            Name=json_data.get("Name"),
            Password=json_data.get("Password"),
            PrivateKey=json_data.get("PrivateKey"),
            PublicKey=json_data.get("PublicKey"),
            TenantRef=json_data.get("TenantRef"),
            Uuid=json_data.get("Uuid"),
            AzureServiceprincipal=deserialize_list(json_data.get("AzureServiceprincipal"), AzureServiceprincipalDefinition),
            AzureUserpass=deserialize_list(json_data.get("AzureUserpass"), AzureUserpassDefinition),
            GcpCredentials=deserialize_list(json_data.get("GcpCredentials"), GcpCredentialsDefinition),
            NsxtCredentials=deserialize_list(json_data.get("NsxtCredentials"), NsxtCredentialsDefinition),
            OciCredentials=deserialize_list(json_data.get("OciCredentials"), OciCredentialsDefinition),
            TencentCredentials=deserialize_list(json_data.get("TencentCredentials"), TencentCredentialsDefinition),
            VcenterCredentials=deserialize_list(json_data.get("VcenterCredentials"), VcenterCredentialsDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class AzureServiceprincipalDefinition(BaseModel):
    ApplicationId: Optional[str]
    AuthenticationToken: Optional[str]
    TenantId: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_AzureServiceprincipalDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AzureServiceprincipalDefinition"]:
        if not json_data:
            return None
        return cls(
            ApplicationId=json_data.get("ApplicationId"),
            AuthenticationToken=json_data.get("AuthenticationToken"),
            TenantId=json_data.get("TenantId"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AzureServiceprincipalDefinition = AzureServiceprincipalDefinition


@dataclass
class AzureUserpassDefinition(BaseModel):
    Password: Optional[str]
    TenantName: Optional[str]
    Username: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_AzureUserpassDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AzureUserpassDefinition"]:
        if not json_data:
            return None
        return cls(
            Password=json_data.get("Password"),
            TenantName=json_data.get("TenantName"),
            Username=json_data.get("Username"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AzureUserpassDefinition = AzureUserpassDefinition


@dataclass
class GcpCredentialsDefinition(BaseModel):
    ServiceAccountKeyfileData: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_GcpCredentialsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_GcpCredentialsDefinition"]:
        if not json_data:
            return None
        return cls(
            ServiceAccountKeyfileData=json_data.get("ServiceAccountKeyfileData"),
        )


# work around possible type aliasing issues when variable has same name as a model
_GcpCredentialsDefinition = GcpCredentialsDefinition


@dataclass
class NsxtCredentialsDefinition(BaseModel):
    Password: Optional[str]
    Username: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_NsxtCredentialsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_NsxtCredentialsDefinition"]:
        if not json_data:
            return None
        return cls(
            Password=json_data.get("Password"),
            Username=json_data.get("Username"),
        )


# work around possible type aliasing issues when variable has same name as a model
_NsxtCredentialsDefinition = NsxtCredentialsDefinition


@dataclass
class OciCredentialsDefinition(BaseModel):
    Fingerprint: Optional[str]
    KeyContent: Optional[str]
    PassPhrase: Optional[str]
    User: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_OciCredentialsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_OciCredentialsDefinition"]:
        if not json_data:
            return None
        return cls(
            Fingerprint=json_data.get("Fingerprint"),
            KeyContent=json_data.get("KeyContent"),
            PassPhrase=json_data.get("PassPhrase"),
            User=json_data.get("User"),
        )


# work around possible type aliasing issues when variable has same name as a model
_OciCredentialsDefinition = OciCredentialsDefinition


@dataclass
class TencentCredentialsDefinition(BaseModel):
    SecretId: Optional[str]
    SecretKey: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_TencentCredentialsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TencentCredentialsDefinition"]:
        if not json_data:
            return None
        return cls(
            SecretId=json_data.get("SecretId"),
            SecretKey=json_data.get("SecretKey"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TencentCredentialsDefinition = TencentCredentialsDefinition


@dataclass
class VcenterCredentialsDefinition(BaseModel):
    Password: Optional[str]
    Username: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_VcenterCredentialsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_VcenterCredentialsDefinition"]:
        if not json_data:
            return None
        return cls(
            Password=json_data.get("Password"),
            Username=json_data.get("Username"),
        )


# work around possible type aliasing issues when variable has same name as a model
_VcenterCredentialsDefinition = VcenterCredentialsDefinition


