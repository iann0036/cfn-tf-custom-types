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
    AptComponents: Optional[Sequence[str]]
    AptDists: Optional[Sequence[str]]
    Arch: Optional[str]
    Breed: Optional[str]
    Comment: Optional[str]
    CreaterepoFlags: Optional[str]
    Environment: Optional[str]
    Id: Optional[str]
    KeepUpdated: Optional[bool]
    Mirror: Optional[str]
    MirrorLocally: Optional[bool]
    Name: Optional[str]
    Owners: Optional[Sequence[str]]
    Proxy: Optional[str]
    RpmList: Optional[Sequence[str]]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceModel"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceModel"]:
        if not json_data:
            return None
        return cls(
            tfcfnid=json_data.get("tfcfnid"),
            AptComponents=json_data.get("AptComponents"),
            AptDists=json_data.get("AptDists"),
            Arch=json_data.get("Arch"),
            Breed=json_data.get("Breed"),
            Comment=json_data.get("Comment"),
            CreaterepoFlags=json_data.get("CreaterepoFlags"),
            Environment=json_data.get("Environment"),
            Id=json_data.get("Id"),
            KeepUpdated=json_data.get("KeepUpdated"),
            Mirror=json_data.get("Mirror"),
            MirrorLocally=json_data.get("MirrorLocally"),
            Name=json_data.get("Name"),
            Owners=json_data.get("Owners"),
            Proxy=json_data.get("Proxy"),
            RpmList=json_data.get("RpmList"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


