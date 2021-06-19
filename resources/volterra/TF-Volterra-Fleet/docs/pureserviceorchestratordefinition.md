# TF::Volterra::Fleet PureServiceOrchestratorDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#clusterid" title="ClusterId">ClusterId</a>" : <i>String</i>,
    "<a href="#enablestoragetopology" title="EnableStorageTopology">EnableStorageTopology</a>" : <i>Boolean</i>,
    "<a href="#enablestricttopology" title="EnableStrictTopology">EnableStrictTopology</a>" : <i>Boolean</i>,
    "<a href="#arrays" title="Arrays">Arrays</a>" : <i>[ <a href="arraysdefinition.md">ArraysDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#clusterid" title="ClusterId">ClusterId</a>: <i>String</i>
<a href="#enablestoragetopology" title="EnableStorageTopology">EnableStorageTopology</a>: <i>Boolean</i>
<a href="#enablestricttopology" title="EnableStrictTopology">EnableStrictTopology</a>: <i>Boolean</i>
<a href="#arrays" title="Arrays">Arrays</a>: <i>
      - <a href="arraysdefinition.md">ArraysDefinition</a></i>
</pre>

## Properties

#### ClusterId

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EnableStorageTopology

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EnableStrictTopology

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Arrays

_Required_: No

_Type_: List of <a href="arraysdefinition.md">ArraysDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

