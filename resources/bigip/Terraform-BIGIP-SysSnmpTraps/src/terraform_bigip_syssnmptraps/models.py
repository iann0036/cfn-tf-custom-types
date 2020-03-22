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
    AuthPasswordencrypted: Optional[str]
    AuthProtocol: Optional[str]
    Community: Optional[str]
    Description: Optional[str]
    EngineId: Optional[str]
    Host: Optional[str]
    Id: Optional[str]
    Name: Optional[str]
    Port: Optional[float]
    PrivacyPassword: Optional[str]
    PrivacyPasswordEncrypted: Optional[str]
    PrivacyProtocol: Optional[str]
    SecurityLevel: Optional[str]
    SecurityName: Optional[str]
    Version: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceModel"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceModel"]:
        if not json_data:
            return None
        return cls(
            tfcfnid=json_data.get("tfcfnid"),
            AuthPasswordencrypted=json_data.get("AuthPasswordencrypted"),
            AuthProtocol=json_data.get("AuthProtocol"),
            Community=json_data.get("Community"),
            Description=json_data.get("Description"),
            EngineId=json_data.get("EngineId"),
            Host=json_data.get("Host"),
            Id=json_data.get("Id"),
            Name=json_data.get("Name"),
            Port=json_data.get("Port"),
            PrivacyPassword=json_data.get("PrivacyPassword"),
            PrivacyPasswordEncrypted=json_data.get("PrivacyPasswordEncrypted"),
            PrivacyProtocol=json_data.get("PrivacyProtocol"),
            SecurityLevel=json_data.get("SecurityLevel"),
            SecurityName=json_data.get("SecurityName"),
            Version=json_data.get("Version"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


