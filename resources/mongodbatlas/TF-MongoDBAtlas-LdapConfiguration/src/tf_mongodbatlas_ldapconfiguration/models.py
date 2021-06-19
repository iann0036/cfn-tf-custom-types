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
    AuthenticationEnabled: Optional[bool]
    AuthorizationEnabled: Optional[bool]
    AuthzQueryTemplate: Optional[str]
    BindPassword: Optional[str]
    BindUsername: Optional[str]
    CaCertificate: Optional[str]
    Hostname: Optional[str]
    Id: Optional[str]
    Port: Optional[float]
    ProjectId: Optional[str]
    UserToDnMapping: Optional[Sequence["_UserToDnMappingDefinition"]]

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
            AuthenticationEnabled=json_data.get("AuthenticationEnabled"),
            AuthorizationEnabled=json_data.get("AuthorizationEnabled"),
            AuthzQueryTemplate=json_data.get("AuthzQueryTemplate"),
            BindPassword=json_data.get("BindPassword"),
            BindUsername=json_data.get("BindUsername"),
            CaCertificate=json_data.get("CaCertificate"),
            Hostname=json_data.get("Hostname"),
            Id=json_data.get("Id"),
            Port=json_data.get("Port"),
            ProjectId=json_data.get("ProjectId"),
            UserToDnMapping=deserialize_list(json_data.get("UserToDnMapping"), UserToDnMappingDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class UserToDnMappingDefinition(BaseModel):
    LdapQuery: Optional[str]
    Match: Optional[str]
    Substitution: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_UserToDnMappingDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_UserToDnMappingDefinition"]:
        if not json_data:
            return None
        return cls(
            LdapQuery=json_data.get("LdapQuery"),
            Match=json_data.get("Match"),
            Substitution=json_data.get("Substitution"),
        )


# work around possible type aliasing issues when variable has same name as a model
_UserToDnMappingDefinition = UserToDnMappingDefinition


