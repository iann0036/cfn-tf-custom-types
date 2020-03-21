# Terraform::Rundeck::Project

CloudFormation equivalent of rundeck_project

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::Rundeck::Project",
    "Properties" : {
        "<a href="#tfcfnid" title="tfcfnid">tfcfnid</a>" : <i>String</i>,
        "<a href="#defaultnodeexecutorplugin" title="DefaultNodeExecutorPlugin">DefaultNodeExecutorPlugin</a>" : <i>String</i>,
        "<a href="#defaultnodefilecopierplugin" title="DefaultNodeFileCopierPlugin">DefaultNodeFileCopierPlugin</a>" : <i>String</i>,
        "<a href="#description" title="Description">Description</a>" : <i>String</i>,
        "<a href="#extraconfig" title="ExtraConfig">ExtraConfig</a>" : <i>[ &lt;a href=&#34;extraconfig.md&#34;&gt;ExtraConfig&lt;/a&gt;, ... ]</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#sshauthenticationtype" title="SshAuthenticationType">SshAuthenticationType</a>" : <i>String</i>,
        "<a href="#sshkeyfilepath" title="SshKeyFilePath">SshKeyFilePath</a>" : <i>String</i>,
        "<a href="#sshkeystoragepath" title="SshKeyStoragePath">SshKeyStoragePath</a>" : <i>String</i>,
        "<a href="#uiurl" title="UiUrl">UiUrl</a>" : <i>String</i>,
        "<a href="#resourcemodelsource" title="ResourceModelSource">ResourceModelSource</a>" : <i>[ &lt;a href=&#34;resourcemodelsource.md&#34;&gt;ResourceModelSource&lt;/a&gt;, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::Rundeck::Project
Properties:
    <a href="#tfcfnid" title="tfcfnid">tfcfnid</a>: <i>String</i>
    <a href="#defaultnodeexecutorplugin" title="DefaultNodeExecutorPlugin">DefaultNodeExecutorPlugin</a>: <i>String</i>
    <a href="#defaultnodefilecopierplugin" title="DefaultNodeFileCopierPlugin">DefaultNodeFileCopierPlugin</a>: <i>String</i>
    <a href="#description" title="Description">Description</a>: <i>String</i>
    <a href="#extraconfig" title="ExtraConfig">ExtraConfig</a>: <i>
      - &lt;a href=&#34;extraconfig.md&#34;&gt;ExtraConfig&lt;/a&gt;</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#sshauthenticationtype" title="SshAuthenticationType">SshAuthenticationType</a>: <i>String</i>
    <a href="#sshkeyfilepath" title="SshKeyFilePath">SshKeyFilePath</a>: <i>String</i>
    <a href="#sshkeystoragepath" title="SshKeyStoragePath">SshKeyStoragePath</a>: <i>String</i>
    <a href="#uiurl" title="UiUrl">UiUrl</a>: <i>String</i>
    <a href="#resourcemodelsource" title="ResourceModelSource">ResourceModelSource</a>: <i>
      - &lt;a href=&#34;resourcemodelsource.md&#34;&gt;ResourceModelSource&lt;/a&gt;</i>
</pre>

## Properties

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DefaultNodeExecutorPlugin

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DefaultNodeFileCopierPlugin

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Description

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ExtraConfig

_Required_: No

_Type_: List of &lt;a href=&#34;extraconfig.md&#34;&gt;ExtraConfig&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SshAuthenticationType

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SshKeyFilePath

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SshKeyStoragePath

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### UiUrl

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ResourceModelSource

_Required_: No

_Type_: List of &lt;a href=&#34;resourcemodelsource.md&#34;&gt;ResourceModelSource&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

#### UiUrl

Returns the &lt;code&gt;UiUrl&lt;/code&gt; value.

