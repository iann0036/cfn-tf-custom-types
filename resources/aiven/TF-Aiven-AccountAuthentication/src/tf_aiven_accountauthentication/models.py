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
    AccountId: Optional[str]
    AuthenticationId: Optional[str]
    CreateTime: Optional[str]
    Enabled: Optional[bool]
    Id: Optional[str]
    Name: Optional[str]
    SamlAcsUrl: Optional[str]
    SamlCertificate: Optional[str]
    SamlEntityId: Optional[str]
    SamlIdpUrl: Optional[str]
    SamlMetadataUrl: Optional[str]
    Type: Optional[str]
    UpdateTime: Optional[str]

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
            AccountId=json_data.get("AccountId"),
            AuthenticationId=json_data.get("AuthenticationId"),
            CreateTime=json_data.get("CreateTime"),
            Enabled=json_data.get("Enabled"),
            Id=json_data.get("Id"),
            Name=json_data.get("Name"),
            SamlAcsUrl=json_data.get("SamlAcsUrl"),
            SamlCertificate=json_data.get("SamlCertificate"),
            SamlEntityId=json_data.get("SamlEntityId"),
            SamlIdpUrl=json_data.get("SamlIdpUrl"),
            SamlMetadataUrl=json_data.get("SamlMetadataUrl"),
            Type=json_data.get("Type"),
            UpdateTime=json_data.get("UpdateTime"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


