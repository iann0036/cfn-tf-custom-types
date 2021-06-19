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
    AccessKeyId: Optional[str]
    AccountId: Optional[str]
    Annotation: Optional[str]
    Description: Optional[str]
    Email: Optional[str]
    HttpProxy: Optional[str]
    Id: Optional[str]
    IsAccountInOrg: Optional[str]
    IsTrusted: Optional[str]
    NameAlias: Optional[str]
    ProviderId: Optional[str]
    Region: Optional[str]
    SecretAccessKey: Optional[str]
    TenantDn: Optional[str]

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
            AccessKeyId=json_data.get("AccessKeyId"),
            AccountId=json_data.get("AccountId"),
            Annotation=json_data.get("Annotation"),
            Description=json_data.get("Description"),
            Email=json_data.get("Email"),
            HttpProxy=json_data.get("HttpProxy"),
            Id=json_data.get("Id"),
            IsAccountInOrg=json_data.get("IsAccountInOrg"),
            IsTrusted=json_data.get("IsTrusted"),
            NameAlias=json_data.get("NameAlias"),
            ProviderId=json_data.get("ProviderId"),
            Region=json_data.get("Region"),
            SecretAccessKey=json_data.get("SecretAccessKey"),
            TenantDn=json_data.get("TenantDn"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


