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
    IsFederated: Optional[bool]
    Issuer: Optional[str]
    JwksKeys: Optional[str]
    JwtProfileType: Optional[str]
    Name: Optional[str]
    TenantRef: Optional[str]
    Uuid: Optional[str]
    ControllerInternalAuth: Optional[Sequence["_ControllerInternalAuthDefinition"]]

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
            IsFederated=json_data.get("IsFederated"),
            Issuer=json_data.get("Issuer"),
            JwksKeys=json_data.get("JwksKeys"),
            JwtProfileType=json_data.get("JwtProfileType"),
            Name=json_data.get("Name"),
            TenantRef=json_data.get("TenantRef"),
            Uuid=json_data.get("Uuid"),
            ControllerInternalAuth=deserialize_list(json_data.get("ControllerInternalAuth"), ControllerInternalAuthDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class ControllerInternalAuthDefinition(BaseModel):
    SymmetricJwksKeys: Optional[Sequence["_SymmetricJwksKeysDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_ControllerInternalAuthDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ControllerInternalAuthDefinition"]:
        if not json_data:
            return None
        return cls(
            SymmetricJwksKeys=deserialize_list(json_data.get("SymmetricJwksKeys"), SymmetricJwksKeysDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ControllerInternalAuthDefinition = ControllerInternalAuthDefinition


@dataclass
class SymmetricJwksKeysDefinition(BaseModel):
    Alg: Optional[str]
    Key: Optional[str]
    Kid: Optional[str]
    Kty: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_SymmetricJwksKeysDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SymmetricJwksKeysDefinition"]:
        if not json_data:
            return None
        return cls(
            Alg=json_data.get("Alg"),
            Key=json_data.get("Key"),
            Kid=json_data.get("Kid"),
            Kty=json_data.get("Kty"),
        )


# work around possible type aliasing issues when variable has same name as a model
_SymmetricJwksKeysDefinition = SymmetricJwksKeysDefinition


