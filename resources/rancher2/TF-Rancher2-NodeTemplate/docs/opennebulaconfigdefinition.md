# TF::Rancher2::NodeTemplate OpennebulaConfigDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#b2dsize" title="B2dSize">B2dSize</a>" : <i>String</i>,
    "<a href="#cpu" title="Cpu">Cpu</a>" : <i>String</i>,
    "<a href="#devprefix" title="DevPrefix">DevPrefix</a>" : <i>String</i>,
    "<a href="#disablevnc" title="DisableVnc">DisableVnc</a>" : <i>Boolean</i>,
    "<a href="#diskresize" title="DiskResize">DiskResize</a>" : <i>String</i>,
    "<a href="#imageid" title="ImageId">ImageId</a>" : <i>String</i>,
    "<a href="#imagename" title="ImageName">ImageName</a>" : <i>String</i>,
    "<a href="#imageowner" title="ImageOwner">ImageOwner</a>" : <i>String</i>,
    "<a href="#memory" title="Memory">Memory</a>" : <i>String</i>,
    "<a href="#networkid" title="NetworkId">NetworkId</a>" : <i>String</i>,
    "<a href="#networkname" title="NetworkName">NetworkName</a>" : <i>String</i>,
    "<a href="#networkowner" title="NetworkOwner">NetworkOwner</a>" : <i>String</i>,
    "<a href="#password" title="Password">Password</a>" : <i>String</i>,
    "<a href="#sshuser" title="SshUser">SshUser</a>" : <i>String</i>,
    "<a href="#templateid" title="TemplateId">TemplateId</a>" : <i>String</i>,
    "<a href="#templatename" title="TemplateName">TemplateName</a>" : <i>String</i>,
    "<a href="#user" title="User">User</a>" : <i>String</i>,
    "<a href="#vcpu" title="Vcpu">Vcpu</a>" : <i>String</i>,
    "<a href="#xmlrpcurl" title="XmlRpcUrl">XmlRpcUrl</a>" : <i>String</i>
}
</pre>

### YAML

<pre>
<a href="#b2dsize" title="B2dSize">B2dSize</a>: <i>String</i>
<a href="#cpu" title="Cpu">Cpu</a>: <i>String</i>
<a href="#devprefix" title="DevPrefix">DevPrefix</a>: <i>String</i>
<a href="#disablevnc" title="DisableVnc">DisableVnc</a>: <i>Boolean</i>
<a href="#diskresize" title="DiskResize">DiskResize</a>: <i>String</i>
<a href="#imageid" title="ImageId">ImageId</a>: <i>String</i>
<a href="#imagename" title="ImageName">ImageName</a>: <i>String</i>
<a href="#imageowner" title="ImageOwner">ImageOwner</a>: <i>String</i>
<a href="#memory" title="Memory">Memory</a>: <i>String</i>
<a href="#networkid" title="NetworkId">NetworkId</a>: <i>String</i>
<a href="#networkname" title="NetworkName">NetworkName</a>: <i>String</i>
<a href="#networkowner" title="NetworkOwner">NetworkOwner</a>: <i>String</i>
<a href="#password" title="Password">Password</a>: <i>String</i>
<a href="#sshuser" title="SshUser">SshUser</a>: <i>String</i>
<a href="#templateid" title="TemplateId">TemplateId</a>: <i>String</i>
<a href="#templatename" title="TemplateName">TemplateName</a>: <i>String</i>
<a href="#user" title="User">User</a>: <i>String</i>
<a href="#vcpu" title="Vcpu">Vcpu</a>: <i>String</i>
<a href="#xmlrpcurl" title="XmlRpcUrl">XmlRpcUrl</a>: <i>String</i>
</pre>

## Properties

#### B2dSize

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Cpu

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DevPrefix

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DisableVnc

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DiskResize

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ImageId

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ImageName

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ImageOwner

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Memory

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NetworkId

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NetworkName

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NetworkOwner

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Password

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SshUser

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TemplateId

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TemplateName

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### User

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Vcpu

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### XmlRpcUrl

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

