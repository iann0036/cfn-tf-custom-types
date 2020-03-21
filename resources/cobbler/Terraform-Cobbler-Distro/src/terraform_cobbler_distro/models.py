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
    Arch: Optional[str]
    BootFiles: Optional[str]
    Breed: Optional[str]
    Comment: Optional[str]
    FetchableFiles: Optional[str]
    Initrd: Optional[str]
    Kernel: Optional[str]
    KernelOptions: Optional[str]
    KernelOptionsPost: Optional[str]
    MgmtClasses: Optional[Sequence[str]]
    Name: Optional[str]
    OsVersion: Optional[str]
    Owners: Optional[Sequence[str]]
    RedhatManagementKey: Optional[str]
    RedhatManagementServer: Optional[str]
    TemplateFiles: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceModel"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceModel"]:
        if not json_data:
            return None
        return cls(
            tfcfnid=json_data.get("tfcfnid"),
            Arch=json_data.get("Arch"),
            BootFiles=json_data.get("BootFiles"),
            Breed=json_data.get("Breed"),
            Comment=json_data.get("Comment"),
            FetchableFiles=json_data.get("FetchableFiles"),
            Initrd=json_data.get("Initrd"),
            Kernel=json_data.get("Kernel"),
            KernelOptions=json_data.get("KernelOptions"),
            KernelOptionsPost=json_data.get("KernelOptionsPost"),
            MgmtClasses=json_data.get("MgmtClasses"),
            Name=json_data.get("Name"),
            OsVersion=json_data.get("OsVersion"),
            Owners=json_data.get("Owners"),
            RedhatManagementKey=json_data.get("RedhatManagementKey"),
            RedhatManagementServer=json_data.get("RedhatManagementServer"),
            TemplateFiles=json_data.get("TemplateFiles"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


