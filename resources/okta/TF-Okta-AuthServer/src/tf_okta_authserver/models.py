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
    Audiences: Optional[Sequence[str]]
    CredentialsLastRotated: Optional[str]
    CredentialsNextRotation: Optional[str]
    CredentialsRotationMode: Optional[str]
    Description: Optional[str]
    Id: Optional[str]
    Issuer: Optional[str]
    IssuerMode: Optional[str]
    Kid: Optional[str]
    Name: Optional[str]
    Status: Optional[str]

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
            Audiences=json_data.get("Audiences"),
            CredentialsLastRotated=json_data.get("CredentialsLastRotated"),
            CredentialsNextRotation=json_data.get("CredentialsNextRotation"),
            CredentialsRotationMode=json_data.get("CredentialsRotationMode"),
            Description=json_data.get("Description"),
            Id=json_data.get("Id"),
            Issuer=json_data.get("Issuer"),
            IssuerMode=json_data.get("IssuerMode"),
            Kid=json_data.get("Kid"),
            Name=json_data.get("Name"),
            Status=json_data.get("Status"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


