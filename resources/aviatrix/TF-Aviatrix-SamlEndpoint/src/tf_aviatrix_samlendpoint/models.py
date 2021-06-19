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
    AccessSetBy: Optional[str]
    ControllerLogin: Optional[bool]
    CustomEntityId: Optional[str]
    CustomSamlRequestTemplate: Optional[str]
    EndpointName: Optional[str]
    Id: Optional[str]
    IdpMetadata: Optional[str]
    IdpMetadataType: Optional[str]
    IdpMetadataUrl: Optional[str]
    RbacGroups: Optional[Sequence[str]]
    SignAuthnRequests: Optional[bool]

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
            AccessSetBy=json_data.get("AccessSetBy"),
            ControllerLogin=json_data.get("ControllerLogin"),
            CustomEntityId=json_data.get("CustomEntityId"),
            CustomSamlRequestTemplate=json_data.get("CustomSamlRequestTemplate"),
            EndpointName=json_data.get("EndpointName"),
            Id=json_data.get("Id"),
            IdpMetadata=json_data.get("IdpMetadata"),
            IdpMetadataType=json_data.get("IdpMetadataType"),
            IdpMetadataUrl=json_data.get("IdpMetadataUrl"),
            RbacGroups=json_data.get("RbacGroups"),
            SignAuthnRequests=json_data.get("SignAuthnRequests"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


