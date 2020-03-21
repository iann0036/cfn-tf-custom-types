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
    BootFiles: Optional[str]
    Comment: Optional[str]
    Distro: Optional[str]
    EnableGpxe: Optional[bool]
    EnableMenu: Optional[bool]
    FetchableFiles: Optional[str]
    KernelOptions: Optional[str]
    KernelOptionsPost: Optional[str]
    Kickstart: Optional[str]
    KsMeta: Optional[str]
    MgmtClasses: Optional[Sequence[str]]
    MgmtParameters: Optional[str]
    Name: Optional[str]
    NameServers: Optional[Sequence[str]]
    NameServersSearch: Optional[Sequence[str]]
    Owners: Optional[Sequence[str]]
    Parent: Optional[str]
    Proxy: Optional[str]
    RedhatManagementKey: Optional[str]
    RedhatManagementServer: Optional[str]
    Repos: Optional[Sequence[str]]
    Server: Optional[str]
    TemplateFiles: Optional[str]
    TemplateRemoteKickstarts: Optional[float]
    VirtAutoBoot: Optional[str]
    VirtBridge: Optional[str]
    VirtCpus: Optional[str]
    VirtDiskDriver: Optional[str]
    VirtFileSize: Optional[str]
    VirtPath: Optional[str]
    VirtRam: Optional[str]
    VirtType: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceModel"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceModel"]:
        if not json_data:
            return None
        return cls(
            tfcfnid=json_data.get("tfcfnid"),
            BootFiles=json_data.get("BootFiles"),
            Comment=json_data.get("Comment"),
            Distro=json_data.get("Distro"),
            EnableGpxe=json_data.get("EnableGpxe"),
            EnableMenu=json_data.get("EnableMenu"),
            FetchableFiles=json_data.get("FetchableFiles"),
            KernelOptions=json_data.get("KernelOptions"),
            KernelOptionsPost=json_data.get("KernelOptionsPost"),
            Kickstart=json_data.get("Kickstart"),
            KsMeta=json_data.get("KsMeta"),
            MgmtClasses=json_data.get("MgmtClasses"),
            MgmtParameters=json_data.get("MgmtParameters"),
            Name=json_data.get("Name"),
            NameServers=json_data.get("NameServers"),
            NameServersSearch=json_data.get("NameServersSearch"),
            Owners=json_data.get("Owners"),
            Parent=json_data.get("Parent"),
            Proxy=json_data.get("Proxy"),
            RedhatManagementKey=json_data.get("RedhatManagementKey"),
            RedhatManagementServer=json_data.get("RedhatManagementServer"),
            Repos=json_data.get("Repos"),
            Server=json_data.get("Server"),
            TemplateFiles=json_data.get("TemplateFiles"),
            TemplateRemoteKickstarts=json_data.get("TemplateRemoteKickstarts"),
            VirtAutoBoot=json_data.get("VirtAutoBoot"),
            VirtBridge=json_data.get("VirtBridge"),
            VirtCpus=json_data.get("VirtCpus"),
            VirtDiskDriver=json_data.get("VirtDiskDriver"),
            VirtFileSize=json_data.get("VirtFileSize"),
            VirtPath=json_data.get("VirtPath"),
            VirtRam=json_data.get("VirtRam"),
            VirtType=json_data.get("VirtType"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


