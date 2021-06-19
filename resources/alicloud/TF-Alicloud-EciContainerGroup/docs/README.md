# TF::Alicloud::EciContainerGroup

CloudFormation equivalent of alicloud_eci_container_group

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::Alicloud::EciContainerGroup",
    "Properties" : {
        "<a href="#containergroupname" title="ContainerGroupName">ContainerGroupName</a>" : <i>String</i>,
        "<a href="#cpu" title="Cpu">Cpu</a>" : <i>Double</i>,
        "<a href="#instancetype" title="InstanceType">InstanceType</a>" : <i>String</i>,
        "<a href="#memory" title="Memory">Memory</a>" : <i>Double</i>,
        "<a href="#ramrolename" title="RamRoleName">RamRoleName</a>" : <i>String</i>,
        "<a href="#resourcegroupid" title="ResourceGroupId">ResourceGroupId</a>" : <i>String</i>,
        "<a href="#restartpolicy" title="RestartPolicy">RestartPolicy</a>" : <i>String</i>,
        "<a href="#securitygroupid" title="SecurityGroupId">SecurityGroupId</a>" : <i>String</i>,
        "<a href="#tags" title="Tags">Tags</a>" : <i>[ <a href="tagsdefinition.md">TagsDefinition</a>, ... ]</i>,
        "<a href="#vswitchid" title="VswitchId">VswitchId</a>" : <i>String</i>,
        "<a href="#zoneid" title="ZoneId">ZoneId</a>" : <i>String</i>,
        "<a href="#containers" title="Containers">Containers</a>" : <i>[ <a href="containersdefinition.md">ContainersDefinition</a>, ... ]</i>,
        "<a href="#dnsconfig" title="DnsConfig">DnsConfig</a>" : <i>[ <a href="dnsconfigdefinition.md">DnsConfigDefinition</a>, ... ]</i>,
        "<a href="#ecisecuritycontext" title="EciSecurityContext">EciSecurityContext</a>" : <i>[ <a href="ecisecuritycontextdefinition.md">EciSecurityContextDefinition</a>, ... ]</i>,
        "<a href="#hostaliases" title="HostAliases">HostAliases</a>" : <i>[ <a href="hostaliasesdefinition.md">HostAliasesDefinition</a>, ... ]</i>,
        "<a href="#initcontainers" title="InitContainers">InitContainers</a>" : <i>[ <a href="initcontainersdefinition.md">InitContainersDefinition</a>, ... ]</i>,
        "<a href="#timeouts" title="Timeouts">Timeouts</a>" : <i><a href="timeoutsdefinition.md">TimeoutsDefinition</a></i>,
        "<a href="#volumes" title="Volumes">Volumes</a>" : <i>[ <a href="volumesdefinition.md">VolumesDefinition</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::Alicloud::EciContainerGroup
Properties:
    <a href="#containergroupname" title="ContainerGroupName">ContainerGroupName</a>: <i>String</i>
    <a href="#cpu" title="Cpu">Cpu</a>: <i>Double</i>
    <a href="#instancetype" title="InstanceType">InstanceType</a>: <i>String</i>
    <a href="#memory" title="Memory">Memory</a>: <i>Double</i>
    <a href="#ramrolename" title="RamRoleName">RamRoleName</a>: <i>String</i>
    <a href="#resourcegroupid" title="ResourceGroupId">ResourceGroupId</a>: <i>String</i>
    <a href="#restartpolicy" title="RestartPolicy">RestartPolicy</a>: <i>String</i>
    <a href="#securitygroupid" title="SecurityGroupId">SecurityGroupId</a>: <i>String</i>
    <a href="#tags" title="Tags">Tags</a>: <i>
      - <a href="tagsdefinition.md">TagsDefinition</a></i>
    <a href="#vswitchid" title="VswitchId">VswitchId</a>: <i>String</i>
    <a href="#zoneid" title="ZoneId">ZoneId</a>: <i>String</i>
    <a href="#containers" title="Containers">Containers</a>: <i>
      - <a href="containersdefinition.md">ContainersDefinition</a></i>
    <a href="#dnsconfig" title="DnsConfig">DnsConfig</a>: <i>
      - <a href="dnsconfigdefinition.md">DnsConfigDefinition</a></i>
    <a href="#ecisecuritycontext" title="EciSecurityContext">EciSecurityContext</a>: <i>
      - <a href="ecisecuritycontextdefinition.md">EciSecurityContextDefinition</a></i>
    <a href="#hostaliases" title="HostAliases">HostAliases</a>: <i>
      - <a href="hostaliasesdefinition.md">HostAliasesDefinition</a></i>
    <a href="#initcontainers" title="InitContainers">InitContainers</a>: <i>
      - <a href="initcontainersdefinition.md">InitContainersDefinition</a></i>
    <a href="#timeouts" title="Timeouts">Timeouts</a>: <i><a href="timeoutsdefinition.md">TimeoutsDefinition</a></i>
    <a href="#volumes" title="Volumes">Volumes</a>: <i>
      - <a href="volumesdefinition.md">VolumesDefinition</a></i>
</pre>

## Properties

#### ContainerGroupName

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Cpu

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### InstanceType

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Memory

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RamRoleName

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ResourceGroupId

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RestartPolicy

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SecurityGroupId

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Tags

_Required_: No

_Type_: List of <a href="tagsdefinition.md">TagsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VswitchId

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ZoneId

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Containers

_Required_: No

_Type_: List of <a href="containersdefinition.md">ContainersDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DnsConfig

_Required_: No

_Type_: List of <a href="dnsconfigdefinition.md">DnsConfigDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EciSecurityContext

_Required_: No

_Type_: List of <a href="ecisecuritycontextdefinition.md">EciSecurityContextDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HostAliases

_Required_: No

_Type_: List of <a href="hostaliasesdefinition.md">HostAliasesDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### InitContainers

_Required_: No

_Type_: List of <a href="initcontainersdefinition.md">InitContainersDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Timeouts

_Required_: No

_Type_: <a href="timeoutsdefinition.md">TimeoutsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Volumes

_Required_: No

_Type_: List of <a href="volumesdefinition.md">VolumesDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

#### Id

Returns the <code>Id</code> value.

#### Status

Returns the <code>Status</code> value.

