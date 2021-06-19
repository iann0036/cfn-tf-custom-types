# TF::Rancher2::ClusterSync NodesDefinition5

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#annotations" title="Annotations">Annotations</a>" : <i>[ <a href="nodesdefinition.md">NodesDefinition</a>, ... ]</i>,
    "<a href="#capacity" title="Capacity">Capacity</a>" : <i>[ <a href="nodesdefinition2.md">NodesDefinition2</a>, ... ]</i>,
    "<a href="#clusterid" title="ClusterId">ClusterId</a>" : <i>String</i>,
    "<a href="#externalipaddress" title="ExternalIpAddress">ExternalIpAddress</a>" : <i>String</i>,
    "<a href="#hostname" title="Hostname">Hostname</a>" : <i>String</i>,
    "<a href="#id" title="Id">Id</a>" : <i>String</i>,
    "<a href="#ipaddress" title="IpAddress">IpAddress</a>" : <i>String</i>,
    "<a href="#labels" title="Labels">Labels</a>" : <i>[ <a href="nodesdefinition3.md">NodesDefinition3</a>, ... ]</i>,
    "<a href="#name" title="Name">Name</a>" : <i>String</i>,
    "<a href="#nodepoolid" title="NodePoolId">NodePoolId</a>" : <i>String</i>,
    "<a href="#nodetemplateid" title="NodeTemplateId">NodeTemplateId</a>" : <i>String</i>,
    "<a href="#providerid" title="ProviderId">ProviderId</a>" : <i>String</i>,
    "<a href="#requestedhostname" title="RequestedHostname">RequestedHostname</a>" : <i>String</i>,
    "<a href="#roles" title="Roles">Roles</a>" : <i>[ String, ... ]</i>,
    "<a href="#sshuser" title="SshUser">SshUser</a>" : <i>String</i>,
    "<a href="#systeminfo" title="SystemInfo">SystemInfo</a>" : <i>[ <a href="nodesdefinition4.md">NodesDefinition4</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#annotations" title="Annotations">Annotations</a>: <i>
      - <a href="nodesdefinition.md">NodesDefinition</a></i>
<a href="#capacity" title="Capacity">Capacity</a>: <i>
      - <a href="nodesdefinition2.md">NodesDefinition2</a></i>
<a href="#clusterid" title="ClusterId">ClusterId</a>: <i>String</i>
<a href="#externalipaddress" title="ExternalIpAddress">ExternalIpAddress</a>: <i>String</i>
<a href="#hostname" title="Hostname">Hostname</a>: <i>String</i>
<a href="#id" title="Id">Id</a>: <i>String</i>
<a href="#ipaddress" title="IpAddress">IpAddress</a>: <i>String</i>
<a href="#labels" title="Labels">Labels</a>: <i>
      - <a href="nodesdefinition3.md">NodesDefinition3</a></i>
<a href="#name" title="Name">Name</a>: <i>String</i>
<a href="#nodepoolid" title="NodePoolId">NodePoolId</a>: <i>String</i>
<a href="#nodetemplateid" title="NodeTemplateId">NodeTemplateId</a>: <i>String</i>
<a href="#providerid" title="ProviderId">ProviderId</a>: <i>String</i>
<a href="#requestedhostname" title="RequestedHostname">RequestedHostname</a>: <i>String</i>
<a href="#roles" title="Roles">Roles</a>: <i>
      - String</i>
<a href="#sshuser" title="SshUser">SshUser</a>: <i>String</i>
<a href="#systeminfo" title="SystemInfo">SystemInfo</a>: <i>
      - <a href="nodesdefinition4.md">NodesDefinition4</a></i>
</pre>

## Properties

#### Annotations

_Required_: No

_Type_: List of <a href="nodesdefinition.md">NodesDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Capacity

_Required_: No

_Type_: List of <a href="nodesdefinition2.md">NodesDefinition2</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ClusterId

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ExternalIpAddress

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Hostname

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Id

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IpAddress

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Labels

_Required_: No

_Type_: List of <a href="nodesdefinition3.md">NodesDefinition3</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NodePoolId

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NodeTemplateId

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ProviderId

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RequestedHostname

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Roles

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SshUser

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SystemInfo

_Required_: No

_Type_: List of <a href="nodesdefinition4.md">NodesDefinition4</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

