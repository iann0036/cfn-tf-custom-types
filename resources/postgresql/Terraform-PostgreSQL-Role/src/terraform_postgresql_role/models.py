# DO NOT modify this file by hand, changes will be overwritten
from dataclasses import dataclass
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
    BaseResourceHandlerRequest,
    BaseResourceModel,
)

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
class ResourceModel(BaseResourceModel):
    tfcfnid: Optional[str]
    BypassRowLevelSecurity: Optional[bool]
    ConnectionLimit: Optional[float]
    CreateDatabase: Optional[bool]
    CreateRole: Optional[bool]
    Encrypted: Optional[str]
    EncryptedPassword: Optional[bool]
    Inherit: Optional[bool]
    Login: Optional[bool]
    Name: Optional[str]
    Password: Optional[str]
    Replication: Optional[bool]
    Roles: Optional[Sequence[str]]
    SearchPath: Optional[Sequence[str]]
    SkipDropRole: Optional[bool]
    SkipReassignOwned: Optional[bool]
    StatementTimeout: Optional[float]
    Superuser: Optional[bool]
    ValidUntil: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceModel"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceModel"]:
        if not json_data:
            return None
        return cls(
            tfcfnid=json_data.get("tfcfnid"),
            BypassRowLevelSecurity=json_data.get("BypassRowLevelSecurity"),
            ConnectionLimit=json_data.get("ConnectionLimit"),
            CreateDatabase=json_data.get("CreateDatabase"),
            CreateRole=json_data.get("CreateRole"),
            Encrypted=json_data.get("Encrypted"),
            EncryptedPassword=json_data.get("EncryptedPassword"),
            Inherit=json_data.get("Inherit"),
            Login=json_data.get("Login"),
            Name=json_data.get("Name"),
            Password=json_data.get("Password"),
            Replication=json_data.get("Replication"),
            Roles=json_data.get("Roles"),
            SearchPath=json_data.get("SearchPath"),
            SkipDropRole=json_data.get("SkipDropRole"),
            SkipReassignOwned=json_data.get("SkipReassignOwned"),
            StatementTimeout=json_data.get("StatementTimeout"),
            Superuser=json_data.get("Superuser"),
            ValidUntil=json_data.get("ValidUntil"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


