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
    AllowAssumedSignin: Optional[bool]
    AuthMethod: Optional[float]
    BrandId: Optional[float]
    Certificate: Optional[Sequence["_CertificateDefinition"]]
    Configuration: Optional[Sequence["_ConfigurationDefinition"]]
    ConnectorId: Optional[float]
    CreatedAt: Optional[str]
    Description: Optional[str]
    IconUrl: Optional[str]
    Id: Optional[str]
    Name: Optional[str]
    Notes: Optional[str]
    PolicyId: Optional[float]
    Provisioning: Optional[Sequence["_ProvisioningDefinition"]]
    Sso: Optional[Sequence["_SsoDefinition"]]
    TabId: Optional[float]
    UpdatedAt: Optional[str]
    Visible: Optional[bool]
    Parameters: Optional[Sequence["_ParametersDefinition"]]

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
            AllowAssumedSignin=json_data.get("AllowAssumedSignin"),
            AuthMethod=json_data.get("AuthMethod"),
            BrandId=json_data.get("BrandId"),
            Certificate=deserialize_list(json_data.get("Certificate"), CertificateDefinition),
            Configuration=deserialize_list(json_data.get("Configuration"), ConfigurationDefinition),
            ConnectorId=json_data.get("ConnectorId"),
            CreatedAt=json_data.get("CreatedAt"),
            Description=json_data.get("Description"),
            IconUrl=json_data.get("IconUrl"),
            Id=json_data.get("Id"),
            Name=json_data.get("Name"),
            Notes=json_data.get("Notes"),
            PolicyId=json_data.get("PolicyId"),
            Provisioning=deserialize_list(json_data.get("Provisioning"), ProvisioningDefinition),
            Sso=deserialize_list(json_data.get("Sso"), SsoDefinition),
            TabId=json_data.get("TabId"),
            UpdatedAt=json_data.get("UpdatedAt"),
            Visible=json_data.get("Visible"),
            Parameters=deserialize_list(json_data.get("Parameters"), ParametersDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class CertificateDefinition(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_CertificateDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_CertificateDefinition"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_CertificateDefinition = CertificateDefinition


@dataclass
class ConfigurationDefinition(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ConfigurationDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ConfigurationDefinition"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ConfigurationDefinition = ConfigurationDefinition


@dataclass
class ProvisioningDefinition(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[bool]

    @classmethod
    def _deserialize(
        cls: Type["_ProvisioningDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ProvisioningDefinition"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ProvisioningDefinition = ProvisioningDefinition


@dataclass
class SsoDefinition(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_SsoDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SsoDefinition"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_SsoDefinition = SsoDefinition


@dataclass
class ParametersDefinition(BaseModel):
    AttributesTransformations: Optional[str]
    DefaultValues: Optional[str]
    IncludeInSamlAssertion: Optional[bool]
    Label: Optional[str]
    ParamKeyName: Optional[str]
    ProvisionedEntitlements: Optional[bool]
    SafeEntitlementsEnabled: Optional[bool]
    SkipIfBlank: Optional[bool]
    UserAttributeMacros: Optional[str]
    UserAttributeMappings: Optional[str]
    Values: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ParametersDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ParametersDefinition"]:
        if not json_data:
            return None
        return cls(
            AttributesTransformations=json_data.get("AttributesTransformations"),
            DefaultValues=json_data.get("DefaultValues"),
            IncludeInSamlAssertion=json_data.get("IncludeInSamlAssertion"),
            Label=json_data.get("Label"),
            ParamKeyName=json_data.get("ParamKeyName"),
            ProvisionedEntitlements=json_data.get("ProvisionedEntitlements"),
            SafeEntitlementsEnabled=json_data.get("SafeEntitlementsEnabled"),
            SkipIfBlank=json_data.get("SkipIfBlank"),
            UserAttributeMacros=json_data.get("UserAttributeMacros"),
            UserAttributeMappings=json_data.get("UserAttributeMappings"),
            Values=json_data.get("Values"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ParametersDefinition = ParametersDefinition


