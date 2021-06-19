# TF::Rancher2::ClusterTemplate CisScanConfigDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#debugmaster" title="DebugMaster">DebugMaster</a>" : <i>Boolean</i>,
    "<a href="#debugworker" title="DebugWorker">DebugWorker</a>" : <i>Boolean</i>,
    "<a href="#overridebenchmarkversion" title="OverrideBenchmarkVersion">OverrideBenchmarkVersion</a>" : <i>String</i>,
    "<a href="#overrideskip" title="OverrideSkip">OverrideSkip</a>" : <i>[ String, ... ]</i>,
    "<a href="#profile" title="Profile">Profile</a>" : <i>String</i>
}
</pre>

### YAML

<pre>
<a href="#debugmaster" title="DebugMaster">DebugMaster</a>: <i>Boolean</i>
<a href="#debugworker" title="DebugWorker">DebugWorker</a>: <i>Boolean</i>
<a href="#overridebenchmarkversion" title="OverrideBenchmarkVersion">OverrideBenchmarkVersion</a>: <i>String</i>
<a href="#overrideskip" title="OverrideSkip">OverrideSkip</a>: <i>
      - String</i>
<a href="#profile" title="Profile">Profile</a>: <i>String</i>
</pre>

## Properties

#### DebugMaster

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DebugWorker

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### OverrideBenchmarkVersion

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### OverrideSkip

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Profile

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

