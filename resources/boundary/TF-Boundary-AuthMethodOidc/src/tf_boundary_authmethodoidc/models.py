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
    AllowedAudiences: Optional[Sequence[str]]
    ApiUrlPrefix: Optional[str]
    CallbackUrl: Optional[str]
    ClientId: Optional[str]
    ClientSecret: Optional[str]
    ClientSecretHmac: Optional[str]
    Description: Optional[str]
    DisableDiscoveredConfigValidation: Optional[bool]
    Id: Optional[str]
    IdpCaCerts: Optional[Sequence[str]]
    IsPrimaryForScope: Optional[bool]
    Issuer: Optional[str]
    MaxAge: Optional[float]
    Name: Optional[str]
    ScopeId: Optional[str]
    SigningAlgorithms: Optional[Sequence[str]]
    State: Optional[str]
    Type: Optional[str]

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
            AllowedAudiences=json_data.get("AllowedAudiences"),
            ApiUrlPrefix=json_data.get("ApiUrlPrefix"),
            CallbackUrl=json_data.get("CallbackUrl"),
            ClientId=json_data.get("ClientId"),
            ClientSecret=json_data.get("ClientSecret"),
            ClientSecretHmac=json_data.get("ClientSecretHmac"),
            Description=json_data.get("Description"),
            DisableDiscoveredConfigValidation=json_data.get("DisableDiscoveredConfigValidation"),
            Id=json_data.get("Id"),
            IdpCaCerts=json_data.get("IdpCaCerts"),
            IsPrimaryForScope=json_data.get("IsPrimaryForScope"),
            Issuer=json_data.get("Issuer"),
            MaxAge=json_data.get("MaxAge"),
            Name=json_data.get("Name"),
            ScopeId=json_data.get("ScopeId"),
            SigningAlgorithms=json_data.get("SigningAlgorithms"),
            State=json_data.get("State"),
            Type=json_data.get("Type"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


