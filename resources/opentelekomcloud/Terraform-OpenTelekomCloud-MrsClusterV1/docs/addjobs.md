# Terraform::OpenTelekomCloud::MrsClusterV1 AddJobs

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#arguments" title="Arguments">Arguments</a>" : <i>String</i>,
    "<a href="#fileaction" title="FileAction">FileAction</a>" : <i>String</i>,
    "<a href="#hivescriptpath" title="HiveScriptPath">HiveScriptPath</a>" : <i>String</i>,
    "<a href="#hql" title="Hql">Hql</a>" : <i>String</i>,
    "<a href="#input" title="Input">Input</a>" : <i>String</i>,
    "<a href="#jarpath" title="JarPath">JarPath</a>" : <i>String</i>,
    "<a href="#joblog" title="JobLog">JobLog</a>" : <i>String</i>,
    "<a href="#jobname" title="JobName">JobName</a>" : <i>String</i>,
    "<a href="#jobtype" title="JobType">JobType</a>" : <i>Double</i>,
    "<a href="#output" title="Output">Output</a>" : <i>String</i>,
    "<a href="#shutdowncluster" title="ShutdownCluster">ShutdownCluster</a>" : <i>Boolean</i>,
    "<a href="#submitjobonceclusterrun" title="SubmitJobOnceClusterRun">SubmitJobOnceClusterRun</a>" : <i>Boolean</i>
}
</pre>

### YAML

<pre>
<a href="#arguments" title="Arguments">Arguments</a>: <i>String</i>
<a href="#fileaction" title="FileAction">FileAction</a>: <i>String</i>
<a href="#hivescriptpath" title="HiveScriptPath">HiveScriptPath</a>: <i>String</i>
<a href="#hql" title="Hql">Hql</a>: <i>String</i>
<a href="#input" title="Input">Input</a>: <i>String</i>
<a href="#jarpath" title="JarPath">JarPath</a>: <i>String</i>
<a href="#joblog" title="JobLog">JobLog</a>: <i>String</i>
<a href="#jobname" title="JobName">JobName</a>: <i>String</i>
<a href="#jobtype" title="JobType">JobType</a>: <i>Double</i>
<a href="#output" title="Output">Output</a>: <i>String</i>
<a href="#shutdowncluster" title="ShutdownCluster">ShutdownCluster</a>: <i>Boolean</i>
<a href="#submitjobonceclusterrun" title="SubmitJobOnceClusterRun">SubmitJobOnceClusterRun</a>: <i>Boolean</i>
</pre>

## Properties

#### Arguments

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FileAction

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HiveScriptPath

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Hql

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Input

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### JarPath

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### JobLog

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### JobName

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### JobType

_Required_: Yes

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Output

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ShutdownCluster

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SubmitJobOnceClusterRun

_Required_: Yes

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

