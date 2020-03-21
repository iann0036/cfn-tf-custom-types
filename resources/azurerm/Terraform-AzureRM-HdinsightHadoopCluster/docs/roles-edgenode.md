# Terraform::AzureRM::HdinsightHadoopCluster Roles EdgeNode

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#targetinstancecount" title="TargetInstanceCount">TargetInstanceCount</a>" : <i>Double</i>,
    "<a href="#vmsize" title="VmSize">VmSize</a>" : <i>String</i>,
    "<a href="#installscriptaction" title="InstallScriptAction">InstallScriptAction</a>" : <i>[ <a href="roles-edgenode-installscriptaction.md">InstallScriptAction</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#targetinstancecount" title="TargetInstanceCount">TargetInstanceCount</a>: <i>Double</i>
<a href="#vmsize" title="VmSize">VmSize</a>: <i>String</i>
<a href="#installscriptaction" title="InstallScriptAction">InstallScriptAction</a>: <i>
      - <a href="roles-edgenode-installscriptaction.md">InstallScriptAction</a></i>
</pre>

## Properties

#### TargetInstanceCount

_Required_: Yes

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VmSize

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### InstallScriptAction

_Required_: No

_Type_: List of <a href="roles-edgenode-installscriptaction.md">InstallScriptAction</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

