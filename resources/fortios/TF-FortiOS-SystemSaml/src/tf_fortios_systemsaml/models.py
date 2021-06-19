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
    Cert: Optional[str]
    DefaultLoginPage: Optional[str]
    DefaultProfile: Optional[str]
    DynamicSortSubtable: Optional[str]
    EntityId: Optional[str]
    Id: Optional[str]
    IdpCert: Optional[str]
    IdpEntityId: Optional[str]
    IdpSingleLogoutUrl: Optional[str]
    IdpSingleSignOnUrl: Optional[str]
    Life: Optional[float]
    PortalUrl: Optional[str]
    Role: Optional[str]
    ServerAddress: Optional[str]
    SingleLogoutUrl: Optional[str]
    SingleSignOnUrl: Optional[str]
    Status: Optional[str]
    Tolerance: Optional[float]
    Vdomparam: Optional[str]
    ServiceProviders: Optional[Sequence["_ServiceProvidersDefinition"]]

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
            Cert=json_data.get("Cert"),
            DefaultLoginPage=json_data.get("DefaultLoginPage"),
            DefaultProfile=json_data.get("DefaultProfile"),
            DynamicSortSubtable=json_data.get("DynamicSortSubtable"),
            EntityId=json_data.get("EntityId"),
            Id=json_data.get("Id"),
            IdpCert=json_data.get("IdpCert"),
            IdpEntityId=json_data.get("IdpEntityId"),
            IdpSingleLogoutUrl=json_data.get("IdpSingleLogoutUrl"),
            IdpSingleSignOnUrl=json_data.get("IdpSingleSignOnUrl"),
            Life=json_data.get("Life"),
            PortalUrl=json_data.get("PortalUrl"),
            Role=json_data.get("Role"),
            ServerAddress=json_data.get("ServerAddress"),
            SingleLogoutUrl=json_data.get("SingleLogoutUrl"),
            SingleSignOnUrl=json_data.get("SingleSignOnUrl"),
            Status=json_data.get("Status"),
            Tolerance=json_data.get("Tolerance"),
            Vdomparam=json_data.get("Vdomparam"),
            ServiceProviders=deserialize_list(json_data.get("ServiceProviders"), ServiceProvidersDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class ServiceProvidersDefinition(BaseModel):
    IdpEntityId: Optional[str]
    IdpSingleLogoutUrl: Optional[str]
    IdpSingleSignOnUrl: Optional[str]
    Name: Optional[str]
    Prefix: Optional[str]
    SpCert: Optional[str]
    SpEntityId: Optional[str]
    SpPortalUrl: Optional[str]
    SpSingleLogoutUrl: Optional[str]
    SpSingleSignOnUrl: Optional[str]
    AssertionAttributes: Optional[Sequence["_AssertionAttributesDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_ServiceProvidersDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ServiceProvidersDefinition"]:
        if not json_data:
            return None
        return cls(
            IdpEntityId=json_data.get("IdpEntityId"),
            IdpSingleLogoutUrl=json_data.get("IdpSingleLogoutUrl"),
            IdpSingleSignOnUrl=json_data.get("IdpSingleSignOnUrl"),
            Name=json_data.get("Name"),
            Prefix=json_data.get("Prefix"),
            SpCert=json_data.get("SpCert"),
            SpEntityId=json_data.get("SpEntityId"),
            SpPortalUrl=json_data.get("SpPortalUrl"),
            SpSingleLogoutUrl=json_data.get("SpSingleLogoutUrl"),
            SpSingleSignOnUrl=json_data.get("SpSingleSignOnUrl"),
            AssertionAttributes=deserialize_list(json_data.get("AssertionAttributes"), AssertionAttributesDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ServiceProvidersDefinition = ServiceProvidersDefinition


@dataclass
class AssertionAttributesDefinition(BaseModel):
    Name: Optional[str]
    Type: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_AssertionAttributesDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AssertionAttributesDefinition"]:
        if not json_data:
            return None
        return cls(
            Name=json_data.get("Name"),
            Type=json_data.get("Type"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AssertionAttributesDefinition = AssertionAttributesDefinition


