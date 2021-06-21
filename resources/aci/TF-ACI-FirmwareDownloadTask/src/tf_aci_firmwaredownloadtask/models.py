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
    Annotation: Optional[str]
    AuthPass: Optional[str]
    AuthType: Optional[str]
    Description: Optional[str]
    DnldTaskFlip: Optional[str]
    Id: Optional[str]
    IdentityPrivateKeyContents: Optional[str]
    IdentityPrivateKeyPassphrase: Optional[str]
    IdentityPublicKeyContents: Optional[str]
    LoadCatalogIfExistsAndNewer: Optional[str]
    Name: Optional[str]
    NameAlias: Optional[str]
    Password: Optional[str]
    PollingInterval: Optional[str]
    Proto: Optional[str]
    Url: Optional[str]
    User: Optional[str]

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
            Annotation=json_data.get("Annotation"),
            AuthPass=json_data.get("AuthPass"),
            AuthType=json_data.get("AuthType"),
            Description=json_data.get("Description"),
            DnldTaskFlip=json_data.get("DnldTaskFlip"),
            Id=json_data.get("Id"),
            IdentityPrivateKeyContents=json_data.get("IdentityPrivateKeyContents"),
            IdentityPrivateKeyPassphrase=json_data.get("IdentityPrivateKeyPassphrase"),
            IdentityPublicKeyContents=json_data.get("IdentityPublicKeyContents"),
            LoadCatalogIfExistsAndNewer=json_data.get("LoadCatalogIfExistsAndNewer"),
            Name=json_data.get("Name"),
            NameAlias=json_data.get("NameAlias"),
            Password=json_data.get("Password"),
            PollingInterval=json_data.get("PollingInterval"),
            Proto=json_data.get("Proto"),
            Url=json_data.get("Url"),
            User=json_data.get("User"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel

