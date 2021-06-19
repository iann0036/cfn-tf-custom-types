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
    Color: Optional[str]
    Comments: Optional[str]
    EncryptionMethod: Optional[str]
    EncryptionSuite: Optional[str]
    Gateways: Optional[Sequence[str]]
    Id: Optional[str]
    IgnoreErrors: Optional[bool]
    IgnoreWarnings: Optional[bool]
    IkePhase1: Optional[Sequence["_IkePhase1Definition"]]
    IkePhase2: Optional[Sequence["_IkePhase2Definition"]]
    Name: Optional[str]
    Tags: Optional[Sequence[str]]
    UseSharedSecret: Optional[bool]
    OverrideVpnDomains: Optional[Sequence["_OverrideVpnDomainsDefinition"]]
    SharedSecrets: Optional[Sequence["_SharedSecretsDefinition"]]

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
            Color=json_data.get("Color"),
            Comments=json_data.get("Comments"),
            EncryptionMethod=json_data.get("EncryptionMethod"),
            EncryptionSuite=json_data.get("EncryptionSuite"),
            Gateways=json_data.get("Gateways"),
            Id=json_data.get("Id"),
            IgnoreErrors=json_data.get("IgnoreErrors"),
            IgnoreWarnings=json_data.get("IgnoreWarnings"),
            IkePhase1=deserialize_list(json_data.get("IkePhase1"), IkePhase1Definition),
            IkePhase2=deserialize_list(json_data.get("IkePhase2"), IkePhase2Definition),
            Name=json_data.get("Name"),
            Tags=json_data.get("Tags"),
            UseSharedSecret=json_data.get("UseSharedSecret"),
            OverrideVpnDomains=deserialize_list(json_data.get("OverrideVpnDomains"), OverrideVpnDomainsDefinition),
            SharedSecrets=deserialize_list(json_data.get("SharedSecrets"), SharedSecretsDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class IkePhase1Definition(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_IkePhase1Definition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_IkePhase1Definition"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_IkePhase1Definition = IkePhase1Definition


@dataclass
class IkePhase2Definition(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_IkePhase2Definition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_IkePhase2Definition"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_IkePhase2Definition = IkePhase2Definition


@dataclass
class OverrideVpnDomainsDefinition(BaseModel):
    Gateway: Optional[str]
    VpnDomain: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_OverrideVpnDomainsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_OverrideVpnDomainsDefinition"]:
        if not json_data:
            return None
        return cls(
            Gateway=json_data.get("Gateway"),
            VpnDomain=json_data.get("VpnDomain"),
        )


# work around possible type aliasing issues when variable has same name as a model
_OverrideVpnDomainsDefinition = OverrideVpnDomainsDefinition


@dataclass
class SharedSecretsDefinition(BaseModel):
    ExternalGateway: Optional[str]
    SharedSecret: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_SharedSecretsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SharedSecretsDefinition"]:
        if not json_data:
            return None
        return cls(
            ExternalGateway=json_data.get("ExternalGateway"),
            SharedSecret=json_data.get("SharedSecret"),
        )


# work around possible type aliasing issues when variable has same name as a model
_SharedSecretsDefinition = SharedSecretsDefinition


